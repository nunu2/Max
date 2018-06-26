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

line = LINE()
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
line.log("Channel Token : " + str(channelToken))

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

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
#~~~~~~~•••~~~~~~~~~~~~~~•~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def helpmessage():
    helpMessage = """ SELFBOT
   ╔════════════
   ║     [🐈 ชุดคำสั่ง ที่ 1 🐈]      ║
   ╚════════════
╔═════════
║🍁🇹🇭 『คท』 =  แสดงคอนแท๊ก
║🍁🇹🇭 『ไอดี』=  แสดงไอดีเรา
║🍁🇹🇭 『เชิญ』= ดึงคนด้วยคท
║🍁🇹🇭 『พูด 』= สั่งสิริพูดตามที่พิม
║🍁🇹🇭 『มิด』= ดูมิดของเรา
║🍁🇹🇭 『ร่าง』= โชว์ร่างคิกเกอร์ของเรา
║🍁🇹🇭 『ของขวัญ』= ส่งของขวัญปลอม
║🍁🇹🇭 『มิด @』= ดูมิดคนอื่น
║🍁🇹🇭 『ขอเพลง 』= ขอเพลงจากยูทูป
║🍁🇹🇭 『บุก』= สั่งร่างคิกเกอร์เข้า
║🍁🇹🇭 『ออก』= สั่งร่างคิกเกอร์ออก
║🍁🇹🇭 『Tl: text』= สร้างชื่อใวรัส
║🍁🇹🇭 『Auto join: on/off』= 
║🍁🇹🇭 『Auto add: on/off』= 
║🍁🇹🇭 『ออกแชท: ไม่ออกแชท』
║🍁🇹🇭 『Clock: on/off』= เปิด/ปิด ชื่อเวลา
║🍁🇹🇭 『Up』= อัพเวลา
║🍁🇹🇭 『ขอลิ้ง』= ขอลิ้งห้อง
║🍁🇹🇭 『กลุ่ม』= เชคกลุ่ม
║🍁🇹🇭 『เพื่อนทั้งหมด』= รายชื่อเพื่อนเรา
║🍁🇹🇭 『บลอค』
║🍁🇹🇭 『แทก』= แทกทั้งห้อง
║🍁🇹🇭 『มึงตาย』= ลงใวรัส 
║🍁🇹🇭 『ลบรัน』= ลบห้องรัน
──┅═✥===========✥═┅──
ᴛᴇᴀᴍᴍᴏᴅᴅᴀʀᴋsᴇʟғʙᴏᴛ            ║
──┅═✥===========✥═┅──
║🍂🇨🇦 『ชื่อ 』= แสดงชื่อเรา
║🍂🇨🇦 『Gn: text 』= เปลี่ยนชื่อกลุ่ม
║🍂🇨🇦 『นน』= เชคคนแอบอ่าน
║🍂🇨🇦 『ออ』= เชคคนอ่าน 
║🍂🇨🇦 『ป้องกันหมด』
║🍂🇨🇦 『ปิดป้องกันหมด║
║🍂🇨🇦 『เชคค่า』= ตรวดสอบตั้งค่า
║🍂🇨🇦 『Link on/off』= เปิด/ปิดไลค์
║🍂🇨🇦 『Spam on/off』= รันแชต
║🍂🇨🇦 『เทส』= เชคบอท
║🍂🇨🇦 『Myginfo』
║🍂🇨🇦 『Gurl』
║🍂🇨🇦 『Glist』
║🍂🇨🇦 『ยูทูป 』= เปิดยูทูป
║🍂🇨🇦 『Phet: Tag』
║🍂🇨🇦 『Gcancel:』
║🍂🇨🇦 『Masuk Join』
║🍂🇨🇦 『Sa:yang』
║🍂🇨🇦 『Beb』
║🍂🇨🇦 『Cinta』
║🍂🇨🇦 『Sayang: 』
║🍂🇨🇦 『P:ulang』
║🍂🇨🇦 『Ban @』= แบน
║🍂🇨🇦 『Uban @』= แก้แบน
║🍂🇨🇦 『เชคดำ』= ดูว่าใครติดแบน
║🍂🇨🇦 『ล้างดำ』= ลบคนรายชื่อแบน
║🍂🇨🇦 『Comment :』
║🍂🇨🇦 『Banlist』
║🍂🇨🇦 『Cekban』
║🍂🇹🇭 『Clear ban』
║🍂🇹🇭 『Kill @ Fuck @』= เตะ
║🍂🇹🇭 『Speed / Sp』= เชคความใว
║🍂🇹🇭 『Hack @2@3@4』= ขโมยรูป
║🍂🇹🇭 『Ambilin @』
║🍂🇹🇭 『Sampul @』
║🍂🇹🇭 『แปลงร่าง @』=ก๊อป
║🍂🇹🇭 『กลับ』= กลับร่างเดิม
║🍂🇹🇭 『Keluar :@』
║🍂🇹🇭 『music』
║🍂🇹🇭 『.reboot』
║🍂🇹🇭 『Wikipedia』
║🍂🇹🇭 『Cleanse』
║🍂🇹🇭 『Bs』= เชคความใวคิกเกอร์
║🍂🇹🇭 『P1-P36 link on/off』
──┅═✥===========✥═┅──
👿 『Key』
👿 『Qr on/off』
👿 『Backup on/off』
👿 『Protect On/off』
👿 『Namelock On/off』
    
        ─┅═✥ᵀᴴᴬᴵᴸᴬᴺᴰ✥═┅─      
             [SELFBOT]
     ──┅═✥============✥═┅──"""
    
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech = """
╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Help protect〙
╠➩〘Help self〙
╠➩〘Help grup〙
╠➩〘Help set〙
╠➩〘Help media〙
╠➩〘Speed〙
╠➩〘Status〙
╚═════════════════
╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Protect on/off〙
╠➩〘Qr on/off〙
╠➩〘Invit on/off〙
╠➩〘Cancel on/off〙
╚═════════════════
╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Me〙
╠➩〘Myname: 〙
╠➩〘Mybio: 〙
╠➩〘Myname〙
╠➩〘Mybio〙
╠➩〘Mypict〙
╠➩〘Mycover〙
╠➩〘My,copy @〙
╠➩〘Mybackup〙
╠➩〘Getgrup image〙
╠➩〘Getmid @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getbio @〙
╠➩〘Getpict @〙
╠➩〘Getcover @〙
╠➩〘Mention〙
╠➩〘Lurk on/off〙
╠➩〘Lurkers〙
╠➩〘Mimic on/off〙
╠➩〘Micadd @〙
╠➩〘Micdel @〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Contact on/off〙
╠➩〘Autojoin on/off〙
╠➩〘Autoleave on/off〙
╠➩〘Autoadd on/off〙
╠➩〘Like me〙
╠➩〘Like friend〙
╠➩〘Like on〙
╠➩〘Respon on/off〙
╠➩〘Read on/off〙
╠➩〘Simisimi on/off〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Link on/off〙
╠➩〘Url〙
╠➩〘Cancel〙
╠➩〘Gcreator〙
╠➩〘Ki'ck @〙
╠➩〘Ulti @〙
╠➩〘Cancel〙
╠➩〘Gname: 〙
╠➩〘Gbroadcast: 〙
╠➩〘Cbroadcast: 〙
╠➩〘Infogrup〙
╠➩〘Gruplist〙
╠➩〘Friendlist〙
╠➩〘Blocklist〙
╠➩〘Ba'n @〙
╠➩〘U'nban @〙
╠➩〘Clearban〙
╠➩〘Banlist〙
╠➩〘Contactban〙
╠➩〘Midban〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Kalender〙
╠➩〘tr-id 〙
╠➩〘tr-en 〙
╠➩〘tr-jp 〙
╠➩〘tr-ko 〙
╠➩〘say-id 〙
╠➩〘say-en 〙
╠➩〘say-jp 〙
╠➩〘say-ko 〙
╠➩〘profileig 〙
╠➩〘checkdate 〙
╚═════════════════
"""
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate = """
   ╔════════════
   ║ [🇹🇭🐈 ชุดคำสั่ง ที่ 3 🐈🇹🇭] ║
   ╚════════════
╔═══════════════
║       🇹🇭เปิด/ปิดข้อความต้อนรับ🇹🇭
╠═══════════════
║🔥 Pea1 on ➠เปิดข้อความต้อนรับ
║🔥 Pea1 off ➠ปิดข้อความต้อนรับ
║🔥 Pea2 on ➠เปิดข้อความออกกลุ่ม
║🔥 Pea2 off ➠เปิดข้อความออกกลุ่ม
║🔥 Pea3 on ➠เปิดข้อความคนลบ
║🔥 Pea3 off ➠เปิดข้อความคนลบ
║🔥 Mbot on ➠เปิดเเจ้งเตือนบอท
║🔥 Mbot off ➠ปิดเเจ้งเตือนบอท
║🔥 M on ➠เปิดเเจ้งเตือนตนเอง
║🔥 M off ➠ปิดเเจ้งเตือนตนเอง
║🔥 เปิดแทค ➠เปิดกล่าวถึงเเท็ค
║🔥 ปิดแทค ➠ปิดกล่าวถึงเเท็ค
║🔥 เปิดเตะแทค ➠เปิดเตะคนเเท็ค
║🔥 ปิดแตะแทค ➠ปิดเตะคนเเท็ค
╚══════════════
╔══════════════
║         🇹🇭โหมดตั้งค่าข้อความ🇹🇭
╠═══════════════
║🔥 Pea1˓: ➠ไส่ข้อความต้อนรับ
║🔥 Pea2˓: ➠ไส่ข้อความออกจากกลุ่ม
║🔥 Pea3˓: ➠ไส่ข้อความเมื่อมีคนลบ
╚═══════════════
╔════════════════
║       🇹🇭โหมดเช็คตั้งค่าข้อความ🇹🇭
╠════════════════
║🔥 Pea1 ➠เช็คข้อความต้อนรับ
║🔥 Pea2 ➠เช็คข้อความคนออก
║🔥 Pea3 ➠เช็คข้อความคนลบ
╚════════════════
"""
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech ="""
   ╔════════════
   ║ [🇹🇭🐈 ชุดคำสั่ง ที่ 4 🐈🇹🇭]  ║
   ╚════════════
╔════════════════
║       By:✾แมวเป้✍Գန້さັএπັஞ➢
╠════════════════
║🇹🇭  เช็คแอด/เชคแอด ➠เช็คแอดมินกลุ่ม
║🇹🇭  ยกเลิก ➠ร่างเรายกเลิกค้างเชิญทั้งหมด
║🇹🇭  ยกเลิก1 ➠คิกเกอร์ยกเลิกค้างเชิญทั้งหมด
║🇹🇭  ข้อมูลเปิด ➠ดูข้อมูลตอนส่งคอนแทค
║🇹🇭  ข้อมูลปิด ➠ปิดดูข้อมูลตอนส่งคอนแทค
║🇹🇭  เตะแม่ง ➠สั่งคิกเกอร์บินห้อง
║🇹🇭  pop1 ➠เชคที่เราตั่งแทค
║🇹🇭  pop2 ➠เชคแทคสอง
║🇹🇭  pop1:.➠ตั้งแทค1
║🇹🇭  pop2:.➠ตั้งแทค2
║🇹🇭  เปิดแทค➠คำสั่งเปิดคทแทค
║🇹🇭  ปิดแทค➠คำสั่งปิดแทค
╚══════════════════════
"""

