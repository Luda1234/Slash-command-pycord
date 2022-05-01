import discord

bot = discord.Bot()
token = "bot_token" 

@bot.slash_command(description="Pong !") 
async def ping(ctx): # 슬래시 커맨드 이름
    await ctx.respond("pong") 

bot.run(token) 