import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import json
import datetime
import subprocess
from os import system
#import youtube_dl
import random
#from PyLyrics import *
import time
import os

AHSBOTTOKEN= 'NTM1NTc0MDg3NTM2MzQ1MTE3.XMoG8A.UGKTFZalOf2QK8k5VA0ioSRfmTM'
TESTTOKEN = 'NTcyNTgwODg0NDY1NzEzMTcy.XMeX9A.BRAMtc35uElsGXKZRi3_n2mi_mA'

TOKEN = AHSBOTTOKEN



cuss = ["BITCH", "ASS", "BASTARD", "SHIT", "SHITTY", "FUCK", "FUCKER", "FUCKS", "SHITS", "FAQ", "FUK", "FUC", "FAC", "FAK", "COCK", 'CUNT', 'NIGGER', 'NIGGA', 'PENIS', 'PUSSY', 'DICK', 'TITS' , 'TIT', 'BOOBS', 'BOOBIES', 'SMD', 'SMC','LOGANG', 'STFU', 'THOT', 'LMFAO', "NWORD", "FCK", "F U C K"]

bypass = ["BYPASS"]

phrases = ["Whoa!  Calm down!  We don't talk like that here.", "Hey, hey, hey!  Not cool.  Take a deep breath, count to ten, then try again.", "Yo.  That's not nice. Take a chill pill and rephrase your sentence.",
           "Swearing's not kool!  Stay in skhool!", "You can't say that here!"]

lists= ['nonononono']
client = commands.Bot(command_prefix = '$')
client.remove_command('help')

Admin_id = ['2003lxp#0907']
general = client.get_channel(520674310801850371)
log = client.get_channel(522142442401693707)
staff = client.get_channel(522142350340784140)

client.remove_command("help")

messages = joined = 0


players = {}
queues = {}

rants = ["Where's banana chat?"]

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

'''
async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await asyncio.sleep(3600)
        except Exception as e:
            print(e)
            await asyncio.sleep(3600)
'''



'''
@client.event
async def on_message(message):
    log = client.get_channel(529758828867223560)
    contents = message.content
    writer = message.author
    channel = message.channel
    for word in str(message.content).upper():
        if word in cuss:
            await message.channel.purge(limit=1)
            warning = await channel.send(writer.mention + "!  " + random.choice(phrases))
            embed=discord.Embed(title=" ", color=0xff0000)
            embed.set_author(name="Message Deleted")
            embed.add_field(name="User", value=message.author.mention, inline=True)
            embed.add_field(name="Author", value=message.channel.mention, inline=True)
            embed.add_field(name="Message", value= message.content, inline=False)
            embed.add_field(name="Word Detected", value= word, inline=False)
            embed.set_footer(text="Please note that this is still a work in progress. If you find any bugs, report them using $report")
            await log.send(embed=embed)
            time.sleep(3)
            await warning.delete()
                                          
    await client.process_commands(message)
'''




@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f"{extension} was loaded")


@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f"{extension} was unloaded")


@client.command(hidden=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f"{extension} was reloaded")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"{filename[:-3]} was loaded.")
        



@client.command(hidden=True)
async def logout(ctx):
    await client.logout()


        




'''@client.command(pass_context=True)
async def rant(ctx):
    if ctx.message.channel.id == '520674423947132938':
        Rant = random.choice(rant)
        await client.say(Rant)
    else:
        await client.say('Type this in #rant-space')

@client.command()
async def war():
    await client.say('https://www.youtube.com/watch?v=UVxU2HzPGug')
    await client.say('T Gay')'''

