class Scripted(object):    


    PROGRESS_DIS = """\n
โญโโโ[**๐Progress Bar๐**]โโโโ
โ<b>๐ : {1} | {2}</b>\n
โ<b>๐ : {0}%</b>\n
โ<b>โก : {3}/s</b>\n
โ<b>โฑ๏ธ : {4}</b>\n
โฐโโโโโโโโโโโโโโโโ"""

    HELP_TEXT = """
<i>๐๐๐ญ๐๐ก ๐๐ข๐๐๐จ ๐๐จ๐ฐ ๐ญ๐จ ๐๐ฌ๐ ๐๐ <a href='https://youtu.be/HnXdu74o34E'>[ แดสษชแดแด สแดสแด ]</a></i>\n
<i>๐๐๐ง๐ ๐ ๐ฉ๐ก๐จ๐ญ๐จ ๐ญ๐จ ๐ฆ๐๐ค๐ ๐ข๐ญ ๐๐ฌ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ (optional)</i>\n
<i>๐๐๐ง๐ ๐ฆ๐ ๐๐ง๐ฒ ๐๐ข๐ฅ๐ (or) ๐๐๐๐ข๐ ๐๐ซ๐จ๐ฆ ๐ญ๐๐ฅ๐๐ ๐ซ๐๐ฆ</i>\n
<i>๐๐จ๐ง๐ฏ๐๐ซ๐ญ ๐๐ข๐ฅ๐๐ฌ ๐ข๐ง๐ญ๐จ ๐ฏ๐ข๐๐๐จ ๐ฎ๐ฌ๐ /convert ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>\n
<i>๐๐๐ฉ๐ฅ๐ฒ ๐ญ๐จ ๐ญ๐ก๐๐ญ ๐๐ข๐ฅ๐ ๐ฐ๐ข๐ญ๐ก /rename ๐ง๐๐ฐ ๐ง๐๐ฆ๐.ext</i>\n
<i>๐๐ข๐๐ฐ ๐ฒ๐จ๐ฎ๐ซ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ /sthumbnail ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>\n
<i>๐๐๐ฅ๐๐ญ๐ ๐ฒ๐จ๐ฎ๐ซ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ /dthumbnail ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>"""


    ABOUT_TEXT = """
โญโโโ[ **๐Rแดษดแดแดแดส DX Bแดแด๐**]โโโโ
โ
โ<b>๐คBot Name : <a href='https://t.me/Renamer_teleroid_bot'>Rename X2 Bot</a></b>\n
โ
โ<b>๐ข Channel : <a href='https://t.me/TeleRoidGroup'>TรLรRรรD</a></b>\n
โ
โ<b>๐ฅ Version : <a href='https://t.me/TeleRoid_Renamer_bot'>0.9.2 beta</a></b>\n
โ
โ<b>๐ข Source : <a href='https://github.com/PredatorHackerzZ/Renamer-bot'>Click Here</a></b>\n
โ
โ<b>๐ Server : <a href='https://heroku.com'>Heroku</a></b>\n
โ
โ<b>๐ Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>\n
โ
โ<b>ใ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>\n
โ
โ<b>๐จโ๐ป Developer : <a href='https://t.me/PredatorHackerZ'>๊ง ฦคโษฤโณโฎรโ ๐ฎ๐ณ ๊ง</a></b>\n
โ
โ<b>๐ธ Powered By : <a href='https://t.me/Moviesflixers_DL'>Tแดแดษชสแดกแดส Tษข Nแดแดแดกแดสแด</a></b>\n
โ
โฐโโโโโโโโโ[Thanks ๐]โโโโโโโโโ"""

    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<b>ยฅou Are Banned ๐ซ</b>"
    BANNED_USER_TEXT = "<i>ยฅou are Banned ๐ซ</i>"
    TRYING_TO_UPLOAD = "<i>Trying to Upload.....</i>"
    CURRENT_THUMBNAIL = "<i>๐๐จ๐ฎ๐ซ ๐๐ฎ๐ซ๐ซ๐๐ง๐ญ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐ญ</i>"
    THUMBNAIL_SAVED = "<i>๐๐จ๐ฎ๐ซ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐๐ฏ๐๐ โ</i>"
    THUMBNAIL_DELETED = "<i>๐๐จ๐ฎ๐ซ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐๐ฅ๐๐ญ๐๐ โ</i>"
    NO_THUMBNAIL_FOUND = "<i>๐๐จ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ๐ฎ๐ง๐ (๐๐จ๐ง๐ฌ๐ข ๐๐๐๐ฅ๐ข ๐๐ก๐๐ก๐ข๐ฒ๐)๐</i>"
    TRYING_TO_DOWNLOAD = "<i>๐๐ซ๐ฒ๐ข๐ง๐  ๐๐จ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐....</i>"
    UPLOAD_SUCCESS = "<u><i>Tสแดษดแดแด Fแดส Usษชษดษข แดแดโค @TheTeleRoid</i></u>"
    REPLY_TO_MEDIA = "<i>๐๐๐ฉ๐ฅ๐ฒ ๐ญ๐จ ๐ญ๐ก๐๐ญ ๐๐๐๐ข๐ ๐ฐ๐ข๐ญ๐ก /convert</i>"
    UPLOAD_START = "<i>๐ค ๐๐ฉ๐ฅ๐จ๐๐๐ข๐ง๐  ๐ฒ๐จ๐ฎ๐ซ ๐๐ข๐ฅ๐ ๐ฉ๐ฅ๐๐๐ฌ๐ ๐ฐ๐๐ข๐ญ...</i>\n"
    DOWNLOAD_START = "<i>๐ฅ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐ข๐ง๐  ๐ฒ๐จ๐ฎ๐ซ ๐๐ข๐ฅ๐ ๐ฉ๐ฅ๐๐๐ฌ๐ ๐ฐ๐๐ข๐ญ...</i>\n"
    JOIN_NOW_TEXT = "<code>๐ฑ๐๐๐๐ ๐ต๐๐๐ ๐ธ๐ ๐๐๐๐๐๐๐ ๐ฎ๐๐๐๐๐๐ ๐ฟ๐ ๐๐๐ ๐ธ๐๐</code>"
    REPLY_TO_FILE = "<i>๐๐๐ฉ๐ฅ๐ฒ ๐ญ๐จ ๐ญ๐ก๐๐ญ ๐๐ข๐ฅ๐ ๐ฐ๐ข๐ญ๐ก /rename ๐ง๐๐ฐ ๐ง๐๐ฆ๐ .๐๐ฑ๐ญ</i>"
    CONTACT_MY_DEVELOPER = "<i>Something Wrong Contact in Support Group @TeleRoid14 ๐</i>"
    START_TEXT = "<i>This is a Fastest File Renamer and Converter Bot With Permanant Thumbnail Support๐ฏ</i>"
    UPGRADE_TEXT = "<b>To upgrade your subscription <a href='https://t.me/TeleRoid14'>[ ๐๐ฅ๐ข๐๐ค ๐๐๐ซ๐ ]</a></b>"
