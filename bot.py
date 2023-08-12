import discord
from discord.ext import commands


token = open("TOKEN", "r").readline().strip()

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')
    print(f'Hello, {ctx.author.name}!')


bot.run(token)