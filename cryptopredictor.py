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
import os.path

from datetime import date, timedelta


intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Crypto Crab Information", description="Presented is a list of all of the commands. what they do, and how to use them.", colour=discord.Colour.dark_red())
    embed.set_image(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fscreenrant.com%2Fspongebob-squarepants-mr-krabs-good-bad-guy%2F&psig=AOvVaw23xOkCJWqy8zkfZDguwcQD&ust=1670381459921000&source=images&cd=vfe&ved=0CA4QjRxqFwoTCNiW4f394_sCFQAAAAAdAAAAABAE")
    embed.add_field(name="Price Graph HTML", value="Allows you to download HTML file of price graph. You can choose your preferred crypto, file name, time period, and candle intervals.")
    await ctx.send(embed=embed)


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

<<<<<<< HEAD
@bot.command(description="Opens price graph ONLY if you have the source code. You can choose your preferred crypto.")
async def pricegraphopen(ctx, crypto):
=======
@bot.command(description="poops") # this decorator makes a slash command
async def poo(ctx): # a slash command will be created with the name "ping"
    await ctx.send("poopy")

@bot.command(description="poops in agony") # this decorator makes a slash command
async def poops(ctx): # a slash command will be created with the name "ping"
    await ctx.send("AHHH")

"""
@bot.command(description="crypto picker")
async def pricegraph(ctx, crypto):
>>>>>>> 5e0184f7a3560398b6d7b788c704bf74f7041faa
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
    figure.update_layout(title = crypto + " Price",
                         xaxis_rangeslider_visible=True)

    figure.show()
<<<<<<< HEAD


@bot.command(description="Allows you to download HTML file of price graph. You can choose your preferred crypto.")
async def pricegraphhtml(ctx, crypto, filename, timeperiod= "24h", candleinterval= "15m"):
    path = r"C:\Users\shimo\Documents\GitHub\pythonfinalproject\graphs\\" + filename + ".html"

    today = date.today()
    first_date = today.strftime("%Y-%m-%d")
    end_date = first_date
    second_date = date.today() - timedelta(days=1000)
    second_date = second_date.strftime("%Y-%m-%d")
    start_date = second_date

    crypto_data = yf.download(tickers= crypto + '-USD', period = str(timeperiod), interval = str(candleinterval))
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
    figure.update_layout(title = crypto + " Price",
                         xaxis_rangeslider_visible=True)
    figure.write_html("graphs/" + filename + ".html")
    await ctx.send(file=discord.File(path))


=======
"""
>>>>>>> 5e0184f7a3560398b6d7b788c704bf74f7041faa
bot.run("MTA0MjIzNjM2ODE2NTgxNDMzMg.GR8DPe.35EGYyBHOFvHsyzK6ufqbVS-xLaQpJ1sQz5G8U")
