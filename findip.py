#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import *
from urllib import *
from time import *



banner = """
\033[1;32m
_|_|_|_|  _|                  _|      _|_|_|
_|            _|_|_|      _|_|_|        _|    _|_|_|
_|_|_|    _|  _|    _|  _|    _|        _|    _|    _|
_|        _|  _|    _|  _|    _|        _|    _|    _|
_|        _|  _|    _|    _|_|_|      _|_|_|  _|_|_|
                                              _|
                                              _|
\033[0m        \t-={ \033[1;36mBy kereh\033[0m }=-
"""

print banner
print
target = raw_input("Enter Your Ip Target :\033[1;32m ")
url = "http://ip-api.com/json/" +target
data = urlopen(url).read().decode("utf-8")
data2 = eval(data)
print
print("\033[1;36m[ # ] \033[1;32mRESULT >>>\033[0m")
print
print "\033[1;36m[ $ ] \033[0mAS :\033[1;32m ", str(data2["as"])
print "\033[1;36m[ $ ] \033[0mCOUNTRY :\033[1;32m ", str(data2["country"])
print "\033[1;36m[ $ ] \033[0mCITY :\033[1;32m ", str(data2["city"])
print "\033[1;36m[ $ ] \033[0mCOUNTRY CODE :\033[1;32m ", str(data2["countryCode"])
print "\033[1;36m[ $ ] \033[0mISP :\033[1;32m ", str(data2["isp"])
print "\033[1;36m[ $ ] \033[0mLATITUDE :\033[1;32m ", str(data2["lat"])
print "\033[1;36m[ $ ] \033[0mLONGTITUDE :\033[1;32m ", str(data2["lon"])
print "\033[1;36m[ $ ] \033[0mORG :\033[1;32m ", str(data2["org"])
print "\033[1;36m[ $ ] \033[0mQUERY :\033[1;32m ", str(data2["query"])
print "\033[1;36m[ $ ] \033[0mREGION :\033[1;32m ", str(data2["region"])
print "\033[1;36m[ $ ] \033[0mREGION NAME :\033[1;32m ", str(data2["regionName"])
print "\033[1;36m[ $ ] \033[0mTIME ZONE :\033[1;32m ", str(data2["timezone"])
print "\033[1;36m[ $ ] \033[0mZIP :\033[1;32m ", str(data2["zip"])
print "\033[1;36m[ $ ] \033[0mSTATUS :\033[1;32m ", str(data2["status"])
print "\033[0m"
