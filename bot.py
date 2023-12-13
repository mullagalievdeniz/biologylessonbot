import telebot
from telebot import types
import time

bot = telebot.TeleBot('6626972464:AAG4PihI3LTIxZJcHtaVhPAxceqdM54dDuk') 

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = types.KeyboardButton('✅ Да')
btn2 = types.KeyboardButton('❌ Нет')
markup.add(btn1, btn2)

user_data = {}

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn3 = types.KeyboardButton('🔁 Пройти тест заново')
markup2.add(btn3)


methodics = {}
methodics['low1'] = 'Для начала найдите глазами прямоугольный предмет: картину, окно или дверь. Далее идем по шагам:  Шаг 1. Посмотрите в верхний левый угол и вдохните, считая при этом до четырех. Шаг 2. Переведите взгляд на верхний правый угол и задержите дыхание, считая до четырех. Шаг 3. Переведите дыхание в нижний правый угол и выдохните, считая до четырех. Шаг 4. Переведите взгляд в нижний левый угол и сделайте задержку с пустыми легкими, считая до 4'
methodics['low2'] = 'Вдох Начинаем дышать животом. Положите одну руку на живот, чтобы отслеживать, как двигается диафрагма во время дыхания. Вторая рука на груди. Грудь во время дыхания не двигается. Делаем вдох через нос. На вдохе диафрагма уходит вниз, живот надувается, заполняется нижняя часть легких.  Выдох Выдыхаем через нос. Живот возвращается в исходное положение. На выдохе брюшная стенка идет обратно, воздух выдавливаем через нос и делаем небольшую задержку.  После этого — новый вдох Если возникают неприятные ощущения в животе, это говорит о том, что диафрагма спазмирована хроническим стрессом. Продолжайте регулярно практиковать диафрагменное дыхание, и дискомфорт пройдет.  Таким дыханием мы стимулируем блуждающий нерв, который ускоряет процесс включения парасимпатического отдела автономной нервной системы. Наш организм переходит в режим расслабления и восстановления'
methodics['middle1'] = 'Не обдумывайте и не подбирайте слова. Пишите первое, что придет в голову в течении 5 минут . Не следите за грамотностью текста. Прекращайте писать по таймеру. Не заканчивайте мысль после сигнала, если еще осталось, что выразить. Пишите без перерыва. Если вы пишете от руки и устаете, сбавьте темп, но не останавливайтесь. Постарайтесь, чтобы поток мыслей был связным'
methodics['middle2'] = 'Это очень простое и эффективное упражнение для переключения из одного эмоционального состояния на другое. Оно поможет вернуться в «здесь и сейчас» и снизит стресс. В момент, когда чувствуете напряжение, беспокойство или гнев, отметьте вокруг себя:  пять предметов, которые вы можете рассмотреть; четыре звука, которые вы слышите; три предмета с разной фактурой, к которым можно прикоснуться; два запаха, которые вы можете ощущать; один вкус, который вы можете попробовать.'
methodics['middle3'] = 'Перед началом упражнений нащупайте свой пульс. Наблюдайте несколько минут, сколько ударов сердца приходится на один выдох и спокойный вдох. Постепенно удлиняйте время выдохов. Первые несколько дыхательных движений продолжайте выдыхать на один удар пульса больше, чем было посчитано до начала упражнения. Обратите внимание на замедление сердечного ритма в соответствии с более глубоким дыханием. Затем увеличьте время выдоха еще на один удар сердца. После нескольких циклов дыхания попробуйте удлинить выдох еще на один удар. Важно постоянно следить за замедлением сердечного ритма во время выполнения упражнения. Такая гимнастика помогает синхронизировать различные процессы в организме, способствует успокоению, расслаблению и возвращению в нормальное состояние.'
methodics['high1'] = 'Достаточно закрыть глаза, выровнять дыхание и представить себя в живописном и безопасном месте. Познайте все детали: цвета, звуки, ароматы, тактильные ощущения. Чем ярче будут ваши образы, тем лучше.'
methodics['high2'] = 'На короткий момент создать сильное мышечное напряжение, чтобы мышцы перенапряглись. Вследствие такого интенсивного напряжения мышцы расслабляются. Таким образом мы избавляемся от хронических мышечных блоков, стимулирующих стрессовое состояние.  Необходимо будет напрячь следующие участки тела: кисти, предплечья, плечи и надплечья, лопатки, лицо, шею, пресс, ягодицы, промежность, бедра, голени, стопы.'
methodics['high3'] = 'Давайте выявим неэффективные модели мышления и измененим их:\n\nШаг 1: Определите негативные мысли\nПервым шагом в когнитивной реструктуризации является выявление негативных мыслей или убеждений, которые способствуют эмоциональному дистрессу или поведенческим проблемам. Эти негативные мысли часто являются автоматическими и укоренившимися, и клиент может не осознавать их. Терапевт поможет клиенту идентифицировать эти негативные мысли, задавая такие вопросы, как:  О чем вы думали, когда чувствовали тревогу/депрессию/злость? Что самое худшее, что может случиться? Какие у Вас есть доказательства, подтверждающие эту мысль?  Например, у клиента с социальной тревожностью может возникнуть негативная мысль: «Я всегда выставляю себя дураком в социальных ситуациях». Терапевт помогает клиенту идентифицировать эту мысль и исследовать доказательства, подтверждающие её.\n\nШаг 2: Оцените доказательства\nКак только негативная мысль будет выявлена, терапевт помогает клиенту оценить доказательства, подтверждающие её. Это включает в себя задавание таких вопросов, как:  Эта мысль основана на фактах или предположениях? Какие у вас есть доказательства, подтверждающие эту мысль? Какие у вас есть доказательства против этой мысли?  Используя приведенный выше пример, терапевт может попросить клиента назвать случаи, когда она/он не выставлял себя дураком в социальных ситуациях. Это может помочь клиенту увидеть, что её/его негативные мысли не совсем точны.\n\nШаг 3: Бросьте вызов негативным мыслям.\nСледующий шаг — бросить вызов негативной мысли и заменить её более реалистичной и адаптивной. Терапевт поможет клиенту переформулировать свои негативные мысли, задавая такие вопросы, как:  Что свидетельствует против этой мысли? Какая мысль более уравновешенная или реалистичная? Как бы другой посмотрел на эту ситуацию?  Используя приведенный выше пример, терапевт может помочь клиенту переформулировать его негативную мысль так: «Я совершал ошибки в определённых ситуациях, но у меня также был и положительный опыт». Эта более сбалансированная мысль может помочь клиенту чувствовать себя менее тревожным в социальных ситуациях.\n\nШаг 4: Практикуйте новые мысли.\nПоследний шаг в когнитивной реструктуризации — практиковать новую мысль или убеждение до тех пор, пока они не станут автоматическими. Терапевт может давать домашние задания, которые включают в себя отработку новой мысли или убеждения в реальных жизненных ситуациях. Это может помочь клиенту обрести уверенность и устойчивость в сложных ситуациях.'
methodics['high4'] = 'Необходимо составить список выгод избавления от тревоги.  я смогу спокойно спать по ночам; я смогу посещать любые места и наслаждаться этим; в течение всего дня я буду чувствовать энергичность и радость; я смогу продуктивно работать и полноценно расслабляться; мои отношения с близкими улучшатся'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Давай пройдём тест на стресс!\n\nПоехали! 😉')
    bot.send_message(message.chat.id, 'Меня мало интересуют окружающие меня люди', reply_markup=markup)
    bot.register_next_step_handler(message, step2)


