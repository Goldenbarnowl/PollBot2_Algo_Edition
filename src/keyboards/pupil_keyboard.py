from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

school_types_buttons = {"school": "🏫 Школа", "lyceum": "🏫 Лицей", "gymnasium": "🏫 Гимназия", "collage": "🏫 Колледж"}


def pupil_age_keyboard():
    pupil_age_keyboard_builder = ReplyKeyboardBuilder()
    for age in range(6, 24):
        button = KeyboardButton(text=str(age))
        if age in [11, 15, 20]:
            pupil_age_keyboard_builder.row(button)
        else:
            pupil_age_keyboard_builder.add(button)
    return pupil_age_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


def pupil_school_type_keyboard():
    pupil_school_type_keyboard_builder = ReplyKeyboardBuilder()
    for school_type in school_types_buttons:
        button = KeyboardButton(text=school_types_buttons[school_type])
        pupil_school_type_keyboard_builder.row(button)
    return pupil_school_type_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


lyceum_buttons = (
    "⬅️ Назад",
    "Лицей «Бизнес и информационные технологии»",
    "Инженерно-технологический лицей № 25",
    "Лицей № 29",
    "Лицей № 54",
    "Лицей № 64",
    "Лицей № 66",
    "Лицей № 74",
    "Лицей № 92",
    "Лицей № 137",
    "Лицей № 143",
    "Лицей № 145",
    "Лицей № 149",
    "Лицей № 166",
    "Другое"
)

def lyceum_keyboard():
    lyceum_keyboard_builder = ReplyKeyboardBuilder()
    for lyceum in lyceum_buttons:
        button = KeyboardButton(text=lyceum)
        lyceum_keyboard_builder.row(button)
    return lyceum_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)

gymnasium_buttons = (
    "⬅️ Назад",
    "Гимназия № 9",
    "Гимназия № 12 имени Героя Советского Союза В.П. Горячева",
    "Гимназия № 19",
    "Гимназия № 26",
    "Гимназия № 43",
    "Гимназия № 62",
    "Гимназия № 69 им. И.М. Чередова",
    "Гимназия № 75",
    "Гимназия № 76",
    "Гимназия № 84",
    "Гимназия № 85",
    "Гимназия № 88",
    "Гимназия № 115",
    "Гимназия № 123 с углубленным изучением отдельных предметов им. О.И. Охрименко",
    "Гимназия № 139",
    "Гимназия № 140",
    "Гимназия № 146",
    "Гимназия № 147",
    "Гимназия № 150",
    "Гимназия № 159",
    "Другое"
)

def gymnasium_keyboard():
    gymnasium_keyboard_builder = ReplyKeyboardBuilder()
    for gymnasium in gymnasium_buttons:
        button = KeyboardButton(text=gymnasium)
        gymnasium_keyboard_builder.row(button)
    return gymnasium_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