'''
@client.command()
async def maketicket(ctx):
    server = ctx.message.guild
    author = ctx.message.author
    reason = ctx.message.content[12:] #subject of ticket


    everyone = discord.PermissionOverwrite(read_messages=False)
    staff = discord.PermissionOverwrite(read_messages=True)
   

    eyedee = random.randrange(1,99999) #assigns id number
    name = "ticket-" + str(eyedee)


    admin = discord.utils.get(server.roles, name="Administrator")
    mod = discord.utils.get(server.roles, name="Moderators")

    
    await server.create_text_channel(name)
    ticket = discord.utils.get(client.get_all_channels(), name = "ticket-" + str(eyedee)) #makes variable to easly call on the channel
    await admin.ticket.set_permissions(staff)
    await server.default_role.ticket.set_permissions(server.default_role, everyone)


    
    #WELCOME MESSAGE
    embed=discord.Embed(title="Welcome!", description="Thank you {} for your ticket about {}!  We'll assist you soon.".format(author.mention, ctx.message.content[12:]), color=0x400080)
    embed.set_author(name="New Ticket")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/522142350340784140/550739276069863446/ahs.png")
    embed.add_field(name="Your ticket number is " + str(eyedee) + '.  You should see it at the top of the list.', value="We will try to assist you within the next 24 hours.", inline=False)
    embed.set_footer(text="Please note that this is still a work in progress.  If you find any bugs, report them using $report")
    
    await client.say(embed=embed) #posts where the user said the command
    
    embed = discord.Embed(title = " ",  color=0x400080)
    embed.set_author(name="New Ticket")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/522142350340784140/550739276069863446/ahs.png")
    embed.add_field(name="Ticket number " + str(eyedee) + ' has been made by ' + str(author) + '.  You should see it at the top of the list.', value="Please try to assist you within the next 24 hours.\nBe sure to add anyone you need to the chat.", inline=False)
    embed.set_footer(text="Please note that this is still a work in progress.  If you find any bugs, report them using $report")

    await client.send_message(discord.Object(id='522142350340784140'), embed=embed) #Posts in #staff-chat


@client.command(pass_context=True)
async def add(ctx):
    if ctx.message.author.id in Admin_id:
        ticket = discord.utils.get(client.get_all_channels(), name = "ticket-" + str(eyedee)) #makes variable to easly call on the channel
        server = ctx.message.server
        staff = discord.PermissionOverwrite(read_messages=True)
        admin = discord.utils.get(server.roles, name="Administrator")
        await client.edit_channel_permissions(ticket, admin, staff)





@client.command()
async def close(ctx):
    channel = ctx.channel
    if "ticket-" in str(ctx.message.channel):
        await channel.delete()
    else:
        await channel.send("I can only close tickets, silly. :stuck_out_tongue_winking_eye: ")

'''
#MUSIC COMMANDS

@client.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")


@client.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")


@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print("No more queued song(s)\n")
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("Song done, playing next queued\n")
                print(f"Songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return

        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")



    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return


    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:
            print("Removed old Queue Folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old Queue folder")

    await ctx.send("Getting everything ready now")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        c_path = os.path.dirname(os.path.realpath(__file__))
        system("spotdl -f " + '"' + c_path + '"' + " -s " + url)

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")


@client.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Music paused")
    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing failed pause")


@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("Music is not paused")
        await ctx.send("Music is not paused")


@client.command(pass_context=True, aliases=['s', 'sto'])
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    queue_infile = os.path.isdir("./Queue")
    if queue_infile is True:
        shutil.rmtree("./Queue")

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("Music stopped")
    else:
        print("No music playing failed to stop")
        await ctx.send("No music playing failed to stop")


queues = {}

@client.command(pass_context=True, aliases=['q', 'que'])
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
    except:
        print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL)")
        q_path = os.path.abspath(os.path.realpath("Queue"))
        system(f"spotdl -ff song{q_num} -f " + '"' + q_path + '"' + " -s " + url)


    await ctx.send("Adding song " + str(q_num) + " to the queue")

    print("Song added to queue\n")


