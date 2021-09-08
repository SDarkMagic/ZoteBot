from twitchio.ext import commands
import json
import random

class dialogue(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.preceptPath = 'src/cogs/precepts.json'
        with open(self.preceptPath, 'rt') as preceptFile:
            self.precepts = json.loads(preceptFile.read())
        self.preceptCount = len(self.precepts)

    @commands.command(name='precept')
    async def precept(self, ctx):
        msg = ctx.message.content
        if len(msg.split(' ')) == 1:
            preceptNum = random.randint(1, self.preceptCount)
        else:
            try:
                preceptNum = int(str(msg).split(' ')[1])
            except:
                preceptNum = 58
                invalidPrecept = str(msg.split(' ')[1])

        if preceptNum <= self.preceptCount and preceptNum >=1:
            await ctx.send(self.precepts[str(preceptNum)])
        else:
            await ctx.send("That isn't a precept of the Mighty Zote!")
        return

    @commands.command(name='reloadPrecepts')
    async def reloadPrecepts(self, ctx):
        with open(self.preceptPath, 'rt') as readPrecepts:
            self.precepts = json.loads(readPrecepts.read())
        await ctx.send('Ah, the memories of my precepts have grown stronger...')
        return

def prepare(bot: commands.Bot):
    bot.add_cog(dialogue(bot))