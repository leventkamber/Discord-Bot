import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"User {member.mention} has been kicked!")

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"User {member.mention} has been banned!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have that permission!")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("There is not such a command!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter required argument!")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send("You have passed too many arguments!!")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Provided member was not found in the bot's cachet!")


def setup(client):
    client.add_cog(Admin(client))
