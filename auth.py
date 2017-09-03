#!/usr/bin/python
# -*- coding: utf-8 -*- 
username = raw_input("Login:")
password = raw_input("Password:")
useBigSmiles = raw_input("Use stickers(0 - no, 1 - yes):")

f = open("config.py", "w")
f.write("username = '" + username + "'\n")
f.write("password = '" + password + "'\n")
f.write("useBigSmiles = " + useBigSmiles + "\n")
f.close()
print
print "Done."
print
