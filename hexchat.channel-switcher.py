# Change HexChat tabs with /g
# Extension of /j functionality
import hexchat

__module_name__ = 'Channel Switcher'
__module_version__ = '1.0'
__module_description__ = 'Change tabs with /g'

def channel_switch(word, word_eol, userdata):
	if len(word) == 3:
		# Server specified
		ctxt = hexchat.find_context(server=word[2])
		if ctxt:
			go_tab(ctxt, word[1])
		else:
			hexchat.prnt('Not connected to {}').format(word[2])

	elif len(word) == 2:
		# Server not specified
		# Find existing channel/user, prioritizing current server
		# and then whatever is found first. If nothing is found,
		# /j channel or /query user on current server
		curr_ctxt = hexchat.get_context()
		channel_list = []
		for channel in hexchat.get_list('channels'):
			if channel.channel.lower() == word[1].lower():
				channel_list.append(channel)
				if channel.server == curr_ctxt.get_info('server'):
					# same tab name, same server; this is what we're looking for
					# so we can just join straight from our current context(server)
					go_tab(curr_ctxt, word[1])
					return hexchat.EAT_ALL
				# otherwise we just end up with a list of channels with matching names
		if len(channel_list)>0:
			go_tab(channel_list[0].context, word[1])
			# if we didn't find a matching tab in our server, but did find a match,
			# just use the first one that was found
		else:
			go_tab(curr_ctxt, word[1])
			# Didn't find anything, so open tab on this server
	else:
		# User failed input
		hexchat.prnt('Usage: /g <#channel | user> [network]')
	return hexchat.EAT_ALL

def go_tab(context, tab_name):
	if tab_name[:1] == '#':
		context.command('JOIN {}'.format(tab_name))
	else:
		context.command('QUERY {}'.format(tab_name))

def unload_callback(userdata):
	hexchat.prnt('RIP channel_switcher')

hexchat.hook_command('g', channel_switch, help='"/g <#channel | user> [network]" to move to that context')
hexchat.hook_unload(unload_callback)
hexchat.prnt('hexchat.channel-switcher.py loaded')