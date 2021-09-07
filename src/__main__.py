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

@bot.event()
async def event_ready(ctx):
  print('Zote has entered the arena and is preparing for combat...')
  await __ws.send_privmsg('ZoteTheMightyBot', 'Booptis')

if __name__ == '__main__':
  bot.run()