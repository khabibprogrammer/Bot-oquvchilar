import telebot
from telebot import types

BOT_TOKEN = "8538888273:AAEvheo3TLnHsnhWXJVRohfJ89k_qq6d6GY"
CHANNEL_ID = "@bright_future_asakaa"  

bot = telebot.TeleBot(BOT_TOKEN)

user_data = {}

def start_process(chat_id):
    user_data[chat_id] = {"step": "wait_media"}
    bot.send_message(chat_id, "Rasm yoki video tashlang 📷🎥")


excel_tasks = [
    "tasks/excel1.jpg",
    "tasks/excel2.jpg",
    "tasks/excel3.jpg",
    "tasks/excel4.jpg"
]
word_tasks = [
    "tasks/word1.jpg",
    "tasks/word2.jpg",
    "tasks/word3.jpg",
    "tasks/word4.jpg",
    "tasks/word5.jpg",
    "tasks/word6.jpg",
    "tasks/word7.jpg",
    "tasks/word8.jpg",
]

powerpoint_tasks = [
    
  
]


def task_keyboard(index):
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton("◀️ Oldingi", callback_data=f"excel_prev_{index}")
    next_btn = types.InlineKeyboardButton("▶️ Keyingi", callback_data=f"excel_next_{index}")
    center_btn = types.InlineKeyboardButton(f"{index+1}/{len(excel_tasks)}", callback_data="none")

    keyboard.row(prev_btn, center_btn, next_btn)
    return keyboard

def funksiyalar():
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton(
        "Word tezkor tugmalar ⌨️",
        callback_data="tezkor"
    )
    next_btn = types.InlineKeyboardButton(
        "Excel funksiyalar 📚",
        callback_data="excel"
    )

    keyboard.row(prev_btn, next_btn)
    return keyboard

def main_menu():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add( "Word vazifa","Excel vazifa", "Yodlash uchun")
    return kb


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalomu alaykum! vazifani rasm yoki video holoatda yuboring", reply_markup=main_menu())

def task_keyboard_excel(index):
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton("◀️ Oldingi", callback_data=f"excel_prev_{index}")
    next_btn = types.InlineKeyboardButton("▶️ Keyingi", callback_data=f"excel_next_{index}")
    center_btn = types.InlineKeyboardButton(f"{index+1}/{len(excel_tasks)}", callback_data="excel_none")

    keyboard.row(prev_btn, center_btn, next_btn)
    return keyboard

def task_keyboard_word(index):
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton("◀️ Oldingi", callback_data=f"word_prev_{index}")
    next_btn = types.InlineKeyboardButton("▶️ Keyingi", callback_data=f"word_next_{index}")
    center_btn = types.InlineKeyboardButton(f"{index+1}/{len(word_tasks)}", callback_data="word_none")

    keyboard.row(prev_btn, center_btn, next_btn)
    return keyboard

def task_keyboard_powerpoint(index):
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton("◀️ Oldingi", callback_data=f"powerpoint_prev_{index}")
    next_btn = types.InlineKeyboardButton("▶️ Keyingi", callback_data=f"powerpoint_next_{index}")
    center_btn = types.InlineKeyboardButton(f"{index+1}/{len(powerpoint_tasks)}", callback_data="powerpoin_none")

    keyboard.row(prev_btn, center_btn, next_btn)
    return keyboard


# --- Excel vazifa bosilganda ---
@bot.message_handler(func=lambda m: m.text == "Excel vazifa")
def excel_start(message):
    chat_id = message.chat.id

    with open(excel_tasks[0], "rb") as img:
        bot.send_photo(
            chat_id,
            img,
            caption="Excel vazifa 1",
            reply_markup=task_keyboard_excel(0)
        )


# --- Word vazifa bosilganda ---
@bot.message_handler(func=lambda m: m.text == "Word vazifa")
def word_start(message):
    chat_id = message.chat.id

    with open(word_tasks[0], "rb") as img:
        bot.send_photo(
            chat_id,
            img,
            caption="Word vazifa 1",
            reply_markup=task_keyboard_word(0)
        )

# @bot.message_handler(func=lambda m: m.text == "PowerPoint vazifa")
# def word_start(message):
#     chat_id = message.chat.id

