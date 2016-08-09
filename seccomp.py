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
	'Balsa 2.2.6',
	'Claws Mail 3.9.3 (GTK+ 2.24.22; i486-pc-linux-gnu)',
	'DTAG NGCS V4-0-7-0',
	'Evolution 3.8.3',
	'Foxmail 7.0.1.92[cn]',
	'Internet Mail Service (5.5.2657.72)',
	'iPad Mail (12B440)',
	'iPhone Mail (1bdfd6a)',
	'Lotus Notes Release 8.5.3FP4 SHF39 May 13, 2013',
	'Microsoft Outlook Express 6.00.3790.3959',
	'Microsoft Windows Live Mail 16.4.3528.331',
	'Mozilla 4.73 [en] (WinNT; I)',
	'Mulberry/4.1.0a1 (Mac OS X)',
	'Mutt 1.0i',
	'Novell GroupWise Internet Agent 8.0.3',
	'Open-Xchange Mailer v7.6.2-Rev28',
	'PHP/4.4.0',
	'PHPMailer [version 1.73]',
	'QUALCOMM Windows Eudora Version 6.2.5.6',
	'Sylpheed-Claws 2.6.0 (GTK+ 2.8.20; i486-pc-linux-gnu)',
	'The Bat! (v4.07.2) Personal',
	'T-Online eMail 6.10.0005',
	'Ximian Evolution 1.4.6 (1.4.6-2)',
	'YahooMailWebService/0.8.191.1',
	'Zimbra 8.6.0_GA_1178 (ZimbraWebClient - GC48 (Win)/8.6.0_GA_1178)',
	'BlackBerry Email (10.3.2.2876)',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Thunderbird/45.1.1',
	'Mutt/1.5.24 (2015-08-30)',
	'Microsoft Outlook 16.0',
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
