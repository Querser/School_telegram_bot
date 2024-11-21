import telebot
import sqlite3


# Установление связь с телеграм ботом, через уникальный токен.
bot = telebot.TeleBot('')


def connectToDataBase():
    '''Соединение с базой данных.'''
    conn = sqlite3.connect('schoolTelegramBot.db')
    cursor = conn.cursor()

    return conn, cursor


def closeConnectionToDataBase(conn, cursor):
    '''Закрытие соединения с базой данных.'''
    cursor.close()
    conn.close()


def updateIdInDb(name_db):
    '''функция востанавливает порядок id'''
    conn, cursor = connectToDataBase()
    cursor.execute(f"SELECT id FROM {name_db};")
    result = cursor.fetchall()

    new_id = 1
    for row in result:
        old_id = row[0]
        if old_id != new_id:
            cursor.execute(f"UPDATE {name_db} SET id = ? WHERE id = ?;", (new_id, old_id))
        new_id += 1
    conn.commit()
    closeConnectionToDataBase(conn, cursor)


# Создание таблиц в базе данных schoolTelegramBot.db.
# conn, cursor = connectToDataBase()
#
# cursor.execute('CREATE TABLE students(id INTEGER PRIMARY KEY, class VARCHAR(30));')
#
# cursor.execute('CREATE TABLE day_of_the_week(id INTEGER PRIMARY KEY, name_day VARCHAR(15));')
#
# cursor.execute('CREATE TABLE lesson_schedule (id INTEGER PRIMARY KEY, class SMALLINT, week_day SMALLINT, lesson TEXT,'
#                'FOREIGN KEY(class) REFERENCES students(id), FOREIGN KEY(week_day) REFERENCES day_of_the_week(id));')
#
# cursor.execute('CREATE TABLE breakfast (id INTEGER PRIMARY KEY, class TEXT, week_day SMALLINT, dish TEXT,'
#                ' FOREIGN KEY(class) REFERENCES students(id), FOREIGN KEY(week_day) REFERENCES day_of_the_week(id));')
#
# cursor.execute('CREATE TABLE lunch (id INTEGER PRIMARY KEY, class TEXT, week_day SMALLINT, dish TEXT,'
#                'FOREIGN KEY(class) REFERENCES students(id), FOREIGN KEY(week_day) REFERENCES day_of_the_week(id));')
#
# cursor.execute('CREATE TABLE superuser (id INTEGER PRIMARY KEY, superuser_name VARCHAR(50));')
#
# cursor.execute('INSERT INTO day_of_the_week(name_day) VALUES("Понедельник");')
# cursor.execute('INSERT INTO day_of_the_week(name_day) VALUES("Вторник");')
# cursor.execute('INSERT INTO day_of_the_week(name_day) VALUES("Среда");')
# cursor.execute('INSERT INTO day_of_the_week(name_day) VALUES("Четверг");')
# cursor.execute('INSERT INTO day_of_the_week(name_day) VALUES("Пятница");')
# cursor.execute('INSERT INTO day_of_the_week(name_day) VALUES("Суббота");')
# cursor.execute('INSERT INTO day_of_the_week(name_day) VALUES("Воскресенье");')
# conn.commit()
# closeConnectionToDataBase(conn, cursor)
#
def lololo():
    conn, cursor = connectToDataBase()
    cursor.execute('SELECT * FROM students;')
    lol = cursor.fetchall()
    cursor.execute('SELECT * FROM lesson_schedule;')
    lol1 = cursor.fetchall()
    cursor.execute('SELECT * FROM breakfast;')
    lol2 = cursor.fetchall()
    cursor.execute('SELECT * FROM lunch;')
    lo3 = cursor.fetchall()
    cursor.execute('SELECT * FROM day_of_the_week;')
    lol4 = cursor.fetchall()
    cursor.execute('SELECT * FROM superuser;')
    lol5 = cursor.fetchall()
    print(lol, lol1, lol2, lo3, lol4, lol5)

# lololo()


