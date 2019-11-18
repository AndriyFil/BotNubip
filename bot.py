import types

import telebot
import json

token = '1034555998:AAGAhwDB8WG0GrTFK5QYG7v0YGaXnE8nBd4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start')
    user_markup.row('⏰Графік пар', '📅Розклад пар')
    user_markup.row('📅Графік навчального процесу 2019-2020','🏨Гуртожиток')
    user_markup.row('💻Все для програміста', '💲Де підзаробити на вихідних?')
    user_markup.row('📜Вся інформація про викладачів', '💸Стипендія')
    user_markup.row('🚘Отримати водійське посвідчення', '➕Як отримати додаткові бали?')
    user_markup.row('💸Оплата за навчання', '☎Контакти НУБіП')
    user_markup.row('⭐Студентська рада НУБіП', '👥Студентська організація')
    user_markup.row('🎫Де взяти проїздні?', '💰Благодійний фонд НУБіП')
    user_markup.row('🆕Новини НУБіП','🏃Новини спорту')
    user_markup.row('☎Контакти деканату', '🇺🇦🇮🇩Як отримати подвійний диплом?🇩🇪🇯🇵')
    user_markup.row('🎧Що послухати?','🌐Elearn')
    user_markup.row('🤖Оцінити роботу бота')
    bot.send_message(message.from_user.id,
                     '😎 Що тебе цікавить?👇\n',
                     reply_markup=user_markup)

    # bot.send_message(message.chat.id, 'Привіт чим можу тобі допомогти❓\n➖➖➖➖➖➖➖➖➖➖➖\n' + help)


@bot.message_handler(commands=['stop'])
def start_message(message):
    hide_markup = telebot.types.ReplyKeyboardHide()
    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)


