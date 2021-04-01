import discord
import os
import requests
import json
from server.keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix="!")

def get_unsplash_image_url():
  unsplash_params = {'count': 1, 'client_id': os.getenv('UNSPLASH_TOKEN')}
  response = requests.get('https://api.unsplash.com/photos/random', params=unsplash_params)
  json_data = json.loads(response.text)
  image_url = json_data[0]["urls"]['full']
  return(image_url)

def get_english_news():
  newsapi_params = {'country':'us', 'pageSize': 1, 'category':'entertainment','apiKey':os.getenv('NEWSAPI_TOKEN')}
  res = requests.get('https://newsapi.org/v2/top-headlines',params=newsapi_params)
  json_data = json.loads(res.text)
  english_text = json_data["articles"][0]
  return(english_text)

def get_spanish_news():
  newsapi_params = {'language':'es', 'pageSize': 1, 'category':'technology','apiKey':os.getenv('NEWSAPI_TOKEN')}
  res = requests.get('https://newsapi.org/v2/top-headlines',params=newsapi_params)
  json_data = json.loads(res.text)
  spanish_text = json_data["articles"][0]
  return(spanish_text)

@client.event
async def on_ready():
  print('My life for Aiur! {0.user} Your command?'.format(client))

@client.listen
async def on_message(message):
  if message.author == client.user:
    return

@client.command()
async def text(ctx):
  if ctx.message.channel.id == 813881490941280328:
    embed = discord.Embed(color = discord.Colour.blue())
    english_text = get_english_news()
    embed.title = english_text["title"]
    embed.description = english_text["description"]
    embed.set_footer(text="Share your thoughts!")
    await ctx.send(embed = embed)

@client.command()
async def image(ctx):
  embed = discord.Embed(color = discord.Colour.blue())
  image_url = get_unsplash_image_url()
  embed.title = "Get inspired by this image, let your writing skills flow!"
  embed.set_image(url = image_url)
  await ctx.send(embed = embed)

@client.command()
async def texto(ctx):
  if ctx.message.channel.id == 813881028493049877:
    embed = discord.Embed(color = discord.Colour.orange())
    spanish_text = get_spanish_news()
    embed.title = spanish_text["title"]
    embed.description = spanish_text["description"]
    embed.set_footer(text="¿Qué opinas al respecto?")
    await ctx.send(embed = embed)

@client.command()
async def imagen(ctx):
  embed = discord.Embed(color = discord.Colour.orange())
  image_url = get_unsplash_image_url()
  embed.title = "¡Inspírate con esta imagen y deja que las palabras fluyan!"
  embed.set_image(url = image_url)
  await ctx.send(embed = embed)

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))