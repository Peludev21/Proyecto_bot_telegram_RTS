from pyrogram import Client,filters
import config,datetime,keyboards,random,json
from FusionBrain_AI import generate
import base64

bot = Client(
    api_id = config.API_ID,
    api_hash = config.API_HASH,
    bot_token = config.BOT_TOKEN,
    name = "Klombo_bot"
)

def button_filter(button):
   async def func(_, __, msg):
       return msg.text == button.text
   return filters.create(func, "ButtonFilter", button=button)

@bot.on_message(filters.command("image"))

async def image(bot,message):
    if len(message.text.split()) > 1:
        await message.reply("Que imagen desea generar, por favor describala")
        query = message.text.replace("/image","")
        await message.reply(f"generando una imagen de {query}")
        await message.reply("Por favor espera un momento")
        images = await generate(query)
        print(images)
        if images:
            image_data = base64.b64decode(images[0])
            img_num = random.randint(1,99)
            with open(f"image{img_num}.jpg","wb") as file:
                file.write(image_data)
            await bot.send_photo(message.chat.id,f"images/{img_num}image.jpg",reply_to_message_id=message.message_id)
    else:
        await message.reply("Porfavor, ingrese una instruccion correcta")
        
            
        

@bot.on_message(filters.command("quest")| button_filter(keyboards.btn_aventura))
async def quest(bot,message):
    await message.reply_text("Te gustaria empezar una aventura legendaria?",reply_markup = keyboards.inLine_kb_start_quest)

@bot.on_callback_query()
async def handle_query(bot,query):
    #await query.message.delete()
    if query.data == "start_quest":
        await bot.answer_callback_query(query.id,text = "¡Bienvenido a la mision llamada busqueda del tesoro!",show_alert = True)
        await query.message.reply_text("Estas parado en frente de dos puertas,cual eliges",reply_markup=keyboards.inline_kb_button_choise_desicion)
    elif query.data == "Puerta izquierda":
        await query.message.reply_text("Entras a una habitacion oscura y ves un dragon, que haras?",reply_markup=keyboards.inline_kb_button_puerta_izquierda)
    elif query.data == "Dragon":
        await bot.answer_callback_query(query.id, text="Luchas contra el dragon, pero el es mas fuerte que tu y te come",show_alert = True)
    elif query.data == "Correr":
        await bot.answer_callback_query(query.id,text = "Intentas escapar, pero el dragon te alcanza y te come",show_alert = True)
    elif query.data == "Puerta derecha":
        await query.message.reply_text("¡Entras en una habitacion llena de tesoros! Elige solo uno",reply_markup=keyboards.inline_kb_button_puerta_derecha)
    elif query.data == "Corona dorada":
        await bot.answer_callback_query(query.id, text = "Tomas la corona dorada y sales de la habitacion, Felicitaciones, ganaste!",show_alert = True)
    elif query.data == "Daga":
        await bot.answer_callback_query(query.id, text="Tomas la daga plateada y sales de la habitacion. Lastimosamente no vale nada!",show_alert = True)
    elif query.data == "Libro":
        await bot.answer_callback_query(query.id, text="Tomas el libro viejo y sales de la habitacion. Resulta que el libro es magico, lo abres y desapareces",show_alert = True)
    else:
        await query.message.reply_text("Opción no válida, por favor intenta de nuevo.")
         
@bot.on_message(filters.command("start") | button_filter(keyboards.btn_atras))
async def start(bot,message):
    await message.reply("¡Bienvenido!",reply_markup = keyboards.kb_main)
    with open("users.json","r")as file:
        users = json.load(file)
    if str(message.from_user.id) not in users.keys():
        users[message.from_user.id] = 100
        with open("users.json","w") as file:
            json.dump(users,file)
    
@bot.on_message(filters.command("info") | button_filter(keyboards.boton_info))
async def info(bot,message):
    await message.reply("Hola! Aqui tienes todas las funcionalidades que tiene el bot y una lista de comandos")
    
@bot.on_message(filters.command("time") | button_filter(keyboards.boton_time))
async def obtener_hora(bot,message):
    date_time = datetime.datetime.now()
    await message.reply(f"Actualmente son las {date_time.time()}")
    
@bot.on_message(filters.command("games") | button_filter(keyboards.boton_juego))
async def mostrar_juegos(bot,message):
    await message.reply(f"Por favor, escoge un videojuego",reply_markup = keyboards.kb_games)
        

@bot.on_message(filters.command("Ppt") | button_filter(keyboards.btn_game))
async def escoger_opcion(bot,message):
    with open("users.json","r") as file:
        users = json.load(file)
        
    if users[str(message.from_user.id)] >= 10:
        await message.reply("Bienvenido a piedra, papel o tijeras, escoge una opcion",reply_markup = keyboards.kb_Ppt)
    else:
        await message.reply(f"Fondos insuficientes {users[str(message.from_user.id)]},")
        
@bot.on_message(filters.command("generate") | button_filter(keyboards.boton_generate_AI))
async def generate_image(bot,message):
    await message.reply("Porfavor, ingrese el texto que desea convertir en imagen")
        
@bot.on_message(button_filter(keyboards.btn_piedra)| 
                button_filter(keyboards.btn_papel) | 
                button_filter(keyboards.btn_tijeras))
async def Ppt(bot,message):
    with open("users.json","r") as file:
        users = json.load(file)
    
    piedra = keyboards.btn_piedra.text
    papel = keyboards.btn_papel.text
    tijeras = keyboards.btn_tijeras.text
    user = message.text
    pc = random.choice([piedra,papel,tijeras])    
    if user == pc:
        await message.reply("Empate")
    elif (user == papel and pc == piedra) or (user == tijeras and pc == papel) or (user == piedra and pc == tijeras):
        await message.reply(f"Has ganado porque el bot eligio: {pc}")
        users[str(message.from_user.id)] += 10
    elif (user == papel and pc == tijeras) or (user == piedra and pc == papel) or (user == tijeras and pc == piedra):
        await message.reply(f"Has perdido porque el bot eligio: {pc}")
        users[str(message.from_user.id)] -= 10
        
    with open("user.json","w") as file:
        json.dump(users,file)
    
                
@bot.on_message()
async def echo(bot,message):
    if message.text == "hola":
        await message.reply("Hola :)")
    elif message.text == "adios":
        await message.reply("hasta luego")
        
        
bot.run()