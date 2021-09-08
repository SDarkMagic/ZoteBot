import asyncio
import twitchio

class checker:
  def __init__(self, client):
    self.game = None
    self.client = client
    self.streams = await getGame()
  
  async def getGame(self):
    game = await self.client.fetch_games(names=['Hollow Knight'])
    streams = await self.client.fetch_streams(game_ids=[game[0].id])
    return streams
    
  async def initCheckLoop(self):
    while True:
      self.streams = await self.getGame()
      asyncio.sleep(30)