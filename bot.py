import discord
import dotenv
import os

dotenv.load_dotenv()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = str(os.getenv("MONGO_URI"))

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged cluster. Successfully connected to MongoDB!")
except Exception as e:
    print(e)


def initCollection(guild_id):
    db = client["Saturn"]
    collection_name = str(guild_id)
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    return db[collection_name]





tkn = str(os.getenv("BOT_TOKEN"))

bot = discord.Bot(debug_guilds=[1366030763979444234])

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")
    
@bot.event
async def on_guild_join(guild):
    guild_id = guild.id
    initCollection(guild_id)
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
    item: discord.Option(str, choices=['epic','user story','bug','task'])
    ):
    pass
bot.run(tkn)