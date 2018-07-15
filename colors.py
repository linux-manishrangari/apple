#!/usr/bin/env python

from fabric.colors import blue, green, red, yellow
import subprocess

# Simple command
print yellow("Running free...")
subprocess.call(['free'], shell=True)

print

print yellow("Running free -m...")
subprocess.call(['free','-m'], shell=True)

# Command with shell expansion
subprocess.call('echo $HOME', shell=True)

subprocess.check_call(['false'])
