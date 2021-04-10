import discord 

from discord.ext import commands
from data.api_calls import API_CALLS

class Writing(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def text(self, ctx):
    if !ctx.channel.id == 813881490941280328:
        await ctx.channel.send("Sorry, you can't use this command in this channel!")
        return
    
    english_text = API_CALLS.get_newsapi_news("english")
    embed = discord.Embed(color = discord.Colour.blue())
    embed.title = english_text["title"]
    embed.description = english_text["description"]
    embed.set_footer(text="Share your thoughts!")

    await ctx.send(embed = embed)
    

  @commands.command()
  async def image(self, ctx):
    if !ctx.channel.id == 813881490941280328:
        await ctx.channel.send("Sorry, you can't use this command in this channel!")
        return
    
    image_url = API_CALLS.get_unsplash_image_url()
    embed = discord.Embed(color = discord.Colour.blue())
    embed.title = "Get inspired by this image, let your writing skills flow!"
    embed.set_image(url = image_url)

    await ctx.send(embed = embed)
    

  @commands.command()
  async def texto(self, ctx):
    if !ctx.channel.id == 813881028493049877:
        await ctx.channel.send("Sorry, you can't use this command in this channel!")
        return
    
    spanish_text = API_CALLS.get_newsapi_news("spanish")
    embed = discord.Embed(color = discord.Colour.orange())
    embed.title = spanish_text["title"]
    embed.description = spanish_text["description"]
    embed.set_footer(text="¿Qué opinas al respecto?")

    await ctx.send(embed = embed)
    

  @commands.command()
  async def imagen(self, ctx):
    if !ctx.channel.id == 813881028493049877:
        await ctx.channel.send("Sorry, you can't use this command in this channel!")
        return
    
    image_url = API_CALLS.get_unsplash_image_url()
    embed = discord.Embed(color = discord.Colour.orange())
    embed.title = "¡Inspírate con esta imagen y deja que las palabras fluyan!"
    embed.set_image(url = image_url)
    
    await ctx.send(embed = embed)
    

def setup(bot):
  bot.add_cog(Writing(bot))