# @bot.message_handler(content_types=['text'])
# def get_func(message):  # получаем фамилию
#     if message.text == '💸Стипендія':
#         bot.send_message(message.from_user.id, "1⃣ Звичайна\n2⃣ Соціальна\nПриклад:(1,2)");
#         bot.register_next_step_handler(message, get_doc);
#
#
# def get_doc(message):
#     if message.text == '1':
#         audio = open('stip.pdf', 'rb')
#         bot.send_document(message.chat.id, audio)
#         bot.register_next_step_handler(message, get_doc);
#     elif message.text == '2':
#         audio = open('socstip.pdf', 'rb')
#         bot.send_document(message.chat.id, audio)
#         bot.register_next_step_handler(message, get_doc);
#
#
# def get_audio(message):
#     if message.text == 'Лох':
#         audio = open('nubip.mp3', 'rb')
#         bot.send_audio(message.chat.id, audio)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '💸Стипендія':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text='Академічна стипендія', callback_data='Док1'))
        keyboard.add(telebot.types.InlineKeyboardButton(text='Соціальна стипендія', callback_data='Док2'))
        bot.send_message(message.chat.id,
                         "💸 Перелік нормативних актів, які визначають порядок\n призначення стипендії у 2018-2019 н.р.",
                         reply_markup=keyboard)
    elif message.text == '📅Графік навчального процесу 2019-2020':
        img = 'https://imbt.ga/Vf2K8kt86O'
        bot.send_message(message.chat.id, f'{img}')
    elif message.text == '💸Оплата за навчання':
        text = '👉 2019-2020'
        img = 'https://imbt.ga/yO98EAacau'
        bot.send_message(message.chat.id, f'{text}\n{img}')
    elif message.text == '🚘Отримати водійське посвідчення':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text='Менше 16 років', callback_data='12'))
        keyboard.add(telebot.types.InlineKeyboardButton(text='16-17 років', callback_data='16'))
        keyboard.add(telebot.types.InlineKeyboardButton(text='Більше 18 років', callback_data='18'))
        bot.send_message(message.chat.id, "👮 Скільки тобі років?", reply_markup=keyboard)
    elif message.text == '🎧Що послухати?':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text='🎤Pop', callback_data='pop'))
        keyboard.add(telebot.types.InlineKeyboardButton(text='🎸Rock', callback_data='rock'))
        keyboard.add(telebot.types.InlineKeyboardButton(text='🎻Класика', callback_data='classic'))
        keyboard.add(telebot.types.InlineKeyboardButton(text='🔥Популярні', callback_data='top'))
        keyboard.add(telebot.types.InlineKeyboardButton(text='👑Гімн НУБіП', callback_data='gimn'))
        bot.send_message(message.chat.id, "🎶 Обери свій жанр", reply_markup=keyboard)
    elif message.text == '➕Як отримати додаткові бали?':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text='Завантажити', callback_data='dopbal'))
        bot.send_message(message.chat.id,
                         "👯 Участь у діяльності органів студентського\n самоврядування та соціальної роботи",
                         reply_markup=keyboard)
    elif message.text == '⏰Графік пар':
        img = 'https://imbt.ga/9exMCNnpZy'
        bot.send_message(message.chat.id, f'{img}')
        bot.register_next_step_handler(message, start);
    elif message.text == '💲Де підзаробити на вихідних?':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://t.me/work4students")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Список пропозицій💲", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '💰Благодійний фонд НУБіП':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://nubip.edu.ua/node/14249")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "📜Інформація про благодійний фонд", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '🌐Elearn':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://elearn.nubip.edu.ua/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "🎓 Навчальний портал НУБіП", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '🏨Гуртожиток':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Студентська рада гуртожитків",
                                                        url="https://nubip.edu.ua/node/26023")
        keyboard.add(url_button)
        url_button = telebot.types.InlineKeyboardButton(text="Інформація про гуртожитки",
                                                        url="https://nubip.edu.ua/node/13260")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "📜Вся інформація про гуртожиткі", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '🇺🇦🇮🇩Як отримати подвійний диплом?🇩🇪🇯🇵':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://nubip.edu.ua/node/31610")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "🎓Освіта за програмами подвійних дипломів", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '☎Контакти НУБіП':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://nubip.edu.ua/node/73")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "📋Контактна інформація НУБіП", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '🤖Оцінити роботу бота':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://forms.gle/pBBdowvMsEm5T1rY7")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "📝Пройдіть будь-ласка опитування для покращення роботи",
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '⭐Студентська рада НУБіП':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://nubip.edu.ua/node/26023")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "📋Все про студентську раду НУБіП", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '🎫Де взяти проїздні?':

        bot.send_message(message.chat.id, "Зверніться до голови профкому ФІТ\n🙎 Валерія Киба @valeriia_kyba")
        bot.register_next_step_handler(message, start);

    elif message.text == '☎Контакти деканату':

        bot.send_message(message.chat.id, "🙎 Оборська Інна Сергіївна\n\n📞 +380633285201 ")
        bot.register_next_step_handler(message, start);
    elif message.text == '🏃Новини спорту':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://nubip.edu.ua/node/69")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "📜Всі новини спорту", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '👥Студентська організація':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://nubip.edu.ua/node/1302")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "📋Все про студентську організацію", reply_markup=keyboard)
        bot.register_next_step_handler(message, start);
    elif message.text == '📅Розклад пар':
        bot.send_message(message.from_user.id, "Спеціальність❓\n Приклад:(ЕКК, КН, ІПЗ, КБ, КІ)");
        bot.register_next_step_handler(message, get_spec);
    elif message.text == '📜Вся інформація про викладачів':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти", url="https://nubip.edu.ua/node/9989")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Для перегляду інформації", reply_markup=keyboard)
    elif message.text == '💻Все для програміста':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Рейтинг IТ-книг 2019",
                                                        url="https://telegra.ph/Rejting-IT-knig-2019-11-11")
        keyboard.add(url_button)
        url_button = telebot.types.InlineKeyboardButton(text="Рейтинг мов програмування 2019",
                                                        url="https://telegra.ph/Rejting-mov-programuvannya-2019-11-11")
        keyboard.add(url_button)
        url_button = telebot.types.InlineKeyboardButton(text="Портрет ІТ-спеціаліста - 2019",
                                                        url="https://telegra.ph/Portret-%D0%86T-spec%D1%96al%D1%96sta--2019-%D0%86nfograf%D1%96ka-11-11")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Що потрібно програмісту в 2019🔥", reply_markup=keyboard)
    elif message.text == '🆕Новини НУБіП':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Дотримання правил проживання в гуртожитку",
                                                        url="https://telegra.ph/Dotrimannya-pravil-prozhivannya-v-gurtozhitku--zaporuka-komfortnogo-prozhivannya-us%D1%96h-meshkanc%D1%96v-11-18")
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="День відкритих дверей в НУБІП",
                                                        url="https://telegra.ph/Den-v%D1%96dkritih-dverej-v-NUB%D0%86P-11-18")
        keyboard.add(url_button)
        url_button = telebot.types.InlineKeyboardButton(
            text="Науковий гурток «Основи наукових досліджень в агробізнесі»",
            url="https://telegra.ph/U-naukovomu-gurtku-Osnovi-naukovih-dosl%D1%96dzhen-v-agrob%D1%96znes%D1%96-p%D1%96dgotovleno-peremozhnicyu-konkursu-studentskih-naukovih-statej-YOUN-11-18")
        keyboard.add(url_button)
        url_button = telebot.types.InlineKeyboardButton(text="Стартап-школа НУБіП",
                                                        url="https://telegra.ph/Startap-shkola-NUB%D1%96P-Ukraini-ogoloshuye-tret%D1%96j-nab%D1%96r-11-18")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "🔥 Актуальні новини НУБіП", reply_markup=keyboard)


    else:
        bot.send_message(message.from_user.id, 'ℹВивести список команд: /start');


