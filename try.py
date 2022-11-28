import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@commands.command()
async def poo(ctx):
    ctx.respond("poopy pants")

bot.run("MTA0MjIzNjM2ODE2NTgxNDMzMg.GR8DPe.35EGYyBHOFvHsyzK6ufqbVS-xLaQpJ1sQz5G8U")
