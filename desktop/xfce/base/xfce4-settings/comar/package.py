#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

	try:
		os.system ("sed -i 's:XFCE\;::' /etc/xdg/autostart/polkit-gnome-authentication-agent-1.desktop")
		os.system ("/bin/echo 'X-XFCE-Autostart-Override=true' >> /etc/xdg/autostart/at-spi-dbus-bus.desktop")
		os.system ("/bin/echo 'Hidden=false' >> /etc/xdg/autostart/pulseaudio.desktop")
	except:
		pass

def postRemove():

	try:
		os.system ("sed -i '/X-XFCE-Autostart-Override=true/d' /etc/xdg/autostart/at-spi-dbus-bus.desktop")
		os.system ("sed -i '/Hidden=false/d' /etc/xdg/autostart/pulseaudio.desktop")
	except:
		pass
