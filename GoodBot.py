#Permission ID: 429497068544
import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	print(f'{message.content} has length {len(message.content)}')
	if ('M' in message.content):
		await message.delete()
		newMessage = message.content.replace('M', ':x:')
		await message.channel.send(newMessage)
	elif ('m' in message.content):
		await message.delete()
		newMessage = message.content.replace('m', ':x:')
		await message.channel.send(newMessage)
	elif message.content == 'raise-exception':
		raise discord.DiscordException
    
client.run(TOKEN)