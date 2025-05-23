from aiogram.utils.markdown import hlink

PERS_DATA_REQUEST = """<b>Привет!</b> 👋

Меня зовут <b>ForgeBot</b> 🤖✨
Я — твой виртуальный проводник в увлекательный мир технологий и крутых мероприятий! 🚀

<b>Вот что я умею сейчас:</b>
🔹 Помочь выбрать будущую профессию 🎓💡
🔹 Оповещать о самых интересных мероприятиях, где ты сможешь проявить себя 🎉📅

<b>А в будущем тебя ждёт кое-что ещё круче!</b>
Я планирую организовать мега-соревнование между учебными заведениями Омска, чтобы определить самый активный и сплочённый коллектив города! 🔥🏆

<b>Ты со мной? Тогда погнали! 🚀💥</b>

<b>❗️ ОЧЕНЬ ВАЖНО ❗️</b>
Перед регистрацией будь внимателен: отвечай на вопросы честно и вдумчиво! 📝🔍
Это поможет мне подобрать для тебя идеальные задания и дать самые полезные советы по профессии! 😎

❗️ Если ты допустил ошибку в опросе, введи команду 
/start (Это перезапустит опрос)

Для продолжения нам нужно согласие на обработку персональных данных.
Пожалуйста, нажми кнопку ниже⬇️"""
NAME_REQUEST = "Укажите Ваше ФИО, пожалуйста."
ERROR_NAME = "Ошибка: некорректное имя. Пожалуйста, введите полное и правильное имя."
YOU_ROLE = "Пожалуйста, укажите Вашу роль (например, ученик, родитель)."
PUPIL_AGE = "Укажите Ваш возраст:"
PUPIL_ERROR_AGE = "Возраст должен быть числом от 3 до 25. Проверьте введенные данные."
SCHOOL_TYPE = "Выберите тип учебного заведения:"
SCHOOL_REQUEST = "Выберете учебное заведение из списка:"
ERROR_SCHOOL = "Ошибка: выберите учебное заведение из списка."
GRADE_REQUEST = "Укажите, в каком классе Вы учитесь:"
ERROR_GRADE = "Класс должен быть числом от 1 до 11. Проверьте, пожалуйста, ввод."
EXAM_REQUEST = "Планируете ли сдавать "
UNIVERSITY_REQUEST = "Собираетесь ли поступать в ВУЗ или СУЗ?"
ERROR_BUTTON = "Ошибка: воспользуйтесь кнопками для продолжения."
UNIVERSITY_LIST_REQUEST = "Укажите, в какой ВУЗ или СУЗ планируете поступать. (не более 3 вариантов)"
GUIDE_UNIVERSITY = "Выберите интересующие Вас образовательные организации высшего и среднего профессионального образования и нажмите кнопку \"Продолжить\"."
ERROR_UNIVERSITY = "Пожалуйста, выберите хотябы один пункт из списка."
PUPIL_Q1 = "Планируете поступление на техническую специальность? "
PUPIL_Q2 = "Планируете ли связать свою жизнь с ИТ?"
PUPIL_Q3 = "Как часто Вы интересуетесь новостями и технологиями из мира ИТ?"
PUPIL_Q4 = "Готовы ли Вы участвовать в дополнительных занятиях и проектах после уроков для развития цифровых навыков?"
PUPIL_Q5 = "Есть ли у Вас любимый язык программирования? Если да, то какой?"
PUPIL_Q6 = "Если бы у Вас была возможность создать свой собственный ИТ-проект, что бы это было?"
PUPIL_THX_7 = """Спасибо за участие в опросе! 
Алгоритмика - это не только школа программирования, но и целая команда учителей, дизайнеров, программистов, делающих изучение программирования интересным и увлекательным!

Специально для тебя мы подготовили увлекательное приключение с нашими героями в мир анимации управления роботами через строчки кода🤖
Скорее подписывайся на наш телеграм и возвращайся сюда за подарком🎁


https://t.me/algo_omsk"""
PUPIL_THX_9 = """Спасибо за участие в опросе! 
Алгоритмика - это не только школа программирования, но и целая команда учителей, дизайнеров, программистов, делающих изучение программирования интересным и увлекательным!

Если ты давно хотел попробовать свои силы в изучении Python или применить свои знания на практике - скорее подписывайся на наш телеграм и возвращайся сюда, мы подготовили для тебя сюрприз🎁

https://t.me/algo_omsk"""
PUPIL_THX = """Спасибо за уделенное время!"""
PUPIL_PRESENT_7 = "Подарок от Алгоритмики 7"
PUPIL_PRESENT_9 = "Подарок от Алгоритмики 9"
PCHILDREN_NAME = "Как зовут Вашего ребенка?"
ERROR_PCHILDREN = "Ошибка: попробуйте ввести имя снова."
PARENT_SCHOOL_TYPE = "В каком учебном заведении учится Ваш ребенок?"
PCHILDREN_AGE = "Укажите, пожалуйста, возраст Вашего ребенка."
PARENT_GRADE_REQUEST = "В каком классе учится Ваш ребенок?"
PARENTS_Q2 = "Планируете связать жизнь ребенка с ИТ?"
PARENTS_Q3 = "Занимается ли ребенок дополнительно занятиями связанными с ИТ?"
NEW_CHILDREN = "Есть ли у Вас еще дети?"
PARENTS_Q5 = ""
PARENTS_Q6 = "Вы поддерживаете своего ребенка в изучении новых технологий?"
PARENTS_Q7 = "Есть ли у Вас опыт работы с ИТ-технологиями?"
PARENTS_Q8 = "Что Вы считаете главным преимуществом для ребенка при изучении ИТ-технологий?"
PARENTS_Q9 = "Какие ИТ-навыки, по вашему мнению, будут наиболее полезны в будущем для вашего ребенка?"
THX_PARENTS = """Спасибо за участие в опросе! 
Алгоритмика - это не только школа программирования, но и целая команда учителей, дизайнеров, программистов, делающих изучение программирования интересным и увлекательным!

С этого года школа программирования Алгоритмика стала официальным партнером ОмГТУ и Министерства цифрового развития Омской области, а так же официальным провайдером федерального проекта "Код будущего" 

Если Ваш ребенок проявляет интерес к компьютеру, телефону, любит изучать новые механизмы и устройство гаджетов - мы сможем развить и приумножить его способности🤗
Чтобы узнать подробнее - подпишитесь на нас в телеграме и возвращайтесь сюда - мы подготовили небольшой презент🎁

https://t.me/algo_omsk"""
THX_PARENTS_END = "Спасибо за уделенное время!"
REPEAT_PARENTS = f"Чтобы получить приз, надо подписаться на канал! \n{hlink('Cсылка *ТЫК*', 'https://t.me/om_fest')}"
PARENT_PRESENT = "Cюрприз🎁"
PARENT_GIVE = "Вы забрали свой подарок!"
THX_TEACHER = """Спасибо за участие в опросе! 
Алгоритмика - это не только школа программирования, но и целая команда учителей, дизайнеров, программистов, делающих изучение программирования интересным и увлекательным!

Если Вы - проактивный, амбициозный и увлеченный педагог - напишите нам по вопросам сотрудничества
(ссылка на мой ватсап/телеграм)
"""
LAST_STAND = "Такого варианта ответа нет. Пожалуйста, воспользуйтесь кнопками или полем ввода."

TEACHER_WAIT_CONTACT_DATA = "Пожалуйста, введите Ваши контактные данные"
TEACHER_CHILDREN_COUNT = "Введите количество учащихся в 5–8 классах. (Введите число)"
TEACHER_Q1 = "Есть ли уже заинтересованные ученики в углубленном изучении ИТ?"
TEACHER_Q2 = "Проводятся ли в школе мероприятия по развитию цифровых навыков?"
TEACHER_Q3 = "Расскажите о наличии оборудования для ИТ-обучения (компьютеры, программы, робототехника)."
TEACHER_Q4 = "Готовы ли Вы уделять дополнительное время на занятия с учениками в рамках программы?"
TEACHER_Q5 = "Вы проходили курсы или повышение квалификации в области ИТ?"
TEACHER_THX = "Спасибо за уделенное время!"
