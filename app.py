import discord
from keepalive import keep_alive
import yt_dlp

cnt=0
client = discord.Client()
old_mess=""

vc=''

@client.event
async def on_ready():
    print("Done")

@client.event
async def on_message(message):
    global cnt
    global old_mess
    global vc
    if message.content==old_mess:
        cnt+=1
    if message.author == client.user:
        print(str(message.author)+' : ',message.content)
        return 
    if cnt==4:
        await message.channel.send("STOP SPAMMING "+str(message.author))
        cnt = 0

    if message.content.startswith("play"):
      try:
        if str(message.author)=="Um....#9661":
          
          user=message.author
          voice_channel=user.voice.channel

          def repeat():
            vc.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: repeat())
          
          if voice_channel!= None:
              command = str(message.content)
              song = (command.split(" "))[1]
              ydl_opts = {'outtmpl': './song',
                  'postprocessors': [{
                  'key': 'FFmpegExtractAudio',
                  'preferredcodec': 'mp3',
                  'preferredquality': '192',
              }],}
              with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                  ydl.download([song])

              

              vc = await voice_channel.connect()
              vc.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: repeat())
              # vc.pause()
              # vc.resume()
              # vc.stop()
          else:
              await message.channel.send('U need to be in voice channel idiot')
              
          await message.channel.send("Enjoy the music")
        else:
          await message.channel.send("U r not mrdogs, ask him for permission to open a song")
      except:
        await message.channel.send("U need to be in voice channel idiot")
    if message.content.startswith("stop"):
      try:
        if str(message.author)=="Um....#9661":
            user=message.author
            voice_channel=user.voice.channel
            if voice_channel!= None:
              await vc.disconnect()
              vc=""
            else:
              await message.channel.send('U need to be in voice channel idiot')    
        else:
          await message.channel.send("U r not mrdogs, ask him for permission to stop a song")
      except:
        await message.channel.send('no song r playing')    

    elif message.content.startswith("hi"):
        await message.channel.send("Hello")
    elif message.content.startswith("owo"):
        if(str(message.channel)=="general"):
          await message.channel.send("GO TO <#931438020543012945> IDIOT "+str(message.author))
    elif "hello" in message.content:
        await message.channel.send("No one care")
    elif "bye" in message.content:
        await message.channel.send("Get out! No one need you")
    elif "suck" in message.content:
        await message.channel.send("hi sucker")
    elif "fuck" in message.content:
        await message.channel.send("dude dont swear too much")
    elif "idiot" in message.content:
        await message.channel.send("I think u an r idiot, not me")
    elif "hmm" in message.content:
        await message.channel.send("stop thinking too much")
    elif "stupid" in message.content:
        await message.channel.send("u r stupid")
    elif "boom" in message.content:
        await message.channel.send("Oh no I gonna dead")
    elif "wifi" in message.content:
        await message.channel.send("I know your wifi suck! stop complain about it")
    elif "nerd" in message.content:
        await message.channel.send("hi nerd")
    elif "creative" in message.content:
        await message.channel.send("Turn to survival, idiot")
    elif "minecraft" in message.content:
        await message.channel.send("Who ever use java to write a game ?")
    elif "nvm" in message.content:
        await message.channel.send("what r u trying to say?")
    elif "stop" in message.content:
        await message.channel.send("YEAH, u should stop")
    elif "kick" in message.content:
        await message.channel.send("DONT KICK ME PLEASE :(")
    elif "bruh" in message.content:
        await message.channel.send("bruhhhhhhhhhh")
    elif "done" in message.content:
        await message.channel.send("Good job!")
    elif "uhm" in message.content:
        await message.channel.send("Stop dude")
    elif "uh" in message.content:
        await message.channel.send("Uh huh")
    elif "hm" in message.content:
        await message.channel.send("Stop dude")
    elif "sex" in message.content:
        await message.channel.send("Stop think about sex")
    elif "dude" in message.content:
        await message.channel.send("hi dude")
    elif "<@!886979172268904479>" in message.content:
        await message.channel.send("WHAT ?")
    elif "bedwar" in message.content:
        await message.channel.send("STOP PLAYING BEDWARS <@884667726025596958>")
    elif "game" in message.content:
        await message.channel.send("Stop playing in the middle of class")
    elif "mc" in message.content:
        await message.channel.send("Stop playing in the middle of class")
    # elif "<@!884667726025596958>" in message.content:
    #     await message.channel.send("Stop pinging him, he is playing bedwar")
    elif "<@!890546259180531732>" in message.content:
        await message.channel.send("<@890546259180531732> is so handsome and smart and hes so friendly so please dont kick me :(")
    elif "lol" in message.content:
        await message.channel.send(":laughing:")
    elif "shit" in message.content:
        await message.channel.send("💩")
    elif "(:" in message.content:
        await message.channel.send("this is 🙂 not (: nerd")
    elif "dogthesuperiors.web.app" in message.content:
        await message.channel.send("Cool Website")
    elif "notcringes.web.app" in message.content:
        await message.channel.send("Really Cool Website")
    elif "dead chat" in message.content:
      await message.channel.send("https://tenor.com/view/pacman-gif-21447981")
    old_mess=message.content
    print(str(message.author)+' : ',message.content)
    
keep_alive()

client.run("OTM1NzU3OTY4MTYxNTE3NTc4.YfDShQ.UfZm1Hi_B-GXf8NrVhE43WLcIhc")