import discord
import random
import os
import datetime
from discord.ext import commands
import asyncio

with open('helpcommand.txt', 'r') as f:
    f_contents = f.read()
message = (f_contents)
def gen():
    chars = ['a', 'b', 'c', 'd',  'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '1','2','3','4','5','6','7','8','9','0'
    ]
    return "".join(random.choices(chars, k=16))
Client = discord.Client()
link = "https://discord.gift/"

@Client.event
async def on_ready():
	print("Ready!")
async def ch_pr():
	await Client.wait_until_ready()

	statuses = [f"{len(Client.guilds)} servers", "Nitro Gen Bot", "/nitro"]

	while not Client.is_closed():

		status = random.choice(statuses)

		await Client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

		await asyncio.sleep(5)

Client.loop.create_task(ch_pr())

@Client.event
async def on_message(message):
    x=0
    if message.author == Client.user:   
        return
    if message.content == '/nitro':
        logmess = "Command run at:"+str(datetime.datetime.now())+"\n"
        f=open("log.txt", "a+")
        f.write(logmess)
        game=discord.Game(name="""discord.gg/F7KD9tjEaw""")
        await Client.change_presence(activity=game)
        while True:
            await message.channel.send(link + gen())
        else:
            return

#client = MyClient()
Client.run(os.environ['TOKEN'])
