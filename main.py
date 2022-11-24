import telebot
import time
from telebot import types
import psycopg2
from psycopg2 import Error
id_no_ref = 1042554792 #
TOKEN = "RUB"
BOT_TOKEN = "5703266677:AAGHGESqvoEB1dUUWOcRPeaqLB9cvcZajgM"
OWNER_ID = 1743902751
CHANNELS = ['@primmer_spo']
Mini_Withdraw = 45
per_ref = 3
userss = [1743902751]

bot = telebot.TeleBot(BOT_TOKEN)
def check(id):
    for i in CHANNELS:
        check = bot.get_chat_member(i, id)
        if check.status != 'left':
            pass
        else:
            return False
    return True

# Подключение к существующей базе данных
db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")

# Курсор для выполнения операций с базой данных
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    user_name TEXT,
    parent_id INT,
    balance INT NOT NULL DEFAULT 0,
    ref1 INT NOT NULL DEFAULT 0,
    ref2 INT NOT NULL DEFAULT 0,
    wallet TEXT,
    sub_chek INT NOT NULL DEFAULT 0,
    ban INT NOT NULL DEFAULT 0   
)""")
db.commit()
db.close()
ban_users = []
@bot.message_handler(func=lambda message: message.chat.id in ban_users)
def some(message):
   bot.send_message(message.chat.id, "Извините, вы были заблокированы за подозрительные действия.")
#..................................................

#...................Рассылка......................
@bot.message_handler(commands=['send'])
def notify(message):
    try:
        command_sender = message.from_user.id

        if message.chat.id not in OWNER_ID:
            bot.send_message(OWNER_ID, f'кто-то хочет юзать рассылку')

        else:
            with open(r'users.txt') as ids:
                for line in ids:
                    user_id = int(line.strip("\n"))
                    try:
                        bot.send_message(user_id, message.text[message.text.find(' '):])
                    except Exception as e:
                        bot.send_message(1042554792, f'ошибка отправки сообщения нескольким юзерам')
    except Exception as e:
        bot.send_message(1042554792, f'ciot ne to')
#........................................................................................................


def menu(id):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('🆔 Аккаунт', '🙌🏻 Рефералы')
    keyboard.row('⚙️ Кошелёк', '💸 Вывод')
    keyboard.row('📊 Информация', '💻  Партнеры')
    bot.send_message(id, "*🏡 Home*", parse_mode="Markdown",reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    userr = message.chat.id
    user_namess = message.from_user.username
    msg = message.text
    startms = msg.split()[0]
    referrer = None
    st = "/start"
    if startms == st:
        db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
        sql = db.cursor()
        sql.execute("SELECT id FROM users WHERE id = %s", [userr])
        values = [userr, user_namess]
        if sql.fetchone() is None:
            sql.execute("INSERT INTO users(id, user_name) VALUES(%s, %s)", values)
            db.commit()
        try:

            ref_id = msg.split()[1]
            userr = message.chat.id
            db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
            sql = db.cursor()
            sql.execute("SELECT parent_id FROM users WHERE id = %s", [userr])
            if sql.fetchone()[0] is None:
                sql.execute("UPDATE users SET parent_id = ? WHERE id = %s", [ref_id, userr])
                db.commit()
        except:
            userr = message.chat.id
            db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
            sql = db.cursor()
            sql.execute("SELECT parent_id FROM users WHERE id = %s", [userr])
            if sql.fetchone()[0] is None:
                sql.execute("UPDATE users SET parent_id = %s WHERE id = %s", [id_no_ref, userr])
                db.commit()

        def check(id):
            for i in CHANNELS:
                check = bot.get_chat_member(i, userr)
                if check.status != 'left':
                    pass
                else:
                    return False
            return True

        msg = message.text
        db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
        sql = db.cursor()
        sql.execute("SELECT id FROM users WHERE id = %s", [userr])
        values = [userr, user_namess, id_no_ref]
        if sql.fetchone() is None:
            sql.execute("INSERT INTO users(id, user_name, parent_id) VALUES(%s, %s, %s)", values)
            db.commit()
        markup = telebot.types.InlineKeyboardMarkup()
        url_btnn1 = types.InlineKeyboardButton(text='Подписаться', url='https://t.me/+El4BNXj0iUJiOWIy')
        url_btnn2 = types.InlineKeyboardButton(text='Подписаться', url='')
        url_btnn3 = types.InlineKeyboardButton(text='Подписаться', url='')
        url_btnn4 = types.InlineKeyboardButton(text='Подписаться', url='')
        url_btnn5 = types.InlineKeyboardButton(text='Подписаться', url='')
        url_btnn6 = types.InlineKeyboardButton(text='Подписаться', url='')
        markup.add(url_btnn1)
        markup.add(telebot.types.InlineKeyboardButton(
            text='🤼‍♂️ Проверить подписку', callback_data='check'))
        msg_start = "*🍔 Добро пожаловать в Бенжи раздаёт!, для начала работы подпишись на наших спонсоров:"
        for i in CHANNELS:
            msg_start + f"https://t.me/+El4BNXj0iUJiOWIy \n"
        msg_start += "*"
        bot.send_message(userr, msg_start,
                         parse_mode="Markdown", reply_markup=markup)
    else:
        user = message.chat.id
        user = str(user)

        markups = telebot.types.InlineKeyboardMarkup()
        markups.add(telebot.types.InlineKeyboardButton(
            text='🤼‍♂️ Проверить подписку', callback_data='check'))
        msg_start = "*🍔 Кажется вы не подписаны на всe каналы.*"
        bot.send_message(user, msg_start,
                         parse_mode="Markdown", reply_markup=markups)
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    try:
        ch = check(call.message.chat.id)
        if call.data == 'check':
            if ch == True:
                user_id = call.message.chat.id
                user_names = call.from_user.username
                user = str(user_id)
                bot.answer_callback_query(
                    callback_query_id=call.id, text='✅ Вы подписались, теперь вы можете зарабатывать деньги.')
                bot.delete_message(call.message.chat.id, call.message.message_id)
                keyboard = telebot.types.ReplyKeyboardMarkup(True)
                keyboard.row('🆔 Аккаунт', '🙌🏻 Рефералы')
                keyboard.row('⚙️ Кошелёк', '💸 Вывод')
                keyboard.row('📊 Информация', '💻  Партнеры')
                bot.send_message(user, "*🏡 Home*", parse_mode="Markdown", reply_markup=keyboard)
                db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
                sql = db.cursor()
                sql.execute("SELECT sub_chek FROM users WHERE id = %s", [user])
                if sql.fetchone()[0] == 0:
                    sql.execute("SELECT parent_id FROM users WHERE id = %s", [user])
                    parent_id = sql.fetchone()[0]
                    sql.execute("SELECT parent_id FROM users WHERE id = %s", [parent_id])
                    parent_id2 = sql.fetchone()[0]
                    sql.execute("SELECT balance FROM users WHERE id = %s", [parent_id])
                    bal_par = sql.fetchone()[0]
                    sql.execute("SELECT ref1 FROM users WHERE id = %s", [parent_id])
                    ref1 = sql.fetchone()[0]
                    sql.execute("SELECT ref2 FROM users WHERE id = %s", [parent_id2])
                    ref2 = sql.fetchone()[0]
                    r1 = ref1 + 1
                    r2 = ref2 + 1
                    bal = bal_par + per_ref
                    sql.execute("UPDATE users SET sub_chek = %s WHERE id = %s",[1, user])
                    sql.execute("UPDATE users SET ref1 = %s WHERE id = %s", [r1, parent_id])
                    sql.execute("UPDATE users SET ref2 = %s WHERE id = %s", [r2, parent_id2])
                    sql.execute("UPDATE users SET sub_chek = %s WHERE id = %s", [1, user])
                    sql.execute("UPDATE users SET balance = %s WHERE id = %s", [bal, parent_id])
                    db.commit()
                    bot.send_message(parent_id, f"*🏧 Пользователь перешёл по вашей ссылке, вы получили : +{per_ref} {TOKEN}*", parse_mode="Markdown")
                    joinedFile = open('users.txt', 'a')
                    joinedFile.write(str(user) + "\n")
                    return
            else:
                    bot.answer_callback_query(
                        callback_query_id=call.id, text='❌ Ты не подписан.')
                    bot.delete_message(call.message.chat.id, call.message.message_id)
                    markupq = types.InlineKeyboardMarkup()
                    url_btnn1 = types.InlineKeyboardButton(text='Подписаться', url='https://t.me/+yWh9mlAcZEk3MTMy')
                    url_btnn2 = types.InlineKeyboardButton(text='Подписаться', url='')
                    url_btnn3 = types.InlineKeyboardButton(text='Подписаться', url='')
                    url_btnn4 = types.InlineKeyboardButton(text='Подписаться', url='')
                    url_btnn5 = types.InlineKeyboardButton(text='Подписаться', url='')
                    url_btnn6 = types.InlineKeyboardButton(text='Подписаться', url='')
                    chekb = types.InlineKeyboardButton(text='🤼‍♂️ Проверить подписку', callback_data='check')
                    markupq.add(url_btnn1)
                    markupq.add(chekb)
                    msg_start = '*🍔 Пожалуйста проверьте подписались ли вы на всё каналы и нажмите "Проверить подписку".*'
                    bot.send_message(call.message.chat.id, msg_start,
                                     parse_mode="Markdown", reply_markup=markupq)


            return
    except:

        bot.send_message(call.message.chat.id ,"Эта команда имеет ошибку, пожалуйста, подождите, пока администратор не исправит её.")
        bot.send_message(OWNER_ID, "Your bot got an error fix it fast!")
        return
@bot.message_handler(content_types=['text'])
def send_text(message):
   try:
    if message.text == '🆔 Аккаунт':
        user_id = message.chat.id
        user = str(user_id)
        db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
        sql = db.cursor()
        accmsg = '*👮 Пользователь : {}\n\n⚙️ Кошелёк : *`{}`*\n\n💸 Баланс : *`{}`* {}*'
        user_id = message.chat.id
        sql.execute("SELECT balance FROM users WHERE id = %s", [user])
        balance = sql.fetchone()[0]
        sql.execute("SELECT wallet FROM users WHERE id = %s", [user])
        wallet = sql.fetchone()[0]
        msg = accmsg.format(message.from_user.first_name, wallet, balance, TOKEN)
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    if message.text == '🙌🏻 Рефералы':
        ref_msg = "*⏯️ Всего приглашено : {} рефералов\n\n👥 Реферальная система:\n\n🥇 1 Реф - {} {}\n\n🔗 Ваша реферальная ссылка⬇️\n{}*"
        bot_name = bot.get_me().username
        user_id = message.chat.id
        user = str(user_id)
        db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
        sql = db.cursor()
        sql.execute("SELECT ref1 FROM users WHERE id = %s", [user])
        ref_count = sql.fetchone()[0]
        ref_link = 'https://telegram.me/{}?start={}'.format(
            bot_name, message.chat.id)
        msg = ref_msg.format(ref_count, per_ref, TOKEN, ref_link)
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    def trx_address(message):
        try:
            if message.text == "🚫 Отмена":
                return menu(message.chat.id)
            if len(message.text) > 8:
                db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
                sql = db.cursor()
                user_id = message.chat.id
                user = str(user_id)
                wallet = message.text
                sql.execute("UPDATE users SET wallet = %s WHERE id = %s", [wallet, user])
                sql.execute("SELECT wallet FROM users WHERE id = %s", [user])
                wal1 = sql.fetchone()[0]
                db.commit()

                bot.send_message(message.chat.id, "*💹Ваш кошелёк установлен, вы можете изменить в любой момент. " +
                                 wal1 + "*", parse_mode="Markdown")
                return menu(message.chat.id)
            else:
                bot.send_message(
                    message.chat.id, "*⚠️ Не валидный кошелёк!*", parse_mode="Markdown")
                return menu(message.chat.id)
        except:
            bot.send_message(message.chat.id,
                             "Эта команда имеет ошибку, пожалуйста, подождите, пока администратор не исправит ошибку.")
            bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: " + message.text)
            return
    if message.text == "⚙️ Кошелёк":
        user_id = message.chat.id
        user = str(user_id)
        markupp = types.InlineKeyboardMarkup()
        url_btnn = types.InlineKeyboardButton(text='Создать PAYEER', url='https://payeer.com/022241524')
        markupp.add(url_btnn)
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('🚫 Cancel')
        send = bot.send_message(message.chat.id, "*⚠️Введите ваш PAYEER кошелёк:*\n\n ",parse_mode="Markdown", reply_markup=keyboard)
        # Next message will call the name_handler function
        bot.register_next_step_handler(message, trx_address)


    if message.text == "📊 Информация":
        user_id = message.chat.id
        user = str(user_id)
        markupp = types.InlineKeyboardMarkup()
        url_bt = types.InlineKeyboardButton(text='Правила', url='https://telegra.ph/Pravila-Benzhi-razdayot-10-17')
        markupp.add(url_bt)
        msg = "Ꮋᴀɯ ᴛᴇᴧᴇᴦᴩᴀʍ ᴋᴀнᴀᴧ - https://t.me/primmer_spo\n\n Чᴛᴏбы нᴇ ʙᴄᴛᴩᴇᴛиᴛь ᴨᴩᴏбᴧᴇʍ нᴀ ᴨᴩᴏᴛяжᴇнии иᴄᴨᴏᴧьɜᴏʙᴀния бᴏᴛᴀ, ᴨᴏжᴀᴧуйᴄᴛᴀ ᴨᴩᴏчᴛиᴛᴇ ᴨᴩᴀʙиᴧᴀ.👇"
        bot.send_message(user, msg, reply_markup=markupp)
        return
    if message.text == "💻  Партнеры":
        user_id = message.chat.id
        user = str(user_id)
        bot.send_message(user,'◾️Обязательно читайте посты спонсоров ❗ \n\n -https://t.me/+El4BNXj0iUJiOWIy')
    def amo_with(message):
        try:
            user_id = message.chat.id
            amo = message.text
            user = str(user_id)
            db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
            sql = db.cursor()
            sql.execute("SELECT balance FROM users WHERE id = %s", [user])
            bal = sql.fetchone()[0]
            sql.execute("SELECT wallet FROM users WHERE id = %s", [user])
            wall = sql.fetchone()[0]
            if amo.isdigit() == False:
                bot.send_message(user_id, "_📛 Недопустимое значение. Введите только числовое значение._", parse_mode="Markdown")
                return
            if int(message.text) < Mini_Withdraw:
                bot.send_message(
                    user_id, f"_❌ Минимальный вывод {Mini_Withdraw} {TOKEN}_", parse_mode="Markdown")
                return
            if int(message.text) > bal:
                bot.send_message(
                    user_id, "_❌ Вы не можете вывести больше, чем ваш имеете на балансе._", parse_mode="Markdown")
                return
            amo = int(amo)
            ball = bal - int(amo)
            sql.execute("UPDATE users SET balance = %s WHERE id = %s", [ball, user])
            db.commit()
            bot.send_message(user_id, "✅ Вывод средств отправлен в обработку.")
            second = time.time()
            user_name = message.from_user.username
            userr = message.chat.id
            pay_id = 5371657093
            bot.send_message(pay_id, '✅#NEWPAY\n\n⭐ Сумма ' + '  I  ' + str(amo) + '  \n\nKошелек  ' + str(wall) + '   \n\nПользователь   ' + str(user_name) + '  \n\n ID пользователя   ' + str(userr) + '   \n\nBремя   ' + time.ctime(second))
        except:
            bot.send_message(message.chat.id,"Эта команда имеет ошибку, пожалуйста, подождите, пока администратор не исправит ошибку.")
            bot.send_message(OWNER_ID, "Your bot got an error fix it fast!\n Error on command: " + message.text)
            return

    if message.text == "💸 Вывод":
        user_id = message.chat.id
        user = str(user_id)

        db = psycopg2.connect(user="myitrkayvvovkm",
                              # пароль, который указали при установке PostgreSQL
                              password="4c652f79a1107d7d4752821bb86dc9a3e0369b8fb2f0c0f6e0429a9e57d0d3f5",
                              host="ec2-34-194-40-194.compute-1.amazonaws.com",
                              port="5432",
                              database="d823td4l4cq140")
        sql = db.cursor()
        sql.execute("SELECT balance FROM users WHERE id = %s", [user])
        bal = sql.fetchone()[0]
        sql.execute("SELECT wallet FROM users WHERE id = %s", [user])
        wall = sql.fetchone()[0]
        if wall == None:
            bot.send_message(user_id, "_❌ Кошелёк не установлен._",
                             parse_mode="Markdown")
            return
        if bal >= Mini_Withdraw:
            bot.send_message(user_id, "_Введите сумму:_",
                             parse_mode="Markdown")
            bot.register_next_step_handler(message, amo_with)
        else:
            bot.send_message(
                user_id,
                f"_❌Ваш баланс меньше минимальной суммы для вывода, у вас должно быть не менee {Mini_Withdraw} {TOKEN} на балансе._",
                parse_mode="Markdown")
            return

   except:
       bot.send_message(user, "Эта команда имеет ошибку, пожалуйста, подождите, пока администратор не исправит её.")
       bot.send_message(OWNER_ID, "Your bot got an error fix it fast!")
       return


if __name__ == '__main__':
    bot.polling(none_stop=True)
