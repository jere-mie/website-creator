import discord
from discord.ext import commands
import json
from makeSite import makeSite
with open('secrets.json') as f:
  data = json.load(f)


commands_list={
    "help": "`~help <command>`\nDisplays details about a specific command, or all commands if <command> field is empty",
    "website": "`~website`\nDisplays the link to the website creator website",
    "make": '`~make <img> <name> <school> <year> <description> <github> <linkedin> <resume>`\nCreates a website given the above fields are all filled in.\n**Note, you must use quotation marks around each argument**\nFor <img>, <github>, <linkedin>, and <resume>, please use a url to each of those resources\n For example:\n*~make "https://i.imgur.com/Y0nThjd.png" "Jeremie" "University of Windsor" "2023" "Computer Science student at UWindsor" "http://github.com/jere-mie" "http://linkedin.com/in/jeremie-bornais" "http://jeremie.bornais.ca/cv.pdf"*'
}



client = commands.Bot(command_prefix='~')
client.remove_command("help")
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)


@client.command()
async def foo(ctx, arg1, arg2):
    await ctx.send(arg1)

@client.command()
async def website(ctx):
    await ctx.send('http://websiteondemand.herokuapp.com')

@client.command()
async def make(ctx, img, name, school, year, desc, github, linkedin, resume):
    info = {
        "name":name,
        "img":img,
        "desc":desc,
        "school":school,
        "year":year,
        "github":github,
        "resume":resume,
        "linkedin":linkedin
    }
    makeSite(info)
    await ctx.send(file=discord.File('out.zip'))

# Thank you to Wahid Bawa for allowing me to use his code for this help menu
# View his code here: https://github.com/UWindsor-Robotics-Tech/UWin-Robotics-Robot/blob/master/robot/main.py
@client.command()
async def help(ctx, *, command=None):
    embed = discord.Embed(title="HELP", colour=0xcccc00)
    if command is None:
        for i in commands_list:
            embed.add_field(name=i, value=commands_list[i], inline=False)
    elif command in commands_list:
        embed.add_field(name=command, value=commands_list[command], inline=False)
    else:
        await ctx.send("This is not an existing command")
        return
    await ctx.send(embed=embed)

client.run(data['token'])