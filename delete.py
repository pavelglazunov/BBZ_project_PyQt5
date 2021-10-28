import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


app = QApplication([])
app.setStyleSheet("QLabel{font-size: 10pt;}")
w = QLabel()

L = open('politic.txt', encoding='utf-8').read().split('\n')
for i in L:
    w.setText(w.text() + i)

# Эта страница используется для информирования посетителей о нашей политике в отношении сбора, использования и раскрытия Личной информации, если кто-либо решил использовать наш Сервис.
#
# Если вы решите использовать наш Сервис, вы соглашаетесь на сбор и использование информации в отношении этой политики. Личная информация, которую мы собираем, используется для предоставления и улучшения Сервиса. Мы не будем использовать или передавать вашу информацию кому-либо, кроме случаев, описанных в настоящей Политике конфиденциальности.
#
# Термины, используемые в настоящей Политике конфиденциальности, имеют то же значение, что и в наших Положениях и условиях, которые доступны на BBZ (Big Batle Zaruba), если иное не определено в настоящей Политике конфиденциальности.
#
# Сбор и использование информации
#
# Для лучшего опыта при использовании нашего Сервиса мы можем потребовать, чтобы вы предоставили нам определенную личную информацию, включая, помимо прочего, IP-адрес, номер вашей карты, вашу душу (для дьявола).
# Информация, которую мы запрашиваем, будет храниться нами и использоваться, как описано в этой политике конфиденциальности.
#
# Приложение использует сторонние сервисы, которые могут собирать информацию, используемую для вашей идентификации.
#
#  Ссылка на политику конфиденциальности сторонних поставщиков услуг, используемых приложением
#
#  Печенье
#
#  Файлы cookie - это файлы с небольшим объемом данных, которые обычно используются в качестве анонимных уникальных идентификаторов. Они отправляются в ваш браузер с веб-сайтов, которые вы посещаете, и хранятся во внутренней памяти вашего устройства.
#
# Этот Сервис не использует эти «куки» явно. Однако приложение может использовать сторонний код и библиотеки, которые используют файлы cookie для сбора информации и улучшения своих услуг. У вас есть возможность принять или отклонить эти файлы cookie и узнать, когда файл cookie отправляется на ваше устройство. Если вы решите отказаться от наших файлов cookie, возможно, вы не сможете использовать некоторые части этого Сервиса.
#
# Безопасность
#
# Мы ценим ваше доверие к предоставлению нам вашей личной информации, поэтому мы стремимся использовать коммерчески приемлемые средства ее защиты. Но помните, что ни один метод передачи через Интернет или метод электронного хранения не является на 100% безопасным и надежным, и мы не можем гарантировать его абсолютную безопасность.
#
#  Конфиденциальность детей
#
#  Эти Услуги не предназначены для лиц младше 13 лет. Мы сознательно не собираем личную информацию от детей младше 13 лет. В случае, если мы обнаруживаем, что ребенок младше 13 лет предоставил нам личную информацию, мы немедленно удаляем ее с наших серверов. Если вы являетесь родителем или опекуном и знаете, что ваш ребенок предоставил нам личную информацию, свяжитесь с нами, чтобы мы могли предпринять необходимые действия.
#
# Изменения в настоящей Политике конфиденциальности
#
# Мы можем время от времени обновлять нашу Политику конфиденциальности. Таким образом, вам рекомендуется периодически просматривать эту страницу на предмет изменений. Мы сообщим вам о любых изменениях, разместив новую Политику конфиденциальности на этой странице.
#
# Эта политика действует с 2021-10-17.
#
#  Связаться с нами
#
# Если у вас есть какие-либо вопросы или предложения относительно нашей Политики конфиденциальности, не стесняйтесь обращаться к нам по адресу pavelpokrov4@gmail.com.
# ')
w.setFont(QFont('Arial', 40))

scroll_area = QScrollArea()
scroll_area.setWidget(w)

scroll_area.show()

app.exec()