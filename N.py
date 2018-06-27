# -*- coding: utf-8 -*-

from linepy import *
from akad.ttypes import Message
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

#line = LINE()
#line = LINE("AuthToken")
#line = LINE("Email","Password")
#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#line = LINE()
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

ki1MID = ki1.profile.mid
ki1Profile = ki1.getProfile()
ki1Settings = ki1.getSettings()

ki2MID = ki2.profile.mid
ki2Profile = ki2.getProfile()
ki2Settings = ki2.getSettings()

ki3MID = ki3.profile.mid
ki3Profile = ki3.getProfile()
ki3Settings = ki3.getSettings()

ki4MID = ki4.profile.mid
ki4Profile = ki4.getProfile()
ki4Settings = ki4.getSettings()

ki5MID = ki5.profile.mid
ki5Profile = ki5.getProfile()
ki5Settings = ki5.getSettings()

ki6MID = ki6.profile.mid
ki6Profile = ki6.getProfile()
ki6Settings = ki6.getSettings()

ki7MID = ki7.profile.mid
ki7Profile = ki7.getProfile()
ki7Settings = ki7.getSettings()

ki8MID = ki8.profile.mid
ki8Profile = ki8.getProfile()
ki8Settings = ki8.getSettings()

ki9MID = ki9.profile.mid
ki9Profile = ki9.getProfile()
ki9Settings = ki9.getSettings()

ki10MID = ki10.profile.mid
ki10Profile = ki10.getProfile()
ki10Settings = ki10.getSettings()


oepoll = OEPoll(ki10)
oepoll = OEPoll(ki9)
oepoll = OEPoll(ki8)
oepoll = OEPoll(ki7)
oepoll = OEPoll(ki6)
oepoll = OEPoll(ki5)
oepoll = OEPoll(ki4)
oepoll = OEPoll(ki3)
oepoll = OEPoll(ki2)
oepoll = OEPoll(ki1)
oepoll = OEPoll(line)
#call = Call(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line,ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
Exc = [ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
lineMID = line.getProfile().mid
ki1MID = ki1.getProfile().mid
ki2MID = ki2.getProfile().mid
ki3MID = ki3.getProfile().mid
ki4MID = ki4.getProfile().mid
ki5MID = ki5.getProfile().mid
ki6MID = ki6.getProfile().mid
ki7MID = ki7.getProfile().mid
ki8MID = ki8.getProfile().mid
ki9MID = ki9.getProfile().mid
ki10MID = ki10.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID,ki1MID,ki2MID,ki3MID,ki4MID,ki5MID,ki6MID,ki7MID,ki8MID,ki9MID,ki10MID]
Family=["u9ed31efc986199adedb27386c9b1f458",lineMID,ki1MID,ki2MID,ki3MID,ki4MID,ki5MID,ik6MID,ki7MID,ki8MID,ki9MID,ki10MID]
admin=['u9ed31efc986199adedb27386c9b1f458',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#

