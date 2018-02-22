import discord
import asyncio
import Settings as Settings

client = discord.Client()


def pass_event_list(e):
    global events
    events = e


def launch_bot():
    client.run("REMOVED_DISCORD_TOKEN")


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    if message.content.startswith(Settings.command_prefix + Settings.valid_command):
        pass_event_list(message.content[len(command_prefix):])
