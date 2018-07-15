#!/usr/bin/python

import json
import subprocess

space = []

df = subprocess.Popen(["df", "-P", "-k"], stdout=subprocess.PIPE)
output = df.communicate()[0]

for line in output.split("\n")[1:]:
	if len(line):
		try:
			device, size, used, available, percentage, mountpoint = line.split()
			space.append(dict(mountpoint=mountpoint, available=available))
		except:
			pass

print json.dumps(dict(space=space), indent=4)
#http://jpmens.net/2012/12/13/obtaining-remote-data-with-ansible-s-api/
