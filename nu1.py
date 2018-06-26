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
#line.log("Auth Token : " + str(line.authToken))
#channelToken = line.getChannelResult()
#line.log("Channel Token : " + str(channelToken))

#ki1 = LINE()
#ki1.log("Auth Token : " + str(line.authToken))
#channelToken = ki1.getChannelResult()
#ki1.log("Channel Token : " + str(channelToken))

#ki2 = LINE()
#ki2.log("Auth Token : " + str(line.authToken))
#channelToken = ki2.getChannelResult()
#ki2.log("Channel Token : " + str(channelToken))

#ki3 = LINE()
#ki3.log("Auth Token : " + str(line.authToken))
#channelToken = ki3.getChannelResult()
#ki3.log("Channel Token : " + str(channelToken))

#ki4 = LINE()
#ki4.log("Auth Token : " + str(line.authToken))
#channelToken = ki4.getChannelResult()
#ki4.log("Channel Token : " + str(channelToken))

#ki5 = LINE()
#ki5.log("Auth Token : " + str(line.authToken))
#channelToken = ki5.getChannelResult()
#ki5.log("Channel Token : " + str(channelToken))

#ki6 = LINE()
#ki6.log("Auth Token : " + str(line.authToken))
#channelToken = ki6.getChannelResult()
#ki6.log("Channel Token : " + str(channelToken))

#ki7 = LINE()
#ki7.log("Auth Token : " + str(line.authToken))
#channelToken = ki7.getChannelResult()
#ki7.log("Channel Token : " + str(channelToken))

#ki8 = LINE()
#ki8.log("Auth Token : " + str(line.authToken))
#channelToken = ki8.getChannelResult()
#ki8.log("Channel Token : " + str(channelToken))

#ki9 = LINE()
#ki9.log("Auth Token : " + str(line.authToken))
#channelToken = ki9.getChannelResult()
#ki9.log("Channel Token : " + str(channelToken))

#ki10 = LINE()
#ki10.log("Auth Token : " + str(line.authToken))
#channelToken = ki10.getChannelResult()
#ki10.log("Channel Token : " + str(channelToken))
