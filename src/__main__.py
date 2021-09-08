import twitchio
import os
from twitchio.ext import commands

bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=['ZoteTheMightyBot']
)

channelList = ['JWDragair', 'JaySkilling']

@bot.event()
async def event_ready():
  bot.load_module('cogs.precepts')
  print('Zote has entered the arena and is preparing for combat...')
  await bot.join_channels(channelList)

@bot.event()
async def event_message(ctx):
  # print(ctx.author)
  return

@bot.command(name='reloadCog')
async def reloadCog(ctx):
  bot.reload_module('cogs.precepts')

if __name__ == '__main__':
  bot.run()