def get_doc(message):
    if message.text == '1':
        audio = open('stip.pdf', 'rb')
        bot.send_document(message.chat.id, audio)
        bot.register_next_step_handler(message, get_doc);
    # elif message.text == '2':
    #     audio = open('socstip.pdf', 'rb')
    #     bot.send_document(message.chat.id, audio)
    #     bot.register_next_step_handler(message, get_doc);


def get_spec(message):  # получаем фамилию
    if message.text == 'ЕКК':
        bot.send_message(message.from_user.id, "День та курс❓\nПриклад:(Вт 1к)");
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'КН':
        bot.send_message(message.from_user.id, "День та курс❓\nПриклад:(Вт 1к)");
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'ІПЗ':
        bot.send_message(message.from_user.id, "День та курс❓\nПриклад:(Вт 1к)");
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'КБ':
        bot.send_message(message.from_user.id, "День та курс❓\nПриклад:(Вт 1к)");
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'КІ':
        bot.send_message(message.from_user.id, "День та курс❓\nПриклад:(Вт 1к)");
        bot.register_next_step_handler(message, get_ki);
    else:
        bot.send_message(message.from_user.id, '🆘 Не розумію\n Приклад:(ЕКК, КН, ІПЗ, КБ, КІ)\n\n🔚 Для виходу натисніть ще раз на нове питання');


def get_ipz(message):  # 1 курс
    if message.text == 'Пн 1к':
        text = '👉 Розклад пар ІПЗ 1 курс'
        img = 'https://imbt.ga/UwBteboRvY'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Вт 1к':
        text = '👉 Розклад пар ІПЗ 1 курс'
        img = 'https://imbt.ga/oELLs39Y21'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Ср 1к':
        text = '👉 Розклад пар ІПЗ 1 курс'
        img = 'https://imbt.ga/HQ3UaqmdbL'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Чт 1к':
        text = '👉 Розклад пар ІПЗ 1 курс'
        img = 'https://imbt.ga/jWQf6Y29f6'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Пт 1к':
        text = '👉 Розклад пар ІПЗ 1 курс'
        img = 'https://imbt.ga/MJQszzmxmH'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);

    # 2

    elif message.text == 'Пн 2к':
        text = '👉 Розклад пар ІПЗ 2 курс'
        img = 'https://imbt.ga/v9ojjMdguA'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Вт 2к':
        text = '👉 Розклад пар ІПЗ 2 курс'
        img = 'https://imbt.ga/3UgdBpSy8s'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Ср 2к':
        text = '👉 Розклад пар ІПЗ 2 курс'
        img = 'https://imbt.ga/qDK2QvbxIe'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Чт 2к':
        text = '👉 Розклад пар ІПЗ 2 курс'
        img = 'https://imbt.ga/5Y7xM7v7xM'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Пт 2к':
        text = '👉 Розклад пар ІПЗ 2 курс'
        img = 'https://imbt.ga/bz2FMnu4Qe'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);

    # 3курс

    elif message.text == 'Пн 3к':
        text = '👉 Розклад пар ІПЗ 3 курс'
        img = 'https://imbt.ga/eOYOkKORif'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Вт 3к':
        text = '👉 Розклад пар ІПЗ 3 курс'
        img = 'https://imbt.ga/hcqLxnNgdx'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Ср 3к':
        text = '👉 Розклад пар ІПЗ 3 курс'
        img = 'https://imbt.ga/6H6RlYdsrw'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Чт 3к':
        text = '👉 Розклад пар ІПЗ 3 курс'
        img = 'https://imbt.ga/RGSxJpMscM'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Пт 3к':
        text = '👉 Розклад пар ІПЗ 3 курс'
        img = 'https://imbt.ga/eXGJWIdLTa'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    # 4курс

    elif message.text == 'Пн 4к':
        text = '👉 Розклад пар ІПЗ 4 курс'
        img = 'https://imbt.ga/bMcDpvXCfa'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Вт 4к':
        text = '👉 Розклад пар ІПЗ 4 курс'
        img = 'https://imbt.ga/S3BqHmtd9q'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Ср 4к':
        text = '👉 Розклад пар ІПЗ 4 курс'
        img = 'https://imbt.ga/fcFd0KSoPi'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Чт 4к':
        text = '👉 Розклад пар ІПЗ 4 курс'
        img = 'https://imbt.ga/ibF5RYEtm8'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    elif message.text == 'Пт 4к':
        text = '👉 Розклад пар ІПЗ 4 курс'
        img = 'https://imbt.ga/pd2i245muT'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ipz);
    else:
        bot.send_message(message.from_user.id, '🆘Не розумію\nПриклад:(Вт 1к)');


