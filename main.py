import discord
from discord.ext import commands
import os

prefix="!"
client=commands.Bot(command_prefix=prefix)
token="NzYzODIwNDkzMTE5MTYwMzcw.X39RRA.bhtOw6jr9zrcRLAH-dy7QcLJ9Fs"

@client.event
async def on_ready():
    print("Bot hazır!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{prefix}yardım"))

    embed = discord.Embed(title="Bilgilendirme",
                          description=f"Botun çalışması için sunucuya *`Oyuncu`* adında bir rol eklemeniz gerekir. Eğer komutlara bakmak isterseniz *`{prefix}yardım`* yazabilirsiniz.")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/763820493119160370/5f457bf2280eef2856a3f74588aa313a.png?size=4096")
    embed.add_field(name="Emeği Geçenler", value="<@495539231469469706> <@736553124206084207>" , inline=False)
    embed.set_footer(text="Bu botu tercih ettiğiniz için teşekkürler!")
    channel = discord.utils.get(client.get_all_channels(), name='genel')
    await channel.send(embed=embed)

@client.command(aliases=['oyunakatıl'])
async def oyunakatil(ctx):
    role = 'Oyuncu'  # role to add
    check_role = get(ctx.message.guild.roles, name='Oyuncu')
    user = ctx.message.author
    userAvatar = user.avatar_url


    if check_role in user.roles:
        em = discord.Embed(title=f'Zaten oyuna katıldın!',author=user ,colour=0xA100FF)
        em.set_author(name=user,
                      icon_url=userAvatar, )
        await ctx.send(embed=em)
    else:
        em=discord.Embed(title=f'`{role}` rolünü alarak "Behind The Past" oyununa katıldın!',author=user ,colour=0xA100FF)
        em.set_author(name=user,
                         icon_url=userAvatar,)
        await ctx.send(embed=em)
        await user.add_roles(discord.utils.get(user.guild.roles, name=role))

@client.command(aliases=['oyunabaşla'])
async def oyunabasla(ctx):
    user = ctx.message.author  # user
    check_role = get(ctx.message.guild.roles, name='Oyuncu')
    if check_role in user.roles:
        await ctx.send("şöyle olmuş böyle olmuş 1.onu yap 2.şunu yap 3. onu yapma"
                       "\n1.yi seçmek için seç1\n2.yi seçmek için seç2\n3.yi seçmek için seç3")
    else:
        await ctx.send("Önce oyuna katılmalısın.\nOyuna katılmak için `.oyunagir` yaz.")

@client.command(aliases=['yardım'])
async def yardim(ctx):
    user = ctx.message.author
    userAvatar = user.avatar_url

    embed = discord.Embed(title="Bilgilendirme")
    embed.set_author(name=user, icon_url = userAvatar)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/763820493119160370/5f457bf2280eef2856a3f74588aa313a.png?size=4096")
    embed.add_field(name=f"*```Prefiximiz```*", value=f"`{prefix}`", inline=False)
    embed.add_field(name=f"*```{prefix}oyunabaşla```*", value="Oyuna başlamanız için yazmanız gereken komuttur.", inline=False)
    embed.add_field(name=f"*```{prefix}oyunakatıl```*", value="Oyuna oynayabilmeniz için gereken perm'i verir.", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)} ms')

client.run(os.environ['token'])