#  Данный код является расширенной версией предыдущего кода.

#  Импортируются необходимые модули
import os

import disnake
from disnake.ext import commands
from Cybernator import Paginator as pg
import random

intents = disnake.Intents.all()  # Подключаем все разрешения

token = ""
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None, test_guilds=["YOUR GUILD ID"])

#  Создается объект intents, который включает все разрешения для бота.
#  Создается экземпляр класса Bot с префиксом команд "!" и указанными разрешениями.


# Определяется функция on_ready, которая будет вызываться, когда бот будет готов к использованию.
@bot.event
async def on_ready():
    print(f"You have just entered as {bot.user}")
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Streaming(name=f'GWP', url='https://github.com/Perminev/GWP')) # Статус бота (Для примера выбрал стриминг)

# При готовности бота, загружает расширения из папки "cogs"
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

# Запускается бот с помощью метода run, передавая ему токен для авторизации.
bot.run(token)
