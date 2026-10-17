# Discord Bot

Python bot experiment with weather and quote commands.

## Setup

Use Python 3.9 or newer. Create and activate a virtual environment, then:

```sh
python -m pip install -r requirements.txt
python bot.py
```

Set `DISCORD_BOT_TOKEN` and `WEATHER_API_KEY` in your shell first. `.env.example` lists the names; the app does not load `.env` automatically. Enable the Message Content intent for the bot in Discord's developer settings and grant access to a test server.

## Commands

- `/weather city`: current condition and temperature in Fahrenheit from WeatherAPI.
- `/inspire`: quote from ZenQuotes.

These are message-prefix commands, not registered Discord application commands.

## Review changes

Adds the missing client startup, reads configuration from the environment, validates the weather argument and handles request failures. HTTP requests use a timeout and run outside the Discord event loop. Live Discord messages and API requests were not used for validation.
## Related projects

See the [project index](https://github.com/Jaeger790#projects) for the rest of my work.