def adminstart(message):
    '''Администрирование бота.'''
    try:
        markup = telebot.types.InlineKeyboardMarkup()

        button_admin_1 = telebot.types.InlineKeyboardButton('Посмотреть расписание урока', callback_data='See_class_schedule')
        # button_admin_2 = telebot.types.InlineKeyboardButton('Посмотреть меню завтрака', callback_data='See_breakfast_menu')
        # button_admin_3 = telebot.types.InlineKeyboardButton('Посмотреть меню обеда', callback_data='See_lunch_menu')
        button_admin_4 = telebot.types.InlineKeyboardButton('Администрировать', callback_data='Administer')

        markup.row(button_admin_1)
        # markup.row(button_admin_2, button_admin_3)
        markup.row(button_admin_4)

        bot.send_message(message.chat.id, 'Приветствую! Вы администратор. И вот что мы можете:', reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


def startmenu(message):
    '''Администрирование бота.'''
    try:
        markup = telebot.types.InlineKeyboardMarkup()

        button_admin_1 = telebot.types.InlineKeyboardButton('Посмотреть расписание урока', callback_data='See_class_schedule')
        # button_admin_2 = telebot.types.InlineKeyboardButton('Посмотреть меню завтрака', callback_data='See_breakfast_menu')
        # button_admin_3 = telebot.types.InlineKeyboardButton('Посмотреть меню обеда', callback_data='See_lunch_menu')

        markup.row(button_admin_1)
        # markup.row(button_admin_2, button_admin_3)

        bot.send_message(message.chat.id, 'Приветствую! Вы администратор. И вот что мы можете:', reply_markup=markup)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.callback_query_handler(func=lambda call: call.data == 'Administer')
def administer(call):
    '''Выбор действий.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)

        markup = telebot.types.InlineKeyboardMarkup()

        button_admin_1 = telebot.types.InlineKeyboardButton('Администрировать расписание уроков', callback_data='Administer_class_schedule')
        # button_admin_2 = telebot.types.InlineKeyboardButton('Администрировать меню завтраков', callback_data='Administer_breakfast_menu')
        # button_admin_3 = telebot.types.InlineKeyboardButton('Администрировать меню обедов', callback_data='Administer_lunch_menu')
        button_admin_4 = telebot.types.InlineKeyboardButton('Администрировать Классы', callback_data='Administer_class')
        button_admin_5 = telebot.types.InlineKeyboardButton('Админская панель', callback_data='Admin_add_del')
        button_back = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')

        markup.row(button_admin_1)
        # markup.row(button_admin_2)
        # markup.row(button_admin_3)
        markup.row(button_admin_4)
        markup.row(button_admin_5)
        markup.row(button_back)

        bot.send_message(call.message.chat.id, 'Выберите действие:', reply_markup=markup)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'Admin_add_del')
def AdminAdmin(call):
    '''Выбор действий для админов.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)

        markup = telebot.types.InlineKeyboardMarkup()
        button_admin_1 = telebot.types.InlineKeyboardButton('Добавить администратора', callback_data='Administer_add')
        button_admin_2 = telebot.types.InlineKeyboardButton('Удалить Администратора', callback_data='Administer_del')

        markup.row(button_admin_1)
        markup.row(button_admin_2)

        bot.send_message(call.message.chat.id, 'Выберите действие:', reply_markup=markup)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'Administer_add')
def addAdminCI(call):
    '''Сбор информации о админе.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите username человека, которого вы хотите добавить в команду администраторов.\n Пример: @admin')
        bot.register_next_step_handler(call.message, addAdmin)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


def addAdmin(message):
    '''Добавление администратора.'''
    try:
        name_new_superuser = message.text
        disverified_super_user_name = message.from_user.username
        conn, cursor = connectToDataBase()

        markup = telebot.types.InlineKeyboardMarkup()
        button_back = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button_back)

        cursor.execute('SELECT superuser_name FROM superuser WHERE superuser_name = ?;', (disverified_super_user_name,))
        verified_super_user_name = cursor.fetchone()

        if verified_super_user_name is None:
            return start(message)

        else:
            cursor.execute('INSERT INTO superuser(superuser_name) VALUES(?);', (name_new_superuser[1:],))
            bot.send_message(message.chat.id, f'Новый администратор: {name_new_superuser} успешно добавлен!', reply_markup=markup)

        conn.commit()
        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.callback_query_handler(func=lambda call: call.data == 'Administer_del')
def delAdminCI(call):
    '''Сбор информации о админе.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите username человека, которого вы хотите удалить из команду администраторов.\n Пример: @admin')
        bot.register_next_step_handler(call.message, delAdmin)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


