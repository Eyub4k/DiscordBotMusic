import discord
from discord.ext import commands
import yt_dlp as ytdl
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Configuration de yt-dlp
ytdl_opts = {
    'format': 'bestaudio/best',
    'quiet': False,  # Affiche des logs détaillés
    'retries': 10,
    'fragment_retries': 10,
    'socket_timeout': 10,
    'noprogress': True,
    'nocheckcertificate': True,
}
# Options pour FFmpeg
ffmpeg_opts = {
    'options': '-vn',  # Nous ne voulons pas de vidéo, seulement de l'audio
}

# Fonction pour joindre le canal vocal
async def join_voice_channel(ctx):
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    return voice

# Fonction pour jouer la musique
async def play_music(ctx, url):
    print(f"Attempting to play music from URL: {url}")  # Log pour vérifier l'URL
    voice = await join_voice_channel(ctx)
    
    # Télécharger l'audio depuis YouTube avec yt-dlp
    with ytdl.YoutubeDL(ytdl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']  # URL du flux audio

        # Lire le flux audio dans le canal vocal
        voice.play(discord.FFmpegPCMAudio(url2, **ffmpeg_opts))
    
    await ctx.send(f"Lecture de la musique: {url}")

# Commande pour jouer la musique
@bot.command()
async def play(ctx, url: str):
    """Commande pour jouer de la musique depuis un lien YouTube."""
    await play_music(ctx, url)

# Commande pour quitter le canal vocal
@bot.command()
async def leave(ctx):
    """Commande pour faire quitter le bot du canal vocal."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Je quitte le canal vocal.")
    else:
        await ctx.send("Je ne suis pas dans un canal vocal.")

# Lancer le bot
bot.run('Your Token ???')
