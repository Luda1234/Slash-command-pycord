import discord

bot = discord.Bot()
token = "bot_token" 

@bot.slash_command(description="Pong !") 
async def ping(ctx): 
    await ctx.respond("pong") 

bot.run(token) 
