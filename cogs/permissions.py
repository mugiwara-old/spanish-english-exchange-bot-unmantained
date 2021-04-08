from discord.ext import commmands

class Perms(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    async def permissions(self, ctx, arg):
        role = ctx.guild.get_role(arg)
        
        if role == None:
            await ctx.channel.send("That's not a valid role ID!")
            return
            
        thing = ""
        for i in role.permissions:
            thing += i
            
        await ctx.channel.send(thing)
