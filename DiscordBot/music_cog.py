import discord
import youtube_dl
from discord.ext import commands
import api


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def play(self, context, url):
        # ако user-a е във 'voice channel'
        if context.author.voice:
            channel = context.author.voice.channel
            await channel.connect()

            voice = context.voice_client
            with youtube_dl.YoutubeDL(api.YDL_OPTIONS) as ydl:
                url_info = ydl.extract_info(url, download=False)
                url = url_info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url, **api.FFMPEG_OPTIONS)
                voice.play(source)

        else:
            await context.send("Please join voice channel in order to use this command")

    @commands.command(pass_context=True)
    async def leave(self, context):
        # ако бот-а е във 'voice channel'
        if context.voice_client:
            # отиди в този сървър(guild), оитиди във voice channel(voice_client) и го махни от там
            await context.guild.voice_client.disconnect()
            await context.send("I left the voice channel")
        else:
            await context.send("I am not in a voice channel")

    @commands.command(pass_context=True)
    async def pause(self, context):
        guild = context.guild
        voice = discord.utils.get(self.client.voice_clients, guild=guild)
        # ако бот-а е пуснат
        if voice.is_playing():
            voice.pause()

    @commands.command(pass_context=True)
    async def resume(self, context):
        guild = context.guild
        voice = discord.utils.get(self.client.voice_clients, guild=guild)
        # ако бот-а е спрян
        if voice.is_paused():
            voice.resume()


def setup(client):
    client.add_cog(Music(client))