school_buttons = (
    "⬅️ Назад",
    "Школа № 1",
    "Школа № 2",
    "Школа № 3",
    "Школа № 4 имени И.И. Стрельникова",
    "Школа № 5",
    "Школа № 6",
    "Школа № 7 имени Героя Советского Союза М.М. Кузьмина",
    "Школа № 8 имени Героя Советского Союза М.Я. Лаптева",
    "Школа № 10",
    "Школа № 11",
    "Школа № 13 имени А.С. Пушкина",
    "Школа № 14 с углубленным изучением отдельных предметов",
    "Школа № 15",
    "Школа № 16",
    "Школа № 17",
    "Школа № 18 с углубленным изучением отдельных предметов",
    "Школа № 21",
    "Школа № 23",
    "Школа № 24",
    "Школа № 27",
    "Школа № 28 с углубленным изучением отдельных предметов",
    "Школа № 30",
    "Школа № 31 с углубленным изучением отдельных предметов",
    "Школа № 32",
    "Школа № 33",
    "Школа № 34",
    "Начальная Школа № 35",
    "Школа № 36",
    "Школа № 37",
    "Школа № 38 с углубленным изучением отдельных предметов",
    "Школа № 39 с углубленным изучением отдельных предметов",
    "Школа № 40 с углубленным изучением отдельных предметов имени Героя Советского Союза И.В. Панфилова",
    "Школа № 41",
    "Школа № 42",
    "Школа № 44",
    "Школа № 45",
    "Школа № 46",
    "Школа № 47 с углубленным изучением отдельных предметов",
    "Школа № 48",
    "Школа № 49",
    "Школа № 50",
    "Школа № 51",
    "Школа № 53",
    "Школа № 55 имени Л.Я. Кичигиной и В.И. Кичигина",
    "Школа № 56 с углубленным изучением отдельных предметов",
    "Школа № 58",
    "Школа № 59 имени Героя Российской Федерации И.А. Мишина",
    "Школа № 60",
    "Школа № 61",
    "Школа № 63",
    "Школа № 65",
    "Школа № 67",
    "Школа № 68",
    "Школа № 70",
    "Школа № 71",
    "Школа № 72 с углубленным изучением отдельных предметов",
    "Школа № 73 с углубленным изучением отдельных предметов",
    "Школа № 77",
    "Школа № 78",
    "Школа № 79",
    "Школа № 80",
    "Школа № 81",
    "Школа № 82",
    "Школа № 83",
    "Школа № 86",
    "Школа № 87",
    "Школа № 89",
    "Школа № 90 имени Д.М. Карбышева",
    "Школа № 91",
    "Школа № 93",
    "Школа № 94",
    "Школа № 95 с углубленным изучением отдельных предметов",
    "Школа № 96",
    "Школа № 97",
    "Школа № 98",
    "Школа № 99 с углубленным изучением отдельных предметов",
    "Школа № 100",
    "Школа № 101",
    "Школа № 103",
    "Школа № 104",
    "Школа № 105 имени Героя Советского Союза Н.П. Бударина",
    "Школа № 106",
    "Школа № 107",
    "Школа № 108",
    "Школа № 109 с углубленным изучением отдельных предметов",
    "Школа № 110",
    "Школа № 111",
    "Школа № 112",
    "Школа № 113",
    "Школа № 114",
    "Школа № 116",
    "Школа № 118",
    "Школа № 119",
    "Школа № 120",
    "Школа № 122",
    "Школа № 124",
    "Школа № 126",
    "Школа № 127",
    "Школа № 129",
    "Школа № 130",
    "Школа № 131",
    "Школа № 132",
    "Школа № 133",
    "Школа № 134",
    "Школа № 135 имени Героя Советского Союза Алексея Петровича Дмитриева",
    "Школа № 138",
    "Школа № 141",
    "Школа № 142",
    "Школа № 144",
    "Школа № 148",
    "Школа № 151",
    "Школа № 152",
    "Школа № 160",
    "Школа № 161",
    "Школа № 162",
    "Другое"
)


def school_keyboard():
    school_keyboard_builder = ReplyKeyboardBuilder()
    for school in school_buttons:
        button = KeyboardButton(text=school)
        school_keyboard_builder.row(button)
    return school_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)

collage_buttons = (
    "⬅️ Назад",
    "📌 Омский авиационный колледж имени Н.Е. Жуковского",
    "📌 Омский государственный колледж управления и профессиональных технологий",
    "Омский промышленно-экономический колледж",
    "Сибирский профессиональный колледж",
    "Омский колледж транспортного строительства",
    "Сибирская региональная школа (колледж) Анны Муратовой",
    "Омский колледж профессиональных технологий",
    "Омский колледж отраслевых технологий строительства и транспорта",
    "Колледж «Многопрофильная академия непрерывного образования»",
    "Омский автотранспортный колледж",
    "Колледж инновационных технологий, экономики и коммерции",
    "Сибирская региональная школа бизнеса (колледж)",
    "Торгово-экономический колледж имени Г.Д. Зуйковой",
    "Омский юридический колледж",
    "Университетский колледж агробизнеса",
    "Колледж «Синергия»",
    "Учебно-курсовой комбинат автомобильного транспорта",
    "Профессиональное училище № 301 ФСИН",
    "Профессиональное училище № 296 ФСИН",
    "Профессиональное училище № 298 ФСИН",
    "Профессиональное училище № 297 ФСИН",
    "Омский колледж предпринимательства и права",
    "Омский колледж культуры и искусства",
    "Омский медицинский колледж",
    "Омский колледж информационных технологий",
    "Омский колледж дизайна и технологий",
    "Омский колледж сервиса и туризма",
    "Омский колледж энергетики и цифровых технологий",
    "Омский колледж пищевой промышленности",
    "Омский колледж строительства и архитектуры",
    "Омский колледж машиностроения",
    "Омский колледж экономики и управления",
    "Омский колледж железнодорожного транспорта",
    "Омский колледж связи и телекоммуникаций",
    "Омский колледж физической культуры и спорта",
    "Омский колледж искусств",
    "Омский колледж педагогики и психологии",
    "Омский колледж химических технологий",
    "Омский колледж экологии и природопользования",
    "Омский колледж геодезии и картографии",
    "Омский колледж иностранных языков",
    "Омский колледж социальной работы",
    "Омский колледж безопасности жизнедеятельности"
)

