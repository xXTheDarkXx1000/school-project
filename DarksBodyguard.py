import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to Nikos Discord Server im Darks bodyguard (the previous Owner) I will keep an :eyes: on @everyone')
    print('Sent message to ' + member.name)
 

@client.event
async def on_message(message):
    if message.content == '!ping':
        await client.send_message(message.channel,'pong')
client.run('NTAwNzc2MjA0NTcyNTU3MzMz.XkBGSw.vvRFv-aZKbGgPa_SI7osul4wwfc')