def delAdmin(message):
    try:
        name_old_superuser = message.text
        disverified_super_user_name = message.from_user.username
        conn, cursor = connectToDataBase()

        markup = telebot.types.InlineKeyboardMarkup()
        button_back = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button_back)

        cursor.execute('SELECT superuser_name FROM superuser WHERE superuser_name = ?;', (disverified_super_user_name,))
        verified_super_user_name = cursor.fetchone()

        if verified_super_user_name is None:
            return start(message)

        else:
            cursor.execute('DELETE FROM superuser WHERE superuser_name = ?;', (name_old_superuser[1:],))
            bot.send_message(message.chat.id, f'Администратор: {name_old_superuser}, успешно удален!',
                             reply_markup=markup)

        conn.commit()
        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.callback_query_handler(func=lambda call: call.data == 'Administer_class')
def adminClass(call):
    '''Выбор действий для классов.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)

        markup = telebot.types.InlineKeyboardMarkup()

        button_admin_1 = telebot.types.InlineKeyboardButton('Добавить класс', callback_data='Add_class')
        button_admin_2 = telebot.types.InlineKeyboardButton('Удалить класс', callback_data='Delete_class')
        button_back = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')

        markup.row(button_admin_1)
        markup.row(button_admin_2)
        markup.row(button_back)

        bot.send_message(call.message.chat.id, 'Выберите:', reply_markup=markup)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)



@bot.callback_query_handler(func=lambda call: call.data == 'Add_class')
def addClassCI(call):
    '''Сбор данных о классе и дне недели.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите класс который вы хотите добавить.\n Пример: 9Г')
        bot.register_next_step_handler(call.message, Add_Class)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


def Add_Class(message):
    '''Добавление класса.'''
    try:
        conn, cursor = connectToDataBase()
        message_of_class = message.text
        message_of_class_upper = message_of_class.upper()

        cursor.execute('INSERT INTO students(class) VALUES(?);', (message_of_class_upper,))

        cursor.execute('SELECT class FROM students;')
        name_class = cursor.fetchall()

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(message.chat.id, f"Класс '{name_class[-1][-1]}' добавлен!", reply_markup=markup)

        conn.commit()


    except:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)

@bot.callback_query_handler(func=lambda call: call.data == 'Delete_class')
def deleteClassCI(call):
    '''Сбор данных о классе и дне недели.'''
    try:

        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Введите класс который вы хотите удалить.\n Пример: 9Г')
        bot.register_next_step_handler(call.message, Delete_Class)

    except:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


def Delete_Class(message):
    '''Удаление класса'''
    try:
        conn, cursor = connectToDataBase()
        message_of_class = message.text
        message_of_class_upper = message_of_class.upper()

        cursor.execute('DELETE FROM students WHERE class = ?;', (message_of_class_upper,))

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(message.chat.id, f"Класс '{message_of_class_upper}' удален!", reply_markup=markup)

        conn.commit()
        closeConnectionToDataBase(conn, cursor)
        updateIdInDb('students')

    except:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.callback_query_handler(func=lambda call: call.data.startswith('Back'))
def back(call):
    '''Обработчик кнопки Назад.'''
    bot.delete_message(call.message.chat.id, call.message.message_id)
    return start(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'Administer_class_schedule')
