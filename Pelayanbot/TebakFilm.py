import json
import ch
import time

game = dict()
f = open("game.txt","r")
print ("[INFO] Loading Game....")
time.sleep(1)
for line in f.readlines():
    try:
        if len(line.strip())>0:
            user , level = json.loads(line.strip())
            game[user] = json.dumps(level)
    except:
        print("[error] Can't load game %s" % line)
    f.close()

def reg(self, user, room):
    user = user.name
    if user not in game:
        info = "1"
        game[user]=json.dumps(info)
        f = open("game.txt", "w")
        for user in game:
            info = json.loads(game[user])
            f.write(json.dumps([user, info])+"\n")
        f.close()
        room.message("Success! Ketik ~tf untuk mulai")
    else:
        room.message("You already registered")
    
def level(self, user):
  if user.name in game:
    if json.loads(game[user.name]) == "1":
        return "<br/><b>Level 1 : <br/>http://i.imgur.com/QG6PZiR.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "2":
        return "<br/><b>Level 2 : <br/>http://i.imgur.com/LyTZvxG.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "3":
        return "<br/><b>Level 3 : <br/>http://i.imgur.com/4zMbDzU.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "4":
        return "<br/><b>Level 4 : <br/>http://i.imgur.com/7tuAmmC.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "5":
        return "<br/><b>Level 5 : <br/>http://i.imgur.com/mYpa5z2.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "6":
        return "<br/><b>Level 6 : <br/>http://i.imgur.com/3tNpASf.png<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "7":
        return "<br/><b>Level 7 : <br/>http://i.imgur.com/A3wzkpG.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "8":
        return "<br/><b>Level 8 : <br/>http://i.imgur.com/XQIZC3r.png<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "9":
        return "<br/><b>Level 9 : <br/>http://i.imgur.com/eyZx5AL.png<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "10":
        return "<br/><b>Level 10 : <br/>http://i.imgur.com/6RZWDoI.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "11":
        return "<br/><b>Level 11 : <br/>http://i.imgur.com/wXVYb3U.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "12":##Age of ultron
        return "<br/><b>Level 12 : <br/>http://i.imgur.com/EZBkPaR.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "13":##Brick Mansion
        return "<br/><b>Level 13 : <br/>http://i.imgur.com/4HUSSIg.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "14":##Escape Plan
        return "<br/><b>Level 14 : <br/>http://i.imgur.com/bWqK6iv.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "15":##lone
        return "<br/><b>Level 15 : <br/>http://i.imgur.com/MFtJULn.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "16":##F7
        return "<br/><b>Level 16 : <br/>http://i.imgur.com/P4QtydY.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "17":##I spit 1
        return "<br/><b>Level 17 : <br/>http://i.imgur.com/mmIBt74.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "18":##fury road
        return "<br/><b>Level 18 : <br/>http://i.imgur.com/zKwywLj.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "19":##Noah
        return "<br/><b>Level 19 : <br/>http://i.imgur.com/4ILhyma.png<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "20":##Sanctum
        return "<br/><b>Level 20 : <br/>http://i.imgur.com/11RMMPU.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "21":##Chronicle
        return "<br/><b>Level 21 : <br/>http://i.imgur.com/mCJVg8I.png<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "22":##Benjamin
        return "<br/><b>Level 22 : <br/>http://i.imgur.com/s4UdVns.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "23":##The last Airbender
        return "<br/><b>Level 23 : <br/>http://i.imgur.com/U6l3l6m.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "24":##this is the end
        return "<br/><b>Level 24 : <br/>http://i.imgur.com/HgPjicR.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "25":##WWZ
        return "<br/><b>Level 25 : <br/>http://i.imgur.com/Rr10P2d.jpg<br/>Untuk jawab ketik ~tebak(spasi)jawaban"
    if json.loads(game[user.name]) == "26":
        return "<br/><b>Akan segera di update ^^</b>"
  else:
      return "You're not registered, do ~reg tf to register"


def tebak(self, user, args, room):
    usr = user.name
    jawab = args
    if json.loads(game[usr]) == "1":
      if jawab == "black hawk down":
        info = "2"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf",True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "2":
      if jawab == "captain america: the winter soldier":
        info = "3"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "3":
      if jawab == "clash of the titans":
        info = "4"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "4":
      if jawab == "dracula untold":
        info = "5"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "5":
      if jawab == "everly":
        info = "6"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "6":
      if jawab == "hansel & gretel: witch hunters":
        info = "7"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "7":
      if jawab == "hercules":
        info = "8"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "8":
      if jawab == "jupiter ascending":
        info = "9"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "9":
      if jawab == "maleficent":
        info = "10"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "10":
      if jawab == "now you see me":
        info = "11"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "11":
      if jawab == "ouija":
        info = "12"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "12":
      if jawab == "avengers: age of ultron":
        info = "13"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "13":
      if jawab == "brick mansion":
        info = "14"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "14":
      if jawab == "escape plan":
        info = "15"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "15":
      if jawab == "the lone ranger":
        info = "16"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "16":
      if jawab == "furious seven":
        info = "17"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "17":
      if jawab == "i spit on your grave":
        info = "18"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "18":
      if jawab == "mad max: fury road":
        info = "19"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "19":
      if jawab == "noah":
        info = "20"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "20":
      if jawab == "sanctum":
        info = "21"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "21":
      if jawab == "chronicle":
        info = "22"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "22":
      if jawab == "the curious case of benjamin button":
        info = "23"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "23":
      if jawab == "the last airbender":
        info = "24"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "24":
      if jawab == "this is the end":
        info = "25"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
    elif json.loads(game[usr]) == "25":
      if jawab == "world war z":
        info = "26"
        game[usr]=json.dumps(info)
        f = open("game.txt", "w")
        for usr in game:
            info = json.loads(game[usr])
            f.write(json.dumps([usr, info])+"\n")
        f.close()
        room.delete(user)
        room.message("<br/>Selamat anda benar "+user.name+" ^.^<br/>Untuk lanjut ketik ~tf", True)
      else:
          room.message("<br/><b>salah, kalau sudah merasa benar pastikan judul sama dengan di IMDB dan tanpa caps", True)