# KI
def get_ki(message):  # 1 курс
    if message.text == 'Пн 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/Zz0GrgK98Y'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);
    elif message.text == 'Вт 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/jM1TFapNvu'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);
    elif message.text == 'Ср 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/TrmJIR3cHo'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Чт 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/EYsx5zbOKR'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Пт 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/uZEc6BglSD'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);


    # 2

    elif message.text == 'Пн 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/3Jysm3MaXZ'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Вт 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/jod2ibefMZ'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Ср 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/nrA1swZX5c'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Чт 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/4RTEzEMcm1'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Пт 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/ZxbfS9NCgE'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);


    # 3курс

    elif message.text == 'Пн 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/meLw9vrDxe'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Вт 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/zi1dJiHQRH'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Ср 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/PBmASfzRVu'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Чт 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/LHl4Z1GMoQ'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Пт 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/yRyGjWMxFA'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);


    # 4курс

    elif message.text == 'Пн 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/2pI2qan5Em'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Вт 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/jhGAUOfooA'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Ср 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/zcpl7GTWvO'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Чт 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/MlWIfijNey'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    elif message.text == 'Пт 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/N3gWlNgThd'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ki);

    else:
        bot.send_message(message.from_user.id, '🆘Не розумію\nПриклад:(Вт 1к)');


# KН
def get_kn(message):  # 1 курс
    if message.text == 'Пн 1к':
        text = '👉 Розклад пар КH 1 курс'
        img = 'https://imbt.ga/Ke9Gz4yMvN'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Вт 1к':
        text = '👉 Розклад пар КH 1 курс'
        img = 'https://imbt.ga/PtTtiOVHNL'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Ср 1к':
        text = '👉 Розклад пар КH 1 курс'
        img = 'https://imbt.ga/X9OLu8LkTn'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Чт 1к':
        text = '👉 Розклад пар КH 1 курс'
        img = 'https://imbt.ga/2DHGAM70Tg'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Пт 1к':
        text = '👉 Розклад пар КH 1 курс'
        img = 'https://imbt.ga/ePDflktRmQ'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);

    # 2

    elif message.text == 'Пн 2к':
        text = '👉 Розклад пар КH 2 курс'
        img = 'https://imbt.ga/PdahLicOum'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Вт 2к':
        text = '👉 Розклад пар КH 2 курс'
        img = 'https://imbt.ga/3fyLhpGP4D'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Ср 2к':
        text = '👉 Розклад пар КH 2 курс'
        img = 'https://imbt.ga/8cWMsuF997'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Чт 2к':
        text = '👉 Розклад пар КH 2 курс'
        img = 'https://imbt.ga/mHWebVwxma'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Пт 2к':
        text = '👉 Розклад пар КH 2 курс'
        img = 'https://imbt.ga/wdgFsHc6gg'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);

    # 3курс

    elif message.text == 'Пн 3к':
        text = '👉 Розклад пар КH 3 курс'
        img = 'https://imbt.ga/H6NI0pYXZ9'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Вт 3к':
        text = '👉 Розклад пар КH 3 курс'
        img = 'https://imbt.ga/0MJJhyUf5m'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Ср 3к':
        text = '👉 Розклад пар КH 3 курс'
        img = 'https://imbt.ga/MmBLM8UpPd'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Чт 3к':
        text = '👉 Розклад пар КH 3 курс'
        img = 'https://imbt.ga/nSVSeG5eIk'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Пт 3к':
        text = '👉 Розклад пар КH 3 курс'
        img = 'https://imbt.ga/0gLVMTURZb'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);

    # 4курс

    elif message.text == 'Пн 4к':
        text = '👉 Розклад пар КH 4 курс'
        img = 'https://imbt.ga/XQBouMvnbI'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Вт 4к':
        text = '👉 Розклад пар КH 4 курс'
        img = 'https://imbt.ga/hC9VuuP7dC'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Ср 4к':
        text = '👉 Розклад пар КH 4 курс'
        img = 'https://imbt.ga/7VR01H0Fni'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Чт 4к':
        text = '👉 Розклад пар КH 4 курс'
        img = 'https://imbt.ga/WwYKcy67eX'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    elif message.text == 'Пт 4к':
        text = '👉 Розклад пар КH 4 курс'
        img = 'https://imbt.ga/idhFFAk0ee'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kn);
    else:
        bot.send_message(message.from_user.id, '🆘Не розумію\nПриклад:(Вт 1к)');


