import threading
import discord.ext
from discord.ext import commands
import webbrowser
from flask import Flask, redirect, url_for

app = Flask(__name__)

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def join(ctx):
    guild_id = '1170003093056929798'
    channel_name = 'The Safe Space'
    
    guild = discord.utils.get(bot.guilds, id=guild_id)
    
    if guild:
        voice_channel = discord.utils.get(guild.voice_channels, name=channel_name)
        
        if voice_channel:
            invite_link = await voice_channel.create_invite()
            return invite_link.url
    
    return 'Error: Voice channel not found.'

@app.route('/')
def home():
    return 'Welcome to the Discord Voice Channel website!'

def run_bot():
    bot.run('MTE2OTk5NzUxOTA3MDE4MzU1Ng.GsHAVi.wUc7LzkJPnbCW4qzM6vGwoLf8O4q6ASpVF2DAs')

def run_app():
    app.run(debug=True)

if __name__ == '__main__':
    # Start the bot in a separate thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    
    # Start the Flask app in the main thread
    run_app()