@client.command(pass_context=True, aliases=['n', 'nex'])
async def next(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Playing Next Song")
        voice.stop()
        await ctx.send("Next Song")
    else:
        print("No music playing")
        await ctx.send("No music playing failed")

'''
@client.command(pass_context=True, aliases=['j'])
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    try:
        await client.join_voice_channel(channel)
    except:
        await client.say('I am already in a voice channel ({})'.format(channel))
        raise Exception ('Already in VC')
    await client.say("Joined {}!".format(channel))


@client.command(pass_context=True, aliases=['l'])
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    await client.say("Leaving! :wave:")


@client.command(pass_context=True, aliases=['p'])
async def play(ctx, url):
    await client.say("Loading...")
    message = ctx.message.content
    server = ctx.message.server
    channel = ctx.message.author.voice.voice_channel
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    try:
        await client.join_voice_channel(channel)
    except:
        pass
    voice_client = client.voice_client_in(server)
    
    channel = ctx.message.author.voice.voice_channel
    author = ctx.message.author
    if url == 'https://www.youtube.com/watch?v=rY-FJvRqK0E':
        await client.say('NO.  I\'m not playing Flamingo by Kero Kero again.  Geez...')
        return
    
    try:
        player = await voice_client.create_ytdl_player(url)
    except:
        await client.say('There was a problem loading your video.  Maybe I\'m not in a voice channel?')
        raise Exception ('error')
        
    
    players[server.id] = player
    
    player.start()
    embed=discord.Embed(title="Playing!", description="Playing {}, requested by {}".format(url, ctx.message.author.mention), color=0xff00f6)
    embed.set_footer(text="Please note that this is still a work in progress.  If you find any bugs, report them using $report")
    await client.say(embed=embed)


@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
    embed=discord.Embed(title="Paused", description="You can resume by typing $resume", color=0xff00f6)
    embed.set_footer(text="Please note that this is still a work in progress.  If you find any bugs, report them using $report")
    await client.say(embed=embed)


@client.command(pass_context=True, aliases=['s'])
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()
    embed=discord.Embed(title="Stopping!", description="Stopping and cleaning out queue.", colour=0xff00f6)
    embed.set_footer(text="Please note that this is still a work in progress.  If you find any bugs, report them using $report")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

@client.command(pass_context=True, aliases=['q'])
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]

    embed=discord.Embed(title="Queued!", description="{} queued by {}.".format(url, ctx.message.author.mention), colour=0xff00f6)
    embed.set_footer(text="Please note that this is still a work in progress.  If you find any bugs, report them using $report")
    print("Music queued")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def lyrics(ctx, song, artist):
    lyricss = getLyrics(artist, song)
    embed=discord.Embed(title="Lyrics for {} by {}!".format(song, artist), colour=0xff00f6)
    embed.insert_field(value=lyricss, inline=False)
    embed.set_footer(text="Please note that this is still a work in progress.  If you find any bugs, report them using $report")
    await client.say(embed=embed)


#GAME COMMANDS
 



#ADMIN COMMANDS
    


    
#HELP COMMANDS
'''
'''
@client.command()
async def help(ctx):
    author = ctx.message.author
    message = ctx.message
    content = ctx.message.content[6:]
    embed = discord.Embed(
        color = discord.Colour.purple()
        )
    embed.set_author(name='Help')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/522142350340784140/550739276069863446/ahs.png")
    #embed.add_field(name='$help <commmand>', value= 'Gives more detail on a command. (WIP)', inline=False)
    embed.add_field(name='$ping', value= 'Returns Pong!', inline=False)
    embed.add_field(name='$oof', value= 'OOF!', inline=False)
    embed.add_field(name='$version', value= 'Returns current version.', inline=False)
    embed.add_field(name='$report <report>', value= 'Sends a report to staff so they can look at it.', inline=False)
    embed.add_field(name='$poke <recipient>', value= 'Sends a DM to the person you specify.', inline=False)
    embed.add_field(name='$suggest <suggestion>', value= 'Sends your suggestion to #server-suggestions.', inline=False)
    embed.add_field(name='$maketicket <subject>', value= 'Makes a ticket for staff to help you with any questions you may have. (WIP)', inline=False)    
    embed.add_field(name='$help_music', value= 'DMs you music command help', inline=False)
    try:
        await author.send(embed=embed)
        await ctx.send("Check your DMs for list of commands!")
    except Exception:
        raise "Pasting help in chat"
        await ctx.send(embed=embed)
        await ctx.send("If you want this DMed to you, friend @AHS Bot#8029.")

@client.command(pass_context=True)
async def help_admin(ctx):

    author = ctx.message.author
    channel = ctx.message.channel
    log = client.get_channel(522142442401693707)
    owner = discord.utils.get(ctx.guild.roles, name="Owner")
    admin = discord.utils.get(ctx.guild.roles, name="Administrator")
    mod = discord.utils.get(ctx.guild.roles, name="Moderators")
    if owner in ctx.author.roles or admin in ctx.author.roles or mod in ctx.author.roles:
    
         embed = discord.Embed(
            color = discord.Colour.purple()
            )
         embed.set_author(name='Help (Admin)')
         embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/522142350340784140/550739276069863446/ahs.png")
         embed.add_field(name='$help_admin', value= 'DMs you this.', inline=False)
         embed.add_field(name='$warn <user> <reason>', value= 'DMs user with reason.', inline=False)
         embed.add_field(name='$purge <amount>', value= 'Deletes messages.', inline=False)
         embed.add_field(name='$mute <user>', value= 'Mutes user.', inline=False)
         embed.add_field(name='$unmute <user>', value= 'Un-mutes user.', inline=False)
         embed.add_field(name='$kick <user> <reason>', value= 'Kicks user with an optional reason', inline=False)
         embed.add_field(name='$nick <user>', value= 'Changes nick on a user', inline=False)
         try:
             await author.send(embed=embed)
             await ctx.send("Check your DMs for list of commands!")
         except Exception:
            raise "Pasting help in chat"
            await ctx.send(embed=embed)
            
    else:
        await ctx.send("You can't use that command!")

@client.command(pass_context=True)
async def help_music(ctx):

    author = ctx.message.author
    
    embed = discord.Embed(
        color = discord.Colour.purple()
        )
    embed.set_author(name='Help (music)')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/522142350340784140/550739276069863446/ahs.png")
    embed.add_field(name='$join', value= 'Joins your voice channel.', inline=False)
    embed.add_field(name='$play <url>', value= 'Plays music to the voice channel.', inline=False)
    embed.add_field(name='$pause', value= 'Pauses song.', inline=False)
    embed.add_field(name='$resume', value= 'Resumes song.', inline=False)
    embed.add_field(name='$stop', value= 'Stops song.', inline=False)
    embed.add_field(name='$queue <url>', value= 'Queues a song to be next.', inline=False)
    embed.add_field(name='$leave', value= 'Leave\'s voice channel', inline=False)

    try:
        await client.send_message(author, embed=embed)
        await client.say("Check your DMs for list of commands!  :musical_note: ")
    except Exception:
        raise "Pasting help in chat"
        await client.say(embed=embed)
'''

client.run(TOKEN)
