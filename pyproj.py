from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMenu, QMenuBar, \
    QStatusBar, QTextBrowser
import sys
import random
import sqlite3
connect = sqlite3.connect('DBFSeva')
cursor = connect.cursor()
try:
    record = cursor.execute('SELECT * FROM MainQuestion1')
except Exception:
    for i in range(1, 11):
        mainquestion = 'MainQuestion' + str(i)
        cursor.execute('''CREATE TABLE %s(
            _id INTEGER, 
            Question TEXT, 
            Answer TEXT, 
            PRIMARY KEY(_id AUTOINCREMENT))''' % mainquestion)
    cursor.execute("""INSERT INTO MainQuestion1(Question, Answer) VALUES
                   ('Найдите значение выражения a / b, при a = 3^8 * 3^5, b = 3^9.', '81'),
                   ('Найдите значение выражения a / b, при a = 0,9, b = 1 + 1/8.', '0,8'),
                   ('Найдите значение выражения a / b, при a = 12, b = 20 * 3.', '0,2'),
                   ('Найдите значение выражения a / b, при a = 6,9 - 1,5, b = 2,4.', '2,25'),
                   ('Найдите значение выражения a * b, при a = 2,1, b = 9,6.', '20,16'),
                   ('Найдите значение выражения a / b, при a = 9,6, b = 1,6.', '6'),
                   ('Найдите значение выражения a / b, при a = 1 + 8/17, b = 12/17 + 2 + 7/11.', '0,44'),
                   ('Найдите значение выражения a * b, при a = 2 + 3/4 + 2 + 1/5, b = 16.', '79,2'),
                   ('Найдите значение выражения a * b + c, при a = 0,6, b = (-10)^3, c = 50.', '-550'),
                   ('Найдите значение выражения a * b * c, при a = 0,03, b = 0,3, c = 30000.', '270')
                   """)
    cursor.execute("""INSERT INTO MainQuestion2(Question, Answer) VALUES
    ('Найдите значение выражения 5{11} * 2{2} * {22}.', '220'),
    ('Найдите значение выражения (8b-8)(8b+8) - 8b(8b+8), при b = 2,6.', '-230,4'),
    ('Найдите значение выражения (2x + 3y)^2 - 3x(4x/3 + 4y), при x = -1,038, y = {3}.', '27'),
    ('Найдите значение выражения a^12 * (a^-4)^4, при a = -1/2.', '16'),
    ('Найдите значение выражения (2 - c)^2 - c(c + 4), при c = 0,5.', '0'),
    ('Найдите значение выражения (2c - 4)/(cd - 2d), при c = 0,5, d = 5.', '0,4'),
    ('Найдите значение выражения {90 * 30 * 3}.', '90'),
    ('Найдите значение выражения (x - 3) / ((x^2 - 6x + 9)/(x + 3)), при x = -21.', '0,75'),
    ('Найдите значение выражения {(4{2} - 7)^2} + 4{2}.', '7'),
    ('Найдите значение выражения (15x^2)/(3x - 2), при x = 0,5.', '-10')
    """)
    cursor.execute("""INSERT INTO MainQuestion3(Question, Answer) VALUES
        ('Решите уравнение: a = b, при a = (5x+4)/2 + 3, b = 9x/4.', '-20'),
        ('Решите уравнение: 3x + 5 + (x + 5) = (1 - x) + 4.', '-1'),
        ('Решите уравнение: x - 6/x = -1.', '-32'),
        ('Решите уравнение: (x - 4)^2 + (x + 9)^2 = 2x^2.', '-9,7'),
        ('Решите уравнение: (5x + 4)/2 + 3 = 9x/4', '-20'),
        ('Решите уравнение: (x - 6)/2 - x/3 = 3.', '36'),
        ('Решите уравнение: -2x^2 + x + 7 = -1x^2 + 5x + (-2 - x^2).', '2,25'),
        ('Решите уравнение: 3 - x/7 = x/3.', '6,3'),
        ('Решите уравнение: -x - 2 + 3(x - 3) = 3(4 - x) - 3.', '4'),
        ('Решите уравнение: 2x^2 + 4x - 4 = x^2 + 5x + (-3 + x^2).', '-1')
        """)
    cursor.execute("""INSERT INTO MainQuestion4(Question, Answer) VALUES
    ('У бабушки 20 чашек: 5 с красными цветами, остальные с синими. Бабушка наливает чай в случайно выбранную чашку.
Найдите вероятность того, что это будет чашка с синими цветами.', '0,75'),
    ('В лыжных гонках участвуют 13 спортсменов из России, 2 спортсмена из Норвегии и 5 спортсменов из Швеции. 
Порядок, в котором спортсмены стартуют, определяется жребием.
Найдите вероятность того, что первым будет стартовать спортсмен не из России.', '0,35'),
    ('На экзамене 25 билетов, Сергей не выучил 3 из них. Найдите вероятность того, что ему попадётся выученный билет.',
    '0,88'),
    ('В каждой десятой банке кофе согласно условиям акции есть приз. Призы распределены по банкам случайно.
Варя покупает банку кофе в надежде выиграть приз. Найдите вероятность того, что Варя не найдет приз в своей банке.',
    '0,9'),
    ('На тарелке 12 пирожков: 5 с мясом, 4 с капустой и 3 с вишней. Наташа наугад выбирает один пирожок.
Найдите вероятность того, что он окажется с вишней.', '0,25'),
    ('На экзамене по геометрии школьнику достаётся одна задача из сборника.
Вероятность того, что эта задача по теме «Углы», равна 0,1.
Вероятность того, что это окажется задача по теме «Параллелограмм», равна 0,6.
В сборнике нет задач, которые одновременно относятся к этим двум темам.
Найдите вероятность того, что на экзамене школьнику достанется задача по одной из этих двух тем.', '0,7'),
    ('Телевизор у Маши сломался и показывает только один случайный канал. Маша включает телевизор.
В это время по трем каналам из двадцати показывают кинокомедии.
Найдите вероятность того, что Маша попадет на канал, где комедия не идет.', '0,85'),
    ('Для экзамена подготовили билеты с номерами от 1 до 50.
Какова вероятность того, что наугад взятый учеником билет имеет однозначный номер?', '0,18'),
    ('В фирме такси в данный момент свободно 20 машин: 9 черных, 4 желтых и 7 зеленых.
По вызову выехала одна из машин, случайно оказавшаяся ближе всего к заказчику.
Найдите вероятность того, что к нему приедет желтое такси.', '0,2'),
    ('Игральную кость бросают дважды. Найдите вероятность того, что хотя бы раз выпало число, большее 3.', '0,75')
    """)
    cursor.execute("""INSERT INTO MainQuestion5(Question, Answer) VALUES
    ('Найдите основание x, если площадь треугольника равна 28м^2, а высота h, проведённая к x, равна 14м', '4'),
    ('Мощность постоянного тока (в ваттах) вычисляется по формуле P = I^2 * R, где I—сила тока (в амперах),
R—сопротивление (в омах). Пользуясь этой формулой, найдите сопротивление R (в омах),
если мощность составляет 150 ватт, а сила тока равна 5 амперам.', '6'),
    ('Из формулы центростремительного ускорения a = ω2R найдите R (в метрах), если ω = 4 с−1 и a = 64 м/с2.', '4'),
    ('Период колебания математического маятника T (в секундах) приближенно можно вычислить по формуле T = 2{l},
где l — длина нити (в метрах). Пользуясь этой формулой, найдите длину нити маятника (в метрах),
период колебаний которого составляет 3 секунды.', '2,25'),
    ('Длину окружности l можно вычислить по формуле l = 2 * p * R, где R — радиус окружности (в метрах), p - число Пи.
Пользуясь этой формулой, найдите радиус окружности, если её длина равна 78 метрам. (Считать  Пи = 3).', '13'),
    ('Найдите высоту h, если основания трапеции равны 5 метров  и 7 метров, а её площадь 24 метров в квадрате.', '4'),
    ('Расстояние s (в метрах) до места удара молнии можно приближённо вычислить по формуле s = 330t,
где t — количество секунд, прошедших между вспышкой молнии и ударом грома.
Определите, на каком расстоянии от места удара молнии находится наблюдатель, если t = 17.
Ответ дайте в километрах, округлив его до целых.', '6'),
    ('Зная длину своего шага, человек может приближённо подсчитать пройденное им расстояние s по формуле s = n * l,
где n — число шагов, l — длина шага.
Какое расстояние прошёл человек, если l = 80см, n = 1600? Ответ выразите в километрах.', '1,28'),
    ('Из формулы центростремительного ускорения a = ω^2 * R найдите R (в метрах), если ω = 4 с^−1 и a = 64 м/с^2.',
    '4'),
    ('В фирме «Эх, прокачу!» стоимость поездки на такси (в рублях) рассчитывается по формуле C = 150 + 11 * (t - 5),
где t — длительность поездки, выраженная в минутах (t > 5).
Пользуясь этой формулой, рассчитайте стоимость 8-минутной поездки.', '183')
    """)
    cursor.execute("""INSERT INTO MainQuestion6(Question, Answer) VALUES
    ('Диагонали AC и BD параллелограмма ABCD пересекаются в точке O, AC=12, BD=20, AB=7. Найдите DO.', '10'),
    ('В треугольнике ABC угол C = 90°, BC = 8, синус A = 0,4. Найдите AB.', '20'),
    ('В трапецию, сумма длин боковых сторон которой равна 18, вписана окружность.
Найдите длину средней линии трапеции.', '9'),
    ('Биссектрисы углов B и C треугольника ABC пересекаются в точке K.
Найдите угол BKC, если угол B = 40°, а угол C = 80°.', '120'),
    ('В выпуклом четырехугольнике ABCD известно, что AB = BC, AD = CD, угол B = 169, угол D = 175.
Найдите угол A. Ответ дайте в градусах.', '8'),
    ('В ромбе ABCD угол ABC равен 72°. Найдите угол ACD. Ответ дайте в градусах.', '54'),
    ('Высота равностороннего треугольника равна 56{3}. Найдите его периметр.', '336'),
    ('В остроугольном треугольнике ABC высота AH равна 2{15}, а сторона AB равна 8. Найдите косинус угла B.', '0,25'),
    ('Площадь прямоугольного треугольника равна 648{3}. Один из острых углов равен 30°.
Найдите длину катета, лежащего напротив этого угла.', '36'),
    ('В остроугольном треугольнике ABC проведена высота BH, угол BAC = 37°. Найдите угол ABH. Ответ дайте в градусах.',
    '53')
        """)
    cursor.execute("""INSERT INTO MainQuestion7(Question, Answer) VALUES
    ('Клиент взял в банке кредит в размере 50 000 р. на 5 лет под 20% годовых.
Какую сумму он должен вернуть в банк в конце срока,
если проценты начисляются ежегодно на текущую сумму долга и весь кредит с процентами возвращается в банк после срока?',
'124416'),
    ('Занятия йогой начинают с 15 минут в день и увеличивают на 10 минут время каждый следующий день.
Сколько дней следует заниматься йогой в указанном режиме, чтобы суммарная продолжительность занятий составила 2 часа?',
'4'),
    ('В фирме «Родник» цена колодца из железобетонных колец рассчитывается по формуле C = 6000 + 4100 * n (рублей),
где n — число колец, установленных при рытье колодца.
Пользуясь этой формулой, рассчитайте цену колодца из 5 колец (в рублях).', '26500'),
    ('Мощности пяти различных электромоторов составляют возрастающую геометрическую прогрессию.
Мощность самого слабого электромотора — 5 кВт, а третьего по мощности — 20 кВт.
Найдите мощность самого мощного электромотора, ответ дайте в кВт.', '80'),
    ('В фирме «Родник» стоимость (в рублях) колодца из железобетонных колец рассчитывается по формуле С=600 + 4100 * n,
где n—число колец, установленных при рытье колодца. Пользуясь этой формулой, рассчитайте стоимость колодца из 5 колец.',
'21100'),
    ('Алик, Миша и Вася покупали блокноты и трехкопеечные карандаши.
Алик купил 2 блокнота и 4 карандаша, Миша — блокнот и 6 карандашей, Вася — блокнот и 3 карандаша.
Оказалось, что суммы, которые уплатили Алик, Миша и Вася, образуют геометрическую прогрессию. Сколько стоит блокнот?',
'18'),
    ('В амфитеатре 13 рядов. В первом ряду 17 мест, а в каждом следующем на 2 места больше, чем в предыдущем.
Сколько всего мест в амфитеатре?', '377'),
    ('В лесу живут белки, каждая из которых, придя на опушку, съедает 10 орехов. В первый день на опушку пришли 6 белок.
В каждый следующий на опушку приходило на две белки больше. Сколько орехов съели белки за 30 дней?', '10500'),
    ('Бизнесмен Бубликов получил в 2000 году прибыль в размере 5000 рублей.
Каждый следующий год его прибыль увеличивалась на 300% по сравнению с предыдущим годом.
Сколько рублей заработал Бубликов за 2003 год?', '320000'),
    ('При свободном падении тело прошло в первую секунду 5 м, а в каждую следующую на 10 м больше.
Найдите глубину шахты, если свободно падающее тело достигло его дна через 5 с после начала падения.', '125')
    """)
    cursor.execute("""INSERT INTO MainQuestion8(Question, Answer) VALUES
    ('В треугольнике одна из сторон равна 10, другая равна 10{2}, а угол между ними равен 135°.
Найдите площадь треугольника.', '50'),
    ('Найдите площадь квадрата, если его диагональ равна 1.', '0,5'),
    ('Высота BH параллелограмма ABCD делит его сторону AD на отрезки AH = 7 и HD = 72.
Диагональ параллелограмма BD равна 97. Найдите площадь параллелограмма.', '5135'),
    ('В прямоугольном треугольнике гипотенуза равна 10, а один из острых углов равен 45°.
Найдите площадь треугольника.', '25'),
    ('Периметр равнобедренного треугольника равен 16, а боковая сторона — 5. Найдите площадь треугольника.', '12'),
    ('В прямоугольнике одна сторона равна 96, а диагональ равна 100. Найдите площадь прямоугольника.', '2688'),
    ('В треугольнике ABC известно, что DE — средняя линия. Площадь треугольника CDE равна 57.
Найдите площадь треугольника ABC.', '228'),
    ('В ромбе сторона равна 10, одна из диагоналей — 5({6} - {2}), а угол, лежащий напротив этой диагонали, равен 30°.
Найдите площадь ромба.', '50'),
    ('В прямоугольном треугольнике один из катетов равен 35, а угол, лежащий напротив него равен 45∘.
Найдите площадь треугольника.', '612,5'),
    ('Сторона квадрата равна 10. Найдите его площадь.', '100')
    """)
    cursor.execute("""INSERT INTO MainQuestion9(Question, Answer) VALUES
    ('Центр окружности, описанной около треугольника ABC, лежит на стороне AB.
Найдите угол ABC, если угол BAC равен 53°. Ответ дайте в градусах.', '37'),
    ('На отрезке AB выбрана точка C так, что AC = 75 и BC = 10. Построена окружность с центром A, проходящая через C.
Найдите длину отрезка касательной, проведённой из точки B к этой окружности.', '40'),
    ('Окружность с центром в точке O описана около равнобедренного треугольника ABC, в котором AB=BC и ∠ABC=62°.
Найдите величину угла BOC. Ответ дайте в градусах.', '118'),
    ('В окружности с центром O отрезки AC и BD — диаметры. Центральный угол AOD равен 124°. Найдите вписанный угол ACB.
Ответ дайте в градусах.', '28'),
    ('Радиус окружности, вписанной в равносторонний треугольник, равен 5. Найдите высоту этого треугольника.', '15'),
    ('Боковая сторона равнобедренного треугольника равна 4. Угол при вершине, противолежащий основанию, равен 120°.
Найдите диаметр окружности, описанной около этого треугольника.', '8'),
    ('Треугольник ABC вписан в окружность с центром в точке O.
Точки O и C лежат в одной полуплоскости относительно прямой AB Найдите угол ACB, если угол AOB равен 153°.
Ответ дайте в градусах', '76,5'),
    ('Отрезок AB = 24 касается окружности радиуса 10 с центром O в точке B. Окружность пересекает отрезок AO в точке D.
Найдите AD.', '16'),
    ('Радиус окружности, описанной около квадрата, равен 34{2}. Найдите длину стороны этого квадрата.', '68'),
    ('Найдите площадь квадрата, описанного вокруг окружности радиуса 39.', '6084')
    """)
    cursor.execute("""INSERT INTO MainQuestion10(Question, Answer) VALUES
    ('Решите уравнение: x^2 − 49 = 0.Если уравнение имеет более одного корня, в ответ запишите меньший из корней.',
'-7'),
    ('Найдите корень уравнения 8 + 7x = 9x + 4.', '2'),
    ('Решите уравнение x - x/7 = 15/7.', '2,5'),
    ('Решите уравнение 4x + 7 = 0.', '-1,75'),
    ('Найдите корень уравнения x + x/11 = 24/11.', '2'),
    ('Решите уравнение 9 + 10(3x - 10) = 2.', '3,1'),
    ('Решите уравнение (- x - 4)(3x + 3) = 0, запишите наибольший корень.', '-1'),
    ('Решите уравнение x^2 + 6x - 16 = 0. Если корней больше одного, в ответе укажите меньший корень.', '-8'),
    ('Найдите корни уравнения x^2 + 6 = 5x. Если корней несколько, запишите наименьший.', '23'),
    ('При каком значении x значения выражений 3x + 4 и 7x + 6 равны?', '-2,5')
    """)
    connect.commit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 600)
        MainWindow.setFixedSize(500, 600)
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFixedSize(500, 600)
        self.InputAnswer = QLineEdit(self.centralwidget)
        self.InputAnswer.setGeometry(QtCore.QRect(40, 330, 420, 60))
        self.InputAnswer.setObjectName("InputAnswer")
        self.InputAnswer.setStyleSheet("padding: 10px;\
        background-color: \
                           rgb(255, 255, 255); \
                           color: rgba(0,0,0,255); \
                           border-width: 3px; \
                           border-color: rgb(0,0,0); \
                           font: bold 20px; \
                           padding: 3px; min-width: 1em; border-style: outset;")
        self.AnswerButton = QPushButton(self.centralwidget)
        self.AnswerButton.setGeometry(QtCore.QRect(150, 420, 191, 51))
        self.AnswerButton.setObjectName("AnswerButton")
        self.AnswerButton.setStyleSheet("padding: 10px;\
        background-color: \
                           rgb(255, 255, 255); \
                           color: rgba(0,0,0,255); \
                           border-radius: 20px; border-width: 2px; \
                           border-color: rgb(0,0,0); \
                           font: bold 20px; \
                           padding: 3px; min-width: 1em; border-style: outset;")
        self.Question = QTextBrowser(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(30, 120, 440, 190))
        self.Question.setObjectName("textBrowser")
        self.Question.setStyleSheet("padding: 10px;\
        background-color: \
                           rgb(255, 255, 255); \
                           color: rgba(0,0,0,255); \
                           border-radius: 20px; border-width: -1px; \
                           border-color: rgb(0,0,0); \
                           font: bold 20px; \
                           padding: 3px; min-width: 1em; border-style: outset;")
        self.ResultsOfTest = QTextBrowser(self.centralwidget)
        self.ResultsOfTest.setGeometry(QtCore.QRect(20, 20, 460, 520))
        self.ResultsOfTest.setObjectName("textBrowser")
        self.ReadyForTestButton = QPushButton(self.centralwidget)
        self.ReadyForTestButton.setGeometry(QtCore.QRect(90, 250, 320, 70))
        self.ReadyForTestButton.setObjectName("ReadyForTest")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 38))
        self.menubar.setObjectName("menubar")
        self.menuTest = QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTest.menuAction())
        self.AnswerButton.setHidden(True)
        self.InputAnswer.setHidden(True)
        self.Question.setHidden(True)
        self.ResultsOfTest.setHidden(True)
        self.ReadyForTestButton.setStyleSheet("margin: 1px; padding: 10px; \
      background-color: \
                           rgb(255,255,250); \
                           color: rgba(0,0,0,255); \
                           border-radius: 10px; border-width: 2px; \
                           border-color: rgb(0,0,0); \
                           font: bold 14px; \
                           min-width: 10em; \
                           padding: 6px; border-style: outset;")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AnswerButton.setText(_translate("MainWindow", "Ответить"))
        self.ReadyForTestButton.setText(_translate("MainWindow", "Начать Тест"))
        self.menuTest.setTitle(_translate("MainWindow", "Test"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.list_of_user_answers = list()
        self.list_of_id = list()
        self.question_number = 1
        self.initUI()
        self.setStyleSheet("background-color: rgb(204, 204, 255);")
    def initUI(self):
        self.ReadyForTestButton.clicked.connect(self.start_test)
        mainquestion_number = 'MainQuestion' + str(self.question_number)
        id_select = random.randint(1, 10)
        self.list_of_id.append(id_select)
        question_from_db = 'SELECT Question FROM %s WHERE _id = %s' % (mainquestion_number, id_select)
        question_from_db = cursor.execute(question_from_db).fetchall()[0]
        self.Question.setText(question_from_db[0])
        self.AnswerButton.clicked.connect(self.next_question)

    def start_test(self):
        self.question_number = 1
        self.ReadyForTestButton.setHidden(True)
        self.AnswerButton.setHidden(False)
        self.InputAnswer.setHidden(False)
        self.Question.setHidden(False)

    def next_question(self):
        self.list_of_user_answers.append(self.InputAnswer.text())
        self.question_number += 1
        if self.question_number > 10:
            self.results_of_test()
        else:
            mainquestion = 'MainQuestion' + str(self.question_number)
            id_select = random.randint(1, 10)
            self.list_of_id.append(id_select)
            question_from_db = 'SELECT Question FROM %s WHERE _id = %s' % (mainquestion, id_select)
            question = cursor.execute(question_from_db).fetchall()[0][0]
            self.Question.setText(question)

    def results_of_test(self):
        self.ResultsOfTest.setHidden(False)
        self.ReadyForTestButton.setHidden(True)
        self.AnswerButton.setHidden(True)
        self.InputAnswer.setHidden(True)
        self.Question.setHidden(True)
        list_of_answers = list()
        for ir in range(1, 11):
            mainanswer = 'MainQuestion' + str(ir)
            id_select = self.list_of_id[ir - 1]
            answer_from_db = 'SELECT Answer FROM %s WHERE _id = %s' % (mainanswer, id_select)
            answer = cursor.execute(answer_from_db).fetchall()[0][0]
            user_answer = self.list_of_user_answers[ir - 1]
            answer_result = 'Вопрос ' + str(ir) + ': Правильный ответ - ' + answer + ', введённый - ' + user_answer + '.'
            list_of_answers.append(answer_result)
        self.ResultsOfTest.setText('\n'.join(list_of_answers))


def except_hook(cls,exception, tryceback):
    sys.__excepthook__(cls, exception, tryceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())