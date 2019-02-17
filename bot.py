import discord
import discord.ext.commands
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print ("Bot is online and connected to Discord")
    
@client.event
async def on_message(message):
    if message.content.startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
        if message.content.upper().startswith('!SAY'):
            if message.author.id == "307820755440107520":
             args = message.content.split(" ")
             await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
             else:
                 await client.send_message(message.channel, "You do not have permission")

 



client.run("BOT_TOKEN")

