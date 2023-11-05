import discord
import requests
import json
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
api_key = 'api_key'
token = 'bot token'


#get weather data function
async def get_weather(location):
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
    response = requests.get(url)

    if response.status_code == 200:
        weather = response.json()
        return weather['current']['condition']['text'], weather['current']['temp_f']
    else:
        return 'Error getting weather data.'


# generate inspiring quote function
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)


#Message commands for bot
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('/weather'):
            location = message.content.split('/weather')[1]
            weather, temperature = await get_weather(location)
            await message.channel.send(f'The current weather in {location} is {weather}. The temperature is {temperature} degrees Farenheit.')
