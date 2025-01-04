import discord
from discord.ext import commands
import yt_dlp as ytdl

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

ytdl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'extract_flat': True,
    'socket_timeout': 120,
    'retries': 10,
    'nocheckcertificate': True,
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'opus',
    }],
}

ffmpeg_opts = {
    'options': '-vn'  # Simplified options
}

async def play_music(ctx, url):
    if not ctx.author.voice:
        await ctx.send("Vous devez être dans un canal vocal!")
        return
        
    voice = ctx.voice_client or await ctx.author.voice.channel.connect()
    
    try:
        with ytdl.YoutubeDL(ytdl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info.get('url') or info['formats'][0]['url']
            source = discord.FFmpegPCMAudio(audio_url, **ffmpeg_opts)
            voice.play(source)
            await ctx.send(f"Lecture de: {info.get('title', 'musique')}")
    except Exception as e:
        await ctx.send(f"Erreur: {str(e)}")

@bot.command()
async def play(ctx, url: str):
    await play_music(ctx, url)

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Canal vocal quitté.")

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

# Lancer le bot
bot.run('Your Token ???')
