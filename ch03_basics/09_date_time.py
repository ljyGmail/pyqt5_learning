from PyQt5.QtCore import QDate, Qt

# 날짜 표시하기(QDate)

# 현재 날짜 출력하기
now = QDate.currentDate()
print(now.toString())

# 날짜 형식 설정하기
now = QDate().currentDate()
print(f'd.M.yy: {now.toString("d.M.yy")}')
print(f'dd.MM.yyyy: {now.toString("dd.MM.yyyy")}')
print(f'ddd.MMMM.yyyy: {now.toString("ddd.MMMM.yyyy")}')
print(f'Qt.ISODate: {now.toString(Qt.ISODate)}')
print(f'Qt.DefaultLocaleLongDate: {now.toString(Qt.DefaultLocaleLongDate)}')

# 시간 표시하기(QTime)

from PyQt5.QtCore import QTime

# 현재 시간 출력하기
time = QTime.currentTime()
print(f'time: {time.toString()}')

# 시간 형식 설정하기
time = QTime.currentTime()
print(f'h.m.s: {time.toString("h.m.s")}')
print(f'hh.mm.ss: {time.toString("hh.mm.ss")}')
print(f'hh.mm.ss.zzz: {time.toString("hh.mm.ss.zzz")}')
print(f'Qt.DefaultLocaleLongDate: {time.toString(Qt.DefaultLocaleLongDate)}')
print(f'Qt.DefaultLocaleShortDate: {time.toString(Qt.DefaultLocaleShortDate)}')

# 날짜와 시간 표시하기(QDateTime)
from PyQt5.QtCore import QDateTime

# 현재 날짜와 시간 출력하기
datetime = QDateTime.currentDateTime()
print(f'datetime: {datetime}')

# 날짜와 시간 형식 설정하기
datetime = QDateTime.currentDateTime()
print(f'd.M.yy hh:mm:ss: {datetime.toString("d.M.yy hh:mm:ss")}')
print(f'dd.MM.yyyy hh:mm:ss: {datetime.toString("dd.MM.yyyy hh:mm:ss")}')
print(f'Qt.DefaultLocaleLongDate: {datetime.toString(Qt.DefaultLocaleLongDate)}')
print(f'Qt.DefaultLocaleShortDate: {datetime.toString(Qt.DefaultLocaleShortDate)}')

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
