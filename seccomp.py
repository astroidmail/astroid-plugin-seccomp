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

class SeccompPlugin (GObject.Object, Astroid.Activatable):
	object = GObject.property (type=GObject.Object)

	def do_activate (self):
		print ('seccomp: activated', __file__)

	def do_deactivate (self):
		print ('seccomp: deactivated')

	def get_user_agent(self):
		print ('seccomp: get_user_agent')
		return 'mutt'

#	def generated_mid(self):
#		print ('seccomp: generated_mid')
#		return ''
#
print ('seccomp: plugin loaded')
