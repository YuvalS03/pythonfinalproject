import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/random'):
        botmess1 = await message.channel.send('poo')
        botmess2 = await message.channel.send('poo')
        botmess3 = await message.channel.send('poo')
        botmess4 = await message.channel.send('poo')
        botmess5 = await message.channel.send('poo')
        await botmess1.edit(content="|  \               /   |")
        await botmess2.edit(content="|      \ /\ /       |")
        await botmess3.edit(content="|          0            |")
        await botmess4.edit(content="|       /      \       |")
        await botmess5.edit(content="|  /               \   |")

        await botmess1.edit(content="|  \               /   |")
        await botmess2.edit(content="|      \       /       |")
        await botmess3.edit(content="|          0>         |")
        await botmess4.edit(content="|       /      \       |")
        await botmess5.edit(content="|  /               \   |")

        await botmess1.edit(content="|  \               /   |")
        await botmess2.edit(content="|      \      /        |")
        await botmess3.edit(content="|          0            |")
        await botmess4.edit(content="|      / \ / \      |")
        await botmess5.edit(content="|  /               \   |")

        await botmess1.edit(content="|  \               /   |")
        await botmess2.edit(content="|      \       /       |")
        await botmess3.edit(content="|        <0           |")
        await botmess4.edit(content="|       /      \       |")
        await botmess5.edit(content="|  /               \   |")




client.run('MTA0MjIzNjM2ODE2NTgxNDMzMg.GR8DPe.35EGYyBHOFvHsyzK6ufqbVS-xLaQpJ1sQz5G8U')
