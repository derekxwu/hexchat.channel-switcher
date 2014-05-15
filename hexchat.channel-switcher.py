# Change HexChat tabs with /g
# Extension of /j functionality
import hexchat

__module_name__ = 'Channel Switcher'
__module_version__ = '0.1'
__module_description__ = 'Change tabs with /g'

def channel_switch(word, word_eol, userdata):
	if len(word) < 2 or len(word) > 3:
	# user fails
		hexchat.prnt('Usage: /g <#channel | user> [network]')
		return hexchat.EAT_ALL
	if len(word) == 3:
	# Changing server
		ctxt = hexchat.find_context(server=word[2])
	else:
	# Staying within current server
		ctxt = hexchat.get_context()
	try:
		if word[1][:1] == '#':
		# /g #channel
			ctxt.command("JOIN {0}".format(word[1]))
		else:
		# /g user
			ctxt.command("QUERY {0}".format(word[1]))
	except:
		hexchat.prnt('Not connected to {}.'.format(word[2]))
	return hexchat.EAT_ALL

hexchat.hook_command('g', channel_switch, help='"/g <#channel | user> [network]" to move to that context')
hexchat.prnt('hexchat.channel-switcher.py loaded')