# EKK
def get_ekk(message):  # 1 курс
    if message.text == 'Пн 1к':
        text = '👉 Розклад пар ЕКК 1 курс'
        img = 'https://imbt.ga/mieEBdMKi8'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Вт 1к':
        text = '👉 Розклад пар ЕКК 1 курс'
        img = 'https://imbt.ga/RhSHopfdp4'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Ср 1к':
        text = '👉 Розклад пар ЕКК 1 курс'
        img = 'https://imbt.ga/C8tFX0KNiC'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Чт 1к':
        text = '👉 Розклад пар ЕКК 1 курс'
        img = 'https://imbt.ga/4yQ4P1uZag'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Пт 1к':
        text = '👉 Розклад пар ЕКК 1 курс'
        img = 'https://imbt.ga/v4MiOHVe5P'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);

    # 2

    elif message.text == 'Пн 2к':
        text = '👉 Розклад пар EKK 2 курс'
        img = 'https://imbt.ga/IHXJmxz1r7'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Вт 2к':
        text = '👉 Розклад пар EKK 2 курс'
        img = 'https://imbt.ga/xpaPNLfYFL'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Ср 2к':
        text = '👉 Розклад пар EKK 2 курс'
        img = 'https://imbt.ga/XHukWZieCp'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Чт 2к':
        text = '👉 Розклад пар EKK 2 курс'
        img = 'https://imbt.ga/yPrapQr62U'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Пт 2к':
        text = '👉 Розклад пар EKK 2 курс'
        img = 'https://imbt.ga/TwlPtGXltq'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);

    # 3курс

    elif message.text == 'Пн 3к':
        text = '👉 Розклад пар EKK 3 курс'
        img = 'https://imbt.ga/9h3ztUuM9x'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Вт 3к':
        text = '👉 Розклад пар EKK 3 курс'
        img = 'https://imbt.ga/vAFcOEmwaw'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Ср 3к':
        text = '👉 Розклад пар EKK 3 курс'
        img = 'https://imbt.ga/4pnToMn7YK'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Чт 3к':
        text = '👉 Розклад пар EKK 3 курс'
        img = 'https://imbt.ga/Ny6XfTcwaE'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Пт 3к':
        text = '👉 Розклад пар EKK 3 курс'
        img = 'https://imbt.ga/1odT8k3C0E'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);

    # 4курс

    elif message.text == 'Пн 4к':
        text = '👉 Розклад пар EKK 4 курс'
        img = 'https://imbt.ga/jzURq3qp6y'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Вт 4к':
        text = '👉 Розклад пар EKK 4 курс'
        img = 'https://imbt.ga/8MBwczJiWh'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Ср 4к':
        text = '👉 Розклад пар EKK 4 курс'
        img = 'https://imbt.ga/IbdJ43WpUe'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Чт 4к':
        text = '👉 Розклад пар EKK 4 курс'
        img = 'https://imbt.ga/pMogx5jJSf'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    elif message.text == 'Пт 4к':
        text = '👉 Розклад пар EKK 4 курс'
        img = 'https://imbt.ga/1jXTAKiRFB'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_ekk);
    else:
        bot.send_message(message.from_user.id, '🆘Не розумію\nПриклад:(Вт 1к)');


