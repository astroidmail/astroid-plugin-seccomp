import gi
gi.require_version ('Astroid', '0.1')
gi.require_version ('Gtk', '3.0')
gi.require_version ('WebKit', '3.0')
gi.require_version ('GMime', '2.6')
from gi.repository import GObject
from gi.repository import Gtk
from gi.repository import WebKit
from gi.repository import Astroid
from gi.repository import GMime
from random import choice, randrange

UAs = (
	'Apple Mail (2.3124)',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Thunderbird/45.1.1',
	'Mutt/1.5.24 (2015-08-30)',
	'Outlook',
	)

class SeccompPlugin (GObject.Object, Astroid.Activatable):
	object = GObject.property (type=GObject.Object)

	def do_activate (self):
		print ('seccomp: activated', __file__)

	def do_deactivate (self):
		print ('seccomp: deactivated')

	def do_get_user_agent(self):
		ua = choice(UAs)
		print ('seccomp: do_get_user_agent', ua)
		return ua

	def do_generate_mid(self):
		mid = '{}-{}-{}@{:x}.{:02x}'.format(
			randrange(0x10000),
			randrange(0x10000),
			randrange(0x10000),
			randrange(0x10000),
			randrange(0x100),
			)
		print ('seccomp: do_generate_mid', mid)
		return mid

print ('seccomp: plugin loaded')
