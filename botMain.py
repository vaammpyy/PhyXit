import discord
import responses
from discord.ext import commands
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if(response[1]=='m'):
            for i in response[0]:
                await message.author.send(file=discord.File(i)) if is_private else await message.channel.send(file=discord.File(i))
        else:
            await message.author.send(response[0]) if is_private else await message.channel.send(response[0])
    except Exception as ex:
        print(ex)
def run_discordbot():
    TOKEN = 'MTEzOTgzMDg5OTY4NTQ3NDM5NQ.G4uAg7.bEMJ5IVJWRGKvg1WoBOTwVH8ppj1T80pfy3JxQ'        
    intents=discord.Intents.default()
    client=discord.Client(intents=intents)
    intents.message_content=True

    @client.event 
    async def on_ready():
        print(f'{client.user} is now running')
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username=str(message.author)
        user_message = str(message.content).split()
        channel = str(message.channel)

        print (f"{username} said {user_message} on {channel}")
        print(f"{message.content}")
        if(user_message[0]=='<@1139830899685474395>'):
            if user_message[1][0] =='$':
                user_message = user_message[1:]
                await send_message(message, user_message[1:], is_private=True)
            else:
                await send_message(message, user_message[1:], is_private=False)
    client.run(TOKEN)