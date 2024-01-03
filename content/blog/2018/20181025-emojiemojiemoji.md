Title:Custom Emoji, Activate!
Date:2018-10-25 23:14
Tags:website, tech, emoji, mastodon
Oh hey, I just wanted to say, custom emoji work! :kay_grinning: I call it Pelimoji, a plugin for Pelican to allow simple replacement of colon-called emoji stored in a pre-defined directory.

This is based roughly off of Mastodon's CSS implementation using emojione. The script implementing this scours a setting directory for `.png` files, and then builds a list of those based on filename, so replacements are done using the filename minus the png, such as &#58;kay_grinning&#58; for the emoji in the opening! I'll try not to:bike_pump:this too much but it's very fun to have this working and usable.

This is based roughly off of the old replacer plugin for Pelican, functioning the same way but completely rewritten to make use of settings and building its own list for replacements to search for. The messy part is this requires scouring EVERY HTML file on write, but it works in the end. I'll have to find a nicer way to hook into this pre-write during the actual HTML-ization.