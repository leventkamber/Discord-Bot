import discord
from discord.ext import commands
import api


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("Bot is ready to be used!")

cogs = ['greetings_cog', 'admin_cogs', 'music_cog']

if __name__ == '__main__':
    for cog in cogs:
        client.load_extension(cog)

client.run(api.BOTTOKEN)
