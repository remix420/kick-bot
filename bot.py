import discord
import asyncio
from discord.ext import tasks
from discord.ext import commands




token = ''





prefix = '!'
client = commands.Bot(command_prefix = prefix)
client.remove_command("help")

count = 0

@client.event
async def on_member_join(member : discord.Member):
	global count
	await member.kick()
	count += 1
	print('kicked {} [{}]'.format(member, count))
	
	

client.run(token)
