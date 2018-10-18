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
    await client.send_message(member, 'Welcome to Darks Discord Server im his bodyguard and ill keep an :eyes: on @everyone')
    print('Sent message to ' + member.name)
 

@client.event
async def on_message(message):
    if message.content == '!ping':
        await client.send_message(message.channel,'pong')
    if message.content == '!kevin':
        em = discord.Embed(description='')
        em.set_image(url='https://media.discordapp.net/attachments/435499565886603275/500688990328848424/1539291477276.png?width=1026&height=258')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('!1-10rng'):
        randomlist = ["1","2","3","4","5","6","7","8","9","10"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!noticemedaddy'):
        await client.send_message(message.channel,'Daddy has noticed you <@%s>!'  %(message.author.id))
    if message.content == '!creator':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/496040752338698268/501342143126962187/Screenshot_2018-10-15-12-33-55-1-1-1-1.png')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('!!rob 356200510916657172'):
        await client.send_message(message.channel,':eyes: <@%s>!'  %(message.author.id))
    if message.content == '!kommo-o':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/353994821247041536/438735309208027136/kommo-o.png')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('!!rob Đark'):
        await client.send_message(message.channel,':eyes: <@%s>!'  %(message.author.id))
    if message.content.startswith('!!rob Đark#6774'):
        await client.send_message(message.channel,':eyes: <@%s>!'  %(message.author.id))
    if message.content.startswith('!!rob @Đark#6774'):
        await client.send_message(message.channel,':eyes: <@%s>!'  %(message.author.id))
    if message.content == '!serverinvite':
        await client.send_message(message.channel,'https://discord.gg/hACbxTS')
    if message.content == '!help':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/496040752338698268/501340889155764224/help.PNG')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('!1-100rng'):
        randomlist = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!raptor'):
        randomlist = ["https://cdn.discordapp.com/attachments/496040752338698268/501121408102039565/raptorhot.PNG","https://cdn.discordapp.com/attachments/496040752338698268/501121569796521984/raptorhot3.PNG",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!8-ball'):
        randomlist = ["It is decidedly so","Without a doubt","Yes, definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Perhaps","Signs point to yes","Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no.","My sources say no","Error Random response ID= 723 not found","It is certain","maybe :rikoshrug:",]
        await client.send_message(message.channel,(random.choice(randomlist)))
        @bot.command(say)
        async def test(ctx, arg):
            await ctx.send(arg)
    client.run('NTAwNzc2MjA0NTcyNTU3MzMz.DqZhzQ.Fojh7wDGPJuU0yxU378oXVbFInM')
