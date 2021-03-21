import os
import discord
import random
import re

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WHITELIST = ["brightenbot"]

client = discord.Client()


class BrightException(Exception):
    pass


class Brightbot:
    def __init__(self, text_channels):
        self.text_channels = text_channels


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord successfully.')


@client.event
async def on_message(message):
    text_channels = discord.utils.get(client.get_all_channels(), guild__name=GUILD, name='experiments')
    # Every time a message is created, a number of handlers will receive the
    # message, processing the message like an assembly line.
    handlers = [
        check_dice_roll
    ]

    # Call each handler function with the message
    for func in handlers:
        result = func(message)
        if result:
            await text_channels.send(content=result)


# ===========================
# OnMessage handlers go below
# ===========================
def check_dice_roll(message):
    try:
        # Sanitize input
        sanitized_message = message.content.lower().replace(' ', '')

        # Does this match the pattern we expect for dice rolling?
        is_roll_message = re.search(r'(\d+)d(\d+)', sanitized_message)
        if is_roll_message:
            # Extract the relevant portions from the string, cast to int
            count = int(is_roll_message.group(1))
            die = int(is_roll_message.group(2))

            # Roll the specified dice however many times, and return the sum
            return sum([random.randint(1, die) for roll in range(count)])

    except BrightException as e:
        return f'Oops! I ran into a bug while trying to roll dice:\n\n{e}.'


client.run(TOKEN)
