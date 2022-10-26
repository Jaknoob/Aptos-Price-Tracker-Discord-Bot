import discord 
import os
from pycoingecko import CoinGeckoAPI
from keep_alive import keep_alive

cg = CoinGeckoAPI()
price = cg.get_price(ids='aptos', vs_currencies='usd')
price_usd = price['aptos']
final_price = (price_usd['usd'])

token = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
my_secret = os.environ['TOKEN']
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("$price"):
    await message.channel.send(final_price)

keep_alive()

client.run(token)