# Kібер безпека
def get_kb(message):  # 1 курс
    if message.text == 'Пн 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/Zz0GrgK98Y'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Вт 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/jM1TFapNvu'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Ср 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/TrmJIR3cHo'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Чт 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/EYsx5zbOKR'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Пт 1к':
        text = '👉 Розклад пар КІ 1 курс'
        img = 'https://imbt.ga/uZEc6BglSD'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);

    # 2

    elif message.text == 'Пн 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/3Jysm3MaXZ'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Вт 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/jod2ibefMZ'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Ср 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/nrA1swZX5c'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Чт 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/4RTEzEMcm1'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Пт 2к':
        text = '👉 Розклад пар КІ 2 курс'
        img = 'https://imbt.ga/ZxbfS9NCgE'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);

    # 3курс

    elif message.text == 'Пн 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/meLw9vrDxe'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Вт 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/zi1dJiHQRH'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Ср 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/PBmASfzRVu'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Чт 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/LHl4Z1GMoQ'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Пт 3к':
        text = '👉 Розклад пар КІ 3 курс'
        img = 'https://imbt.ga/yRyGjWMxFA'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);

    # 4курс

    elif message.text == 'Пн 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/2pI2qan5Em'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Вт 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/jhGAUOfooA'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Ср 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/zcpl7GTWvO'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Чт 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/MlWIfijNey'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    elif message.text == 'Пт 4к':
        text = '👉 Розклад пар КІ 4 курс'
        img = 'https://imbt.ga/N3gWlNgThd'
        bot.send_message(message.chat.id, f'{text}\n{img}')
        bot.register_next_step_handler(message, get_kb);
    else:
        bot.send_message(message.from_user.id, '🆘Не розумію\nПриклад:(Вт 1к)');


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Док1":
        doc = open('stip.pdf', 'rb')
        bot.send_document(call.message.chat.id, doc)
    elif call.data == 'Док2':
        doc = open('socstip.pdf', 'rb')
        bot.send_document(call.message.chat.id, doc)
    elif call.data == 'dopbal':
        doc = open('reitung.pdf', 'rb')
        bot.send_document(call.message.chat.id, doc)
    elif call.data == '12':
        bot.send_message(call.message.chat.id,
                         '🙅 Вибач, але водійське посвідчення можна  отримати  з 16 років, тільки для категорій А1 і М.\nЗ 18 років можна отримати водійське посвідчення на всі інші  категорії, крім D,D1 ці категорії можна отримати з 21 року ')
    elif call.data == '16':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://nubip.edu.ua/node/15803")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id,
                         '🔞 Отримати водійські права з 16 років можливо тільки для категорій А1 і М.',
                         reply_markup=keyboard)

    elif call.data == '18':
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Перейти",
                                                        url="https://nubip.edu.ua/node/15803")
        keyboard.add(url_button)
        bot.send_message(call.message.chat.id,
                         '❗ З 18 років можна отримати водійське посвідчення на всі інші  категорії, окрім категорії D,D1 ці категорії можна отримати з 21 року ',
                         reply_markup=keyboard)

    elif call.data == 'gimn':
        audio = open('nubip.mp3', 'rb')
        bot.send_message(call.message.chat.id,
                         '👑Гімн НУБіП👑')
        bot.send_audio(call.message.chat.id, audio)
    elif call.data == 'rock':

        bot.send_message(call.message.chat.id,
                         '🎸Топ 5 композицій🎸')

        for number in range(5):
            number += 1
            audio = open('rock' + str(number) + '.mp3', 'rb')
            bot.send_audio(call.message.chat.id, audio)

    elif call.data == 'pop':

        bot.send_message(call.message.chat.id,
                         '🎤Топ 5 композицій🎤')

        for number in range(5):
            number += 1
            audio = open('pop' + str(number) + '.mp3', 'rb')
            bot.send_audio(call.message.chat.id, audio)

    elif call.data == 'classic':

        bot.send_message(call.message.chat.id,
                         '🔥Топ 5 композицій🔥')

        for number in range(5):
            number += 1
            audio = open('clas' + str(number) + '.mp3', 'rb')
            bot.send_audio(call.message.chat.id, audio)

    elif call.data == 'top':

        bot.send_message(call.message.chat.id,
                         '🔥Top 5🔥')

        for number in range(10):
            number += 1
            audio = open('top' + str(number) + '.mp3', 'rb')
            bot.send_audio(call.message.chat.id, audio)


bot.polling()
