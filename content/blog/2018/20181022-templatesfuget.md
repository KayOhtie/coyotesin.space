Title:Templates fuget
Date: 2018-10-22 16:43
Tags: website, tech, google
Been meaning to make this site really look a lot nicer, so I've been faffing around with things and I think I've finally got the beginnings of something! I still need to theme <a href="/tags.html" class="link">the tags page</a> to look nicer, but the indexes look OK so far. 

I think I could do with having a visible sub-title for each type of index which will require fucking around with indexes a little more, and mapping specific templates to each index. Pelican does have some really neat flexibility, but the documentation is kind of poor. For instance, I had to explore to realize, hey, I can make a baseline no-content template that any fully-root pages can use (such as the home/index) and then make the actual `base.html` (which it uses for all the other themes typically) extend this `prebase.html` instead. 

Technicalities aside I really like what Pelican can do, and I want to see what I can do to push it further. I'd love to try and extend their documentation with better understanding, though their 'contributing' guide doesn't actually state anything about contributing to their somewhat lacking docs so...I guess I should just PR and find out how it goes? I guess @ me somewhere on input there! I've never really PR'd before to a public project.

Which...brings me to another question -- is it really worth it for me to host my own gitea instance at <a class="link" href="https://coding.coyotesin.space">coding.coyotesin.space</a> for my projects instead of github? I mean it's at least trivial to move something to Github -- make blank repo, add remote, `git push -u github`, done. Dunno! Anywho, that's all I was thinking right now.
