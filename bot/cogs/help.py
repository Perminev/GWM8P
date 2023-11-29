# Импортируем необходимые модули из библиотеки Disnake.
import disnake
from disnake.ext import commands
from Cybernator import Paginator as pg
import random


# Определяем класс "Help", который является расширением (Cog) для бота.
class Help(commands.Cog):
    # Инициализируем класс "Help" и сохраняем объект бота в атрибуте "self.bot".
    def __init__(self, bot):
        self.bot = bot

    # Определяем метод "help", который будет вызываться при выполнении команды "/help".
    @commands.slash_command(description="help", brief="help", usage="help")
    async def help(self, ctx):
        embed=disnake.Embed(title="Help/Помощь", description="Комманды:")
        embed.set_author(name="Perminev", url="https://github.com/Perminev", icon_url="https://avatars.githubusercontent.com/u/131896208?v=4")
        embed.add_field(name="/memes", value="Показывает случайные мемы про глобальное потепление.", inline=False)
        embed.add_field(name="!causes_un", value="Рассказывает о причинах глобального потепления в виде красивого списка.", inline=True)
        embed.add_field(name="/help", value="Показывает эту команду.", inline=True)
        embed.set_footer(text="Источники: un.org")
        await ctx.send(embed=embed)



# Определяем функцию "setup", которая добавляет расширение "Help" в бота.
def setup(bot):
    bot.add_cog(Help(bot))
