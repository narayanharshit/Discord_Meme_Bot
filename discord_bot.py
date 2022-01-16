import json
from discord import Embed
from discord.ext.commands import Bot
from requests import get
from dotenv import dotenv_values

'''
    OAuth2 Url to add it to your guild/server
    https://discord.com/oauth2/authorize?client_id=931963591253430312&permissions=277025445888&scope=bot
'''

meme_bot = Bot(command_prefix = '$')

config = dotenv_values(".env")

@meme_bot.event
async def on_ready():
    print(f"{meme_bot.user} has connect to Discord!; and the bot is online - NOW!")

@meme_bot.command()
async def ping(ctx):
    await ctx.send("pong!") 

@meme_bot.command()
async def hi(ctx):
    await ctx.send("Hey There!, I am {}".format(meme_bot.user))

@meme_bot.command()
async def meme(ctx):
    raw_data = get("https://meme-api.herokuapp.com/gimme").text
    meme = Embed(title=f"{json.loads(raw_data)['title']}").set_image(url=f"{json.loads(raw_data)['url']}")
    await ctx.reply(embed=meme)

@meme_bot.command()
async def info(ctx):
    await ctx.send("This a bot that embeds a random hysterical meme from Reddit into your text channel as an embedded message, using an API call.")

@meme_bot.command()
async def who_made_you(ctx):
    await ctx.send("I was made by a guy named: {} with Discord username: {}".format(config['AUTHOR_NAME'], config['AUTHOR_DISCORD_USERNAME']))

meme_bot.run(config['DISCORD_BOT_TOKEN'])
