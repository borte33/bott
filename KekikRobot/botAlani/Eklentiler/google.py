# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, Filters
from time import time
from google_search_client.search_client import GoogleSearchClient
import ast

@Client.on_message(Filters.command(['google'], ['!','.','/']))
async def google(client, message):
    # < Başlangıç
    await message.reply_chat_action("typing")
    await asyncio.sleep(0.3)
    uyku = await message.reply("__asyncio.sleep(0.3)__")

    cevaplanan_mesaj    = message.reply_to_message
    if cevaplanan_mesaj is None:
        yanitlanacak_mesaj  = message.message_id
    else:
        yanitlanacak_mesaj = cevaplanan_mesaj.message_id
    
    await uyku.delete()
    ilk_mesaj = await message.reply("__Bekleyin..__",
        reply_to_message_id         = yanitlanacak_mesaj,
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >

    girilen_yazi = message.text
    if len(girilen_yazi.split()) == 1:
        await ilk_mesaj.edit("Arama yapabilmek için kelime girmelisiniz..")
        return
    await ilk_mesaj.edit("Aranıyor...")
    
    basla = time()
    girdi = " ".join(girilen_yazi.split()[1:])
    mesaj = f"Aranan Kelime : `{girdi}`\n\n"
    
    istek = GoogleSearchClient()
    sonuclar = istek.search(girdi).to_json()
    
    if sonuclar:
        i = 1
        for sonuc in ast.literal_eval(sonuclar):
            mesaj += f"🔍 [{sonuc['title']}]({sonuc['url']})\n"
            i += 1
            if i == 5:
                break
        
        bitir = time()
        sure = bitir - basla
        mesaj += f"\nTepki Süresi : `{str(sure)[:4]} sn`"
        
        try:
            await ilk_mesaj.edit(mesaj)
        except Exception as hata:
            await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")
    except Exception as hata:
        await ilk_mesaj.edit(f"**Uuppss:**\n\n`{hata}`")