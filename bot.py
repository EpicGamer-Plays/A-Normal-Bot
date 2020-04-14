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
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$ping':
        await client.send_message(message.channel,'pong')
    if ('T-series') in message.content:
       await client.delete_message(message)
    if ('T series') in message.content:
       await client.delete_message(message)
    if ('Homework') in message.content:
       await client.delete_message(message)
    if ('love') in message.content:
       await client.delete_message(message)
    if message.content == '$poop':
        em = discord.Embed(description='We entered ur house after u pooped and fished out this bad boi')
        em.set_image(url='https://discordapp.com/channels/657637646452916265/699573438120984576/699588952826314814')
        await client.send_message(message.channel, embed=em)
    if message.content == '$fish':
        em = discord.Embed(description='Umm bro...')
        em.set_image(url='https://discordapp.com/channels/657637646452916265/699573438120984576/699590761410461706')
        await client.send_message(message.channel, embed=em)
    if message.content == '$kill':
        em = discord.Embed(description='OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOF')
        em.set_image(url='https://discordapp.com/channels/657637646452916265/699573438120984576/699591788104777738')
        await client.send_message(message.channel, embed=em)
    if ('nigger') in message.content:
       await client.delete_message(message)
    if ('cunt') in message.content:
       await client.delete_message(message)
    if message.content.startswith('$insult'):
        randomlist = ["Douchebag""Asslicker""Poophead""U Mine diamonds with a stone pick""OOF boi""chicken""Retard""cow""bigtits""Tomiprime fan""frog"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '$bedrock':
        em = discord.Embed(description='Still going man')
        em.set_image(url='https://discordapp.com/channels/657637646452916265/699573438120984576/699594593909473360')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('$pingme'):
        await client.send_message(message.channel,'PING PONG, <@%s>'  %(message.author.id))
client.run('Njk5NTY5MTEwMjUzNjk5MDkz.XpWi6w.FJU6pcy2ADYaP4FlGJh6AZMP37s')
