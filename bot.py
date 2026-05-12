import discord
from discord.ext import commands

# Enable intents
intents = discord.Intents.default()

# Create bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Event when bot is online
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Bot is online!")

# Run bot
bot.run("YOUR_BOT_TOKEN")
