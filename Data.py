from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ 🔥", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "✨ ᴏᴜʀ ᴏᴛʜᴇʀ ʙᴏᴛs ᴀɴᴅ sᴛᴀᴛᴜs ✨", url="https://t.me/jasa_kirito"
            )
        ],
        [
            InlineKeyboardButton("🤔 ʜᴏᴡ ᴛᴏ ᴜsᴇ 🤔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("💌 ᴏᴛʜᴇʀ ʙᴏᴛs 💌", url="https://t.me/jasa_kirito")],
    ]

    START = """
ʜᴀɪ {}
ꜱᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ {}
ᴊɪᴋᴀ ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ᴍᴇᴍᴘᴇʀᴄᴀʏᴀɪ ʙᴏᴛ ɪɴɪ,
1) ʙᴇʀʜᴇɴᴛɪ ᴍᴇᴍʙᴀᴄᴀ ᴘᴇꜱᴀɴ ɪɴɪ
2) ʜᴀᴘᴜꜱ ᴏʙʀᴏʟᴀɴ ɪɴɪ
ᴍᴀꜱɪʜ ᴍᴇᴍʙᴀᴄᴀ?
ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴀʏᴀ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ꜱᴛʀɪɴɢ ᴘʏʀᴏɢʀᴀᴍ ᴀᴛᴀᴜ ᴛᴇʟᴇᴛʜᴏɴ.
 ɢᴜɴᴀᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍᴘᴇʟᴀᴊᴀʀɪ ʟᴇʙɪʜ ʟᴀɴᴊᴜᴛ!

ʙʏ @kiritonibos
    """

    HELP = """
✨ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** ✨

/about - ᴛᴇɴᴛᴀɴɢ ʙᴏᴛ
/help - ᴜɴᴛᴜᴋ ʙᴀɴᴛᴜᴀɴ
/start - sᴛᴀʀᴛ ʙᴏᴛ
/repo - ᴍᴇɴɢᴀᴍʙɪʟ ʀᴇᴘᴏ
/generate - ᴍᴇᴍᴜʟᴀɪ ᴍᴇɴɢᴀᴍʙɪʟ ꜱᴛʀɪɴɢ
/cancel - ʙᴇʀʜᴇɴᴛɪ ᴍᴇɴᴊᴀʟᴀɴᴋᴀɴ ᴘʀᴏꜱᴇꜱ
/restart - ᴍᴇᴍᴜʟᴀɪ ᴜʟᴀɴɢ ᴘʀᴏꜱᴇꜱ
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @kiritonibos

sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/DjeFaris)
ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)
ᴏᴡɴᴇʀ : @kiritonibos
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
💥 A ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ
ᴏғ ♻️ ͔`ꝛɪᴛᴏ </> 🔥
━━━━━━━━━━━━━━━━━
ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴇʀ [͔`ꝛɪᴛᴏ </>](https://t.me/kiritonibos)
┣★ ʙᴏᴛ ᴜᴏᴅᴀᴛᴇs [ᴏᴜʀ ᴏᴛʜᴇʀ ʙᴏᴛs](https://t.me/jasa_kirito
┣★ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/DjeFaris
┣★ ɴᴇᴛᴡᴏʀᴋ [ʀᴏᴄᴋs](https://t.me/ritolog)
┗━━━━━━━━━━━━━━━━━┛
💞 
ᴋᴀʟᴀᴜ ᴀᴅᴀ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ʟᴇʙɪʜ ʟᴀɴᴊᴜᴛ ꜱɪʟᴀʜᴋᴀɴ ʙᴇʀᴛᴀɴʏᴀ
 » ᴋᴇ » [OWNER] @kiritonibos
   """
