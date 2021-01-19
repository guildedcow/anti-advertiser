import asyncio
import discord
import random
import confidental  # separate python file to store my bot token

client = discord.Client()
listOfStatuses = ["for children to run over", "fox news", "for self advertisers", "for based individuals"]


async def changePresence():
    randomNum = random.randint(0, len(listOfStatuses) - 1)
    activity = discord.Activity(name=listOfStatuses[randomNum], type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)


@client.event
async def on_ready():
    print(f"Logged in: {client.user}")
    await changePresence()


@client.event
async def on_message(message):
    if message.author == client.user:
        if "no self advertising" in message.content:
            await asyncio.sleep(3)
            await message.delete()
        return

    if 'discord.gg' in message.content:
        await message.delete()
        await message.channel.send("no self advertising.")



client.run(confidental.token)  # replace with whatever discord token you want to use
