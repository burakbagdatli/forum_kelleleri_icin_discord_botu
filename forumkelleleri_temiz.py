"""
Anlatsam dedim ama gerek yok
"""
import json
import discord

with open("kellelistesi.json", mode="r") as kelle_listesi:
    KELLELER = json.load(kelle_listesi)

client = discord.Client()
@client.event
async def on_ready():
    print("Logging in as ", client.user.name, " ", client.user.id)
    print("------")
@client.event
async def on_message(mesaj):
    #if message.content.startswith("!deneme"):
    #    await client.send_message(message.channel, "Hooop! Burdayım!")
    if mesaj.content.startswith("!"):
        kelle_resmi_adresi = KELLELER.get(mesaj.content[1:], None)
        if kelle_resmi_adresi is not None:
            kelle_embed = discord.Embed()
            kelle_embed.set_image(url=kelle_resmi_adresi)
            await client.send_message(mesaj.channel, embed=kelle_embed)
    # if mesaj.content.startswith("~"):
    #     # Bu çalışmıyor, başkalarının mesajlarını düzenleme özelliği yokmuş discordda
    #     kelle_resmi_adresi = KELLELER.get(mesaj.content[1:], None)
    #     if kelle_resmi_adresi is not None:
    #         kelle_embed = discord.Embed()
    #         kelle_embed.set_image(url=kelle_resmi_adresi)
    #         await client.edit_message(mesaj, embed=kelle_embed)

client.run("gizli_hede")
