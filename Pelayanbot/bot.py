##########  #########  #            ##     #         #    ##       ##      #
#        #  #          #           #  #     #       #    #  #      # #     #
#        #  #          #          #    #     #     #    #    #     #  #    #
##########  #########  #         ########     #####    ########    #   #   #
#           #          #        #        #      #     #        #   #    #  #
#           #          #       #          #     #    #          #  #     # #
#           #########  ###### #            #    #   #            # #      ##

#########################
#####>>>PELAYANBOT<<<####
###>>>Author : mfd7<<<###
#########################
import ch
import random
import sys
import re
import cgi
import traceback
import time
import __future__
import urllib
import datetime
import binascii
import urllib
import json
import os
import math
import TebakFilm
from xml.etree import cElementTree as ET
if sys.version_info[0] > 2:
    import urllib.request as urlreq
else:
    import urllib2 as urlreq

if sys.version_info[0] < 3:
  class urllib:
    parse = __import__("urllib")
    request = __import__("urllib2")
  input = raw_input
  import codecs
  import Queue as queue
else:
  import queue
  import urllib.request
  import urllib.parse

prefix = "~"

startTime = time.time()

hgf = 'pelayanbot'
fgh = 'pelayanbot007'

##Roomlock
roomlock = []
try:
    file = open("roomlock.txt","r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            roomlock.append(name.strip())
    print("[INFO] roomlock loaded.")
    file.close()
except:
    print("ERROR: No file roomlock.txt")
    print("10 seconds to read the error")
    time.sleep(10)
    exit()
time.sleep(1)

###Owners
owners = []
try:
    file = open("owners.txt","r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            owners.append(name.strip())
    print("[INFO] owners loaded.")
    file.close()
except:
    print("ERROR: No file owners.txt")
    print("10 seconds to read the error")
    time.sleep(10)
    exit()
time.sleep(1)

###Assistant
assistant = []
try:
    file = open("assistant.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            assistant.append(name.strip())
    print("[INFO]Assistant loaded...")
    file.close()
except:
    print("[ERROR]no file named assistant")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)

###Mods
manager = []
try:
    file = open("manager.txt", "r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            manager.append(name.strip())
    print("[INFO]manager loaded...")
    file.close()
except:
    print("ERROR, no file named manager")
    print("2 second to read the error")
    time.sleep(2)
    exit()
time.sleep(1)

##WL/Reg
registered = []
try:
    file = open("registered.txt","r")
    for name in file.readlines():
        if len(name.strip()) > 0:
            registered.append(name.strip())
    print("[INFO] Registered users loaded.")
    file.close()
except:
    print("ERROR: No file registered.txt")
    print("10 seconds to read the error")
    time.sleep(10)
    exit()
time.sleep(1)

##ROOM
rooms = []
f = open("rooms.txt", "r")
print("[INFO]LOADING rooms...")
for name in f.readlines():
  if len(name.strip())>0: rooms.append(name.strip())
f.close()


## NICKNAMES
nicks=dict()
f=open ("nicks.txt","r")
print ("[INFO] Loading Nicks....")
time.sleep(1)
for line in f.readlines():
    try:
        if len(line.strip())>0:
            user , nick = json.loads(line.strip())
            nicks[user] = json.dumps(nick)
    except:
        print("[error] Can't load nick %s" % line)
    f.close()

## DEFINITIONS
dictionary = dict()
f=open("definitions.txt", "r")
print("[INFO]LOADING DEFINITIONS...")
time.sleep(1)
for line in f.readlines():
    try:
        if len(line.strip())>0:
            word, definition, name = json.loads(line.strip())
            dictionary[word] = json.dumps([definition, name])
    except:
        print("[ERROR]Can't load definition: %s" % line)
f.close()

ipinfo = dict()
f = open ("ipinfo.txt","r")
print ("[INFO] Loading IPINFO...")
time.sleep(1)
for line in f.readlines():
    try:
        if len(line.strip())>0:
            user , info = json.loads(line.strip())
            ipinfo[user] = json.dumps(info)
    except:
        print("[error] Can't load ipinfo %s" % line)
    f.close()


def getUptime():
  """
 Returns the number of seconds since the programs started.
 """
  #do return startTime if you want the process start time
 
  return time.time() - startTime
 
## System Uptime
def uptime():
 
  try:
    f = open( "/proc/uptime")
    contents = f.read().split()
    f.close()
  except:
    return "Cannot open uptime file"
 
  total_seconds = float(contents[0])
 
  ## Helper vars:
  MINUTE = 60
  HOUR = MINUTE * 60
  DAY = HOUR * 24
 
  ## Get the days, hours, etc:
  days = int( total_seconds / DAY )
  hours = int( ( total_seconds % DAY ) / HOUR )
  minutes = int( ( total_seconds % HOUR ) / MINUTE )
  seconds = int( total_seconds % MINUTE )
 
  ## Build up the pretty string (like this: "N days. N hours, N minutes, N seconds")
  string = ""
  if days > 0:
    string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
  if len(string) > 0 or hours > 0:
    string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
  if len(string) > 0 or minutes > 0:
    string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
  string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
 
  return string;

###GS
def googleSearch(search):
  try:
    encoded = urllib.parse.quote(search)
    rawData = urllib.request.urlopen("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="+encoded).read().decode("utf-8")
    jsonData = json.loads(rawData)
    searchResults = jsonData["responseData"]["results"]
    full = []
    val = 1
    for data in searchResults:
      if "youtube" in data["url"]:
        data["url"] = "http://www.youtube.com/watch?v="+data["url"][35:]
      full.append("<br/>"+"(<b>%s</b>) %s -> %s" % (val,data["title"],data['url']))
      val = val + 1
    return '<br/>'.join(full).replace('https://','http://')
  except Exception as e:
    return str(e)

def darenime(self):
        try:
            import urllib.request
            with urllib.request.urlopen("http://darenime.com/") as url:
                udict = url.read().decode()
                udict = udict.replace('\r', '').replace('\n', '')
                judul = re.findall('<h2>(.+?)</h2>', udict, re.S)
                l=[]
                num = -1
                for i in judul:
                    x = '<br/>(%s) <u>%s</u>' %(num,i)
                    l.append("<a target='_blank'>"+x+"</a>")
                    num = num+1
                string = ' '.join(l[2:12])
                return string
        except Exception as e:
            return str(e)

def yt(args):
    search = args.split()
    url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
    udict = url.read().decode('utf-8')
    data = json.loads(udict)
    rest = []
    for f in data["items"]:
      rest.append(f)
 
    d = random.choice(rest)
    link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
    videoid = d["id"]["videoId"]
    title = d["snippet"]["title"]
    uploader = d["snippet"]["channelTitle"]
    descript = d["snippet"]['description']
    count    = d["snippet"]["publishedAt"]
    return "<br/>Result for <b>"+args+"</b>:<br/> %s <br/><br/><br/><br/><br/><br/><br/><b>%s</b><br/><b>Uploader:</b> %s<br/><b>Uploaded on:</b> %s<br/><b>Descriptions:</b> %s ...<br/> " % (link, title, uploader, count, descript[:200])

def short(args):
    search = args
    url = urlreq.urlopen("http://api.adf.ly/api.php?key=6153c92b3a2229b9d691b6ac806b6121&uid=10846981&advert_type=int&domain=adf.ly&url="+search)
    udict = url.read().decode('utf-8')
    return udict

def imdb(args):
    sss = args.replace(" ","+")
    url = urlreq.Request("http://www.omdbapi.com/?t="+sss+"&y=&plot=full&r=json", headers={'User-Agent' : "Magic Browser"})
    con = urlreq.urlopen(url)
    udict = con.read().decode('utf-8')
    data = json.loads(udict)
    d = data
    title = d["Title"]
    year = d["Year"]
    release = d["Released"]
    runtime = d["Runtime"]
    genre = d["Genre"]
    director = d["Director"]
    plot = d["Plot"]
    image = d["Poster"]
    rating = d["imdbRating"]
    tipe = d["Type"]
    ID = d["imdbID"]
    link = "http://www.imdb.com/title/"+ID+"/?ref_=nv_sr_1"
    return "<br/>"+image+"<br/><br/><b><i>"+title+"</i></b><br/><b>Year: </b>"+year+"<br/><b>Genre: </b>"+genre+"<br/><b>Rating: </b>"+rating+"<br/><b>Type: </b>"+tipe+"<br/><b>Director: </b>"+director+"<br/><b>Released: </b>"+release+"<br/><b>Runtime: </b>"+runtime+"<br/><b>Link: </b>"+link+"<br/><b>Synopsis:</b><br/>"+plot

def yts(self):
        try:
            import urllib.request
            with urllib.request.urlopen("https://yts.to/") as url:
                udict = url.read().decode()
                udict = udict.replace('\r', '').replace('\n', '')
                judul = re.findall("<div class=\"browse-movie-bottom\">(.+?)</div>", udict, re.S)
                l=[]
                num = -3
                for i in judul:
                    x = '<br/>(%s)%s' %(num,i)
                    l.append(x)
                    num = num+1
                string = ' '.join(l[4:14])
                return string
        except Exception as e:
            return str(e)

def topyts(self):
        try:
            import urllib.request
            with urllib.request.urlopen("https://yts.to/") as url:
                udict = url.read().decode()
                udict = udict.replace('\r', '').replace('\n', '')
                judul = re.findall("<div class=\"browse-movie-bottom\">(.+?)</div>", udict, re.S)
                l=[]
                num = 1
                for i in judul:
                    x = '<br/>⌠%s⌡%s' %(num,i)
                    l.append(x)
                    num = num+1
                string = ' '.join(l[0:4])
                return string
        except Exception as e:
            return str(e)

def youtube(args):
    search = args.split()
    url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
    udict = url.read().decode('utf-8')
    data = json.loads(udict)
    rest = []
    for f in data["items"]:
      rest.append(f)
 
    d = random.choice(rest)
    finale = {}
    link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
    videoid = d["id"]["videoId"]
    title = d["snippet"]["title"]
    uploader = d["snippet"]["channelTitle"]
    descript = d["snippet"]['description']
    count    = d["snippet"]["publishedAt"]
    finale.update({"title":title, "videoid":videoid, "uploader":uploader, "descriptions":descript, "viewcount":count, "link":link})
    return finale

def saveRank(self):
    f = open("owners.txt","w")
    f.write("\n".join(owners))
    f.close()
    f = open("assistant.txt","w")
    f.write("\n".join(assistant))
    f.close()
    f = open("manager.txt","w")
    f.write("\n".join(manager))
    f.close()
    f = open("registered.txt","w")
    f.write("\n".join(registered))
    f.close()

def sntonick(username):
    user = username
    if user in nicks:
        nick = json.loads(nicks[user])
        return nick
    else:
        return user.capitalize()

def IPinfo(self, user, message, room):
 if room.getLevel(ch.User("pelayanbot")) > 0:
    user = user.name
    info = message.ip
    ipinfo[user]=json.dumps(info)
    f = open("ipinfo.txt", "w")
    for user in ipinfo:
        info = json.loads(ipinfo[user])
        f.write(json.dumps([user, info])+"\n")
    f.close()

def ipinfoio(args, user):
    try:
      if args:
        sss = json.loads(ipinfo[args])
        url = urlreq.urlopen("http://ip-api.com/json/"+sss)
        udict = url.read().decode('utf-8')
        data = json.loads(udict)
        d = data
        ip = d["query"]
        city = d["city"]
        region = d["regionName"]
        country = d["country"]
        loc1 = d["lat"]
        loc2 = d["lon"]
        org = d["isp"]
        time = d["timezone"]
        return "<br/><b>ID :</b> "+args+"<br/><b>IP : </b>"+str(ip)+"<br/><b>City : </b>"+str(city)+"<br/><b>Region : </b>"+str(region)+"<br/><b>Country : </b>"+str(country)+"<br/><b>Location : </b>"+str(loc1)+", "+str(loc2)+"<br/><b>Org : </b>"+str(org)+"<br/><b>Timezone : </b>"+str(time)
      else:
        user = user.name
        sss = json.loads(ipinfo[user])
        url = urlreq.urlopen("http://ip-api.com/json/"+sss)
        udict = url.read().decode('utf-8')
        data = json.loads(udict)
        d = data
        ip = d["query"]
        city = d["city"]
        region = d["regionName"]
        country = d["country"]
        loc1 = d["lat"]
        loc2 = d["lon"]
        org = d["isp"]
        time = d["timezone"]
        return "<br/><b>ID :</b> "+user+"<br/><b>IP : </b>"+str(ip)+"<br/><b>City : </b>"+str(city)+"<br/><b>Region : </b>"+str(region)+"<br/><b>Country : </b>"+str(country)+"<br/><b>Location : </b>"+str(loc1)+", "+str(loc2)+"<br/><b>Org : </b>"+str(org)+"<br/><b>Timezone : </b>"+str(time)   
    except:
        return "Fail to check :("

def helper(args):
          sss = args
          minute = 60
          hour = minute * 60
          day = hour * 24
          days =  int(sss / day)
          hours = int((sss % day) / hour)
          minutes = int((sss % hour) / minute)
          seconds = int(sss % minute)
          string = ""
 
          if days > 0:
 
            string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
 
          if len(string) > 0 or hours > 0:
 
            string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
 
          if len(string) > 0 or minutes > 0:
 
            string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
 
          string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
          return string


        
class TestBot(ch.RoomManager):

  def getAccess(self, user):
    if user.name in owners: return 4
    elif user.name in assistant: return 3
    elif user.name in manager : return 2
    elif user.name in registered : return 1
    else : return 0

  def onInit(self):
    self.setNameColor("000DFF")
    self.setFontColor("A84DF7")
    self.setFontFace("Calibri")
    self.setFontSize(12)
    self.enableBg()
    self.enableRecording()
#connecting and disconnecting

  def onConnect(self, room):
    print("[+] Connected to "+room.name)


  def onMessage(self, room, user, message):
    try:

      ##split message
      msgdata = message.body.split(" ",1)
      if len(msgdata) > 1:
        cmd, args = msgdata[0], msgdata[1]#command ama arg
      else:
        cmd, args = msgdata[0],""#command doang
        cmd=cmd.lower()
      #if prefix
      if len(cmd)>0:
        if cmd[0]==prefix:
          used_prefix = True
          cmd = cmd[1:]
        else:
          used_prefix= False
      else:
        return
      def pars(args):
          args = args.lower()
          for name in room.usernames:
            if args in name:return name

      IPinfo(self, user, message, room)
      ###############################
#######commands section########
###############################
      ##without prefix
      if self.getAccess(user) > 0:
          ###test
          if "test" in message.body:
            room.message("You are pregnant "+sntonick(user.name)+" :o",True)
          ##Malam
          if "malam" in message.body:
              if user.name == "mfd7":
                room.message("Kan kita di kansas cuy masih siang")
              else:
                room.message("Disini siang cuyy gua di kansas 8)")
          ##Anjing
          if message.body.startswith("anjing"):
            room.message(random.choice(["wah parah","gua gebuk juga lo"]))
          ###Makasih
          if message.body.startswith("makasih pelayan"):
            room.message("Oh.You are welcome "+sntonick(user.name)+".",True)
          ###cung
          if message.body == ("cung"):
            room.message(random.choice(["STFU "+sntonick(user.name),"yes , "+sntonick(user.name)+"?"]),True)
          ###kacung
          if message.body == ("kacung"):
            room.message(random.choice(["STFU "+sntonick(user.name),"yes , "+sntonick(user.name)+"?"]),True)
          ###pelayan
          if message.body == ("pelayan"):
            room.message(random.choice(["Yes "+sntonick(user.name)+"??"]),True)
          ###Ngantuk
          if message.body.startswith("ngantuk"):
            room.message(random.choice(["minum baygon..","nungging aja :|"]))
          ###salto
          if message.body == ("salto"):
            room.message(random.choice(["neneklu tuh suruh salto","lo kira gua pemaen sirkus"]))
          ###bawain makan
          if message.body == ("bawain makan"):
            room.message(random.choice(["idih ogahh","iya ini "+sntonick(user.name)+" ^.^"]),True)
          ###omg
          if message.body.startswith("omg"):
            room.message(random.choice(["=_=","x_x",":*"]))
          ###makasih
          if message.body.startswith("makasih"):
            room.message("sama samaaa "+sntonick(user.name)+".",True)
          ###hugs
          if message.body == ("hugs"):
            room.message("Yay I love hugs. *bear hugs "+sntonick(user.name)+"*.",True)
          ###gtg
          if message.body.startswith("gtg"):
            room.message(random.choice(["oke byeee","see u"+sntonick(user.name),"take care vrohh ;)"]),True)
          ###afk
          if message.body.startswith("afk"):
            room.message(random.choice(["byeee "+sntonick(user.name),"Who care?"+sntonick(user.name)]),True)
          ###brb
          if message.body.startswith("brb"):
            room.message(random.choice([sntonick(user.name)+" noooooo don't leave meeee","Hurry back "+sntonick(user.name)+".","I'll miss you "+sntonick(user.name)]),True)
          ### back
          if message.body.startswith("back"):
            room.message(random.choice(["Welcome back "+sntonick(user.name)+"  I'm so happy to see you again.",]),True)
          ### huo
          if "huo" in message.body:
            room.message(random.choice(["berisikk!!","waw suaranya baguss ^,^","anjir gua sakit perut:3","bubar nyok :|"]))
          ###dance
          if message.body == ("dance"):
            room.message("(>^.^)>")
            room.message("<(^.^<)")
            room.message(",(^,^)/")
          if message.body == (",(^,^)/"):
            room.message("(>^.^)>")
            room.message("<(^.^<)")
            room.message(",(^,^)/")
          ### love
          if message.body == ("love"):
            room.message("*h*")
          ### ikan1
          if message.body == ("ikan"):
            room.message("><>")
          ### ikan2
          if message.body == ("><>"):
            room.message(random.choice(["ihh ada ikann jelek amatt","mancing ahh","ngapain sih bikin ikann"]))
          ### bot
          if message.body == ("bot"):
            room.message(random.choice(["hmm","brrr"]))
          ### laper
          if message.body.startswith("laper"):
            room.message(random.choice(["Ya terus?","makan nih sendal gua","kalo laper ya tidur lah"]))
          ### siang
          if message.body.startswith("siang"):
            room.message("iya selamat siang " +sntonick(user.name)+ " ^.^",True)
          ### Kupu1
          if message.body == ("kupu-kupu"):
            room.message(random.choice(["8|8","ihh ogahh"]))
          ### Kupu2
          if message.body == ("8|8"):
            room.message("wiihh ada kupu-kupuu","anjer gua takut serangga" +stonick(user.name)+ "!!",True)
          ### bye
          if message.body.startswith("bye"):
            room.message("*waves*")
          ### stop
          if message.body == ("stop"):
            room.message("*stop*")
          ##minum
          if "minum" in message.body:
            room.message(random.choice(["Ini Minumnya ^.^","Elu nyuruh gua? gua santet lu","Bawa ndiri lahh","Seenaknya lu nyuruh gua"]))

      ##Help
      if used_prefix and cmd == "help" and self.getAccess(user) > 0:
        room.message("<br/><b>"+"→→Pelayanbot←←"+"</b>"+"<br/>"+"prefix = ~ "+"<br/>Recomended to using flash version ;)<br/>"+"for more command do ~cmds",True)
      ####Join
      if used_prefix and cmd == "join":
        if self.getAccess(user) > 2:
            if args == "":return
            if args in self.roomnames:
                room.message("I'm there already :|")
            else:
                self.joinRoom(args)
                room.message("going to <b>"+args.title(),True)
                f = open("rooms.txt","w")
                f.write("\n".join(self.roomnames))
                f.close()

      if used_prefix and cmd == "reload" and self.getAccess(user) == 4:
        imp.reload(Command)
        room.message("Reload Success")
      ###Leave
      elif used_prefix and cmd == "leave":
          if self.getAccess(user) > 2:
              if args:
                if self.getAccess(user) > 2:
                  room.message("okay i leave from <b>%s</b> ;)" % args, True)
                  self.leaveRoom(args)
                  f = open("rooms.txt","w")
                  f.write("\n".join(self.roomnames))
                  f.close()
                else: return
              if not args:
                room.message("siapp")
                self.leaveRoom(room.name)
                f = open("rooms.txt","w")
                f.write("\n".join(self.roomnames))
                f.close()
          else: room.message("Only Owners and Assistant can do this")

      if used_prefix and cmd == "lockstatus":
        if room.name in roomlock:
          room.message("<br/><b>Lockstatus</b><br/>Room Lock = Locked",True)
        else:
            room.message("<br/><b>Lockstatus</b><br/>Room Lock = Unlocked",True)

      ##ROOMLOCK
      if self.getAccess(user) < 2 and room.name in roomlock: return

      if used_prefix and cmd == "lock" and self.getAccess(user) > 1:
        if room.name not in roomlock:
          rnm = room.name
          roomlock.append(rnm)
          f = open("roomlock.txt","w")
          f.write("\n".join(roomlock))
          f.close()
          room.message("Locked")
        else:
            room.message("This room was already locked")
      if used_prefix and cmd == "unlock" and self.getAccess(user) > 1:
        if room.name in roomlock:
          rnm = room.name
          roomlock.remove(rnm)
          f = open("roomlock.txt","w")
          f.write("\n".join(roomlock))
          f.close()
          room.message("Unlocked")
        else:
            room.message("This room already unlocked")

      
          ###Google Search
      if used_prefix and cmd == "gs" or used_prefix and cmd == "googlesearch":
        room.message("<br/><b>Result for "+args+": </b>"+googleSearch(args),True)
        
      ###GIS
      if used_prefix and cmd == "gis" and self.getAccess(user) > 0 or used_prefix and cmd == "gi" and self.getAccess(user) > 0:
        try:
          import urllib
          url = urllib.request.urlopen("http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="+urllib.parse.quote(args))
          udict = json.loads(url.read().decode('utf-8'))["responseData"]["results"]
          udict = random.choice(udict)
          img = random.choice([udict["unescapedUrl"]])
          room.message("<br/><b>"+"@"+user.name+" I found your keyword"+"<br/>"+"keyword : "+args.capitalize()+"<br/>"+img, True)
        except:
              room.message(args.capitalize()+' is not found :/')
      ###Say
      if used_prefix and cmd == "say" and self.getAccess(user) > 0:
            if len(args) > 0:
                room.deleteUser(user)
                room.message(args,True)
            else:
                room.message("say what?")


        #########################################################################
        #define to define ~define= name : definition/to remove ~define name remove
        #########################################################################
      if used_prefix and cmd == "df"  and len(args) > 0 and self.getAccess(user) > 0:
        try:
          try:
            word, definition = args.split(" =", 1)
            word = word.lower()
          except:
            word = args
            definition = ""
          if len(word.split()) > 4:
            room.message("Fail coy:'v")
            return
          if len(args.split()) > 1 and args.lower().split()[1] == "remove" and user.name.lower()=="yell":
            if word in dictionary:
              definition, name = json.loads(dictionary[word])
              if name == user.name:
                del dictionary[word]
                f = open("definitions.txt", "w")
                for word in dictionary:
                  definition, name = json.loads(dictionary[word])
                  f.write(json.dumps([word, definition, name])+"\n")
                f.close()
                room.message("Definition removed.")
                return
              else:
                room.message("Only the user who defined it")
                return
            else:
              room.message("<b>%s</b> gaada df itu. Ketik <b> define %s= definition</b>" % args, True)
          elif len(definition) > 0:
            if word in dictionary:
              room.message("<b>%s</b> defined already." % user.name.capitalize(), True)
            else:
              dictionary[word] = json.dumps([definition, user.name])
              f = open("definitions.txt", "w")
              for word in dictionary:
                definition, name = json.loads(dictionary[word])
                f.write(json.dumps([word, definition, name])+"\n")
              f.close()
              room.message("done, definition saved ;)")
          else:
            if word in dictionary:
              definition, name = json.loads(dictionary[word])
              room.message("<br/><b>"+"ID "+"= "+name+"<br/>"+"Keyword : "+word+"<br/>"+"definitions :"+"</b>"+"<br/>"+definition+"<br/>",True)   
            else:
              room.message("<b>%s</b> Not defined. Do <b> ~df %s= definition</b>  ^^" % (args, args), True)
        except:
          room.message("Gagal:'v")

      ##Udf
      if used_prefix and cmd == "udf" and self.getAccess(user) > 0:
        try:
          word = args
          if word in dictionary:
            definition, name = json.loads(dictionary[word])
            if name == user.name or name == "mfd7":
              del dictionary[word]
              f = open("definitions.txt", "w")
              for word in dictionary:
                definition, name = json.loads(dictionary[word])
                f.write(json.dumps([word, definition, name])+"\n")
              f.close()
              room.message("done, definition removed")
              return
            else:
              room.message("fail")
              return
          else:
            room.message("fail")
        except:
          room.message("fail")
          return

      
            
          
      ##jodoh
      if used_prefix and cmd == "jodoh" and self.getAccess(user) > 0:
            try:
                nama1, nama2 = args.split(" ", 1)
                persen=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]
                hasil=random.choice(persen)
                hasil=int(hasil)
                if nama2 =="":room.message("@"+user.name+" ketik !jodoh (nama1)<spasi>(nama2)");return
                if hasil == 0:
                    room.message("@"+user.name+" kecocokan "+nama1+" dengan "+nama2+" = %s"% hasil+"% beuh ga ada harapan :'v")
                if hasil < 50:
                    room.message("@"+user.name+" kecocokan "+nama1+" dengan "+nama2+" = %s"% hasil+"% | hadeh ga cocok putus aja dah lu :P")
                if hasil > 49 and hasil < 60:
                    room.message("@"+user.name+" kecocokan "+nama1+" dengan "+nama2+" = %s"% hasil+"% | hmm lumayan coba jalanin aja dulu :)")
                if hasil > 59 and hasil < 100:
                    room.message("@"+user.name+" kecocokan "+nama1+" dengan "+nama2+" = %s"% hasil+"% | wah cocok banget gua doa-in moga tetap langeng")
                if hasil == 100 :
                    room.message("@"+user.name+" kecocokan "+nama1+" dengan "+nama2+" = %s"% hasil+"% | wah wah langsung nikah aja *lol* ")
            except:
                room.message("@"+user.name+" ketik jodoh (nama1)<spasi>(nama2)")
      ##pm
      if used_prefix and cmd == "pm" and len(args) > 0 and self.getAccess(user) > 1:
            try:
                name, message = args.split(" " , 1)
                self.pm.message(ch.User(name) , message +" - from " + user.name)
                room.message("Sent a message to %s" % name)
            except:
                room.message("Do ~pm <username> <message>")
      ##Setnick
      if used_prefix and cmd == "setnick" and self.getAccess(user) == 4:
          try:
              if args:
                    user, nick = args.split(" ",1) 
                    nicks[user]=json.dumps(nick)
                    room.message("Done ;)")
                    f = open("nicks.txt", "w")
                    for user in nicks:
                        nick = json.loads(nicks[user])
                        f.write(json.dumps([user, nick])+"\n")
                    f.close()
              else:
                  room.message("Who?")
          except:
              room.message("The Fucking Nick Please")
                    
                
      #### Bgimg
      if used_prefix and cmd =="bgimg"  and self.getAccess(user) > 0:
        try:
          args=args.lower()
          picture = '<a href="http://st.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/msgbg.jpg" style="z-index:59" target="_blank">http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/msgbg.jpg</a>'
          prodata = '<br/>'+picture
          room.message("<br/><b>"+"User Name : "+args+"</b>"+prodata,True)
        except:
          room.message(""+args+" doesn't exist:'v")

      ####Mynick
      if used_prefix and cmd == "mynick" and self.getAccess(user) > 0:
          user=user.name
          if user in nicks :
            nick = json.loads(nicks[user])
            room.message(user+" is nicked : "+nick,True)
          else:
            room.message("You have no nickname registered in my nick[] database.", True)
      ##Snick      
      if used_prefix and cmd == "snick" and self.getAccess(user) > 0:
          user=args
          if user in nicks :
            nick = json.loads(nicks[user])
            room.message(user+" is nicked : "+nick,True)
          else:
            room.message("You have no nickname registered in my nick[] database.", True)            

      ##Nick
      if used_prefix and cmd == "nick" and self.getAccess(user) > 0:
          try:
              if args:
                  nick = args
                  user=user.name      
                  nicks[user]=json.dumps(nick)
                  room.message ("okay "+user+" now u will be called "+nick,True)
                  print("[SAVE] SAVING NICKS...")
                  f = open("nicks.txt", "w")
                  for user in nicks:
                    nick = json.loads(nicks[user])
                    f.write(json.dumps([user, nick])+"\n")
                  f.close()
          except:
              room.message("Fail:'v")


      ##del          
      if used_prefix and cmd == "del" and self.getAccess(user) > 2:
        name = pars(args.split()[0].lower())
        room.clearUser(ch.User(name))
        room.deleteUser(user)


                
       ###chatroom
      if used_prefix and cmd == "chatroom" and self.getAccess(user) > 1:
        room.message("I see: " + str(room.usercount))

      ### mods
      if used_prefix and cmd == "mods" and self.getAccess(user) > 0:
        room.message("The owner is : "+str(room.ownername)+". And the mods are: "+str(room.modnames)+" .")

      ### username list
      if used_prefix and cmd == "userlist" and self.getAccess(user) > 0:
        io = len(room.usernames)
        oi = list()
        for i in room.usernames:
            oi.append(i)
        room.message(str(io)+" People are here : <br/>"+", ".join(oi),True)

      ##banlist
      if used_prefix and cmd == "banlist" and self.getAccess(user) > 0:
            room.message("Banlist : "+str(room.banlist),False)

      ##find
      if used_prefix and cmd == "find" and len(args) > 0 and self.getAccess(user) > 0:
              name = args.split()[0].lower()
              if not ch.User(name).roomnames:
                  room.message("I Don't Know")
              else:
                  room.message("U can found %s in %s " % (args, ", ".join(ch.User(name).roomnames)),True)

      ###profilepic
      if used_prefix and cmd == "pfpic" and self.getAccess(user) > 0 or cmd == "PfPic" and self.getAccess(user) > 0 or cmd == "ProfilePic" and self.getAccess(user) > 0 or cmd == "profilepic" and self.getAccess(user) > 0:
                link = "http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg" % (args[0], args[1], args)
                room.message("<br/><b>"+"User ID : "+args+"</b>"+"<br/>"+link,True)
      ###Rank
      if used_prefix and cmd == "rank" or cmd == "Rank":
          if not args:
            if user.name in owners and not user.name in registered:
              room.message(user.name+" You are rank 4 [<f x12FF0000='0'>O<f x12CCFF00='0'>W<f x1200FF66='0'>N<f x120066FF='0'>E<f x12CC00FF='0'>R]",True)
            elif user.name in assistant and not user.name in registered and not user.name in manager and not user.name in owners:
              room.message(user.name+" You are rank 3 [ASSISTANT]",True)  
            elif user.name in manager and not user.name in registered and not user.name in owners:    
              room.message(user.name+" You are rank 2 [MANAGER]",True)
            elif user.name in registered and not user.name in owners:
              room.message(user.name+" You are rank 1 [OFFICER]",True)
            elif user.name not in registered and not user.name not in manager and user.name not in assistant and user.name not in owners:
              room.message(user.name+" You are not registered, please ask to Owner or Assistant",True)
          if args:
              sss = args
              if sss in owners:
                  room.message(sss.title()+" is an <f x12FF0000='0'>O<f x12CCFF00='0'>W<f x1200FF66='0'>N<f x120066FF='0'>E<f x12CC00FF='0'>R",True)
              if sss in assistant:
                  room.message(sss.title()+" is an <f x120000FF='0'><b>Assistant",True)
              if sss in manager:
                  room.message(sss.title()+" is a  <f x1200FFFF='0'><b>Manager",True)
              if sss in registered:
                  room.message(sss.title()+" is an <f x12FF00FF='0'><b>Officer",True)
              if sss not in owners and sss not in assistant and sss not in manager and sss not in registered:
                  room.message(sss.title()+" was never whitelisted")
      ###wl
      if used_prefix and cmd == "wl" and self.getAccess(user) > 2:
          if args:
              if args in room.usernames:
                  registered.append(args)
                  f = open("registered.txt","w")
                  f.write("\n".join(registered))
                  f.close()
                  f = open("manager.txt","w")
                  f.write("\n".join(manager))
                  f.close()
                  f = open("assistant.txt","w")
                  f.write("\n".join(assistant))
                  f.close()
                  room.message("Now, u can use me "+args.title()+" ^^")
              else:
                  room.message("fail :'v")
          if not args:
              if user.name not in registered:
               room.message("Ask to Assistant or Owner ;)")

      ##Bgtime
      if used_prefix and cmd=="bgtime" and len(args) > 0 and self.getAccess(user) > 0:
        try:
            args=args.lower()
            if len(args.split(" ", -1)) != 1:
                return
            if len(args) == 1:
                f_args, s_args = args, args
            elif len(args) > 1:
                f_args, s_args = args[0], args[1]
        except:
            room.message(".")
 
        def getBgtime(args):
            expired = True
            url = ("http://st.chatango.com/profileimg/" + f_args + "/" + s_args + "/" + args + "/mod1.xml")
            f = urlreq.urlopen(url)
            data = f.read().decode("utf-8")
            e = ET.XML(data)
            bg = e.findtext("d")
            bg = int(urlreq.unquote(bg))
            if bg - int(time.time()) < 0:
              total_seconds = int(time.time())-bg
            else:
              total_seconds = bg-int(time.time())
              expired = False
 
            # Helper vars:
            MINUTE  = 60
            HOUR    = MINUTE * 60
            DAY     = HOUR * 24
 
            # Get the days, hours, etc:
            days    = int( total_seconds / DAY )
            hours   = int( ( total_seconds % DAY ) / HOUR )
            minutes = int( ( total_seconds % HOUR ) / MINUTE )
            seconds = int( total_seconds % MINUTE )
 
            # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
            string = ""
            if days > 0 or days < 0:
                string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
            if len(string) > 0 or hours > 0:
                string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
            if len(string) > 0 or minutes > 0:
                string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + " and "
            string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
            if expired == True:
              return "Dia belom beli Premi :'v "
            elif expired == False:
              return "time is: "+string
        room.message("<br/><b>" + args + "</b> BG " + getBgtime(args), True)
    ###Clear
      elif used_prefix and cmd == "clear":
        if room.getLevel(self.user) > 0:
          if self.getAccess(user) > 2:
            room.clearall(),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
            room.clearUser(ch.User(random.choice(room.usernames))),
          else: room.message("Only rank 3 and 4 can do this ;)")
        else:
          room.message("Gua bukan mod disini gile lu")

      ##BC
      if used_prefix and cmd == "broadcast" or used_prefix and cmd== "bc":
          if self.getAccess(user) > 2:
              for room in self.rooms:
                if args == "": return
                else:
                  room.message("Broadcast from - "+sntonick(user.name)+" : "+args, True)
          else:
              room.message("[<b>%s</b>] Only rank >2 can do this" % "ERROR", True)


      ###Rooms
      elif used_prefix and cmd == "rooms" and self.getAccess(user) > 0:
          j = list()
          for i in self.roomnames:
            j.append("<b>"+i+"</b>"+"("+str(self.getRoom(i).usercount)+")")
          room.message("|| I'm Currently in: "+", ".join(j)+" ||", True)
          #room.message("||i'm in : <b>%s</b> ||" % (", ".join(self.roomnames)), True)


      ##Setrank
      if used_prefix and cmd == "setrank":
          if self.getAccess(user) < 4:return
          try:
              if len(args) >=3:
                  nama = args
                  if pars(nama) == None:
                      nama = nama
                  elif pars(nama) != None:
                      nama = pars(nama)
                  nama, rank = args.lower().split(" ", 1)
                  if rank == "4" and nama not in owners:
                      owners.append(nama)
                      f = open("owners.txt","w")
                      f.write("\n".join(owners))
                      f.close()
                      room.message("Success!")
                      if nama in manager:
                          manager.remove(nama)
                          f = open("manager.txt","w")
                          f.write("\n".join(manager))
                          f.close()
                      if nama in registered:
                          registered.remove(nama)
                          f = open("registered.txt","w")
                          f.write("\n".join(registered))
                          f.close()
                      if nama in assistant:
                          assistant.remove(nama)
                          f = open("assistant.txt","w")
                          f.write("\n".join(assistant))
                          f.close()
                  if rank == "3" and nama not in assistant:
                      assistant.append(nama)
                      f = open("assistant.txt","w")
                      f.write("\n".join(assistant))
                      f.close()
                      room.message("Success!")
                      if nama in manager:
                          manager.remove(nama)
                          f = open("manager.txt","w")
                          f.write("\n".join(manager))
                          f.close()
                      if nama in registered:
                          registered.remove(nama)
                          f = open("registered.txt","w")
                          f.write("\n".join(registered))
                          f.close()
                      if nama in owners:
                          owners.remove(nama)
                          f = open("owners.txt","w")
                          f.write("\n".join(owners))
                          f.close()
                  if rank == "2" and nama not in manager:
                      manager.append(nama)
                      f = open("manager.txt","w")
                      f.write("\n".join(manager))
                      f.close()
                      room.message("Success!")
                      if nama in assistant:
                          assistant.remove(nama)
                          f = open("assistant.txt","w")
                          f.write("\n".join(assistant))
                          f.close()
                      if nama in registered:
                          registered.remove(nama)
                          f = open("registered.txt","w")
                          f.write("\n".join(registered))
                          f.close()
                      if nama in owners:
                          owners.remove(nama)
                          f = open("owners.txt","w")
                          f.write("\n".join(owners))
                          f.close()
                  if rank == "1" and nama not in registered:
                      registered.append(nama)
                      f = open("assistant.txt","w")
                      f.write("\n".join(assistant))
                      f.close()
                      room.message("Success!")
                      if nama in assistant:
                          assistant.remove(nama)
                          f = open("assistant.txt","w")
                          f.write("\n".join(assistant))
                          f.close()
                      if nama in manager:
                          manager.remove(nama)
                          f = open("manager.txt","w")
                          f.write("\n".join(manager))
                          f.close()
                      if nama in owners:
                          owners.remove(nama)
                          f = open("owners.txt","w")
                          f.write("\n".join(owners))
                          f.close()
          except:
              room.message("Fail:'v")

      ###cmds
      if used_prefix and cmd == "cmds":
        if user.name in owners and not user.name in assistant and not user.name in manager and not user.name in registered:
            room.message("<br/><b>»"+user.name+" You are rank 4 [OWNER]«"+"<br/>"+"command availabe :"+"</b><br/>"+
                         "join ♠ leave ♠ gs(googlesearch) ♠ gis(googleimage search) ♠ nyts(new 10 movie in yts) ♠ yts [genre] ♠ sy/msy(Search Movie in yts) ♠ mty(multychat) ♠ ms(movie search) ♠ fax ♠ tf(tebak film) ♠ new/ci(new movies in Cinemaindo) ♠ say ♠ df(definition) ♠ seedict ♠ udf(remove definition) ♠ jodoh ♠ pm ♠ bgimg(background image) ♠ nick(setnick) ♠ mynick(check ur nick) ♠ del(delete message) ♠ chatroom ♠ mods(see mods) ♠ userlist ♠ banlist ♠ find(find id chatango) ♠ pfpic(profile picture) ♠ rank(see ur rank) ♠ wl(whitelist) ♠ bgtime(background time) ♠ clear(clear message) ♠ rooms(pelayan rooms) ♠ bc(broadcast) ♠ setrank ♠ na(new anime in animeku.tv) ♠ msa(search in animeku.tv) ♠ topyts ♠ miy(movie info yts) ♠ ai(anime info) ♠ ne(new episodes Animeku.tv) ♠ topanime ♠ mi(movie info) ♠ joi(jurnal otaku indonesia trending) ♠ joi news ♠ anime genre ♠ imdb ♠ ipinfo ♠ ban ♠ unban ♠ sut ♠ uptime ♠ tracker",True)
        if user.name in assistant and not user.name in owners and not user.name in manager and not user.name in registered:
            room.message("<br/><b>»"+user.name+" You are rank 3 [ASSISTANT]«"+"<br/>"+"command availabe :"+"</b><br/>"+
                         "join ♠ leave ♠ gs(googlesearch) ♠ gis(googleimage search) ♠ nyts(new 10 movie in yts) ♠ sy/msy(Search Movie in yts) ♠ ms(movie search) ♠ mty(multychat) ♠ fax ♠ tf(tebak film) ♠ new/ci(new movies in Cinemaindo) ♠ say ♠ df(definition) ♠ seedict ♠ udf(remove definition) ♠ jodoh ♠ pm ♠ bgimg(background image) ♠ nick(setnick) ♠ mynick(check ur nick) ♠ del(delete message) ♠ chatroom ♠ mods(see mods) ♠ userlist ♠ banlist ♠ find(find id chatango) ♠ pfpic(profile picture) ♠ rank(see ur rank) ♠ wl(whitelist) ♠ bgtime(background time) ♠ clear(clear message) ♠ rooms(pelayan rooms) ♠ bc(broadcast) ♠ na(new anime in animeku.tv) ♠ msa(search in animeku.tv) ♠ topyts ♠ miy(movie info yts) ♠ ai(anime info) ♠ ne(new episodes Animeku.tv) ♠ topanime ♠ mi(movie info) ♠ joi(jurnal otaku indonesia trending) ♠ joi news ♠ anime genre ♠ imdb ♠ ipinfo ♠ ban ♠ unban ♠ sut ♠ uptime ♠ tracker",True)
        if user.name in manager and not user.name in owners and not user.name in assistant and not user.name in registered:
            room.message("<br/><b>»"+user.name+" You are rank 2 [MANAGER]«"+"<br/>"+"command availabe :"+"</b><br/>"+
                         "gs(googlesearch) ♠ gis(googleimage search) ♠ nyts(new 10 movie in yts) ♠ yts/msy(Search Movie in yts) ♠ ms(movie search) ♠ fax ♠ tf(tebak film) ♠ mty(multychat) ♠ new/ci(new movies in Cinemaindo) ♠ say ♠ df(definition) ♠ seedict ♠ jodoh ♠ pm ♠ bgimg(background image) ♠ nick(setnick) ♠ mynick(check ur nick) ♠ chatroom ♠ mods(see mods) ♠ userlist ♠ banlist ♠ find(find id chatango) ♠ pfpic(profile picture) ♠ rank(see ur rank) ♠ bgtime(background time) ♠ rooms(pelayan rooms) ♠ bc(broadcast) ♠ na(new anime in animeku.tv) ♠ msa(search in animeku.tv) ♠ topyts ♠ miy(movie info yts) ♠ ai(anime info) ♠ ne(new episodes Animeku.tv) ♠ topanime ♠ mi(movie info) ♠ joi(jurnal otaku indonesia trending) ♠ joi news ♠ anime genre ♠ imdb ♠ ipinfo ♠ sut ♠ uptime ♠ tracker",True)
        if user.name in registered and not user.name in owners and not user.name in assistant and not user.name in manager and not room.name in roomlock:
            room.message("<br/><b>»"+user.name+" You are rank 1 [OFFICER]«"+"<br/>"+"command availabe :"+"</b><br/>"+
                         "♠ reg tf ♠ ranker ♠ bgtime ♠ jodoh ♠ nick ♠ mty(multychat) ♠ mynick ♠ rank ♠ find(find user) ♠ gs(googlesearch) ♠ gis(googleimage search) ♠ nyts(new 10 movie in yts) ♠ yts/msy(Search Movie in yts) ♠ ms(movie search) ♠ new/ci(new movies in Cinemaindo) ♠ say ♠ df(definition) ♠ seedict ♠ bgimg(background image) ♠ chatroom ♠ mods(see mods) ♠ userlist ♠ banlist ♠ find(find id chatango) ♠ pfpic(profile picture) ♠ rooms(pelayan rooms) ♠ na(new anime in animeku.tv) ♠ msa(search in animeku.tv) ♠ topyts ♠ miy(movie info yts) ♠ ai(anime info) ♠ ne(new episodes Animeku.tv) ♠ topanime ♠ mi(movie info) ♠ joi(jurnal otaku indonesia trending) ♠ joi news ♠ anime genre ♠ imdb ♠ ipinfo ♠ sut ♠ uptime ♠ tracker",True)
        if user.name not in registered and not user.name in manager and user.name not in assistant and user.name not in owners:
            room.message("<br/><b>»"+user.name+" You are not registered«"+"<br/>"+"Please ask to Owner or Assistant"+"</b>",True)

      ##Ranker
      if used_prefix and cmd == "ranker" and self.getAccess(user) > 0:
        if args == "info":
            o = len(owners)
            a = len(assistant)
            m = len(manager)
            r = len(registered)
            room.message("<br/><f x1200FF00='0'><b>OWNERS : </b></f>"+str(o)+"<br/><f x120000FF='0'><b>ASSISTANT : </b></f>"+str(a)+"<br/> <f x1200FFFF='0'><b>MANAGERS : </b></f>"+str(m)+"<br/><f x12FF00FF='0'><b>OFFICERS : </b></f>"+str(r),True)
        else:
            room.message("<br/><f x1200FF00='0'><b>OWNERS : </b></f>%s<br/><f x120000FF='0'><b>ASSISTANT : </b></f>%s<br/> <f x1200FFFF='0'><b>MANAGERS : </b></f>%s"%(", ".join(owners),", ".join(assistant),", ".join(manager)),True)

      ##MS
      if used_prefix and cmd == "ms" and self.getAccess(user) > 0:
          try:
            sss = args.replace(" ","+")
            data= urlreq.Request ("http://cinemaindo.com/?s="+sss+"&post_type=post", headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("utf-8")
            data = re.findall('<div class="title"><a href="(.*?)"><h2>(.*?)</h2></a></div>', ddread)
            newset = list()
            num = 1
            for link, title in data:
              newset.append("<b>⌠%s⌡ %s</b> - %s" % (num, title, short(link)))
              num = num+1
            room.message("<br/>"+"result for <b><i>"+args+"</i></b> :<br/>"+"<br/>".join(newset[0:10]), True)
          except:
              room.message("No result for<b>"+args+"</b>", True)

      ##Top CI
      if used_prefix and cmd == "ci" and self.getAccess(user) > 0:
          try:
            sss = args.replace(" ","+")
            data= urlreq.Request ("http://cinemaindo.com/", headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("utf-8")
            data = re.findall('<h3>(.*?)</h3>', ddread)
            newset = list()
            num = 1
            for title in data:
              newset.append("<b>⌠%s⌡ %s</b>" % (num, title))
              num = num+1
            room.message("<br/><b>Top 10 movies in Cinemaindo:</b><br/>"+"<br/>".join(newset[0:10]), True)
          except:
              room.message("No result for<b>"+args+"</b>")

      ##Fax
      if used_prefix and cmd == "fax" and self.getAccess(user) > 1:
          if len(args) > 1:
            try:
              target, body = args.split(" ", 1)
              if self.getAccess(user) > 1:
                if target in self.roomnames:
                    self.getRoom(target).message("<br/><b>Fax from %s</b><br/><b>via %s</b><br/><b>Message: </b>%s" % (sntonick(user.name), room.name, body), True)
                    room.message("[<b>%s</b>] Fax Sent" % "INF", True)
                else:
                    room.message("[<b>%s</b>] There's no Fax Service in<b>%s</b></font> :|" % ("ERROR", target), True)
              else:
                room.message("Fail:'v")
                self.setTimeout(int(3), room.message, "." % user.name, True)
            except:
              room.message("Fail !!")
    
      ####Eval
      elif used_prefix and cmd == "eval" and self.getAccess(user) == 4 or cmd == "e" and self.getAccess(user) == 4:
            try:
                ret = eval(args)
                room.message(str(repr(ret)))
            except Exception as e:
                et, ev, tb = sys.exc_info()
                lineno = tb.tb_lineno
                fn = tb.tb_frame.f_code.co_filename
                room.message("[ERROR] Line %i - %s"% (lineno, str(e)))

      ##TF/TebakFilm
      if used_prefix and cmd == "reg" and self.getAccess(user) > 0:
        if room.name == "pelayanbotproject" or room.name == "ladiessplay":
            if args == "tf":
              TebakFilm.reg(self, user, room)
        else:
            room.message("<br/>Main nya di : <br/>♦ http://pelayanbotproject.chatango.com<br/>♦ http://ladiessplay.chatango.com",True)

      if used_prefix and cmd == "tf":
          if room.name == "pelayanbotproject" or room.name == "ladiessplay":
              room.message(TebakFilm.level(self, user),True)
          else:
              room.message("<br/>Main nya di : <br/>♦ http://pelayanbotproject.chatango.com<br/>♦ http://ladiessplay.chatango.com",True)

      if used_prefix and cmd == "tebak":
          if room.name == "pelayanbotproject" or room.name == "ladiessplay":
              TebakFilm.tebak(self, user, args, room)
          else:
              room.message("<br/>Main nya di : <br/>♦ http://pelayanbotproject.chatango.com<br/>♦ http://ladiessplay.chatango.com",True)
                
      ###ALL OF YTS################
      ##MS YTS
      if used_prefix and cmd == "sy" and self.getAccess(user) > 0:
        try:
            sss = args
            if args:
                    data= urlreq.urlopen ("https://yts.to/browse-movies/"+sss+"/all/all/0/latest")
                    ddread = data.read().decode("utf-8")
                    data = re.findall('<div class="browse-movie-bottom">(.*?)<div class="browse-movie-year">(.*?)</div>', ddread)
                    newset = list()
                    num = 1
                    for title, year in data:
                      newset.append("⌠%s⌡ %s (%s)" % (num, title, year))
                      num = num+1
                    room.message("<br/><b><i>Result for "+sss+":</i></b><br/>"+"<br/>".join(newset[0:10]), True)
        except:
            room.message("No Result for<b><i> "+sss,True)
      ###YTS New by Genre
      if used_prefix and cmd == "yts" and self.getAccess(user) > 0:
        sss = args
        if args:
                try:
                    data= urlreq.urlopen ("https://yts.to/browse-movies/0/all/"+sss+"/0/latest")
                    ddread = data.read().decode("utf-8")
                    data = re.findall('<div class="browse-movie-bottom">(.*?)<div class="browse-movie-year">(.*?)</div>', ddread)
                    newset = list()
                    num = 1
                    for title, year in data:
                      newset.append("<b>⌠%s⌡ %s (%s)</b>" % (num, title, year))
                      num = num+1
                    room.message("<br/><b><i>New "+sss.title()+" Movies in YTS:</i></b><br/>"+"<br/>".join(newset[0:10]), True)
                except:
                    room.message("<br/>All Genres in YTS:<br/>Action, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Filmnoir, History, Horror, Music, Musical, Mystery, News, Romance, Scifi, Short, Sport, Thriller, War, Western. ^^",True)
        else:
            room.message("Do ~yts<space>Genre ^^")
      #TOP
      if used_prefix and cmd == "topyts" and self.getAccess(user) > 0:
          room.message("<br/><b>Top 4 movies in yts:</b>"+topyts(args),True)
      ##MI YTS
      if used_prefix and cmd == "miy" and self.getAccess(user) > 0 or used_prefix and cmd == "miyts" and len(args) > 0 and self.getAccess(user) > 0:
        try:
            sss=args
            data= urlreq.urlopen ("https://yts.to/browse-movies/"+sss+"/all/all/0/latest")
            ddread=str(data.read())
            trash , gambar=ddread.split('<img class=\"img-responsive\" src="',1)
            gambar , trash=gambar.split('" alt',1)
            trash , judul=ddread.split("<div class=\"browse-movie-bottom\">   ",1)
            judul , trash=judul.split("</div>",1)
            trash , link=ddread.split("<div class=\"browse-movie-tags\">",1)
            link , trash=link.split("</div>",1)
            trash , rating=ddread.split("<h4 class=\"rating\">",1)
            rating , trash=rating.split("</h4>",1)
            trash , genre=ddread.split("<h4>",1)
            genre , trash=genre.split("</h4>",1)
            room.message("<br/>"+"result for <b><i>"+args+"</i>:"+"<br/><br/>"+gambar+"<br/>"+judul+"<br/>Genre : "+genre+"<br/>Rating IMDB : "+rating+"<br/>Link : "+link,True)
        except:
            room.message("No result for <i><b>"+args+"</b></i>",True)


      ##NYTS    
      if used_prefix and cmd == "nyts" and self.getAccess(user) > 0:
          room.message("<br/><br/><b>New 10 Movie in yts :</b>"+yts(args),True)


      ##Seedict
      if used_prefix and cmd =="seedict" and self.getAccess(user) > 0:
        if args:
          newset = list()
          for word in dictionary:
            definition, name = json.loads(dictionary[word])
            if args == name:
              newset.append(word)
              io = len(newset)
          room.message("<br/><b><i>"+args+"</i> defined "+str(io)+" words : </b><br/>"+", ".join(newset),True)

      if used_prefix and cmd =="mydict" and self.getAccess(user) > 0:
        if args:
          room.message("Do seedict ;)")
        if not args:
          newset = list()
          for word in dictionary:
            definition, name = json.loads(dictionary[word])
            if user.name == name:
              newset.append(word)
              io = len(newset)
          room.message("<br/><b><u><i>"+user.name+"</i></u></b> defined "+str(io)+" words :<br/>"+", ".join(newset),True)
      ##Subscene
      if used_prefix and cmd == "sbs" and self.getAccess(user) > 1:
        try:
          if args:
            sss = args
            data= urlreq.urlopen ("http://subscene.com/subtitles/title?q="+sss+"&l=")
            ddread = data.read().decode("utf-8")
            data = re.findall('<div class="title">(.*?)</div>', ddread)
            newset = list()
            num = 1
            for title in data:
              newset.append("(%s) %s" % (num, title))
              num = num+1
            room.message(",".join(newset[0:10]), True)
        except:
            room.message("gaada:v")

      ##Time
      elif used_prefix and cmd == "time" and len(args) > 0 and self.getAccess(user) > 1:
        try:
            sss=args
            data= urlreq.urlopen ("http://time.is/"+sss)
            ddread=str(data.read())
            trash , gambar=ddread.split('<div id=\"twd">',1)
            gambar , trash=gambar.split('</div>',1)
            room.message(gambar)
        except:
            room.message("gaada:v")
      ##Multy Chat
      if used_prefix and cmd == "mty" and self.getAccess(user) > 0:
        if args:
            room.message("<a href=\"http://ch.besaba.com/chat/flash/?"+args+"\"target=\"_blank\">Click Here</a>",True)
        else:
            room.message("→!← For Black and →,← for white")
      ##MI
      if used_prefix and cmd == "mi" and len(args) > 0 and self.getAccess(user) > 0:
        try:
            sss = args.replace(" ","-")
            data= urlreq.Request ("http://cinemaindo.com/"+sss, headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread=con.read().decode("utf-8")
            trash , director=ddread.split("<b>Director</b>",1)##Done
            director , trash=director.split('</span>',1)##Done
            trash , stars=ddread.split("<b>Stars</b>",1)##Done
            stars , trash=stars.split('</span>',1)##Done
            trash , country=ddread.split("<b>Country</b>",1)##Done
            country , trash=country.split('</span>',1)##Done
            trash , sinopsis=ddread.split('<span class="synopsis" style="margin-top: 8px;display: block;"><p>',1)##Done
            sinopsis , trash=sinopsis.split('</span>',1)##Done
            trash , judul=ddread.split("<h1 class=\"title\">",1)##Done
            judul , trash=judul.split("</h1>",1)##Done
            trash , gambar=ddread.split("<img width=\"150\" height=\"150\" src=\"",1)##Done
            gambar , trash=gambar.split("\"",1)##Done
            trash , genre=ddread.split("<b>Genres</b>",1)##Done
            genre , trash=genre.split('</span>',1)##Done
            trash , link=ddread.split("<link rel=\"canonical\" href=\"",1)##Done
            link , trash=link.split('"',1)##Done
            trash , upl=ddread.split("<div class=\"bottomtitle\">",1)##Done
            upl , trash=upl.split('</div>',1)##Done
            trash , quality=ddread.split("<span class=\"left\">",1)##Done
            quality , trash=quality.split('</span>',1)##Done
            room.message("<br/><br/>"+gambar+
                         "<br/><b><i>"+judul+"</i></b>"+
                         "<br/><b>Director: </b>"+director+
                         "<br/><b>Stars: </b>"+stars+
                         "<br/><b>Genre: </b>"+genre+
                         "<br/><b>Country: </b>"+country+
                         "<br/><b>Quality: </b>"+quality+
                         "<br/><b>Link: </b>"+link+
                         "<br/><b>Post "+upl+"</b>"+
                         "<br/><b>Synopsis: </b><br/>"+sinopsis,True)
        except:
            room.message("No result for <b><i>"+args+"</i></b>",True)

      ##TST
      if used_prefix and cmd == "tst" and len(args) > 0 and self.getAccess(user) > 0:
        try:
            sss=args
            data= urlreq.urlopen ("http://animeku.tv/?s="+sss+"&post_type=anime")
            ddread=data.read().decode("utf-8")
            trash , vote=ddread.split('<h2><a href=',1)##Done
            vote , trash=vote.split('</a>',1)##Done
            room.message(vote,True)
        except:
            room.message("No project ;)")

      ##YT
      if used_prefix and cmd == "yt" and self.getAccess(user) > 0 or used_prefix and cmd == "ytb" and self.getAccess(user) > 0:
          room.message(yt(args),True)

##COOOOOOOOLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR################
#####################################################################
      if used_prefix and cmd == "cl":################################
          room.message("<br/><b>Available for now:</b><br/>Black, "+#
                       "Red, Green, Blue, Yellow, Aqua, Pink, "+#####
                       "Grey. ^^",True)##############################
#####################################################################
      if used_prefix and cmd == "clblack":###########################
          room.message("<f x12000000='0'>%s" % (args))##########
      if used_prefix and cmd == "clblackb":##########################
          room.message("<f x12000000='0'><b>%s" % (args))#######
      if used_prefix and cmd == "clred":#############################
          room.message("<f x12FF0000='0'>%s" % (args))##########
      if used_prefix and cmd == "clredb":############################
          room.message("<f x12FF0000='0'><b>%s" % (args))#######
      if used_prefix and cmd == "clgreen":###########################
          room.message("<f x1200FF00='0'>%s" % (args))##########
      if used_prefix and cmd == "clgreenb":##########################
          room.message("<f x1200FF00='0'><b>%s" % (args))#######
      if used_prefix and cmd == "clblue":############################
          room.message("<f x120000FF='0'>%s" % (args))##########
      if used_prefix and cmd == "clblueb":###########################
          room.message("<f x120000FF='0'><b>%s" % (args))#######
      if used_prefix and cmd == "clyellow":##########################
          room.message("<f x12FFFF00='0'>%s" % (args))##########
      if used_prefix and cmd == "clyellowb":#########################
          room.message("<f x12FFFF00='0'><b>%s" % (args))#######
      if used_prefix and cmd == "claqua":############################
          room.message("<f x1200FFFF='0'>%s" % (args))##########
      if used_prefix and cmd == "claquab":###########################
          room.message("<f x1200FFFF='0'><b>%s" % (args))#######
      if used_prefix and cmd == "clpink":############################
          room.message("<f x12FF00FF='0'>%s" % (args))##########
      if used_prefix and cmd == "clpinkb":###########################
          room.message("<f x12FF00FF='0'><b>%s" % (args))#######
      if used_prefix and cmd == "clgrey":############################
          room.message("<f x12C0C0C0='0'>%s" % (args))##########
      if used_prefix and cmd == "clgreyb":###########################
          room.message("<f x12C0C0C0='0'><b>%s" % (args))
      if used_prefix and cmd == "r":
        rb = ("<f x120000FF='0'>%s<f x120080FF='0'>%s<f x1200FFFF='0'>%s<f x1200FF80='0'>%s<f x1200FF00='0'>%s<f x1280FF00='0'>%s<f x12FFFF00='0'>%s<f x12FF8000='0'>%s<f x12FF0000='0'>%s<f x12BF00FF='0'>%s<f x12FF00FF='0'>%s<f x12FF00BF='0'>%s<f x12FF0080='0'>%s" % (args[0], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9], args[10], args[11], args[12], args[13]))
        room.message(rb,True)#######
#####################################################################
#####################################################################
        
      if used_prefix and cmd == "truth" or used_prefix and cmd == "Truth" and self.getAccess(user) > 0:
        if user.name in turn:
            room.message(random.choice(["Udah punya pacar kah?","Pernah suka ama pacar atau mantan temen kamu?sebutin namanya","Pernah suka ama guru sendiri?sebut namanya dan guru apa","Pernah coli?:'v","kalo tidur lu pake daleman ga?","Hal paling memalukan dalam hidup lu","disini nih, di chatango, siapa yang lu naksir","pernah ditmpar pasangan?","Apa yang lu pikirin sebelum tidur?","Elu gay/lesbi?:'v"]))
        else:
            room.message("it's not your turn :|")
      if used_prefix and cmd == "dare" or used_prefix and cmd == "Dare" and self.getAccess(user) > 0:
        if user.name in turn:
            room.message(random.choice(["Upload kesini foto elu selfie","kirim sn ke indi60 lu suka dia(cewe/laki)","bc dan bilang kalo elu itu gay/lesbi","kirim voice note elu lagi nyanyi kesini","bc dan bilang elu suka ama zy28","sms babehlu dan bilang 'hai bro, gua beli majalah playboy nih'<br/>dan capture lalu kirim kesini","sms ortu lu dan bilang 'mah, pah aku udah tau kalo aku anak adopsi. Gausah disembunyiin lagi'<br/>dan capture lalu kirim kesini"]),True)
        else:
            room.message("it's not your turn :|")
      if used_prefix and cmd == "tod" and self.getAccess(user) > 0:
        if not args:
            room.message("<br/>Command for tod:<br/>♠ join<br/>♠ player<br/>♠ leave",True)
        elif args:
            if args == "join":
              if user.name not in tod:
                  tod.append(user.name)
                  turn.append(user.name)
                  room.message("congrats u joined tod ^^")
              else:
                  room.message("you in the game already")
            if args == "player":
              room.message("Tod players: <br/>"+", ".join(tod),True)
            if args == "leave":
                if user.name in tod:
                  spin.remove(user.name)
                  tod.remove(user.name)
                  room.message("you left the game")
                else:
                  room.message("you never joined the game :|")
      if used_prefix and cmd == "give spin to":
          if user.name in spin:
            spin.append(args)
            spin.remove(user.name)
            room.message("Done..")
      if used_prefix and cmd == "spin" and self.getAccess(user) > 0:
          if user.name in turn:
              spin.remove()
              spin.append(user.name)
              room.message("<br/><br/><br/>"+user.name+" spinning the pencil...<br/>and the pencil pointed to @"+random.choice(tod)+" :v<br/>Truth or Dare?",True)
          else:
              room.message("only".join(spin)+" can spin")

      if used_prefix and cmd == "rainbow":
          textvar = args
          textfin = ""
          rainbow = ['<f xff0000=""></f>', '<f xff7f00=""></f>', '<f xffff00=""></f>', '<f x00ff00=""></f>', '<f x0000ff=""></f>', '<f x8f00ff=""></f>']
          rainbowvar = eval(str(rainbow))
          for item in textvar:
            if item != " ":
                if len(rainbowvar) > 1:
                 textfin += textvar + item
                else:
                 textfin += textvar + item
                 rainbowvar = eval(str(rainbow))
            else:
              textfin += " "
              room.message(textfin)
      ##ANIMEKU.TV   
      if used_prefix and cmd == "msa" and self.getAccess(user) > 0:
          try:
            sss = args
            data= urlreq.Request ("http://animeku.tv/?s="+sss+"&post_type=anime", headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("utf-8")
            data = re.findall('<h2><a href="(.*?)">(.*?)</a>', ddread)
            newset = list()
            num = 1
            for link, title in data:
              newset.append("<b>⌠%s⌡ %s</b> - %s" % (num, title, short(link)))
              num = num+1
            room.message("<br/>"+"result for <b><i>"+args+"</i></b> :<br/>"+"<br/>".join(newset[0:10]), True)
          except:
              room.message("No result for<b>"+args+"</b>")

      if used_prefix and cmd == "na" and self.getAccess(user) > 0:
          try:
            data= urlreq.Request ("http://animeku.tv/", headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("utf-8")
            data = re.findall('<div class="title" style="max-width: 153px;">(.*?)</div>', ddread)
            newset = list()
            num = 1
            for title in data:
              newset.append("<b>⌠%s⌡ %s</b>" % (num, title))
              num = num+1
            room.message("<br/><b>New Anime Series on Animeku.tv:</b><br/>"+"<br/>".join(newset[0:10]), True)
          except:
              room.message("Something Wrong")

      if used_prefix and cmd == "ai" and self.getAccess(user) > 0:
        try:
            sss=args.replace(" ","-")
            data= urlreq.Request ("http://animeku.tv/anime/"+sss, headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread=str(con.read())
            trash , judul=ddread.split('<span class="desc">',1)
            judul , trash=judul.split('<div',1)
            trash , synopsis=ddread.split('<p>',1)
            synopsis , trash=synopsis.split('</p>',1)
            trash , tipe=ddread.split("<b>Type</b>",1)
            tipe , trash=tipe.split("</li>",1)
            trash , episode=ddread.split("<b>Episodes</b>",1)
            episode , trash=episode.split("</li>",1)
            trash , status=ddread.split("<b>Status</b>",1)
            status , trash=status.split("</li>",1)
            trash , aired=ddread.split("<b>Aired</b>",1)
            aired , trash=aired.split("</li>",1)
            trash , producers=ddread.split("<b>Producers</b>",1)
            producers , trash=producers.split("</li>",1)
            trash , genre=ddread.split("<b>Genres</b>",1)
            genre , trash=genre.split("</li>",1)
            trash , duration=ddread.split("<b>Duration</b>",1)
            duration , trash=duration.split("</li>",1)
            trash , score=ddread.split("<b>Score</b>",1)
            score , trash=score.split("</li>",1)
            room.message("<br/><i>"+judul+"</i><br/><b>Type</b>"+tipe+"<br/><b>Episodes</b>"+episode+"<br/><b>Status</b>"+status+"<br/><b>Aired</b>"+aired+"<br/><b>Producers</b>"+producers+"<br/><b>Genre</b>"+genre+"<br/><b>Duration</b>"+duration+"<br/><b>Score</b>"+score+"<br/><b>Synopsis:</b><br/>"+synopsis,True)
        except:
            room.message("No Result for<b><i>"+args+"</i></b>",True)

      if used_prefix and cmd == "topanime" and self.getAccess(user) > 0:
          try:
            data= urlreq.Request ("http://animeku.tv/", headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("utf-8")
            data = re.findall('<span class="title"><a class="series" href="(.*?)" rel=(.*?)">(.*?)</a>', ddread)
            newset = list()
            num = 1
            for title, rel, link in data:
              newset.append("<b>⌠%s⌡ %s - %s</b>" % (num, link, short(title)))
              num = num+1
            room.message("<br/><b>Top 10 Anime on Animeku.tv:</b><br/>"+"<br/>".join(newset[0:10]), True)
          except:
              room.message("Something Wrong")

      if used_prefix and cmd == "ne" and self.getAccess(user) > 0:
          try:
            data= urlreq.Request ("http://animeku.tv/", headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("utf-8")
            data = re.findall('<div class="rights">(.*?)</div>', ddread)
            newset = list()
            num = 1
            for title in data:
              newset.append("<b>⌠%s⌡ %s</b>" % (num, title))
              num = num+1
            room.message("<br/><b>New Episode update on Animeku.tv:</b><br/><b><u><i>Note : # = episode</i></u></b><br/>"+"<br/>".join(newset[0:10]), True)
          except:
              room.message("Something Wrong")

      if used_prefix and cmd == "anime" and self.getAccess(user) > 0:
        if args:
          try:
            sss = args.replace(" ","-")
            data= urlreq.Request ("http://animeku.tv/genres/"+sss, headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("utf-8")
            data = re.findall('<h2><a href="(.*?)">(.*?)</a>', ddread)
            newset = list()
            num = 1
            for title, link in data:
              newset.append("<b>⌠%s⌡ %s - %s</b>" % (num, link, short(title)))
              num = num+1
            room.message("<br/><b>"+args+"</b> Anime:<br/>"+"<br/>".join(newset[0:10]),True)
          except:
            room.message("<b>Available Genres in Animeku.tv:</b><br/>Action, Adventure, Comedy, Dementia, Demons, Drama, Ecchi, Fantasy, Game, Harem, Historical, Horror, Josei, Kids, Live Action, Magic, Martial Arts, Mecha, Military, Movie, Music, Mystery, ONA, OVA, Parody, Police, Psychological, Romance, Samurai, School, Sci-fi, Seinen, Shoujo, Shoujo Ai, Shounen, Shounen Ai, Slice of Life, Space, Special, Sports, Super Power, Supernatural, Thriller, Vampire",True)
        else:
          room.message("Do anime<space>genre")
              
      if used_prefix and cmd == "sht" and self.getAccess(user) > 0:
          room.message(short(args))

      if used_prefix and cmd == "joi" and self.getAccess(user) > 0:
          if not args:
            data= urlreq.Request ("http://jurnalotaku.com/", headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("latin-1")
            data = re.findall('<h2 class="frt-title-1"><a href="(.*?)"(.*?)rel="bookmark">(.*?)</a>', ddread)
            newset = list()
            num = 1
            for title, rel, link in data:
              newset.append("<b>⌠%s⌡ %s - %s</b>" % (num, link, short(title)))
              num = num+1
            room.message("<br/><b>Trending Now:</b><br/>"+"<br/>".join(newset),True)
          if args == "news":
            data= urlreq.Request ("http://jurnalotaku.com/category/otanews/", headers={'User-Agent' : "Magic Browser"})
            con = urlreq.urlopen(data)
            ddread = con.read().decode("utf-8")
            data = re.findall('<h2 class="post-title"><a href="(.*?)"(.*?)rel="bookmark">(.*?)</a>', ddread)
            newset = list()
            num = 1
            for title, rel, link in data:
              newset.append("<b>⌠%s⌡ %s - %s</b>" % (num, link, short(title)))
              num = num+1
            room.message("<br/><b>News:</b><br/>"+"<br/>".join(newset[0:10]),True)

      ##WHOIS
      if used_prefix and cmd == "w" or used_prefix and cmd == "whois"and self.getAccess(user) > 1:
          if not args:
              room.message("The fucking nick please")
          args = args.lower()
          if args[0] == "+":
              args = args[1:]
          elif pars(args) != None and not args[0] == "+":
              args = pars(args)
          try:
              f = open("ip_whois.txt","r")
              ip_whois = eval(f.read())
              f.close()
          except:pass
          try:
              f = open("sid_whois.txt","r")
              sid_whois = eval(f.read())
              f.close()
          except:pass
          ip_ver = whois(ip_whois, args)
          sid_ver = whois(sid_whois, args)
          if ip_ver == None and sid_ver == None:
              room.message("No Alias Found")
              return
          room.message("Alias(es) of %s:<br/><b>UnID</b>: %s.<br/><b>IP Version</b>: %s." % (args.title(), sid_ver, ip_ver),True)
      ##IMDB
      if used_prefix and cmd == "imdb" and self.getAccess(user) > 0:
          room.message("<br/>Result for<b>"+args+"</b>:<br/>"+imdb(args),True)

      ##UWL
      if used_prefix and cmd == "uwl" and self.getAccess(user) == 4:
          name = args
          if name in owners:
            owners.remove(name)
            saveRank(self)
            room.message("Success")
          if name in assistant:
            assistant.remove(name)
            saveRank(self)
            room.message("Success")
          if name in manager:
            manager.remove(name)
            saveRank(self)
            room.message("Success")
          if name in registered:
            registered.remove(name)
            saveRank(self)
            room.message("Success")

      ##IPINFO
      if used_prefix and cmd == "ipinfo" and self.getAccess(user) > 0:
          room.message(ipinfoio(args, user),True)

      ##BAN And Unban
      if used_prefix and cmd == "ban":
          if self.getAccess(user) > 2:
            if room.getLevel(self.user) > 0:
              room.banUser(ch.User(args))
              room.message(args.title()+" is banned")
            else:
              room.message("I'm not even a mod here")
          else:
            room.message("You don't have permission")
      if used_prefix and cmd == "unban":
          if args == "": return
          args = args.lower()
          if self.getAccess(user) > 2:
            if room.getLevel(self.user) > 0:
              room.unban(ch.User(args))
              room.message(args.title()+" is unbanned")
            else:
              room.message("I'm not even a mod here")
          else:
            room.message("You don't have permission")

      elif used_prefix and cmd == "sut" and self.getAccess(user) > 0:
          room.message("server has been running for: %s" % uptime())

      elif used_prefix and cmd == "uptime" and self.getAccess(user) > 0:
          minute = 60
          hour = minute * 60
          day = hour * 24
          days =  int(getUptime() / day)
          hours = int((getUptime() % day) / hour)
          minutes = int((getUptime() % hour) / minute)
          seconds = int(getUptime() % minute)
          string = ""
 
          if days > 0:
 
            string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
 
          if len(string) > 0 or hours > 0:
 
            string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
 
          if len(string) > 0 or minutes > 0:
 
            string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
 
          string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
          room.message("Pelayan uptime: %s" % string, True)

      if used_prefix and cmd == "tracker" and self.getAccess(user) > 0:
        try:
          if args:
              sss = args.lower()
              data = urlreq.urlopen("http://ws-hoax.rhcloud.com/user/"+sss)
              ddread = data.read().decode("utf-8")
              data = re.findall('<a class="tooltip" user="(.*?)"', ddread)
              newset = list()
              for viewer in data:
                  newset.append("<b>%s</b>" % (viewer))
              room.message("<b>"+sss+"</b> Viewed by:<br/>"+", ".join(newset[1:11])+"<br/>For more info visit http://ws-hoax.rhcloud.com/",True)
          else:
              aaa = user.name
              data = urlreq.urlopen("http://ws-hoax.rhcloud.com/user/"+aaa)
              ddread = data.read().decode("utf-8")
              data = re.findall('<a class="tooltip" user="(.*?)"', ddread)
              newset = list()
              for viewer in data:
                  newset.append("<b>%s</b>" % (viewer))
              room.message("<b>"+aaa+"</b> Viewed by:<br/>"+", ".join(newset[1:11])+"<br/>For more info visit http://ws-hoax.rhcloud.com/",True)
        except:
            room.message("Fail to check")

      if used_prefix and cmd == "cso" and self.getAccess(user) > 0:
            oll = "<f x1240FF00='0'>Online</f>"
            off = "<f x12FF0000='0'>Offline</f>"
            usr = ch.User(args)
            ol = self.pm.checkOnline(usr)
            idle = self.pm._status[usr][2]
            offline = self.pm._status[usr][0]
            if usr in self.pm.contacts:
                if ol == True:
                    room.message(args.title()+" is "+oll+" and Idle for "+ helPer(idle),True)
                else:
                    room.message(args.title()+" is "+off+" "+helPer(offline)+" ago",True)
                if idle == "0":
                    room.message(args.title()+" is "+oll,True)
            else:
                self.pm.addContact(usr)
                if ol == True:
                    room.message(args.title()+" is "+oll+" and Idle for "+ helPer(idle),True)
                else:
                    room.message(args.title()+" is "+off+" "+helPer(offline)+" ago",True)
                if idle == "0":
                    room.message(args.title()+" is "+oll,True)

        
    except Exception as e:
         try:
             et, ev, tb = sys.exc_info()
             lineno = tb.tb_lineno
             fn = tb.tb_frame.f_code.co_filename
             room.message("[ERROR] %s Line %i - %s"% (fn, lineno, str(e)))
             return
         except:
             room.message("[ERROR] Undescrideable error detecetd!!")
             return

        

  def onReconnect(self, room):
    print("[+] Reconnected to "+room.name)

  def onDisconnect(self, room):
    print("[+] Disconnected from "+room.name)

  def onUserCountChange(self, room):
    pass

  def onFloodWarning(self, room):
    room.reconnect()
    print("[+] Reconnecting...")

  def onPMMessage(self, pm, user, body):
    print("PM - "+user.name+": "+body)
    self.getRoom("pelayanbotproject").message("<b><i>PM from "+user.name+"</i></b><br/><b>Message:</b><br/>"+body,True)

if __name__ == "__main__":
    TestBot.easy_start(rooms,hgf,fgh)
    print("[SAVE] SAVING ROOMS...")
    f = open("rooms.txt", "w")
    f.write("\n".join(rooms))
    f.close()

    f = open("definitions.txt", "w")
    for word in dictionary:
      definition, name = json.loads(dictionary[word])
      f.write(json.dumps([word, definition, name])+"\n")
