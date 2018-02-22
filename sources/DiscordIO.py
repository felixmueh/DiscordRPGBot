import discord
import asyncio
import DiscordRPGBot.Settings as Settings


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
    if(message.content.startswith(Settings.command_prefix)):
        print(message.content)
