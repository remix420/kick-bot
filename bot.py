import discord
import asyncio
from discord.ext import tasks
from discord.ext import commands

token = ''


prefix = '!'
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True) # Enable intents in discord devolper portal!!!
client = commands.Bot(command_prefix = prefix, intents = intents)



	




count = 0




@client.event
async def on_member_join(member : discord.Member):
	global count
	await member.kick()
	count += 1
	print('kicked {} [{}]'.format(member, count))
	
	

client.run(token)
