import discord
from dotenv import load_dotenv
import os
from random import choice
from discord.ext import commands

class TobiBot(commands.Bot):
    def __init__(self):
        # Intents for join/remove/member count thing
        intents = discord.Intents.default()
        intents.members = True
        intents.messages = True
        # Intent to see message content
        intents.message_content = True

        super().__init__(command_prefix=".", intents=intents, help_command=None)

    # React then greet when "lahn" is mentioned
    async def on_message(self, message):
        if 'tobi' in message.content.lower():
            # Check if the bot itself sent it so no double message
            # First id is Exp Lahn, second is Lahn
            if int(message.author.id) != 1175010259681681419:
                channel = message.channel
                greetings = ['Gago ka',
                'Putanginamo',
                'Fuck',
                ]
                greeting = choice(greetings)
                await channel.send(greeting)
        

# Load secrets
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Make bot instance
bot = TobiBot()
bot.run(TOKEN)