#     with open(powerpoint_tasks[0], "rb") as img:
#         bot.send_video(
#             chat_id,
#             img,
#             caption="Word vazifa 1",
#             reply_markup=task_keyboard_word(0)
#         )
@bot.message_handler(func=lambda m: m.text == "Yodlash uchun")
def yodla(message):
    chat_id = message.chat.id

    bot.send_message(
        chat_id,
        "Qaysi birini tanlaysiz?",
        reply_markup=funksiyalar()
    )



@bot.callback_query_handler(func=lambda call: call.data.startswith("excel_"))
def excel_callbacks(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    data = call.data.split("_")
    action = data[1]
    index = int(data[2])

    if action == "next":
        new_index = index + 1
        if new_index >= len(excel_tasks):
            new_index = 0

    elif action == "prev":
        new_index = index - 1
        if new_index < 0:
            new_index = len(excel_tasks) - 1

    # Yangi rasmni yuborish
    with open(excel_tasks[new_index], "rb") as img:
        new_media = types.InputMediaPhoto(img, caption=f"Excel vazifa {new_index+1}")

        bot.edit_message_media(
            media=new_media,
            chat_id=chat_id,
            message_id=msg_id,
            reply_markup=task_keyboard_excel(new_index)
        )

@bot.callback_query_handler(func=lambda call: call.data.startswith("word_"))
def word_callbacks(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    data = call.data.split("_")
    action = data[1]
    index = int(data[2])

    if action == "next":
        new_index = index + 1
        if new_index >= len(word_tasks):
            new_index = 0

    elif action == "prev":
        new_index = index - 1
        if new_index < 0:
            new_index = len(word_tasks) - 1

    # Yangi rasmni yuborish
    with open(word_tasks[new_index], "rb") as img:
        new_media = types.InputMediaPhoto(img, caption=f"Word vazifa {new_index+1}")

        bot.edit_message_media(
            media=new_media,
            chat_id=chat_id,
            message_id=msg_id,
            reply_markup=task_keyboard_word(new_index)
        )

@bot.callback_query_handler(func=lambda call: call.data.startswith("powerpoint_"))
def word_callbacks(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    data = call.data.split("_")
    action = data[1]
    index = int(data[2])

    if action == "next":
        new_index = index + 1
        if new_index >= len(word_tasks):
            new_index = 0

    elif action == "prev":
        new_index = index - 1
        if new_index < 0:
            new_index = len(word_tasks) - 1

    # Yangi rasmni yuborish
    with open(word_tasks[new_index], "rb") as img:
        new_media = types.InputMediaVideo(img, caption=f"Powerpoint vazifa {new_index+1}")

        bot.edit_message_media(
            media=new_media,
            chat_id=chat_id,
            message_id=msg_id,
            reply_markup=task_keyboard_word(new_index)
        )

@bot.message_handler(commands=['add'])
def add(message):
    start_process(message.chat.id)


@bot.message_handler(content_types=['photo', 'video','animation'])
def handle_media(message):
    chat_id = message.chat.id

    if chat_id in user_data and user_data[chat_id]["step"] == "wait_media":

        if message.content_type == "photo":
            user_data[chat_id]["media_type"] = "photo"
            user_data[chat_id]["file_id"] = message.photo[-1].file_id

        elif message.content_type == "video":
            user_data[chat_id]["media_type"] = "video"
            user_data[chat_id]["file_id"] = message.video.file_id
        
        elif message.content_type == "animation":  
            user_data[chat_id]["media_type"] = "gif"
            user_data[chat_id]["file_id"] = message.animation.file_id

        user_data[chat_id]["step"] = "wait_name"
        bot.send_message(chat_id, "Ism familiyangizni yozing ✍️")

@bot.callback_query_handler(func=lambda call: call.data == "tezkor")
def word_tezkor(call):
    text = (
        "📘 *Microsoft Word tezkor tugmalari*\n\n"
        "1. Ctrl + C — Nusxalash\n"
        "2. Ctrl + X — Kesish\n"
        "3. Ctrl + V — Joylashtirish\n"
        "4. Ctrl + Z — Bekor qilish\n"
        "5. Ctrl + S — Saqlash\n"
        "6. Ctrl + O — Faylni ochish\n"
        "7. Ctrl + N — Yangi hujjat\n"
        "8. Ctrl + P — Chop etish\n"
        "9. Ctrl + A — Hammasini belgilash\n"
        "10. Ctrl + F — Qidirish\n"
        "11. Ctrl + B — Qalin (Bold)\n"
        "12. Ctrl + I — Italic\n"
        "13. Ctrl + U — Tagiga chiziq\n"
        "14. Ctrl + L — Chapga tekislash\n"
        "15. Ctrl + R — O‘ngga tekislash\n"
        "16. Ctrl + E — Markazlash\n"
        "17. Ctrl + J — Justify\n"
        "18. Ctrl + K — Hyperlink\n"
        "19. Ctrl + Y — Qayta bajarish\n"
        "20. Ctrl + F4 — Hujjatni yopish"
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "excel")
def excel_funksiyalar(call):
    text = (
        "📊 *Microsoft Excel asosiy funksiyalari*\n\n"
        "🔹 *SUM* – СУММ → Sonlarni qo‘shadi\n\n"
        "🔹 *AVERAGE* – СРЗНАЧ → O‘rtacha qiymatni hisoblaydi\n\n"
        "🔹 *IF* – ЕСЛИ → Shart tekshiradi va natijaga qarab qiymat qaytaradi\n\n"
        "🔹 *VLOOKUP* – ВПР → Jadval ustunidan ma’lumot qidiradi\n\n"
        "🔹 *HLOOKUP* – ГПР → Jadval satridan ma’lumot qidiradi\n\n"
        "🔹 *UPPER* – ПРОПИСН → Hamma harflarni katta qiladi\n\n"
        "🔹 *LOWER* – СТРОЧН → Hamma harflarni kichik qiladi\n\n"
        "🔹 *PROPER* – ПРОПНАЧ → Har bir so‘zni bosh harf bilan yozadi\n\n"
        "🔹 *COUNT* – СЧЁТ → Raqamli kataklar sonini sanaydi\n\n"
        "🔹 *COUNTA* – СЧЁТЗ → Bo‘sh bo‘lmagan kataklar sonini sanaydi\n\n"
        "🔹 *MAX* – МАКС → Eng katta qiymatni topadi\n\n"
        "🔹 *MIN* – МИН → Eng kichik qiymatni topadi\n\n"
        "🔹 *ROUND* – ОКРУГЛ → Sonni belgilangan raqamgacha yaxlitlaydi\n\n"
        "🔹 *CONCAT / TEXTJOIN* – СЦЕПИТЬ → Matnlarni birlashtiradi\n\n"
        "🔹 *NOW* – ТДАТАВРЕМЯ → Hozirgi sana va vaqtni ko‘rsatadi\n\n"
        "🔹 *TODAY* – СЕГОДНЯ → Hozirgi sanani ko‘rsatadi\n\n"
        "🔹 *ABS* – ABS → Sonning musbat qiymatini qaytaradi (modul)\n\n"
        "🔹 *PMT* – ПЛТ → Kredit to‘lovini hisoblaydi"
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown"
    )

    
@bot.message_handler(func=lambda msg: True)
def handle_name(message):
    chat_id = message.chat.id

    if chat_id in user_data and user_data[chat_id]["step"] == "wait_name":
        full_name = message.text
        media_type = user_data[chat_id]["media_type"]
        file_id = user_data[chat_id]["file_id"]

        if media_type == "photo":
            bot.send_photo(
                CHANNEL_ID,
                file_id,
                caption=f"👤 {full_name}\n bugungi vazifasi\n08.12.2025"
            )
        elif media_type == "video":
            bot.send_video(
                CHANNEL_ID,
                file_id,
                caption=f"👤 {full_name}\n bugungi vazifasi\n 08.12.2025"
            )
        elif media_type == "gif":
            bot.send_animation(
                CHANNEL_ID,
                file_id,
                caption=f"👤 {full_name}"
            )




        bot.send_message(chat_id, "Ma'lumotlar kanlaga yuborildi! ✅\nYana rasm yoki video yuborish uchun /add bosing.")

        user_data.pop(chat_id, None)


bot.polling()