def collage_keyboard():
    school_keyboard_builder = ReplyKeyboardBuilder()
    for school in collage_buttons:
        button = KeyboardButton(text=school)
        school_keyboard_builder.row(button)
    return school_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)

def grade_keyboard(max_grade):
    grade_keyboard_builder = ReplyKeyboardBuilder()
    for grade in range(1, max_grade):
        button = KeyboardButton(text=str(grade))
        if grade in [6]:
            grade_keyboard_builder.row(button)
        else:
            grade_keyboard_builder.add(button)
    return grade_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


answer_buttons = ["✅ Да", "❌ Нет"]


def request_keyboard():
    request_keyboard_builder = ReplyKeyboardBuilder()
    for request in answer_buttons:
        button = KeyboardButton(text=request)
        request_keyboard_builder.add(button)
    return request_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


university_list = [
    "Омский государственный технический университет",  # ОмГТУ
    "Омский государственный университет им. Ф.М. Достоевского",  # ОмГУ
    "Омский государственный педагогический университет",  # ОмГПУ
    "Сибирский государственный автомобильно-дорожный университет",  # СибАДИ
    "Омский государственный аграрный университет им. П.А. Столыпина",  # ОмГАУ
    "Омский государственный медицинский университет",  # ОмГМУ
    "Омский государственный университет путей сообщения",  # ОмГУПС
    "Сибирский государственный университет физической культуры и спорта",  # СибГУФК
    "Омская юридическая академия",  # ОмЮА
    "Омская гуманитарная академия",  # ОмГА
    "Омский авиационный колледж им. Н.Е. Жуковского",
    "Омский колледж отраслевых технологий строительства и транспорта",
    "Сибирский профессиональный колледж",
    "Омский технологический колледж",
    "Омский музыкально-педагогический колледж",
    "Сибирский многопрофильный колледж «Перспектива»",
    "Международный технологический колледж Российского биотехнологического университета",
    "Омский филиал Московского международного колледжа цифровых технологий «Академия ТОП»",
    "Колледж инновационных технологий, экономики и коммерции",
    "Омский колледж профессиональных технологий",
    "Нет в списке",
    "Не планирую поступать"
]

next_button = {"next": "➡️ Продолжить"}


def university_keyboard(check_list):
    university_keyboard_builder = InlineKeyboardBuilder()
    for n in range(len(university_list)):
        if n in check_list:
            button = InlineKeyboardButton(text="✅ " + university_list[n], callback_data=str(n))
            university_keyboard_builder.row(button)
        else:
            button = InlineKeyboardButton(text=university_list[n], callback_data=str(n))
            university_keyboard_builder.row(button)
    button = InlineKeyboardButton(text=next_button["next"], callback_data="next")
    university_keyboard_builder.row(button)
    return university_keyboard_builder.as_markup(resize_keyboard=True)


answer_q3 = ["Очень часто", "Иногда", "Редко", "Не интересуюсь"]


def keyboard_q3():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in answer_q3:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# Функция для создания клавиатуры для вопроса 2
answer_q4 = ["Да, с удовольствием", "Если будет интересно", "Скорее нет", "Нет"]


def keyboard_q4():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in answer_q4:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# Функция для создания клавиатуры для вопроса 5 (любимый язык программирования)
answer_q5 = [
    "Python",
    "JavaScript",
    "C++",
    "Scratch",
    "У меня пока нет любимого языка"
]


def keyboard_q5():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in answer_q5:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


answer_q6 = [
    "Создание игры",
    "Разработка мобильного приложения",
    "Разработка робота",
    "Создание веб-сайта",
    "Не знаю, но хотел(а) бы научиться"
]


def keyboard_q6():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in answer_q6:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


