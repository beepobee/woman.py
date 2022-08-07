import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
from colorama import Fore, Style
from discord import Member
import requests
import json
from discord.ext.commands import has_permissions, MissingPermissions
import random
import time
import sys

anydeskid = random.randint(1000000,999999999)


  
 




client = commands.Bot(command_prefix="-")

@client.event
async def on_connect():
  print ("Connected!")
  await client.change_presence(activity=discord.Streaming(name='idk?', url=''))


owner = 924351148352217129
@client.command()
async def nothingimportant(ctx):
  await ctx.send("No")

@client.command()
async def test(ctx):
  await ctx.send("This is a test message.")
  
@client.command()
async def bye(ctx):
 await ctx.send("bye")

jokes = ["I SLEPT WITH YOUR MOTHER", "STOP CALLING NOW.", 
 "STOP. CALLING. THIS. CALL. CENTER. @NoMoreScammers", "You're gonna get scammed"]


  
@client.command()
async def uwu(ctx):
  await ctx.send("https://tenor.com/view/memes-gif-24034402")


@client.command()
async def commands(ctx):
    await ctx.send(
        "shrug")

activity_string = 'on {} servers.'.format(len(client.guilds))

owner = 924351148352217129
@client.command()
async def dnd(ctx):
 if ctx.author.id == owner:
  await client.change_presence(status=discord.Status.dnd) 
  await ctx.send("DND.")
 else: await ctx.send(":dash:")

@client.command()
async def idle(ctx):
  if ctx.author.id == owner:
   await ctx.send("Status is now in idle")
   await client.change_presence(status=discord.Status.idle) 
  else: await ctx.send(":dash:")


@client.command()
async def restart(ctx):
 if ctx.author.id == owner:
  await ctx.send("refreshing")
  await client.change_presence(activity=discord.Streaming(name='-help', url='https://buzzr.is-from.space/cookie.jpeg'))
 else: await ctx.send("you dont have perms bud.....")


@client.command()
async def sus(ctx):
 await ctx.send("https://tenor.com/view/raccoon-sus-camera-ngl-thats-kinda-sus-bro-gif-22434863")

@client.command()
async def qwerty(ctx):
  await ctx.send("A phenomena that happens to a computer's keyboard when a human being is bored to death")

@client.command()
async def Floppa(ctx):
 await ctx.send("https://tenor.com/view/caracal-big-floppa-flop-fo-gif-18296053")

@client.command()
async def broom(ctx):
 await ctx.send("shoo")

@client.command()
async def hello(ctx):
  await ctx.send("hi chat")

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)
 await ctx.send(f'bye')

@client.command()
async def yipee(ctx):
  await ctx.send("https://tenor.com/view/yipee-meme-gif-25350387")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f'ban')



@client.command()
async def e(ctx):
    await ctx.send("Honey, I am home")


keep_alive()

token = os.environ['Token']
client.run(token)