import discord
from discord.ext import commands
import api
from profanityfilter import ProfanityFilter


class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):
        pf = ProfanityFilter()
        if pf.is_profane(msg.content):
            censored = pf.censor(msg.content)
            await msg.delete()
            await msg.channel.send(censored)
            await msg.channel.send("Don't swear, otherwise you will be banned!")

    @commands.command()
    async def hello(self, context):
        await context.send("Hey, your bot is here!")

    @commands.command()
    async def bye(self, context):
        await context.send("Goodbye!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        server = self.client.get_guild(api.SERVER_ID)
        channel = self.client.get_channel(api.CHANNEL_ID)
        embed = discord.Embed(title=f"Welcome to the {server}!")
        await channel.send(f"Welcome {member.mention}")
        await member.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(api.CHANNEL_ID)
        await channel.send(f"See you {member.mention}")

    @commands.command()
    async def msg(self, context, member: discord.Member, *, message=None):
        await member.send(message)


def setup(client):
    client.add_cog(Greetings(client))
