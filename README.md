#hexchat.channel-switcher.py
With HexChat, you can quickly switch tabs with `/j #channel` or `/query username`. This script merges that functionality and adds an optional `network` parameter to switch to channels/queries on other servers.

###Installation
Copy this into Hexchat's `addons` folder.

###Usage
#####`/g <#channel | username>`
Changes the focus to the specified channel or query tab. Opens a tab for the channel or query if none already exists.
`/g #help`

#####`/g <#channel | username> server`
Same as above, but the channel or query will be found on the specified server. If `server` is not found, nothing happens.
`/g #help Freenode`