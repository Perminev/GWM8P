# Импортируем необходимые модули из библиотеки Disnake.
import disnake
from disnake.ext import commands
from Cybernator import Paginator as pg
import random


# Определяем класс "Credits", который является расширением (Cog) для бота.
class Credits(commands.Cog):
    # Инициализируем класс "Credits" и сохраняем объект бота в атрибуте "self.bot".
    def __init__(self, bot):
        self.bot = bot

    # Определяем метод "credits", который будет вызываться при выполнении команды "!credits".
    @commands.command(description = 'Причины')
    async def credits(self, ctx):
            embed1 = disnake.Embed(title = 'Автор:',
                           description = 'Глеб Перминев',
                           color=disnake.Color.red())
            embed1.set_author(icon_url='https://avatars.githubusercontent.com/u/131896208?v=4', name = "Gleb Perminev"),
            embed1.set_thumbnail(url="https://avatars.githubusercontent.com/u/131896208?v=4"),
            embed2 = disnake.Embed(title = 'Под руководством:',
                            description = 'Школы программирования Kodland',
                            color=disnake.Color(0x6592e2))
            embed2.set_author(icon_url='https://www.kodland.org/images/Frame-48097135_1.png', name = "Kodland"),
            embed2.set_thumbnail(url="https://www.kodland.org/images/num-ico.png"),
            embed3 = disnake.Embed(title = 'Благодарности:',
                            description = 'Спасибо большое школе Kodland за обучение меня языку программирования Python! Благодарю преподователя Амура Альмухаметова за интересное и доходчивое объяснение материала! Это было приятное время!',
                            color=disnake.Color(0x6592e2))
            embed3.set_author(icon_url='https://avatars.githubusercontent.com/u/131896208?v=4', name = "Gleb Perminev"),
            embed3.set_thumbnail(url="https://www.kodland.org/images/Frame-48096992.png"),
            embeds = [embed1 , embed2, embed3]
            
            message = await ctx.send(embed = embed1)
            page = pg(self.bot, message, only=ctx.author, use_more=False, embeds=embeds)
            await page.start()


# Определяем функцию "setup", которая добавляет расширение "Credits" в бота.
def setup(bot):
    bot.add_cog(Credits(bot))