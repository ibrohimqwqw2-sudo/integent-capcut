import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

# ===== TOKEN VA ADMIN ID =====
TOKEN = "8119618358:AAEjiK_lS2Ax8FQIHBJZmYgtI6dAaNiBqhM"
ADMIN_ID = 8326607612  # Admin ID yozing

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ===== INLINE KNOPKALAR =====
tarif_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💠 STANDART TARIF", callback_data="standart")],
        [InlineKeyboardButton(text="💎 PREMIUM TARIF", callback_data="premium")]
    ]
)

# ===== USERNAME FUNKSIYA =====
def get_username(user):
    return f"@{user.username}" if user.username else "Username yo‘q"

# ===== /start =====
@dp.message(Command("start"))
async def start_handler(message: Message):
    text = """
Assalomu alaykum hammaga 👋

Endi sizlar bitta obed puliga butunlik kursini o‘rganasizlar.

Iltimos Tarifni Tanlang:

💠 STANDART TARIF (100 ming so‘m)
🔹 14 ta montaj darslik
🔹 1 ta katta AI darslik

💎 PREMIUM TARIF (150 ming so‘m)
🔶 16 ta montaj darslik
🔶 1 ta katta AI darslik
🔶 Bonus (Sound sfx, music, lut, fonts, background)

Hammaga omad 🍀
"""
    await message.answer(text, reply_markup=tarif_kb)

# ===== STANDART BOSILDI =====
@dp.callback_query(F.data == "standart")
async def standart_tarif(callback: CallbackQuery):

    user = callback.from_user

    await callback.message.answer("Rahmat qabul qilindi ✅ Tez orada siz bilan admin bog‘lanadi.")
    await callback.answer()

    await bot.send_message(
        ADMIN_ID,
        f"""
📥 Yangi buyurtma!

👤 Ism: {user.full_name}
🆔 ID: {user.id}
📱 Username: {get_username(user)}
📦 Tarif: STANDART
"""
    )

# ===== PREMIUM BOSILDI =====
@dp.callback_query(F.data == "premium")
async def premium_tarif(callback: CallbackQuery):

    user = callback.from_user

    await callback.message.answer("✅ Tez orada siz bilan admin bog‘lanadi.")
    await callback.answer()

    await bot.send_message(
        ADMIN_ID,
        f"""
📥 Yangi buyurtma!

👤 Ism: {user.full_name}
🆔 ID: {user.id}
📱 Username: {get_username(user)}
📦 Tarif: PREMIUM
"""
    )

# ===== BOTNI ISHGA TUSHIRISH =====
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
