import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

bot.run("MTE5NTAwNjU2MjI4OTMxOTk0OA.GuahBQ.9pnq2UexOU7rQWRD2C7lJYdqAUvtM7EwfCvLcI")
