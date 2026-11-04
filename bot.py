import asyncio
import os

import discord
import requests


async def fetch_json(url, params=None):
    def request():
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    # Keep network requests off Discord's event loop.
    return await asyncio.to_thread(request)


def create_client(weather_api_key):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_message(message):
        if message.author.bot:
            return
        command, _, argument = message.content.partition(" ")
        try:
            if command == "/inspire":
                data = await fetch_json("https://zenquotes.io/api/random")
                await message.channel.send(f"{data[0]['q']} - {data[0]['a']}")
            elif command == "/weather":
                if not argument.strip():
                    await message.channel.send("Usage: /weather city")
                    return
                data = await fetch_json("https://api.weatherapi.com/v1/current.json", {
                    "key": weather_api_key, "q": argument.strip()
                })
                current = data["current"]
                await message.channel.send(
                    f"The current weather in {argument.strip()} is {current['condition']['text']}. "
                    f"The temperature is {current['temp_f']} degrees Fahrenheit."
                )
        except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
            await message.channel.send("Unable to fetch that information. Try again later.")

    return client


def main():
    token = os.environ.get("DISCORD_BOT_TOKEN")
    weather_key = os.environ.get("WEATHER_API_KEY")
    if not token or not weather_key:
        raise SystemExit("Set DISCORD_BOT_TOKEN and WEATHER_API_KEY before running.")
    create_client(weather_key).run(token)


if __name__ == "__main__":
    main()
