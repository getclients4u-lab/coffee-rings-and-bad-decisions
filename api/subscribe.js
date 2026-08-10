// Vercel serverless: Coffee Rings launch list — appends to private coffee-rings-launchlist/leads.json
// Pattern: em-leads / everlastingmemories submit.js (GitHub contents API, no external sends)

const OWNER = 'getclients4u-lab';
const REPO  = 'coffee-rings-launchlist';
const PATH  = 'leads.json';

const GH = (path, options = {}) =>
  fetch(`https://api.github.com/repos/${OWNER}/${REPO}/contents/${path}`, {
    headers: { Authorization: `token ${process.env.GITHUB_TOKEN}`, Accept: 'application/vnd.github.v3+json', ...(options.headers || {}) },
    ...options,
  });

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const token = process.env.GITHUB_TOKEN;
  if (!token) return res.status(500).json({ error: 'Server not configured' });

  const email = String((req.body && req.body.email) || '').trim().toLowerCase();
  const name  = String((req.body && req.body.name) || '').trim().slice(0, 80);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) return res.status(400).json({ error: 'Valid email required' });

  const lead = { name, email, source: 'coffee-rings-website', ts: new Date().toISOString() };

  // Retry loop to handle concurrent-write 409 conflicts
  for (let attempt = 0; attempt < 5; attempt++) {
    try {
      const getRes = await GH(PATH);
      let data = { leads: [] }, sha = null;
      if (getRes.status === 200) {
        const file = await getRes.json();
        try { data = JSON.parse(Buffer.from(file.content, 'base64').toString('utf8')); } catch (e) { data = { leads: [] }; }
        sha = file.sha;
      } else if (getRes.status !== 404) {
        throw new Error(`GitHub GET ${getRes.status}`);
      }

      if (!Array.isArray(data.leads)) data.leads = [];
      if (data.leads.some(l => l.email === email)) {
        return res.status(200).json({ success: true, duplicate: true, message: 'You are already on the list ☕' });
      }
      data.leads.push(lead);

      const putRes = await GH(PATH, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: `Launch list signup: ${email}`,
          content: Buffer.from(JSON.stringify(data, null, 2)).toString('base64'),
          ...(sha ? { sha } : {}),
        }),
      });

      if (putRes.status === 200 || putRes.status === 201) {
        return res.status(200).json({ success: true, message: 'Welcome to the Coffee Ring ☕' });
      }
      if (putRes.status === 409) { await new Promise(r => setTimeout(r, 400 + attempt * 300)); continue; }
      throw new Error(`GitHub PUT ${putRes.status}`);
    } catch (err) {
      if (attempt === 4) return res.status(500).json({ error: 'Storage error' });
      await new Promise(r => setTimeout(r, 400 + attempt * 300));
    }
  }
  return res.status(500).json({ error: 'Storage error' });
};
