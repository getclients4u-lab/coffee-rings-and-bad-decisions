#!/usr/bin/env python3
"""Expand all chapters under 3000 words to 3000-4000 words.
Appends scene-rich continuation content that preserves plot and tone.
"""
from pathlib import Path
import re

BASE = Path('/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/drafts')
TARGET = 3000

# Additional content blocks keyed by chapter number.
# These are contextual expansions that fit the existing plot.
EXPANSIONS = {
 2: """Maya closed the shop early that evening, a decision that felt radical in itself. For three years, closing before 8 p.m. had been unthinkable — there was always something to do, always a bag to restock, always a light bulb to replace or a spill to mop. Today, though, she found herself turning the sign to CLOSED at 7:17 precisely, a time she'd never before considered as an endpoint.

Sam looked up from the register. "You're leaving early."

"I'm leaving on time," Maya corrected. "There's a difference."

"There's also a difference between 'on time' and 'before the sun goes down,' which is what this is."

Maya shrugged. She was carrying a lightness she didn't trust. "The beans are sorted. The lottery tickets are restocked. The espresso machine is behaving. What else is there?"

"Planning. Thinking. Worrying. The usual."

"I'm done worrying for today."

She meant it, too. She walked upstairs with the particular buoyancy of someone who'd just made a decision without consulting her anxiety. She made pasta — not the good pasta, just the regular pasta with butter and parmesan, the kind of meal that didn't require thought. She ate at the kitchen table while looking out the window at Alberta Street, which was quiet in the way it got right around dusk, when the workers had gone home and the restaurant staff hadn't yet arrived and the street belonged to the cats and the shadows.

Her phone buzzed. It was her sister, Jen, calling from New York. Maya picked up.

"You sound happy," Jen said immediately.

"I sound like I'm talking on the phone."

"You sound less like you're talking from the edge of a cliff. What happened?"

Maya told her. The 500-pound order. The lottery. Tom. The fundraiser. She left out Leo. She left out the kiss and the almost-kiss and the particular heat of having him in the shop. Some things felt too intimate for phone calls, even with her sister.

Jen was quiet for a moment. "You're doing it, aren't you? You're actually doing the thing."

"What thing."

"Building something. Instead of just surviving."

Maya looked out the window. Down on the street, a woman walked a dog that was very small and very fluffy and that stopped to investigate every fire hydrant with the thoroughness of a detective. "Maybe," she said. "Or maybe I'm just really good at pretending."

"You're not pretending," Jen said. "I can hear it in your voice. You've been tired for three years, Maya. Tired and funny and stubborn. Today you're just funny and stubborn. The tired part is gone."

Maya wanted to believe that. She wanted to believe that the tired part was gone, that it had been burned away by espresso steam and good news and a man who'd given her an importer's name and a reason to keep going. She wasn't sure she deserved to believe it. But she let herself entertain the possibility, just a little.

"Call me tomorrow," Jen said. "And tell me about the suit."

"There's nothing to tell."

"Bullshit. I can hear the smile in your voice. Call me tomorrow."

Maya hung up. She finished her pasta. She did the dishes. She went to bed at 10, which was early for her, and she slept without dreaming about coffee beans or Bean & Leaf or financial ruin. She dreamed about the ocean again, just briefly — a wave, the smell of salt, the particular gray-green of Oregon water — and woke up feeling, inexplicably, like the dream had been a promise.

At 6:42 a.m., she woke to the sound of the espresso machine downstairs. She'd forgotten to turn it off. The machine had been hissing gently all night, a soft mechanical sigh that said I am still here, I am still working, I still believe in coffee. Maya went downstairs. She turned it off. She stood in the quiet shop and listened to the silence, which felt different now — not empty, but expectant.

She made coffee. She opened her laptop. She opened the email she'd drafted to Tom but hadn't sent. She added a paragraph: "Can we also create a limited-edition Mystery Blend that has a storytelling component? Each bag tells part of a story about the farm, the farmers, the journey. People buy stories as much as they buy coffee."

She sent it. Then she stood at the window and watched the sun come up over Alberta Street, painting the buildings in shades of orange and pink and gold, and for a moment, just a moment, she allowed herself to imagine a future in which the shop not only survived but thrived, in which the Mystery Bean Lottery became an annual tradition, in which the chalkboard dragon had its own merchandise line and the regulars brought their children and told them stories about the time Coffee Rings almost went under and was saved by a community that loved it.

The moment passed. The sun rose fully. The shop got busy. But the feeling lingered, like the aftertaste of good coffee — warm, persistent, just a little bit sweet.""",

 4: """Later that afternoon, when the festival crowd had thinned and the mad rush became a gentle flow of stragglers with coffee in hand and pastries in paper bags, Maya stepped outside to breathe. The air was thick with the particular scent of a Portland spring — rain that hadn't quite stopped, earth that was warming up, coffee that had conquered the block. She leaned against the brick wall of the building next door and closed her eyes.

"Hey," someone said.

Maya opened her eyes. It was Claire, the reporter from the Observer. She was sitting on a folding chair, typing rapidly on her laptop, and she looked up with a smile. "I've got two thousand words," she said. "And I haven't even written the lede."

"You're fast."

"I'm paid to be fast. Also, your story is really good. People love a comeback narrative. They love a loser who fights back."

"Loser," Maya repeated.

"Not in a bad way. In a narrative way. The underdog. The small shop taking on the big chain. It's everything."

Maya took it as a compliment. She wasn't sure it was one. "The chain isn't the villain," she said. "It's just... bigger."

"That's the story. Not villainy. Just scale. And community pushing back. It's classic."

They talked for another twenty minutes. Claire asked questions about the loan, about the lottery, about Leo. Maya answered honestly but carefully, leaving out the kiss and the fight and the particular knot of feelings she was still trying to untangle. Claire wrote. She wrote fast. She wrote with the particular intensity of a journalist who'd found a story that felt alive, that had teeth and heart and a protagonist who wasn't playing the part of a hero but was, instead, just trying to pay her rent.

By evening, the shop was emptying. The last customer left at 6:42 — Maya noted the time because her phone died at 6:42 once and she'd never forgotten. Sam locked the front door. Maya stacked the last of the Mystery Bean tickets. Leo was already gone — he'd left at 5:30 to take a call, saying he'd be back in the morning.

Maya went upstairs alone. She made tea — chamomile, because she was trying to sleep — and she sat at the kitchen table and stared at the spreadsheet. The numbers were better now. Not good. Not fixed. Better. The difference was small but it was there, like a candle in a dark room.

She opened her email. She saw a message from Tom: photos of the roasted beans, laid out on a table, looking beautiful and dangerous and expensive. He'd written: "These are going to change your life. Or at least your revenue."

Maya laughed. She replied: "Looking forward to it. Can't wait to sell them all and stop being a 500-pound emergency."

Tom wrote back: "You're not an emergency. You're a customer who ordered ambitiously."

She liked that. She saved the email. She closed the laptop. She went to the window and looked down at the street, still wet from the afternoon rain, reflecting the lights from the shops. She thought about Mrs. Hsu's floorboards and the speakeasy and the storytelling and the way old things held onto their stories even when the people who'd lived them were gone.

She thought she'd like this shop to be that kind of place someday. Not a speakeasy — well, maybe a speakeasy, if the neighborhood ever needed one again. But a place with stories. A place people remembered. A place that mattered.

She went to bed at 10:30. She slept. When she woke at 5:58, the first thought in her head was: Today is the day we open the pop-up.

The second thought was: I miss Leo already.

She didn't like the second thought. She sat with it anyway.""",

 5: """The kiss changed things. It changed nothing and everything simultaneously, the way meaningful moments often do — altering the atmosphere without moving the furniture.

By Thursday, they'd settled into a rhythm that was mostly professional and strangely intimate, as if the kiss had given them permission to cross a boundary they hadn't known was there. Leo still arrived at 8 a.m. with his thermos and his notebook. Maya still poured the coffee before he ordered it. But now their hands brushed when they reached for the same cup. Now their voices dropped when the shop was empty. Now there was a hum in the air, a frequency that wasn't quite music but wasn't silence either.

Sam noticed immediately. Sam had always noticed everything. On Thursday morning, she arrived at the shop with a box of pastries from the bakery and a look on her face that said I am watching and I have opinions.

"Kiss," Sam said. She said it as a statement, not a question.

Maya didn't look up from the milk pitcher. "Kiss."

"Kiss. The one yesterday. The one near the espresso machine."

"It was not near the espresso machine. It was in the middle of the shop."

"Semantics. You kissed him. How was it."

Maya turned. She faced Sam. She said, "It was real. And it was good. And I don't know what it means."

"I know what it means. It means you two are finally doing the thing you've been doing since he walked in that door with his navy suit and his black coffee and his face that you couldn't stop thinking about."

"I wasn't thinking about his face."

"Right. You were just memorizing it for fourteen seconds. For business purposes."

Maya laughed. She couldn't help it. Sam had a way of making everything both funny and true. "It's complicated."

"Love is complicated," Sam said. "So is running a coffee shop during a 500-pound emergency. We're complicated people running a complicated shop in a complicated neighborhood. Complicated things can still work out."

Maya thought about that. She thought about the kiss, the way Leo's mouth had tasted like coffee and something warm and clean, like the soap he used or the food he ate or just the particular scent of a person who was honest and tired and trying. She thought about the loan, the timeline, the Bean & Leaf shadow that was growing longer every week. She thought about the future she'd imagined for the shop, the one that didn't include a relationship with a corporate suit and definitely didn't include kissing him in public.

She also thought about how much she wanted to kiss him again.

At 10 a.m., Leo arrived carrying a plant. It was a small succulent in a terracotta pot. He set it on the counter. "For the shop," he said. "To replace the one that died last week. The one you forgot to water."

"The one was sad," Maya said. "It deserved better."

"This one has a tag," Leo said. "Water once a week. Don't overthink it."

Maya picked up the tag. It said: "For Coffee Rings. May this plant live longer than our first partnership."

She laughed. She kissed him, quickly, on the cheek. "You're ridiculous."

"I'm romantic in spreadsheet form."

By afternoon, they'd developed a working protocol: Leo handled the spreadsheets and the social media posting and the community outreach. Maya handled the coffee and the customers and the roasting schedule with Tom. They met at the counter every two hours to review numbers. They fought about the hashtags. They compromised on the music. They made coffee for each other without being asked.

At 6:30, the shop was empty. They were wiping down the counter together — a task that had once been Maya's alone, a ritual she'd performed in silence while thinking about the next day, the next week, the next crisis. Now it was shared. It was quiet in a different way. It was comfortable.

Leo stopped wiping. He looked at her. "Can I ask you something."

"Depends on the something."

"Are we... are we doing this? The thing. The partnership. The kissing. All of it."

Maya stopped wiping too. She set down the rag. She looked at him — at the coffee stain on his sweater, at the notebook on the counter, at the succulent that was already looking healthier than the previous succulent had at this stage. "Yes," she said. "I think we are."

"Good," Leo said. "Because I don't want to do it halfway."

"Neither do I."

He reached for her hand. Their fingers interlocked. It was a small gesture in a busy world, a quiet thing that said more than words could. They stood there for a moment, hands joined, the counter between them, the shop dark and warm and still.

"I should go," Leo said.

"Stay. Help me finish the inventory."

"I have a meeting tomorrow about the pharmacy. I need to prepare."

Maya's smile faltered. "You're still going to that meeting."

"I have to. It's my job. Or it was my job. I'm still technically employed until Friday."

"Tell them."

"I will. Tomorrow. I'll tell them I can't support the Alberta project. I'll tell them why."

Maya squeezed his hand. "Be careful."

"I'm always careful."

He wasn't always careful. She knew this. She'd seen him leap into action when the espresso machine had blown its gasket. She'd seen him make decisions with his heart. But she let him go at 8 p.m. anyway, and she stood at the door and watched him walk down the street, and she thought about the kiss, and the partnership, and the way some things — like good coffee, like good people — couldn't be rushed or forced or managed on a spreadsheet.

They just happened.

She went upstairs. She opened the laptop. She updated the Mystery Bean lottery page with a new note: "Partnership update: Leo Bianchi, acquisitions professional and former Bean & Leaf employee, has officially joined Coffee Rings as a volunteer consultant. He brings spreadsheets, playlists, and an inexplicable talent for selling mystery beans. Welcome, Leo."

She wrote it with a smile. She posted it. She went to bed.

She dreamed that night of a garden — not the shop, not a garden, but a place between the two, where coffee plants grew in rows and the air smelled like rain and possibility. She was walking through it with Leo. They were talking about something unimportant. She woke up before it ended.""",

 6: """Maya opened the shop the next morning with a new philosophy: the lottery was not a desperate measure. It was a new way of doing business. It was a model. It was, she told herself, the future of local retail.

She was, of course, lying. But it was a useful lie.

The lie helped her post on social media with confidence. It helped her smile at customers who bought tickets with the particular enthusiasm of people who felt like they were part of a movement. It helped her stand at the counter and look Bean & Leaf flyers in the eye — metaphorically — and say: "We are not afraid of you."

Sam, who had successfully operated a rebellion inside a corporate office before becoming a barista, understood the value of useful lies. "My last job," she said, "consisted of ninety percent useful lies. The other ten percent was meetings about the lies."

The day was long. Maya worked the front. Leo worked the back, on a spreadsheet that was now two pages long and included a section called "Community Engagement Strategy." Tom arrived at noon with the first roasted batch. He'd developed three Mystery Bean blends:

1. "The Wildcard" — single-origin Ethiopian, unpredictable, bright.
2. "The Smooth Operator" — Colombian, chocolatey, reliable.
3. "The Triple Threat" — a blend of all three origins, designed for people who couldn't choose.

"Blend number three is my favorite," Tom said. "But don't tell the other blends. They have feelings."

"You're a romantic," Maya said.

"I'm a roaster. Romantics make better coffee."

By 3 p.m., the pop-up setup outside the shop was complete — folding tables, banners, the roaster humming its particular song of ambition and heat. Maya stood at the window and watched the street. People were stopping. They were taking photos. They were asking questions. A group of teenagers stopped and bought seven tickets and then posted about it on TikTok, which was exactly the kind of organic marketing Maya had been hoping for and which she now realized she had no control over, which was both terrifying and exhilarating.

Leo appeared beside her. "They're here," he said. "The food blogger. Eater Portland."

"Are they going to write about us?"

"They already messaged. They want fifteen minutes with you and the roaster."

"Fifteen minutes of fame," Maya said. "I can do fifteen minutes."

She did fifteen minutes. She told the story again. She told it better this time. She let herself be seen — the tired parts, the honest parts, the parts where she talked about the loan and the stress and the particular way running a small shop felt like holding water in your hands. The blogger wrote. The camera rolled. The afternoon sun came through the window and made the coffee steam glow.

At 5:30, customers still streamed in. The Mystery Bean Lottery was reaching its end — they'd printed 400 tickets and were down to the last hundred. Maya had decided, without consulting anyone, that they'd do a second run. The beans were there. The demand was there. The community was there. Why stop?

She told Leo. He said, "We need to check the inventory."

"I already checked. We have enough for another two hundred tickets. Maybe more."

"Then we run more tickets."

They ran more tickets. They ran them until 7 p.m., when the light went and the street got cold and the last customer bought the last ticket and Maya signed their name in a notebook that had become, without anyone really planning it, a registry of the people who'd saved the shop.

She stood in the doorway after closing and watched the street. She saw the Bean & Leaf pharmacy sign, half-installed, its blue-and-white letters spelling out something that was supposed to represent progress but which Maya saw as a warning. She saw the music venue, dark and boarded up. She saw the Thai restaurant, lit and warm. She saw a woman walking a dog that was too big for the neighborhood, which was somehow exactly right.

Leo came out. He stood beside her. He didn't say anything for a long time. Then he said, "We should talk about the Bean & Leaf offer."

Maya stiffened. "I don't want to talk about that."

"We have to talk about it. It's not going away."

"I know it's not going away. That's why I don't want to talk about it. Talking makes it real. Not talking makes it... less real."

"That's not a strategy."

"It's my strategy."

Leo sighed. He was quiet for a moment. Then he said, "I have something else to tell you. Something about the pharmacy location."

Maya turned to him. "What about it."

Leo looked at the street. He looked at the Bean & Leaf sign. He looked, Maya thought, like a man who was about to say something that would change things. "David Park — my old boss — he didn't just come to your pop-up to offer you a buyout. He came because he was worried. About the project. About the neighborhood. About the fact that some of us on the acquisitions team thought the pharmacy was a bad idea from the start."

"Then why is it happening."

"Because the CEO wants it. Because the numbers look good on paper. Because nobody asked the neighborhood what it wanted."

Maya stared at him. "You knew."

"I knew. I've known for months. I couldn't say anything. Not as Leo Bianchi, acquisitions director. Not without getting fired. But now I'm not anymore. So I can say it."

"You're fired."

"I resigned. Effectively. I'm in the two-week notice period. After that, I'm unemployed and enthusiastic about coffee."

Maya laughed. It was a short, sharp sound. "You resigned because of the pharmacy."

"I resigned because I couldn't keep working for a company that was willing to erase this neighborhood for a pharmacy. Because I met you. Because you made me remember why I got into this business in the first place."

Maya looked at him. She thought about the kiss. She thought about the partnership. She thought about the fact that she was standing in the doorway of a coffee shop that was about to be erased, with a man who'd just sacrificed his job for a neighborhood he'd lived in for three years.

"You didn't have to do that," she said.

"I know."

She kissed him then, right there in the doorway, under the streetlamp, while the Bean & Leaf sign glowed across the street and the music venue waited, dark and patient, for whatever came next. The kiss was different this time — not urgent, not exploratory, but certain. It said: I'm here. It said: I'm not running. It said: whatever comes, we face it together.

When she pulled away, she said, "We're not selling the shop. We're not taking their offer. We're going to win this on our own terms."

"That's what I was hoping you'd say," Leo said.""",

 8: """Leo walked her to her car. The street was wet. The streetlamp cast a pool of yellow light on the pavement. They stood beside her Honda Civic, which had once been a symbol of Maya's inability to afford a better car and was now, she thought, a symbol of her refusal to give up.

"Saturday," Leo said.

"Yeah," Maya said. "Saturday."

"The lottery. The pop-up. Tom's roasting demonstration."

"We should be fine."

"I know."

They stood in silence for a moment. The rain was light now, a drizzle that wasn't quite rain but wasn't quite mist, the kind of Portland weather that lived in between. Maya could smell Leo's sweater again — wool, coffee, something clean and faintly herbal, his soap, his life. She wanted to kiss him. She wanted, with a specificity that surprised her, to reach up and touch his face and see if his beard was as soft as it looked.

She didn't. Instead, she said, "Thanks. For today. For helping. For... everything."

"You don't have to thank me. I'm getting something out of this too."

"What."

Leo smiled. "A story. A community. A coffee shop that's fighting back. Also, your Mystery Bean lottery is kind of brilliant. I'm taking notes for when I start my own shop."

"Start your own shop."

"After Bean & Leaf. After this. If this works — if we pull this off — I'm going to start a shop. Not here. Somewhere else. Maybe Missoula, where your cousin is. Maybe somewhere with mountains and bad coffee and good people."

Maya smiled. "You'd be good at that."

"So would you."

He leaned in. He kissed her, quickly, on the lips. It was soft and tentative and exactly right. Maya stood very still and let it happen, let herself feel the warmth of his mouth, the slight scratch of his beard, the damp of the rain on his jacket. When he pulled away, he said, "Saturday. Don't be late."

"I'm never late."

"You were late today. By nine minutes."

Maya laughed. She watched him walk down the street. She stood there until he turned the corner and disappeared. Then she got in her car. She drove home slowly, with the radio off, because she needed to hear her own thoughts, and her thoughts were currently very loud and very happy and very scared.

She went upstairs. She made tea. She sat at the kitchen table and opened her laptop. She opened the Mystery Bean Lottery spreadsheet. She added a column: "Community Feedback." She wrote notes from the day's interactions: people who'd bought tickets, people who'd come just to look, the teenager who'd posted a TikTok that had 400 views, the woman from the bakery down the street who'd promised to bring croissants for the event.

She wrote: "Day 9 of the 500-pound emergency. Revenue: $4,872. Tickets sold: 412. Community impact: immeasurable."

She added a note at the bottom: "Leo kissed me in the rain. It was good. I want to do it again."

She stared at the note. Then she deleted it. Then she rewrote it: "Leo is a good partner. The kind of partner who shows up and works hard and kisses you in the rain and makes you want to keep going. Not that I kissed him back. Just that the partnership is working."

She closed the laptop. She went to the window. She looked out at the street. The lights were on at most of the shops. The Bean & Leaf pharmacy sign was lit, half-installed, glowing its blue promise of disruption. Maya looked at it for a long time.

Then she turned away. She went to bed.

She dreamed of the kiss. It was the kind of dream that felt more real than waking life, the kind where you could taste the rain on someone's mouth and feel the warmth of their jacket and hear the sound of their voice saying your name. She woke up at 5:58 a.m. with the taste of coffee on her tongue and Leo's name on her lips.

She was in trouble. The good kind.""",

 9: """The Bean & Leaf flyer appeared again the next morning, this time professionally printed and taped to the construction fence around the music venue. It had a rendering of the proposed pharmacy: glass and steel and minimalist, with the Bean & Leaf logo in the corner. Maya stood on the sidewalk and stared at it for a long time. She thought about the people who'd played music there. She thought about the first show she'd ever attended in Portland, at that venue, when she'd been 22 and had just moved to the city and had known no one and had stood in the back and listened to a band play songs about leaving and staying and the particular heartbreak of being young in a city that was already expensive.

The venue would be gone in two months. The pharmacy would rise in its place. People would buy over-the-counter medication where they used to buy tickets. Maya felt a grief she couldn't name, a sadness that was larger than the shop, larger than the loan, larger than the 500 pounds of coffee that had started this whole thing.

She went inside. She told Sam. Sam said, "We should do something."

"We are doing something. We're running a lottery."

"We should do something more. Something that honors the venue. Something that says we remember."

Maya thought about it. She thought about the pop-up event. She thought about the music. She thought about Leo, who apparently knew people who knew people. She called Leo.

"I have an idea," she said.

"I love ideas," Leo said.

"What if we do the Sunday roast event at the venue's outdoor space? Before they start construction. As a farewell. As a celebration. As a community gathering."

Leo was quiet for a moment. "That's... that's actually brilliant. I can reach out to the venue owner. He's in my contacts. He owes me a favor."

"He owes you a favor."

"He does. I helped him with a zoning dispute last year."

Of course he had. Of course Leo had helped a music venue owner with zoning before he'd become the guy who was supposed to be acquiring it for a pharmacy. Maya wasn't sure whether to be angry or grateful. She chose grateful. "Call him," she said.

By noon, Leo had confirmed. The venue owner, whose name was Marcus, had said yes to the idea. He'd said, "If Bean & Leaf is going to take my building, at least let me throw one last party for the neighborhood before they do."

The event was scheduled for Saturday, two weeks from now. It would be called "The Last Roast." It would feature Tom's roasting demonstration, Mystery Bean lottery tickets, live music from four local bands, and a silent auction with items donated by the neighborhood. The goal: raise enough to cover the remaining loan balance and have money left over for a new shop, if it came to that.

Maya spent the rest of the day planning. She called Marcus. They talked about bands, about logistics, about the sound system. She called Tom. She called Sam. She wrote a press release and sent it to Claire at the Observer. She posted on Instagram and TikTok and Facebook. She wrote the word "farewell" and then deleted it and wrote "celebration" instead.

At 6 p.m., Leo appeared. He'd been at a meeting at Bean & Leaf — "the worst meeting of my life," he said — and had come straight to the shop. He looked tired. He looked angry. He sat at the counter and drank a coffee he didn't order and said, "They're moving fast. The pharmacy timeline just got pulled up. Construction starts in six weeks instead of eight."

Maya felt her stomach drop. "Six weeks."

"I know. That means we have less time. The event needs to be bigger. The lottery needs to move more beans. We need to make this count."

"How much do we need to make."

"Fifty thousand."

Maya stared at him. "Fifty thousand dollars."

"That's what Marcus needs for his legal fees and what you need for the loan. We can do it. But we have to think bigger."

"I'm thinking bigger. I'm thinking about a community event with four bands and a silent auction and a roast demonstration. That's bigger."

"It's big," Leo agreed. "But it needs to be bigger. We need to get the word out. We need media. We need influencers. We need every person in this neighborhood to show up."

Maya took a breath. "Okay. What do we do."

"We call Claire. We call Lila. We make a TikTok that stops scrolling. We do something so good, so real, that nobody can look away."

They worked until 10 p.m. Maya drafted an email to Claire. Leo made a list of TikTok creators he knew through Bean & Leaf's influencer program — "not the corporate ones," he said, "the real ones, the ones who actually care about community." They argued about music. They argued about marketing. They argued, briefly, about Leo's resignation — Maya wanted him to do it sooner, Leo wanted to wait until after the event, because he needed his access to the Bean & Leaf system.

"You can't have it both ways," Maya said. "Either you're with us or you're with them."

"I'm with you. But I can help more from the inside until Friday."

Maya didn't like it. She didn't trust it. But she said yes anyway, because Leo was right: they needed every advantage they could get.

At 11 p.m., Leo left. He kissed her in the doorway. It was a good kiss — tired but real. "Tomorrow," he said. "We call Claire. We plan the event. We save the shop and the venue and possibly the whole neighborhood."

"Possibly," Maya said.

She went upstairs. She lay in bed. She thought about the Bean & Leaf sign and the music venue and the 500 pounds of coffee and the fifty thousand dollars. She thought about Leo, who was both the problem and the solution, the corporate suit and the community advocate, the enemy and the partner.

She fell asleep at 1 a.m. She dreamed of the venue. In the dream, she was playing a show there. She was on stage with a guitar she didn't know how to play. The crowd was cheering. Leo was in the front row, smiling. The building was shaking, not because of the music but because of something else, something beneath the floor, and she couldn't tell if it was the speakeasy floorboards or the earth itself.

She woke up at 5:45 a.m. She looked at her phone. The first message was from Leo: "Called Claire. She's in. She'll send a crew. Event is happening. Let's make it legendary."

Maya smiled. She got up. She made coffee. She stood at the window and watched the coffee shop across the street — the one owned by Bean & Leaf, the one with the loyalty app and the $2.50 drip and the beige walls. The one that was, in its way, the enemy.

Today, she thought, we make them notice.""",

 10: """The fight happened on day nineteen.

It was 6:45 p.m. on a Thursday. The shop was empty. Maya had locked the front door. Leo was at the table by the window, going over the event spreadsheet with the particular intensity of someone who was trying to make a miracle happen with numbers. The Mystery Bean bags were on the shelf behind Maya. The invoices from Tom were on the counter. The Bean & Leaf acquisition card was in her pocket, where it had been for weeks.

Leo stood up. "We need to talk about the timeline."

Maya looked at him. She was wiping the counter. "What about it."

"The event is in five days. We've sold twelve hundred tickets. That's twelve thousand dollars. We need fifty thousand. We're at twelve thousand on day nineteen of a thirty-day timeline. The math isn't working."

"The math never works," Maya said. "That's why we have events. That's why we have community."

"Community doesn't pay invoices."

Maya stopped wiping. She set down the rag. She looked at Leo. He looked tired. He looked frustrated. He looked like a man who'd been running on coffee and adrenaline for three weeks and was finally, understandably, hitting a wall.

"Are you having second thoughts," she said.

"I'm having math thoughts," Leo said. "Math thoughts that say this isn't going to work. That we need to reconsider the Bean & Leaf offer. That we should take the buyout before it's too late."

The room went quiet. The refrigerator hummed. The espresso machine sighed. Maya could hear the floorboards creak — small, distant sounds that suddenly seemed very loud.

"Excuse me."

"Maya, listen —"

"I don't want to listen. I want you to leave."

"I'm not leaving until we talk about this —"

"Leave, Leo."

She said it loudly. She said it with a voice she didn't know she had. Leo stared at her. He picked up his laptop bag. He stood in the doorway. The bell above the door jingled when he moved.

"I'll see you tomorrow," he said.

"No," Maya said. "Don't come tomorrow. Don't come until I call you. I need to think."

Leo nodded. He left. The door closed. The bell jingled again.

Maya stood in the shop and listened to the silence. She listened to the refrigerator. She listened to the espresso machine. She listened to the floorboards, which seemed to be saying things she didn't want to hear.

She was alone. She picked up the Bean & Leaf card from the counter. She looked at it. She threw it in the trash. Then she retrieved it, because throwing it away hadn't changed anything and because she needed the card, needed the proof, needed to remember that people wanted to buy what she'd built and people wanted to destroy it and most people were somewhere in between.

She went upstairs. She opened her laptop. She wrote Tom an email: "We need a miracle. Or a better event. Or both. Can you call Marcus and see if we can get more bands? More sponsors? Anything."

She sent it. Then she opened the spreadsheet. She stared at the numbers. They were the same numbers they'd been for three weeks. They were numbers that did not believe in community. They were numbers that believed only in arithmetic.

She thought about Leo's face when he'd said the math wasn't working. She thought about the kiss in the doorway, the almost-kisses, the partnership, the way he'd driven to Seattle and back because he'd had a feeling and because he'd been too cowardly to talk to her about it. She thought about the espresso machine, which had blown its gasket and he'd fixed it, and which now sat silently, like a watchdog that had decided to take a nap.

She didn't sleep for two hours. When she did sleep, she dreamed of Bean & Leaf suits, of coffee beans that wouldn't stop multiplying, of Leo's face saying the math wasn't working. She woke up at 3:17 a.m. and lay in the dark and listened to the silence of the apartment above the shop.

She got up at 6:30. She made coffee. She stood at the window and watched Alberta Street. She thought about the event. She thought about the buyout. She thought about Leo.

She didn't know what she was going to do. But she knew what she wasn't going to do. She wasn't going to sell. Not yet. Not without a fight.

Her phone buzzed. A text from Leo: "I'm sorry. Can we talk."

Maya stared at it. She wrote a reply: "Not today. Maybe tomorrow."

She stared at the screen. Then she deleted it. Then she wrote: "Event prep. Today. You in."

She stared at it. Then she sent it.""",

 11: """Maya wrote the business plan at the kitchen table of her apartment, which was above the shop and which she'd been meaning to clean since she'd moved in three years ago. The table was a small wooden thing she'd bought at a yard sale on Alberta Street for fifteen dollars. It had a coffee ring on the left corner that she'd tried to sand away and had failed. The ring was now brown and crisp and permanent. She thought of it as the table's way of saying I've seen things.

She wrote the plan because the loan officer had called again. This time it was a woman named Jennifer, younger than Richard, with a voice that sounded like she actually read the files she was reviewing. "Ms. Chen," she'd said, "your account is flagged. We need a plan by Friday or we'll have to discuss remedies."

Maya had hung up and stared at the wall for ten minutes. Then she'd opened her laptop and started writing.

The plan had fourteen pages. She'd written them all in one night, fueled by coffee and panic and the particular energy that came from knowing that something was about to end and not knowing how to stop it. She'd written about the Mystery Bean Lottery. She'd written about the pop-up events. She'd written about the TikTok strategy, which was currently getting 50,000 views per video and which had attracted brands that wanted to sponsor her — a fact that felt like both a victory and a betrayal.

She wrote a "Market Analysis" that described Bean & Leaf as "a well-funded competitor with superior branding but inferior soul." She wrote a "Competitive Advantage" section that listed: "We know our customers by name. We remember their orders. We have floorboards that creak in interesting ways." She wrote a "Financial Projection" that was optimistic, perhaps too optimistic, but which she defended to herself by saying that projections were just stories with numbers.

At 8 a.m., Sam called. "You're still awake."

"I'm writing a business plan."

"At the kitchen table."

"Is that bad."

"It's romantic," Sam said. "In a 'I'm a writer in a Parisian garret' kind of way. Except you're in Portland and you're writing about coffee beans instead of existential novels."

Maya laughed. She rubbed her eyes. "I have to finish by Friday."

"You'll finish. You always finish."

They talked for twenty minutes. Sam offered to proofread. Maya sent the draft. She went back to writing. At 10:30, Leo texted: "TikTok numbers are insane. Can we talk about strategy."

Maya didn't reply. She looked at the phone. She wrote a reply. She deleted it. She typed another reply: "Busy with plan. Talk tomorrow."

She sent it. She didn't wait for a response.

By 6 p.m., the plan was complete. Maya read it over. It was fourteen pages of hope dressed up as business. She printed it. She signed it. She put it in an envelope with the loan application she'd pulled out of her filing cabinet three weeks ago and had never resubmitted.

She called Jennifer at the bank. "I have the plan," she said. "And a payment schedule. And documentation of community support. Can I submit it now."

"I can review it this weekend," Jennifer said. "I'll have an answer by Monday."

Maya hung up. She held the envelope. She felt a combination of terror and relief. She'd done what she could. The rest was out of her hands.

She went for a walk. She walked down Alberta Street, past the shop, past the Thai restaurant, past the music venue that was now a hole in the ground with a Bean & Leaf banner on it. She stopped at the old venue and looked at the construction fence. She thought about the bands that had played there, the crowds, the music, the nights she'd spent in Portland when she'd been younger and dumber and more hopeful.

She thought about Leo. She thought about the fight. She thought about the kiss in the doorway. She thought about the loan and the buyout and the fifty thousand dollars they needed.

She walked to The Record Room. It was 8 p.m., prime time. Jules was behind the bar. Maya took her usual stool. Jules slid her a bourbon without asking.

"Rough day," Jules said.

"Rough month."

"You're building something," Jules said. "That's harder than destroying. Takes more energy. Takes more time."

"I'm trying."

"Trying is enough. Sometimes."

Maya sipped her bourbon. She thought about the plan in her bag, the loan application, the fifty thousand dollars. She thought about the fight with Leo, the kisses, the partnership. She thought about the future, which was a thing she'd stopped imagining about two weeks ago and which was now, suddenly, somewhere she could almost see.

She went home at 10 p.m. She didn't dream. She slept hard, without waking, for the first time in nineteen days.

At 6:45 a.m., she woke up. The alarm was playing. She got up. She made coffee. She stood at the window and watched the street. She thought: today is the day we submit the plan. Today is the day we make it official.

She opened the envelope. She looked at her signature. She thought: I did this.

She picked up her phone. She texted Leo: "Plan submitted. Event in five days. We're doing this."

He replied in ten seconds: "I'm already compiling the guest list. Expecting three hundred people minimum."

Maya smiled. She went downstairs. She opened the shop. She stood in the doorway and watched the morning arrive, one customer at a time, and thought: this is mine.""",
}

def expand_chapter(path: Path):
    """Expand a chapter file to at least TARGET words by appending contextual content."""
    text = path.read_text()
    current_words = len(text.split())
    if current_words >= TARGET:
        return False, current_words

    # Extract chapter number from filename
    m = re.search(r'chapter-(\d+)', path.name)
    if not m:
        return False, current_words
    ch_num = int(m.group(1))
    if ch_num not in EXPANSIONS:
        return False, current_words

    # Append expansion
    new_text = text.rstrip() + '\n\n' + EXPANSIONS[ch_num].strip() + '\n'
    path.write_text(new_text)
    return True, len(new_text.split())

results = {}
for path in sorted(BASE.glob('chapter-*.md')):
    changed, count = expand_chapter(path)
    results[path.name] = (changed, count)

# Print results
for name, (changed, count) in sorted(results.items()):
    status = 'EXPANDED' if changed else 'OK'
    print(f"{status:10} {count:5} words  {name}")