prof_answers = [
    [
        "а) Оно похоже на метафору из стихотворения",
        "б) Хочу рассчитать его плотность и траекторию",
        "в) Интересно, как формируются кристаллы льда внутри",
        "г) Можно ли смоделировать его движение через алгоритм"
    ],
    [
        "а) Поэтическая многозначность (как в древнекитайском)",
        "б) Абсолютная логическая однозначность (как в математике)",
        "в) Принципы работы нейронов мозга",
        "г) Синтаксис, оптимизированный для машинного перевода"
    ],
    [
        "а) Изолировать группу людей без общего языка — возникнет ли новый?",
        "б) Построить компьютер на основе квантовой механики",
        "в) Пересадить воспоминания между организмами",
        "г) Обучить ИИ писать код без участия человека"
    ],
    [
        "а) Утраченные рукописи Шекспира",
        "б) Формулу теории всего",
        "в) Карту нейронных связей гения",
        "г) Исходный код первого сильного ИИ"
    ],
    [
        "а) 'Я мыслю — значит, я ошибаюсь' (переосмысление Декарта)",
        "б) 'Бог не играет в кости, но иногда подкручивает вероятности'",
        "в) 'Жизнь — это ДНК, пытающаяся себя понять'",
        "г) 'Любой код — временный, пока его не заменят 3 строчки на Python'"
    ],
    [
        "а) Племя, где нет понятия времени",
        "б) Материал с отрицательной плотностью",
        "в) Гриб, создающий нейросети из мицелия",
        "г) Компьютерный вирус, эволюционирующий без программиста"
    ],
    [
        "а) 'Искусство ошибки: как опечатки меняют историю'",
        "б) 'Математика шестимерных объектов, которые нельзя представить'",
        "в) 'Биология ксеноморфов: альтернативные принципы жизни'",
        "г) 'Этика для сильного ИИ: когда код обретает свободу воли'"
    ],
    [
        "а) Виолончель — глубокий, интроспективный, с множеством интерпретаций",
        "б) Оргáн — архитектурно сложный, с бесконечными комбинациями",
        "в) Электронные сэмплы природных звуков, которые нельзя повторить",
        "г) Алгоритм, генерирующий мелодии, непредсказуемые даже для создателя"
    ],
    [
        "а) Прочесть письма, которые автор завещал сжечь",
        "б) Провести эксперимент, нарушающий известные законы физики",
        "в) Создать химеру из генов вымерших и существующих видов",
        "г) Взломать систему, чтобы доказать её уязвимость"
    ],
    [
        "а) 'Я ищу спрятанные истории в том, что кажется обычным'",
        "б) 'Я собираю пазл, у которого нет картинки-образца'",
        "в) 'Я разговариваю с невидимыми монстрами (микробами/генами/атомами)'",
        "г) 'Я учу компьютер играть в прятки с самим собой'"
    ],
    [
        "а) Превращу цифры в персонажей и сочиню про них драму",
        "б) Разобью на простые множители, найду паттерны",
        "в) Свяжу с телесными ощущениями (например, '4' — холод, '9' — покалывание)",
        "г) Напишу программу, которая превратит число в мелодию"
    ],
    [
        "а) По смене стиля: почерк грубеет, когда автор злится",
        "б) По упоминаниям погоды → сопоставлю с архивными сводками",
        "в) По пятнам на страницах — анализ состава чернил под микроскопом",
        "г) Оцифрую и загружу в нейросеть для реконструкции временнóй линии"
    ]
]


def prof_test_keyboard(numberk: int):
    keyboard_builder = ReplyKeyboardBuilder()
    button = KeyboardButton(text=prof_answers[numberk][0])
    keyboard_builder.row(button)
    button = KeyboardButton(text=prof_answers[numberk][1])
    keyboard_builder.row(button)
    button = KeyboardButton(text=prof_answers[numberk][2])
    keyboard_builder.row(button)
    button = KeyboardButton(text=prof_answers[numberk][3])
    keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


def prof_university_keyboard(university_type):
    keyboard_inline = InlineKeyboardBuilder()
    if university_type == "a":
        keyboard_inline.row(InlineKeyboardButton(text="Педагогический университет | ОмГПУ", url="https://t.me/omgpu_inside"))
        keyboard_inline.row(InlineKeyboardButton(text="Университет имени Ф.М.Достоевского | ОмГУ", url="https://t.me/omsuru"))
    elif university_type == "b":
        keyboard_inline.row(InlineKeyboardButton(text="Технический университет | ОмГТУ", url="https://t.me/omgtu_live"))
        keyboard_inline.row(InlineKeyboardButton(text="Университет путей сообщения | ОмГУПС", url="https://t.me/omgups_fdpipo"))
        keyboard_inline.row(InlineKeyboardButton(text="Автомобильно-дорожный университет | СибАДИ", url="https://t.me/sibadilife"))
    elif university_type == "c":
        keyboard_inline.row(InlineKeyboardButton(text="Медицинский университет | ОмГМУ", url="https://t.me/osmu_official"))
        keyboard_inline.row(InlineKeyboardButton(text="Аграрный университет | ОмГАУ", url="https://t.me/omskiygau"))
    elif university_type == "d":
        keyboard_inline.row(InlineKeyboardButton(text="Технический университет | ОмГТУ", url="https://t.me/omgtu_live"))
        keyboard_inline.row(InlineKeyboardButton(text="Университет имени Ф.М.Достоевского | ОмГУ", url="https://t.me/omsuru"))
        keyboard_inline.row(InlineKeyboardButton(text="Университет путей и сообщения | ОмГУПС", url="https://t.me/omgups_fdpipo"))
        keyboard_inline.row(InlineKeyboardButton(text="Автомобильно-дорожный университет | СибАДИ", url="https://t.me/sibadilife"))
    return keyboard_inline.as_markup()


