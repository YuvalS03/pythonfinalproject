import discord


intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} ist online")






bot.run("MTA0MjIzNjM2ODE2NTgxNDMzMg.GR8DPe.35EGYyBHOFvHsyzK6ufqbVS-xLaQpJ1sQz5G8U")
