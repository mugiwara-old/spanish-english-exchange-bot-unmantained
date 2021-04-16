#TODO, status: cog in progress...
import discord 

from discord.ext import commands
from data.api_calls import API_CALLS

class Words(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def word(self, ctx):
    #TODO
    word = API_CALLS.get_dictionaryapi_word()
    
    msg = word.get('english')

    await ctx.send(msg)


def setup(bot):
  bot.add_cog(Words(bot))