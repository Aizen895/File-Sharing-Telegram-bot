from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> ⟦⟧ Hi There Vro!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=http://t.me/AdultPremium_Pro_Bot>Ʉ₦₭Ø₩₦</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Adult_Madness>ᴄᴜʟᴛᴜʀᴇᴅ</a>\n◈ ʜᴇɴᴛᴀɪ : <a href=https://t.me/+0VRiOl0R0n02NzY1>ʜᴇɴᴛᴀɪ</a>\n◈ɪɴᴅɪᴀɴ ʟᴇᴀᴋs: <a href=https://t.me/+7QnVvptszo5hYzll>ɪɴᴅɪᴀɴ ʟᴇᴀᴋs</a>\n◈  :\n┗━━━━━━━❪❂❫━━━━━━━━</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"👋 ᴋᴏɴɪᴄʜɪᴡᴀ {query.from_user.username}\n ⛩️ 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗕𝗲𝗻𝗲𝗳𝗶𝘁𝘀 & 𝗣𝗲𝗿𝗸𝘀⛩️ \n 💦 𝗗𝗶𝗿𝗲𝗰𝘁 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗟𝗶𝗻𝗸𝘀, 𝗡𝗼 𝗔𝗱 𝗟𝗶𝗻𝗸𝘀\n 𝗦𝗽𝗲𝗰𝗶𝗮𝗹 𝗔𝗰𝗲𝘀𝘀 𝗧𝗼 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀\n🎖️ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs :\n\n● {PRICE1} rs ғᴏʀ 7 ᴅᴀʏs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE2} rs ғᴏʀ 1 ᴍᴏɴᴛʜ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE3} rs For 3 ᴍᴏɴᴛʜs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE4} rs For 6 ᴍᴏɴᴛʜs ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n● {PRICE5} rs For 1 ʏᴇᴀʀ ᴘʀɪᴍᴇ ᴍᴇᴍʙᴇʀsʜɪᴘ\n\n\n💵 UPI ID -  <code>{UPI_ID}</code>\n\n\n📸ғᴏʀ ʙᴜʏɪɴɢ ᴘʀᴇᴍɪᴜᴍ ᴅᴍ({UPI_IMAGE_URL})\n\n♻️ 𝗛𝘂𝗿𝗿𝘆 𝗨𝗽 𝗔𝗻𝗱 𝗚𝗲𝘁 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗡𝗼𝘄 𝗔𝗻𝗱 𝗘𝗻𝗷𝗼𝘆 𝗟𝗼𝗻𝗲𝗹𝘆 𝗡𝗶𝗴𝗵𝘁 𝗪𝗶𝘁𝗵 𝗨𝘀",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("sᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴇɴsʜᴏᴛ(ADMIN) 📸", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
            )
