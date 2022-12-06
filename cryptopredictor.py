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
    file = discord.File(r"C:\Users\shimo\Downloads\ezgif.com-gif-maker.png", filename="ezgif.com-gif-maker.png")
    embed = discord.Embed(title="Crypto Crab Information", description="Presented is a list of all of the commands. what they do, and how to use them.", colour=discord.Colour.dark_red())
    embed.set_footer(text="$$$Mr. Crypto Crab$$$")
    embed.set_image(url="attachment://ezgif.com-gif-maker.png")
    embed.add_field(name="Price Graph HTML", value="Allows you to download HTML file of price graph. You can choose your preferred crypto, file name, time period, and candle intervals.")
    embed.add_field(name="Price Graph Open", value="Opens price graph ONLY if you have the source code. You can choose your preferred crypto, file name, time period, and candle intervals.")
    embed.add_field(name="Random", value="Randomly picks a crypto and will create an HTML file with a graph of its price with a 24h time period and 30m candle intervals. It will pick from BTC, BNB, ETH, and DOGE.")
    embed.add_field(name="Command Presets", value="The time period that is preset is 24 hours. The candle intervals that is preset is 15 minutes.")
    embed.add_field(name="How To Set Cryptocurrency", value="When setting a crypto make sure you enter an all-caps version of its abbreviation. You should be able to enter most cryptocurrencies. If the graph is blank it may be because the database does not have the crypto.")
    embed.add_field(name="How To Set Time Periods and Candle Intervals", value="When setting time periods or candle intervals, use 'm' for minutes, 'h' for hours, 'd' for days, 'mo' for months, and 'y' for years. Be mindful of the time period and intervals. If the difference between them is too big the graph will be blank.")

    await ctx.send(file=file, embed=embed)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('/random'):
        filename="cryptograph"
        timeperiod="24h"
        candleinterval="30m"
        randomnum = random.randint(0,4)
        botmess = await message.channel.send(file=discord.File(r"C:\Users\shimo\Downloads\SpinningWheel.gif"))
        await asyncio.sleep(5)
        await botmess.delete()
        if(randomnum == 0):
            await message.channel.send(file=discord.File(r"C:\Users\shimo\Downloads\GreenWins.png"))
            await message.channel.send('DOGE')
            crypto = 'DOGE'
        elif(randomnum == 1):
            await message.channel.send(file=discord.File(r"C:\Users\shimo\Downloads\YellowWins.png"))
            await message.channel.send('BNB')
            crypto = 'BNB'
        elif(randomnum == 2):
            await message.channel.send(file=discord.File(r"C:\Users\shimo\Downloads\RedWins.png"))
            await message.channel.send('ETH')
            crypto = 'ETH'
        else:
            await message.channel.send(file=discord.File(r"C:\Users\shimo\Downloads\BlueWins.png"))
            await message.channel.send('BTC')
            crypto = 'BTC'
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
    await message.channel.send(file=discord.File(path))


@bot.command(description="Opens price graph ONLY if you have the source code.")
async def pricegraphopen(ctx, crypto, timeperiod= "24h", candleinterval= "30m"):
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
    figure.show()


@bot.command(description="Allows you to download HTML file of price graph.")
async def pricegraphhtml(ctx, crypto, filename, timeperiod= "24h", candleinterval= "30m"):
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



bot.run("MTA0MjIzNjM2ODE2NTgxNDMzMg.GR8DPe.35EGYyBHOFvHsyzK6ufqbVS-xLaQpJ1sQz5G8U")
