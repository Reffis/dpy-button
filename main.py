import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

client = commands.Bot(command_prefix="!")
DiscordComponents(client)


@client.command(aliases=["샌즈"])
async def sans(ctx):
    await ctx.send("샌즈!", components=[
        [Button(label="와", style=ButtonStyle.blue, id="WA"),
         Button(label="샌즈", style=ButtonStyle.red, id="SANS"),
         Button(label="아시는구나!", style=ButtonStyle.green, id="AAA"),
         Button(label="ㄷㅅㄷ", style=ButtonStyle.URL,
                url="https://ko.wikipedia.org/wiki/%EC%83%8C%EC%A6%88_(%EC%96%B8%EB%8D%94%ED%85%8C%EC%9D%BC)")]
    ])


@client.event
async def on_button_click(res):
    try:
        await res.respond(
            type=InteractionType.DeferredUpdateMessage, content=f"{res.component.label} (개인만 볼수있음)"
        )

        if res.component.id == "WA":
            await res.channel.send(f"와!")
        elif res.component.id == "SANS":
            await res.channel.send(f"샌즈!")
        elif res.component.id == "AAA":
            await res.channel.send(f"아시는구나!")

        else:
            pass
    except discord.errors.NotFound:
        pass



client.run("Token")
