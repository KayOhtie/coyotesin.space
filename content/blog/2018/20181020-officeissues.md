Title:Which office suite am I using?
Date: 2018-10-20 16:30
Tags: parents, support, tech, msoffice, microsoft, google
I've been handling computer support for my dad for the better part of the last 15 years, give and take some times when he's had someone else working on it. I've helped him grow from using a local ISP's email, to using self-hosted email with his own domain on some Windows 2000 server, to using Exchange Server on a 2008 Small Biz server, and finally to using Google Apps for Biz. And this, my friends, is where the story begins.

Now, I have to preface this story with something. Throughout using Google, the debit card he had attached frequently wouldn't have money in the specific account for it and couldn't pay the monthly bill. He'd ignore the billing messages until it was too late and service was suspended. Sometimes he'd put money on that card, sometimes he changed to a different card. But without fail, this issue would occur, regardless of the card. Seriously why do some boomers have so many debit cards what the fuck. There were like, 6 or 7 different banks.

Now, every time the billing failed, I'd have to remind my dad we were paying Google to host his email. I'd have to play the exact same round of "20 Questions" to answer him, "yes we switched because your ISP wasn't reliable enough for Exchange", "no it's not running out of your office", "no this isn't free just because Gmail is free", "yes you still get emails from everyone". Every time it was the same questions. But let's move on.

Two years ago and change, I'm realizing Google is *not* the right solution for my dad. The Outlook sync client would always break and he hated using the web UI for both Gmail and Google Calendar. The support for opening Word files in the online one sucked, and you can't open Gdoc files in Microsoft Office (you can but it's finicky to do). It simply was not what he needed.

At this point I proposed Office 365. I put together pricing, benefits, and presented it. He balked at the cost...and also forgot he was paying Google, again, for everything. I pushed a few times but never got the OK, so I let it be for a while...until his server started to have hardware issues.

He'd been storing files on his server for years and the age of the drives was showing. I'd never had an opportunity to rebuild his server from the ground up in order to properly get RAID going for redundancy on drives (was going to RAID1 three drives, because I knew I'd not hear about hardware failure until two had died). So I warned him of the dangers and told him we needed to move his files. I finally get the OK to move him to Microsoft. He'd balked in part at the cost because "I already have office", except it was a pirate copy (oops).

I get his email and calendar and contacts migrated without a hitch and Outlook reconfigured. Since it's 365, sync is flawless, everything Just Works and all seems to be right with the world. And this time, learning from my mistakes with Google, I'm handling billing myself. I knew I'd always have money on my account for it. I even start getting him going with OneDrive but...

...Now instead of thinking it's self-hosted mail, he thinks it's with Google. It's like he's one step behind, constantly, on where things are. Now, he asks why I'm paying Microsoft for his mail. He says "But I thought we paid Google for that". Every time I re-explain my logic for the change. He also acknowledges the billing concern with why I took over it and refuse to relinquish the billing control.

During vacation last weekend, my dad had some issues getting his tablet to talk to email. He forgot his password (again), so I logged in under my admin account and reset it for him and we got him signed in to his phone and tablet again. Fast forward to Wednesday, he's at home now and tells me Outlook isn't syncing. Now, I made the mistake of thinking he remembered to update his password (you see where this is going).

But, more than that...he now told me Google was holding everything for ransom for $100 and thought Google was still using it. Turns out, he signed into his Google apps account in Chrome, and completely disregarded the password prompt in Outlook after what he thought was the password didn't work. I freak out, and finally get a chance to remote in. Plugged in his new password and all was well in Outlook, and I just signed him out of the defunct account in Chrome.

Moral of the story: Google sucks massively.