def administerClassSchedule(call):
    '''Управление расписанием.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)

        markup = telebot.types.InlineKeyboardMarkup()

        button_admin_1 = telebot.types.InlineKeyboardButton('Добавить расписание', callback_data='Add_schedule')
        button_admin_2 = telebot.types.InlineKeyboardButton('Удалить расписание', callback_data='Delete_schedule')
        button_back = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')

        markup.row(button_admin_1)
        markup.row(button_admin_2)
        markup.row(button_back)

        bot.send_message(call.message.chat.id, 'Выберите:', reply_markup=markup)

    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'Add_schedule')
def addScheduleCI(call):
    '''Сбор данных о классе и дне недели.'''
    try:

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(call.message.chat.id, 'Введите класс и день недели через запятые. Пример:\n 9Г, Понедельник',
                         reply_markup=markup)
        bot.register_next_step_handler(call.message, addScheduleCIL)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)

global message_class_week_day

def addScheduleCIL(message):
    '''Сбор данных о уроках.'''
    try:
        global message_class_week_day
        message_class_week_day = message.text

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(message.chat.id, 'Введите названия уроков через запятые. Пример:\n Русский язык, Математика, Физика',
                         reply_markup=markup)
        bot.register_next_step_handler(message, addSchedule)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


def addSchedule(message):
    '''Добавление рассписания'''
    try:
        message_lesson = message.text
        split_message_lesson = message_lesson.split(',')

        global message_class_week_day

        split_message_class_week_day = message_class_week_day.split(',')
        format_split_message_class_week_day = split_message_class_week_day[1].strip().capitalize()

        conn, cursor = connectToDataBase()

        cursor.execute('SELECT id FROM students WHERE class = ?;', (split_message_class_week_day[0],))
        id_class = cursor.fetchone()

        cursor.execute('SELECT id FROM day_of_the_week WHERE name_day = ?;', (format_split_message_class_week_day,))
        id_week_day = cursor.fetchone()

        for lesson in split_message_lesson:
            format_split_message_lesson = lesson.strip().capitalize()
            cursor.execute('INSERT INTO lesson_schedule(class, week_day, lesson) VALUES(?, ?, ?);',
                           (id_class[0], id_week_day[0], format_split_message_lesson))

        cursor.execute('SELECT lesson FROM lesson_schedule WHERE class = ? AND week_day = ?;',
                       (id_class[0], id_week_day[0]))
        lesson_schedule = cursor.fetchall()

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад',
                                                    callback_data='Back')
        markup.row(button)

        formatted_schedule = ', '.join([lesson[0] for lesson in lesson_schedule])

        bot.send_message(message.chat.id, f"{split_message_class_week_day[0]} - {format_split_message_class_week_day}. Уроки: {formatted_schedule}",
                                                    reply_markup=markup)
        conn.commit()
        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)

@bot.callback_query_handler(func=lambda call: call.data == 'Delete_schedule')
def deleteScheduleCI(call):
    '''Сбор данных о классе и дне недели.'''
    try:

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(call.message.chat.id, 'Введите класс и день недели через запятые. Пример:\n 9Г, Понедельник',
                         reply_markup=markup)
        bot.register_next_step_handler(call.message, deleteSchedule)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


def deleteSchedule(message):
    '''Удаление расписания.'''
    try:
        conn, cursor = connectToDataBase()

        class_week_day_message = message.text
        split_class_week_day_message = class_week_day_message.split(',')
        week_day = split_class_week_day_message[1].strip().capitalize()

        cursor.execute('SELECT id FROM students WHERE class = ?;', (split_class_week_day_message[0],))
        id_class = cursor.fetchone()

        cursor.execute('SELECT id FROM day_of_the_week WHERE name_day = ?;', (week_day,))
        id_week_day = cursor.fetchone()

        cursor.execute('DELETE FROM lesson_schedule WHERE class = ? AND week_day = ?;', (id_class[0], id_week_day[0]))

        conn.commit()

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(message.chat.id, f"Рассписание на {split_class_week_day_message[1]}"
                                          f" для {split_class_week_day_message[0]} успешно удалено!",
                         reply_markup=markup)

        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)

@bot.callback_query_handler(func=lambda call: call.data == 'Administer_breakfast_menu')
def administerBreakfastMenu(call):
    '''Управление меню завтрака.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)

        markup = telebot.types.InlineKeyboardMarkup()

        button_admin_1 = telebot.types.InlineKeyboardButton('Добавить меню завтрака', callback_data='Add_breakfast_menu')
        button_admin_2 = telebot.types.InlineKeyboardButton('Удалить меню завтрака', callback_data='Remove_breakfast_menu')
        button_back = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')

        markup.row(button_admin_1)
        markup.row(button_admin_2)
        markup.row(button_back)

        bot.send_message(call.message.chat.id, 'Выберите:', reply_markup=markup)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'Add_breakfast_menu')