def step2(message):
   user_data[message.chat.id] = {}
   user_data[message.chat.id]['step1'] = 0

   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1

   bot.send_message(message.chat.id, 'Я часто не могу избавиться от некоторых навязчивых мыслей')
   bot.register_next_step_handler(message, step3, user_data)


def step3(message, user_data):
   if message.text == '✅ Да':
      user_data[message.chat.id]['step1'] += 1

   bot.send_message(message.chat.id, 'У меня часто меняется настроение')
   bot.register_next_step_handler(message, step4, user_data)
    

def step4(message, user_data):

   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1

   bot.send_message(message.chat.id, 'Я плохо сплю и встаю с большим трудом')
   bot.register_next_step_handler(message, step5, user_data)


def step5(message, user_data):

   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1

   bot.send_message(message.chat.id, 'В одиночестве у меня часто появляются тоска или тревожные мысли')
   bot.register_next_step_handler(message, step6, user_data)


def step6(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Я часто принимаю успокаивающие или стимулирующие средства')
   bot.register_next_step_handler(message, step7, user_data)


def step7(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Как правило, меня утомляет общение с другими людьми, я стремлюсь к уединению')
   bot.register_next_step_handler(message, step8, user_data)


def step8(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Я часто испытываю трудности в управлении своими мыслями и желаниями')
   bot.register_next_step_handler(message, step9, user_data)


def step9(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Я не жду ничего хорошего в моей будущей жизни')
   bot.register_next_step_handler(message, step10, user_data)


def step10(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Иногда у меня бывают головокружения или слабость в теле')
   bot.register_next_step_handler(message, step11, user_data)


def step11(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Часто я долго не могу заснуть')
   bot.register_next_step_handler(message, step12, user_data)

def step12(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Обычно мне трудно отключиться даже от мелких конфликтов и текущих неприятностей на учёбе')
   bot.register_next_step_handler(message, step13, user_data)

def step13(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Как правило, мне трудно сконцентрироваться на одном деле или действиях')
   bot.register_next_step_handler(message, step14, user_data)

def step14(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'По утрам я часто чувствую себя разбитым')
   bot.register_next_step_handler(message, step15, user_data)
   

def step15(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Физические упражнения и спорт меня не привлекают')
   bot.register_next_step_handler(message, step16, user_data)
   
def step16(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'У меня часто бывает плохое настроение')
   bot.register_next_step_handler(message, step17, user_data)

def step17(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Я часто просыпаюсь по ночам')
   bot.register_next_step_handler(message, step18, user_data)

def step18(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Иногда я испытываю тревогу или страх в темноте и в закрытых помещениях')
   bot.register_next_step_handler(message, step19, user_data)

def step19(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Лучший способ решения сложного вопроса — «утопить» его в вине')
   bot.register_next_step_handler(message, step20, user_data)

def step20(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'После рабочей недели я предпочитаю отдыхать в одиночестве и без физических нагрузок')
   bot.register_next_step_handler(message, step21, user_data)

def step21(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'У меня бывают мысли, от которых мне трудно избавиться')
   bot.register_next_step_handler(message, step22, user_data)

def step22(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Мое настроение часто меняется в течение дня без явных причин')
   bot.register_next_step_handler(message, step23, user_data)

def step23(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Иногда у меня бывают приступы дрожи или жара')
   bot.register_next_step_handler(message, step24, user_data)

def step24(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'У меня бывают навязчивые страхи')
   bot.register_next_step_handler(message, step25, user_data)


def step25(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'После сильных стрессов я предпочитаю «забыться» и «отключиться» от всего')
   bot.register_next_step_handler(message, step26, user_data)

def step26(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Часто я не могу упорядочить мои мысли и сконцентрироваться на главном')
   bot.register_next_step_handler(message, step27, user_data)

def step27(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Мое настроение очень изменчиво и зависит от внешних обстоятельств')
   bot.register_next_step_handler(message, step28, user_data)


def step28(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Я постоянно испытываю тревогу и ожидаю неприятностей')
   bot.register_next_step_handler(message, step29, user_data)


def step29(message, user_data):
   if message.text == '✅ Да':
     user_data[message.chat.id]['step1'] += 1
   bot.send_message(message.chat.id, 'Я постоянно принимаю успокаивающие или возбуждающие средства, чтобы нормализовать свое состояние и лучше приспособиться к жизненным обстоятельствам')
   bot.register_next_step_handler(message, step30, user_data)




def step30(message, user_data):
   if user_data[message.chat.id]['step1'] < 10:
      bot.send_message(message.chat.id, 'У Вас высокий уровень психологической устойчивости к экстремальным условиям, состояние хорошей адаптированности 😀')
      bot.send_message(message.chat.id, 'Однако не стоит останавливаться на достигнутом! Предлагаю к Вашему вниманию следующие методики, которые смогут повысить вашу психологическую устойчивость!')
      bot.send_message(message.chat.id, f'1️⃣ Аутогенная медитация  визуализация\n\n{methodics['high1']}')
      bot.send_message(message.chat.id, f'2️⃣ Мышечное расслабление\n\n{methodics['high2']}')
      bot.send_message(message.chat.id, f'3️⃣ Когнетивная реструктуризация\n\n{methodics['high3']}')
      bot.send_message(message.chat.id, f'4️⃣ Мотивация\n\n{methodics['high4']}', reply_markup=markup2)
      bot.register_next_step_handler(message, wait, user_data)

   elif user_data[message.chat.id]['step1'] > 10 and user_data[message.chat.id]['step1'] < 18:
      bot.send_message(message.chat.id, 'Средний уровень психологической устойчивости к экстремальным условиям, состояние удовлетворительной  адаптированности')
      bot.send_message(message.chat.id, 'Предлагаю к Вашему вниманию методики, которые помогут Вам улучшить стрессоустойчивость')
      bot.send_message(message.chat.id, f'1️⃣ Техника Фрирайтинг\n\n{methodics['middle1']}')
      bot.send_message(message.chat.id, f'2️⃣ Упражнение 5 чувств\n\n{methodics['middle2']}')
      bot.send_message(message.chat.id, f'3️⃣ Дыхательная гимнастика\n\n{methodics['middle3']}', reply_markup=markup2)
      bot.register_next_step_handler(message, wait, user_data)

   else:
      bot.send_message(message.chat.id, '❗Низкая стрессоустойчивость, высокий риск патологических стрессреакций и невротических расстройств, состояние дезадаптации')
      bot.send_message(message.chat.id, 'Предлагаю к Вашему вниманию методики, которые помогут Вам улучшить стрессоустойчивость')
      bot.send_message(message.chat.id, f'1️⃣ Дыхание по квадрату\n\n{methodics['high1']}')
      bot.send_message(message.chat.id, f'2️⃣ Упражнение 5 чувств\n\n{methodics['high2']}', reply_markup=markup2)
      bot.register_next_step_handler(message, wait, user_data)


def wait(message, user_data):
   user_data[message.chat.id]['step1'] = 0

   if message.text == '🔁 Пройти тест заново':
      start()
   else:
      bot.send_message('Вы можете пройти тест заново. Для этого используйте команду /start')

while True:
    try:
        bot.polling(none_stop=True, timeout=90)
    except Exception as e:
        print(e)
        time.sleep(5)
        continue
