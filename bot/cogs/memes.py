# Импортируем необходимые модули из библиотеки Disnake.
import disnake
from disnake.ext import commands
import random


# Определяем класс "Memes", который является расширением (Cog) для бота.
class Memes(commands.Cog):
    # Инициализируем класс "Ping" и сохраняем объект бота в атрибуте "self.bot".
    def __init__(self, bot):
        self.bot = bot

    # Определяем метод "memes", который будет вызываться при выполнении команды "/memes".
    @commands.slash_command(description = 'Мемы')
    async def memes(self, ctx):
            random_number = random.randint(1, 5)
            if random_number == 1:
                embed = disnake.Embed(title = '',
                                    description = '', 
                                    color=disnake.Color.light_gray())
                embed.set_image(url='https://github.com/Perminev/GWM8P/blob/main/mem.png?raw=true')
                await ctx.send(embed=embed)
            elif random_number == 2:
                embed = disnake.Embed(title = '',
                                    description = '', 
                                    color=disnake.Color.light_gray())
                embed.set_image(url='https://sun9-17.userapi.com/impg/c854124/v854124078/252dc3/ESlzcXNZFOo.jpg?size=409x604&quality=96&sign=63fa87d69f639dfdc891564a05a4f8b3&type=album')
                await ctx.send(embed=embed)
            elif random_number == 3:
                embed = disnake.Embed(title = '',
                                    description = '', 
                                    color=disnake.Color.orange())
                embed.set_image(url='https://github.com/Perminev/GWM8P/blob/main/0215da3a016b62f76ff46bf4f92ae42a.jpg?raw=true')
                await ctx.send(embed=embed)
            elif random_number == 4:
                embed = disnake.Embed(title = '',
                                    description = '', 
                                    color=disnake.Color.orange())
                embed.set_image(url='https://github.com/Perminev/GWM8P/blob/main/a7904c28f573af4150ad440c8de0bd4c.jpg?raw=true')
                await ctx.send(embed=embed)
            elif random_number == 5:
                embed = disnake.Embed(title = '',
                                    description = '', 
                                    color=disnake.Color.dark_orange())
                embed.set_image(url='https://github.com/Perminev/GWM8P/blob/main/3fe79e75c37fed05072e11ff3bff4cc0.jpg?raw=true')
                await ctx.send(embed=embed)


# Определяем функцию "setup", которая добавляет расширение "Memes" в бота.
def setup(bot):
    bot.add_cog(Memes(bot))