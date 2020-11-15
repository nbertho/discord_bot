'''
    Discord bot made with python
    Made by nbertho and clossetdidier
'''

# Import
import os
import discord
from dotenv import load_dotenv


# Bot config
load_dotenv()

TOKEN = str(os.getenv('DISCORD_TOKEN'))
SERVER = str(os.getenv('DISCORD_SERVER'))

client = discord.Client()

# Functions
def print_help():
    """
    Print the bot help
    """
    print('Discord bot help : ')


# Events

@client.event
async def on_ready():
    ''' Triggered on connection '''
    guild = discord.utils.get(client.guilds, name=SERVER)
    print(
        f'{client.user} is now connected to the following server:\n'
        f'\t{guild.name} (id: {guild.id})'
    )

@client.event
async def on_message(message):
    ''' Triggered on new message '''

    # Prevent bot to reply to his own message
    if message.author == client.user:
        return