from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram import emoji

inLine_kb_start_quest = InlineKeyboardMarkup([
    [InlineKeyboardButton("Empezar una mision",callback_data="start_quest")]
])


boton_info = KeyboardButton(f"{emoji.INFORMATION} Info")
boton_juego = KeyboardButton(f"{emoji.VIDEO_GAME} Juegos")
boton_perfil = KeyboardButton(f"{emoji.PERSON} Perfil")
boton_time = KeyboardButton(f"{emoji.TIMER_CLOCK} Hora")
boton_generate_AI = KeyboardButton(f"{emoji.CAMERA} Generar imagen")

kb_main = ReplyKeyboardMarkup(
    keyboard = [
        [boton_info,boton_juego,boton_perfil,boton_time,boton_generate_AI]
    ],
    resize_keyboard=True
)


btn_game = KeyboardButton(f"{emoji.ROCK}{emoji.PAGE_FACING_UP}{emoji.SCISSORS} Piedra,papel o tijeras")
btn_aventura = KeyboardButton(f"{emoji.WORLD_MAP}Aventura")
btn_atras = KeyboardButton(f"{emoji.LEFT_ARROW}Volver atras")

kb_games = ReplyKeyboardMarkup(
    keyboard = [
        [btn_game,btn_aventura,btn_atras]
    ],
    resize_keyboard=True 
)

btn_piedra = KeyboardButton(f"{emoji.ROCK}")
btn_papel = KeyboardButton(f"{emoji.NOTEBOOK}")
btn_tijeras = KeyboardButton(f"{emoji.SCISSORS}")

kb_Ppt = ReplyKeyboardMarkup(
    keyboard = [
        [btn_piedra,btn_papel,btn_tijeras],
        [btn_atras]
    ],
    resize_keyboard=True
)
#Aqui iran todos los teclados que tengan que ver con el boton aventura

inline_kb_button_choise_desicion = InlineKeyboardMarkup([
    [InlineKeyboardButton("Puerta izquierda 🚪⬅️", callback_data="Puerta izquierda")],
    [InlineKeyboardButton("Puerta derecha ➡️🚪", callback_data="Puerta derecha")]
])
inline_kb_button_puerta_izquierda = InlineKeyboardMarkup([
    [InlineKeyboardButton("🐉Lucha con el dragon", callback_data="Dragon")],
    [InlineKeyboardButton("🏃Intenta escapar",callback_data="Correr")]
])
inline_kb_button_puerta_derecha = InlineKeyboardMarkup([
    [InlineKeyboardButton("👑Corona dorada",callback_data="Corona dorada")],
    [InlineKeyboardButton("🗡️Daga de plata",callback_data="Daga")],
    [InlineKeyboardButton("📕Libro Viejp", callback_data="Libro")]
])