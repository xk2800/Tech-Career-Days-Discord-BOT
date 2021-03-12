import discord
#from discord.ext.commands import Bot
from discord.ext import commands
#import asyncio
import os
import requests
import json
import random
from replit import db
from flash import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="Bring in Tech Career Days"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  msg = message.content


  if message.content.startswith("!TCD"):
      await message.channel.send('**Tech Career Days 2021**\n6th January - 7th January 2021, 10am to 5pm')

  if message.content.startswith("!help"):
      await message.channel.send('using !<command> will trigger command\n\n\nAvailable list of commands:\n`!TCD`\n`!list`\n`!webteam`\n`!website`\n`!event-management`\n`!marketing`\n`!publicity`\n`!sponsorship`')

  if message.content.startswith("!list"):
      f = open("designition.txt", "r")
      await message.channel.send(f.read())

  if message.content.startswith("!webteam"):
      f = open("webteam.txt", "r")
      await message.channel.send(f.read())

  if message.content.startswith("!event-management"):
      f = open("managementteam.txt", "r")
      await message.channel.send(f.read())

  if message.content.startswith("!marketing"):
      f = open("marketingteam.txt", "r")
      await message.channel.send(f.read())

  if message.content.startswith("!publicity"):
      f = open("publicityteam.txt", "r")
      await message.channel.send(f.read())

  if message.content.startswith("!sponsorship"):
      f = open("sponsorshipteam.txt", "r")
      await message.channel.send(f.read())

  if message.content.startswith("!website"):
      f = open("webteam.txt", "r")
      await message.channel.send(f.read() + '\n\nWebsite Link : https://techcareerdays.com\nResume Portal: https://resume.techcareerdays.com/')
      
keep_alive()
client.run(os.getenv('TOKEN'))