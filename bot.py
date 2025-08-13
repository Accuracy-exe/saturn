import discord
import dotenv
import os
import ItemCreation
import database as db
dotenv.load_dotenv()







tkn = str(os.getenv("BOT_TOKEN"))

bot = discord.Bot(debug_guilds=[1366030763979444234])

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")
    
@bot.event
async def on_guild_join(guild):
    guild_id = guild.id
    db.initCollection(guild_id)
    print(f"Created collection for guild: {guild_id}")

@bot.command(name="latency", description="Check Latency")
async def latency(ctx: discord.ApplicationContext):
    await ctx.respond(f"Latency : {round(bot.latency,2)} ms")

@bot.command(name="hello", description="Greet the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.slash_command(name="add", description="Create a new Work Item")
async def add(
    ctx: discord.ApplicationContext,
    item: discord.Option(str, choices=['Epic','User Story','Bug','Task'])
    ):
    if item not in ['Epic','User Story','Bug','Task']:
        await ctx.respond("Invalid option chosen :/")
        return
    title = f"Create a new Work Item: {item}"
    if item == "Epic":
        form = ItemCreation.EpicCreator(title=title,gid=ctx.guild.id)
    if item == "User Story":
        form = ItemCreation.StoryCreator(title=title,gid=ctx.guild.id)
    if item == "Bug":
        form = ItemCreation.BugCreator(title=title,gid=ctx.guild.id)
    if item == "Task":
        form = ItemCreation.TaskCreator(title=title,gid=ctx.guild.id)
    await ctx.send_modal(form)
bot.run(tkn)