def addBreakfastCI(call):
    '''Сбор данных о классе и дне недели.'''
    try:

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(call.message.chat.id, 'Введите класс и день недели через запятые. Пример:\n 9Г, Понедельник',
                         reply_markup=markup)
        bot.register_next_step_handler(call.message, addbreakfastCIL)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)

global class_week_day_breakfast

def addbreakfastCIL(message):
    '''Сбор данных о завтраке.'''
    try:
        global class_week_day_breakfast
        class_week_day_breakfast = message.text

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(message.chat.id, 'Введите названия блюда через запятые. Пример:\n Овсянка',
                         reply_markup=markup)
        bot.register_next_step_handler(message, addBreakfast)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


def addBreakfast(message):
    '''Добавление меню завтрака'''
    try:
        message_breakfast = message.text
        split_message_breakfast = message_breakfast.split(',')

        global class_week_day_breakfast

        split_message_class_week_day = class_week_day_breakfast.split(',')
        format_split_message_class_week_day = split_message_class_week_day[1].strip().capitalize()

        conn, cursor = connectToDataBase()

        cursor.execute('SELECT id FROM students WHERE class = ?;', (split_message_class_week_day[0],))
        id_class = cursor.fetchone()

        cursor.execute('SELECT id FROM day_of_the_week WHERE name_day = ?;', (format_split_message_class_week_day,))
        id_week_day = cursor.fetchone()

        for breakfast in split_message_breakfast:
            format_split_message_breakfast = breakfast.strip().capitalize()
            cursor.execute('INSERT INTO breakfast(class, week_day, dish) VALUES(?, ?, ?);',
                           (id_class[0], id_week_day[0], format_split_message_breakfast))

        cursor.execute('SELECT dish FROM breakfast WHERE class = ? AND week_day = ?;',
                       (id_class[0], id_week_day[0]))
        breakfast_menu = cursor.fetchall()

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад',
                                                    callback_data='Back')
        markup.row(button)

        formatted_breakfast = ', '.join([lesson[0] for lesson in breakfast_menu])

        bot.send_message(message.chat.id, f"{split_message_class_week_day[0]} - {format_split_message_class_week_day}. Завтрак: {formatted_breakfast}",
                                                    reply_markup=markup)
        conn.commit()
        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.callback_query_handler(func=lambda call: call.data == 'Remove_breakfast_menu')
def deleteBreakfastCI(call):
    '''Сбор данных о классе и дне недели.'''
    try:

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(call.message.chat.id, 'Введите класс и день недели через запятые. Пример:\n 9Г, Понедельник',
                         reply_markup=markup)
        bot.register_next_step_handler(call.message, deleteBreakfast)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


def deleteBreakfast(message):
    '''Удаление меню завтрака.'''
    try:
        conn, cursor = connectToDataBase()

        class_week_day_message = message.text
        split_class_week_day_message = class_week_day_message.split(',')
        week_day = split_class_week_day_message[1].strip().capitalize()

        cursor.execute('SELECT id FROM students WHERE class = ?;', (split_class_week_day_message[0],))
        id_class = cursor.fetchone()

        cursor.execute('SELECT id FROM day_of_the_week WHERE name_day = ?;', (week_day,))
        id_week_day = cursor.fetchone()

        cursor.execute('DELETE FROM Breakfast WHERE class = ? AND week_day = ?;', (id_class[0], id_week_day[0]))

        conn.commit()

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(message.chat.id, f"Меню завтрака на {split_class_week_day_message[1]}"
                                          f" для {split_class_week_day_message[0]} успешно удалено!",
                         reply_markup=markup)

        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.callback_query_handler(func=lambda call: call.data == 'Administer_lunch_menu')
