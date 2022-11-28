
import discord

bot = discord.Bot()

# we need to limit the guilds for testing purposes
# so other users wouldn't see the command that we're testing

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(description="takes shit") # this decorator makes a slash command
async def poo(ctx): # a slash command will be created with the name "ping"
    await ctx.send("poopy")

@bot.command(description="shits") # this decorator makes a slash command
async def shits(ctx): # a slash command will be created with the name "ping"
    await ctx.send("AHHH")

bot.run("MTA0MjIzNjM2ODE2NTgxNDMzMg.GR8DPe.35EGYyBHOFvHsyzK6ufqbVS-xLaQpJ1sQz5G8U")