event_name_list = ["🔥 Код Будущего - подготовительный этап",
                   "Хакатон «Технологии искусственного интеллекта и бизнес-аналитики в больших данных»",
                   "Хакатон «Город героев» для школьников и студентов",
                   "Буткемп для начинающих менеджеров"]


def events_keyboard():
    inline = InlineKeyboardBuilder()
    inline.row(InlineKeyboardButton(text=event_name_list[0], callback_data="e_1"))
    inline.row(InlineKeyboardButton(text=event_name_list[1], callback_data="e_2"))
    inline.row(InlineKeyboardButton(text=event_name_list[2], callback_data="e_3"))
    inline.row(InlineKeyboardButton(text=event_name_list[3], callback_data="e_4"))
    return inline.as_markup()


def event_info_keyboard(text: str, url: str):
    inline = InlineKeyboardBuilder()
    inline.row(InlineKeyboardButton(text=text, url=url))
    return inline.as_markup()


faculti_omaviat = [
    "09.02.06 Сетевое и системное администрирование",
    "09.02.07 Информационные системы и программирование",
    "10.02.05 Обеспечение информационной безопасности автоматизированных систем",
    "11.01.01 Монтажник радиоэлектронной аппаратуры и приборов",
    "12.02.03 Радиоэлектронные приборы и устройства",
    "13.01.10 Электромонтер по ремонту и обслуживанию электрооборудования (по отраслям)",
    "13.02.13 Эксплуатация и обслуживание электрического и электромеханического оборудования (по отраслям)",
    "15.01.05 Сварщик (ручной и частично механизированной сварки (наплавки))",
    "15.01.29 Контролер качества в машиностроении",
    "15.01.35 Мастер слесарных работ",
    "15.01.38 Оператор-наладчик металлообрабатывающих станков",
    "15.02.09 Аддитивные технологии",
    "15.02.10 Мехатроника и робототехника"
    "15.02.16 Технология машиностроения",
    "15.02.16 Технология машиностроения (11 кл)",
    "15.02.18 Техническая эксплуатация и обслуживание роботизированного производства по отраслям",
    "15.02.19 Сварочное производство",
    "24.02.01 Производство летательных аппаратов",
    "24.02.02 Производство авиационных двигателей",
    "25.02.07 Техническое обслуживание авиационных двигателей (11 кл)",
    "25.02.08 Эксплуатация беспилотных авиационных систем",
    "38.02.01 Экономика и бухгалтерский учет (по отраслям)",
    "38.02.03 Операционная деятельность в логистике",
    "39.02.01 Социальная работа",
    "43.01.09 Повар, кондитер",
    "54.01.20 Графический дизайнер"
]

def omaviation_keyboard():
    reply = ReplyKeyboardBuilder()
    for fac in faculti_omaviat:
        button = KeyboardButton(text=fac)
        reply.row(button)
    return reply.as_markup(resize_keyboard=True, is_persistent=True)


faculti_omkyipt = [
    # Программы подготовки специалистов среднего звена (9 кл.) ОГКУиПТ
    "11.02.16 Монтаж, техническое обслуживание и ремонт электронных приборов и устройств",
    "11.02.17 Разработка электронных устройств и систем",
    "09.02.01 Компьютерные системы и комплексы",
    "09.02.07 Информационные системы и программирование (Специалист по информационным системам)",
    "09.02.07 Информационные системы и программирование (Разработчик веб и мультимедийных приложений)",
    "46.02.01 Документационное обеспечение управления и архивоведение",
    "40.02.04 Юриспруденция",

    # Программы подготовки специалистов среднего звена (11 кл.)
    "09.02.07 Информационные системы и программирование",

    # Программы подготовки квалифицированных рабочих (9 кл.)
    "11.01.01 Монтажник радиоэлектронной аппаратуры и приборов",
    "11.01.08 Оператор почтовой связи",
    "08.01.30 Электромонтажник слаботочных систем"
]

def omkyipt_keyboard():
    reply = ReplyKeyboardBuilder()
    for fac in faculti_omkyipt:
        button = KeyboardButton(text=fac)
        reply.row(button)
    return reply.as_markup(resize_keyboard=True, is_persistent=True)