def administerLunchMenu(call):
    '''Управление меню обеда.'''
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)

        markup = telebot.types.InlineKeyboardMarkup()

        button_admin_1 = telebot.types.InlineKeyboardButton('Добавить меню обеда', callback_data='Add_lunch_menu')
        button_admin_2 = telebot.types.InlineKeyboardButton('Удалить меню обеда', callback_data='Remove_lunch_menu')
        button_back = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')

        markup.row(button_admin_1)
        markup.row(button_admin_2)
        markup.row(button_back)

        bot.send_message(call.message.chat.id, 'Выберите:', reply_markup=markup)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'Add_lunch_menu')
def addlunchCI(call):
    '''Сбор данных о классе и дне недели.'''
    try:

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(call.message.chat.id, 'Введите класс и день недели через запятые. Пример:\n 9Г, Понедельник',
                         reply_markup=markup)
        bot.register_next_step_handler(call.message, addlunchCIL)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)

global class_week_day_lunch

def addlunchCIL(message):
    '''Сбор данных меню обеда.'''
    try:
        global class_week_day_lunch
        class_week_day_lunch = message.text

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(message.chat.id, 'Введите названия блюда через запятые. Пример:\n Овощное рагу',
                         reply_markup=markup)
        bot.register_next_step_handler(message, addlunch)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


def addlunch(message):
    '''Добавление обедаю'''
    try:
        message_lunch = message.text
        split_message_lunch= message_lunch.split(',')

        global class_week_day_lunch

        split_message_class_week_day = class_week_day_lunch.split(',')
        format_split_message_class_week_day = split_message_class_week_day[1].strip().capitalize()

        conn, cursor = connectToDataBase()

        cursor.execute('SELECT id FROM students WHERE class = ?;', (split_message_class_week_day[0],))
        id_class = cursor.fetchone()

        cursor.execute('SELECT id FROM day_of_the_week WHERE name_day = ?;', (format_split_message_class_week_day,))
        id_week_day = cursor.fetchone()

        for lunch in split_message_lunch:
            format_split_message_lunch = lunch.strip().capitalize()
            cursor.execute('INSERT INTO breakfast(class, week_day, dish) VALUES(?, ?, ?);',
                           (id_class[0], id_week_day[0], format_split_message_lunch))

        cursor.execute('SELECT dish FROM breakfast WHERE class = ? AND week_day = ?;',
                       (id_class[0], id_week_day[0]))
        lunch_menu = cursor.fetchall()

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад',
                                                    callback_data='Back')
        markup.row(button)

        formatted_lunch = ', '.join([lesson[0] for lesson in lunch_menu])

        bot.send_message(message.chat.id, f"{split_message_class_week_day[0]} - {format_split_message_class_week_day}. На обед: {formatted_lunch}",
                                                    reply_markup=markup)
        conn.commit()
        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.callback_query_handler(func=lambda call: call.data == 'Remove_lunch_menu')
def deletelunchCI(call):
    '''Сбор данных о классе и дне недели.'''
    try:

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(call.message.chat.id, 'Введите класс и день недели через запятые. Пример:\n 9Г, Понедельник',
                         reply_markup=markup)
        bot.register_next_step_handler(call.message, deletelunch)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(call.message)


def deletelunch(message):
    '''Удаление меню обеда.'''
    try:
        conn, cursor = connectToDataBase()

        class_week_day_message = message.text
        split_class_week_day_message = class_week_day_message.split(',')
        week_day = split_class_week_day_message[1].strip().capitalize()

        cursor.execute('SELECT id FROM students WHERE class = ?;', (split_class_week_day_message[0],))
        id_class = cursor.fetchone()

        cursor.execute('SELECT id FROM day_of_the_week WHERE name_day = ?;', (week_day,))
        id_week_day = cursor.fetchone()

        cursor.execute('DELETE FROM Breakfast WHERE class = ? AND week_day = ?;', (id_class[0], id_week_day[0]))

        conn.commit()

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        bot.send_message(message.chat.id, f"Меню обеда на {split_class_week_day_message[1]}"
                                          f" для {split_class_week_day_message[0]} успешно удалено!",
                         reply_markup=markup)

        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.callback_query_handler(func=lambda call: call.data == 'See_class_schedule')
