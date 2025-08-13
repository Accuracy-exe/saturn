import discord
import dotenv
import os

dotenv.load_dotenv()
tkn = str(os.getenv("BOT_TOKEN"))

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")

@bot.slash_command(name="hello", description="Greet the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

bot.run(tkn)