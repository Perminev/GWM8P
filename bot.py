import disnake
from disnake.ext import commands
from Cybernator import Paginator as pg
import random

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=disnake.Intents.default(), help_command=None, test_guilds=[1161681641870213295])

@bot.event
async def on_ready():
    print(f"You have just entered as {bot.user}")
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Streaming(name=f'GWP', url='https://github.com/Perminev/GWM8P')) # Статус бота (Для примера выбрал стриминг)
 
@bot.command()
async def ping(ctx):
    await ctx.send("ping")
    
@bot.command(aliases = ['causes_un'])
async def __list(ctx):
    embed1 = disnake.Embed(title = 'Производство электроэнергии',
                           description = 'Значительная доля глобальных выбросов связана с производством электроэнергии и тепла путем сжигания ископаемых видов топлива. Бóльшая часть электроэнергии по-прежнему производится посредством сжигания угля, нефти или газа, в результате чего образуются углекислый газ и закись азота – мощные парниковые газы, которые покрывают Землю и задерживают солнечное тепло. Во всем мире чуть более четверти электроэнергии вырабатывается за счет ветра и солнца и поступает из других возобновляемых источников, которые, в отличие от ископаемых видов топлива, практически не выделяют в атмосферу парниковых газов или загрязняющих веществ.',
                           color=disnake.Color.red())
    embed1.set_author(icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/2405px-UN_emblem_blue.svg.png', name = "ООН"),
    embed1.set_thumbnail(url="https://www.un.org/sites/un2.un.org/files/causes01_1.png"),
    embed2 = disnake.Embed(title = 'Изготовление товаров',
                           description = 'Предприятия обрабатывающей и других отраслей промышленности производят выбросы, в большинстве случаев являющиеся результатом сжигания ископаемых видов топлива в целях выработки энергии, необходимой для получения цемента, железа, стали, электронных устройств, пластмасс, одежды и других товаров. При добыче полезных ископаемых и других промышленных процессах, равно как и при строительстве, также выделяются газы. Машины, используемые в производственном процессе, зачастую работают на угле, нефти или газе, а некоторые материалы, такие как пластмассы, производятся из химических веществ, получаемых из ископаемых видов топлива. Обрабатывающая промышленность является одним из крупнейших источников выбросов парниковых газов в мире.',
                           color=disnake.Color.red())
    embed2.set_author(icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/2405px-UN_emblem_blue.svg.png', name = "ООН"),
    embed2.set_thumbnail(url="https://www.un.org/sites/un2.un.org/files/causes01_1.png"),
    embed3 = disnake.Embed(title = 'Вырубка лесов',
                           description = 'В результате вырубки лесов для создания ферм или пастбищ либо по иным причинам образуются выбросы, поскольку вырубаемые деревья высвобождают накопленный углерод. Ежегодно уничтожается около 12 млн гектаров леса. Поскольку леса поглощают углекислый газ, их уничтожение также ограничивает способность природы удерживать выбросы в атмосферу. Обезлесение наряду с сельским хозяйством и другими изменениями в землепользовании является причиной примерно четверти глобальных выбросов парниковых газов.',
                           color=disnake.Color.red())
    embed3.set_author(icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/2405px-UN_emblem_blue.svg.png', name = "ООН"),
    embed3.set_thumbnail(url="https://www.un.org/sites/un2.un.org/files/causes01_1.png"),
    embed4 = disnake.Embed(title = 'Использование транспорта',
                           description = 'Большинство автомобилей, грузовиков, кораблей и самолетов работают на ископаемых видах топлива. Это делает транспорт одним из главных источников выбросов парниковых газов, особенно выбросов углекислого газа. Наибольшая их часть приходится на дорожные транспортные средства в связи со сжиганием продуктов нефтепереработки, таких как бензин, в двигателях внутреннего сгорания. При этом выбросы морских и воздушных судов продолжают расти. На транспорт приходится почти четверть глобальных выбросов углекислого газа, связанных с энергоснабжением. Существующие тенденции указывают на вероятность значительного увеличения энергопотребления в транспортном секторе в ближайшие годы.',
                           color=disnake.Color.red())
    embed4.set_author(icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/2405px-UN_emblem_blue.svg.png', name = "ООН"),
    embed4.set_thumbnail(url="https://www.un.org/sites/un2.un.org/files/causes01_1.png")
    embed5 = disnake.Embed(title = 'Производство продуктов питания',
                           description = 'Производство продуктов питания приводит к выбросам углекислого газа, метана и других парниковых газов разными путями, включая вырубку лесов и расчистку земель для ведения сельского хозяйства и выпаса скота, работу пищеварительных систем коров и овец, производство и применение удобрений и навоза для выращивания сельскохозяйственных культур и использование энергии для эксплуатации сельскохозяйственного оборудования или рыболовецких судов, обычно работающих на ископаемых видах топлива. Все это делает производство продуктов питания одним из основных факторов, способствующих изменению климата. Выбросы парниковых газов также связаны с упаковкой и распространением продуктов питания.',
                           color=disnake.Color.red())
    embed5.set_author(icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/2405px-UN_emblem_blue.svg.png', name = "ООН"),
    embed5.set_thumbnail(url='https://www.un.org/sites/un2.un.org/files/causes01_1.png')
    embed6 = disnake.Embed(title = 'Энергоснабжение зданий',
                           description = 'В мировом масштабе жилые и коммерческие здания потребляют более половины всей электроэнергии. В связи с продолжающимся использованием угля, нефти и природного газа для целей отопления и охлаждения они выбрасывают значительные количества парниковых газов. В последние годы повышение спроса на энергию для отопления и охлаждения с ростом численности владельцев кондиционеров и увеличение потребления электричества для освещения и обеспечения работы бытовой техники и подключенных устройств способствовали увеличению выбросов углекислого газа, производимых зданиями и связанных с энергоснабжением.',
                           color=disnake.Color.red())
    embed6.set_author(icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/2405px-UN_emblem_blue.svg.png', name = "ООН"),
    embed6.set_thumbnail(url='https://www.un.org/sites/un2.un.org/files/causes01_1.png')
    embed7 = disnake.Embed(title = 'Слишком интенсивное потребление',
                           description = 'Ваш дом и использование электроэнергии, то, как вы передвигаетесь, то, что вы едите, и количество того, что вы выбрасываете, влияют на выбросы парниковых газов. Это же можно сказать о потреблении таких товаров, как одежда, электронные устройства и пластмассы. Значительная часть глобальных выбросов парниковых газов связана с частными домохозяйствами. Наш образ жизни оказывает глубокое воздействие на нашу планету. Самые состоятельные лица несут наибольшую ответственность: на 1 процент самых богатых жителей планеты в совокупности приходится больше выбросов парниковых газов, чем на 50 процентов беднейшего населения.',
                           color=disnake.Color.red())
    embed7.set_author(icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/UN_emblem_blue.svg/2405px-UN_emblem_blue.svg.png', name = "ООН"),
    embed7.set_thumbnail(url='https://www.un.org/sites/un2.un.org/files/causes01_1.png')
    embeds = [embed1 , embed2 , embed3, embed4, embed5, embed6, embed7]
    
    message = await ctx.send(embed = embed1)
    page = pg(bot, message, only=ctx.author, use_more=False, embeds=embeds)
    await page.start()
    
@bot.command(aliases = ['memes'])
async def __memeslist(ctx):
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
        embed.set_image(url='https://github.com/Perminev/GWM8P/blob/main/mem.png?raw=true')
        await ctx.send(embed=embed)
    elif random_number == 3:
        embed = disnake.Embed(title = '',
                            description = '', 
                            color=disnake.Color.light_gray())
        embed.set_image(url='https://github.com/Perminev/GWM8P/blob/main/mem.png?raw=true')
        await ctx.send(embed=embed)
    elif random_number == 4:
        embed = disnake.Embed(title = '',
                            description = '', 
                            color=disnake.Color.light_gray())
        embed.set_image(url='https://github.com/Perminev/GWM8P/blob/main/mem.png?raw=true')
        await ctx.send(embed=embed)
    elif random_number == 5:
        embed = disnake.Embed(title = '',
                            description = '', 
                            color=disnake.Color.light_gray())
        embed.set_image(url='https://github.com/Perminev/GWM8P/blob/main/mem.png?raw=true')
        await ctx.send(embed=embed)


bot.run("MTE2MTY4Njk0OTk4NDIyNzQyOQ.GSPCDu.4cnNzAkd-jUVeldSghBxUBnny7ufZBJDTRMha4")