def collectionInformationLessonSchedule(call):
    '''Сбор данных о классе.'''
    try:
        # Удаляем сообщение, используя call.message
        bot.delete_message(call.message.chat.id, call.message.message_id)

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        # Проверка для администратора или пользователя
        disverified_super_user_name = call.from_user.username

        if disverified_super_user_name is None:
            bot.send_message(call.message.chat.id, "У вас нет username. Установите его в настройках Telegram.")
            return

        conn, cursor = connectToDataBase()

        cursor.execute('SELECT superuser_name FROM superuser WHERE superuser_name = ?;', (disverified_super_user_name,))
        verified_super_user_name = cursor.fetchone()

        if verified_super_user_name is not None:
            checkLessonSchedule(call.message, is_admin=True)
        else:
            bot.send_message(call.message.chat.id, 'Введите класс, расписание которого вы хотите увидеть. \nПример: 9Г',
                             reply_markup=markup)
            bot.register_next_step_handler(call.message, lambda msg: checkLessonSchedule(msg, is_admin=False))
    except Exception as e:
        bot.send_message(call.message.chat.id, f"Произошла ошибка: {e}. Попробуйте еще раз.")
        return start(call.message)


def checkLessonSchedule(message, is_admin=False):
    '''Показ расписания.'''
    try:
        class_message = message.text if not is_admin else None
        conn, cursor = connectToDataBase()
        message_text = ""

        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton('Назад', callback_data='Back')
        markup.row(button)

        if is_admin:
            cursor.execute('''
                SELECT lesson, students.class, day_of_the_week.name_day
                FROM lesson_schedule
                JOIN students ON students.id = lesson_schedule.class
                JOIN day_of_the_week ON day_of_the_week.id = lesson_schedule.week_day;
            ''')
            vip_lesson_schedule = cursor.fetchall()

            # Формируем расписание для каждого уникального класса и дня недели
            classes_schedule = {}
            for lesson, cls, day in vip_lesson_schedule:
                classes_schedule.setdefault(cls, {}).setdefault(day, []).append(lesson)

            for cls, days in classes_schedule.items():
                message_text += f"\nРасписание для класса {cls}:\n"
                for day, lessons in days.items():
                    lesson_list = ', '.join(lessons)
                    message_text += f"{day}: {lesson_list}\n"

        else:
            cursor.execute('''
                SELECT lesson, day_of_the_week.name_day
                FROM lesson_schedule
                JOIN students ON students.id = lesson_schedule.class
                JOIN day_of_the_week ON day_of_the_week.id = lesson_schedule.week_day
                WHERE students.class = ?;
            ''', (class_message,))
            lesson_schedule = cursor.fetchall()

            if lesson_schedule:
                message_text += f"Расписание для класса {class_message}:\n"
                days_schedule = {}
                for lesson, day in lesson_schedule:
                    days_schedule.setdefault(day, []).append(lesson)

                for day, lessons in days_schedule.items():
                    lesson_list = ', '.join(lessons)
                    message_text += f"{day}: {lesson_list}\n"
            else:
                message_text = f"Расписание для класса {class_message} не найдено."

        # Отправляем всё расписание одним сообщением
        bot.send_message(message.chat.id, message_text.strip(), reply_markup=markup)
        closeConnectionToDataBase(conn, cursor)
    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


@bot.message_handler(commands=['start'])
def start(message):
    '''Обработчик команды старт.'''
    try:
        disverified_super_user_name = message.from_user.username
        conn, cursor = connectToDataBase()

        cursor.execute('SELECT superuser_name FROM superuser WHERE superuser_name = ?;', (disverified_super_user_name,))
        verified_super_user_name = cursor.fetchone()

        if verified_super_user_name is not None:
            adminstart(message)
        else:
            startmenu(message)

    except Exception as e:
        bot.send_message(message.chat.id, f"Попробуйте еще раз! Произошла ошибка! Пожалуйста следуйте инструкции!")
        return start(message)


# Запуск бота
bot.polling(non_stop=True)