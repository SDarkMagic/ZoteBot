import twitchio
import os
import json
import threading
import Util as util
from twitchio.ext import commands

def readConfig:
  with open('config.json', 'rt') as readConfig:
    config = json.loads(readConfig.read())
  return config

def initChecker(bot):
  streamChecker = util.checker(bot.client)

bot = commands.Bot(
    token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=['ZoteTheMightyBot']
)

channelList = config['channelList']

@bot.event()
async def event_ready():
  global config
  config = readConfig()
  bot.load_module('cogs.precepts')
  print('Zote has entered the arena and is preparing for combat...')
  await bot.join_channels(channelList)

@bot.event()
async def event_message(ctx):
  await bot.process_commands()
  return

@bot.command(name='reloadCog')
async def reloadCog(ctx):
  bot.reload_module('cogs.precepts')
  
@bot.command(name='neglect')
async def neglect(ctx):
  return

if __name__ == '__main__':
  bot.run()