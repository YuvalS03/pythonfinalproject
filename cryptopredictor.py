import discord
import asyncio
import random
import pandas as pd
import yfinance as yf
import datetime
import plotly
import plotly.graph_objects as go
from autots import AutoTS
import plotly.io as pio
import os
from datetime import date, timedelta


intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('/random'):
        randomnum = random.randint(0,4)
        botmess = await message.channel.send(file=discord.File(r"C:\Users\ianth\Pictures\Saved Pictures\SpinningWheel.gif"))
        await asyncio.sleep(5)
        await botmess.delete()
        if(randomnum == 0):
            await message.channel.send(file=discord.File(r"C:\Users\ianth\Pictures\Screenshots\GreenWins.png"))
            await message.channel.send('DOGE')
            return 'DOGE'
        elif(randomnum == 1):
            await message.channel.send(file=discord.File(r"C:\Users\ianth\Pictures\Screenshots\YellowWins.png"))
            await message.channel.send('BNB')
            return 'BNB'
        elif(randomnum == 2):
            await message.channel.send(file=discord.File(r"C:\Users\ianth\Pictures\Screenshots\RedWins.png"))
            await message.channel.send('BTH')
            return 'BTH'
        else:
            await message.channel.send(file=discord.File(r"C:\Users\ianth\Pictures\Screenshots\BlueWins.png"))
            await message.channel.send('BTC')
            return 'BTC'

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(description="poops") # this decorator makes a slash command
async def poo(ctx): # a slash command will be created with the name "ping"
    await ctx.send("poopy")

@bot.command(description="poops in agony") # this decorator makes a slash command
async def poops(ctx): # a slash command will be created with the name "ping"
    await ctx.send("AHHH")

"""
@bot.command(description="crypto picker")
async def pricegraph(ctx, crypto):
    today = date.today()
    first_date = today.strftime("%Y-%m-%d")
    end_date = first_date
    second_date = date.today() - timedelta(days=730)
    second_date = second_date.strftime("%Y-%m-%d")
    start_date = second_date

    crypto_data = yf.download(tickers= crypto + '-USD', period = '22h', interval = '15m')
    crypto_data["Date"] = crypto_data.index
    crypto_data = crypto_data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
    crypto_data.reset_index(drop=True, inplace=True)
    print(crypto_data.head())
    print(crypto_data.shape)

    figure = go.Figure(data=[go.Candlestick(x=crypto_data["Date"],
                                            open=crypto_data["Open"],
                                            high=crypto_data["High"],
                                            low=crypto_data["Low"],
                                            close=crypto_data["Close"])])
    figure.update_layout(title = "Cryptocurrency Price",
                         xaxis_rangeslider_visible=True)

    figure.show()
"""
bot.run("MTA0MjIzNjM2ODE2NTgxNDMzMg.GR8DPe.35EGYyBHOFvHsyzK6ufqbVS-xLaQpJ1sQz5G8U")
