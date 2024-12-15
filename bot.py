import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load Token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Bot Setup
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Command: Trivia
@bot.command()
async def trivia(ctx):
    question = "What is the capital of the Fortress of Guffal?"
    await ctx.send(f"Trivia Time! {question}")

# Command: Leaderboard
@bot.command()
async def leaderboard(ctx):
    await ctx.send("🏆 Leaderboard:\n1. Player1 - 150pts\n2. Player2 - 120pts")

# Run Bot
bot.run(TOKEN)