KAC = [line]
mid = line.getProfile().mid
#Amid1 = ki1.getProfile().mid
#Amid2 = ki2.getProfile().mid
#Amid3 = ki3.getProfile().mid
#Amid4 = ki4.getProfile().mid
#Amid5 = ki5.getProfile().mid
#Amid6 = ki6.getProfile().mid
#Amid7 = ki7.getProfile().mid
#Amid8 = ki8.getProfile().mid
#Amid9 = ki9.getProfile().mid
#Amid10 = ki10.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
mid = line.getProfile().mid
Bots = ["ใส่เอมไอดี",mid]
self = ["ใส่เอมไอดี",mid]
admin = "ใส่เอมไอดี"
admsa = "ใส่เอมไอดี"
owner = "ใส่เอมไอดี"
adminMID = "ใส่เอมไอดี"
Creator="ใส่เอมไอดี"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~☆~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
wait = {
    "alwayRead":False,
    "detectMention":True,    
    "kickMention":False,
    "steal":False,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"[ตอบรับ อัตโนมัติ]",
    'message':"Thanks for add Me SELFBOT",
    "lang":"JP",
    "comment":"AutoLike by Moddark",
    "commentOn":False,
    "acommentOn":False,
    "bcommentOn":False,
    "ccommentOn":False,
    "Protectcancl":False,
    "pautoJoin":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"SELFBOT",
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "ainvite":False,
    "binvite":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Pea1":False,
    "Pea2":False,
    "Pea3":False,
    "Notifed":False,
    "Notifedbot":False,
    "atjointicket":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "tag1":"\nโอ้ย...!!!!!!!!!โอ่ยยย!!!ไรอีกวะเนี้ย",
    "tag2":"\nเอาเข้าไป..✊แทคยุได้บักหำ",
	"posts":False,
	}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'
      
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~●~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
contact = line.getProfile()
mybackup = line.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


#contact = ki1.getProfile()
#backup = ki1.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki2.getProfile()
#backup = ki2.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki3.getProfile()
#backup = ki3.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki4.getProfile()
#backup = ki4.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki5.getProfile()
#backup = ki5.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki6.getProfile()
#backup = ki6.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki7.getProfile()
#backup = ki7.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki8.getProfile()
#backup = ki8.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki9.getProfile()
#backup = ki9.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki10.getProfile()
#backup = ki10.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus
                                  
#~~~~~~~~~••~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
        
