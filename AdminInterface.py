import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit


class User():
    def __init__(self):
        self.email = ''
        self.barcode = ''
        self.groups = []


class NewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 450, 500)
        self.setWindowTitle('Новый пользователь')

        self.user = User()

        self.email_label = QLabel(self)
        self.email_label.setText('Email:')
        self.email_label.move(80, 30)

        self.email_gap = QLineEdit(self)
        self.email_gap.move(80, 70)

        self.barcode_label = QLabel(self)
        self.barcode_label.setText('Штих-код:')
        self.barcode_label.move(80, 130)

        self.barcode_gap = QLineEdit(self)
        self.barcode_gap.move(80, 170)

        self.group_label = QLabel(self)
        self.group_label.setText('По одной введите группы пользователя:')
        self.group_label.move(80, 230)

        self.group_gap = QLineEdit(self)
        self.group_gap.move(80, 270)

        self.add_group_btn = QPushButton('Добавить группу в список групп', self)
        self.add_group_btn.resize(self.add_group_btn.sizeHint())
        self.add_group_btn.move(75, 310)
        self.add_group_btn.clicked.connect(self.add_group)

        self.btn = QPushButton('Добавить в базу', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(40, 380)
        self.btn.clicked.connect(self.user_init)

        self.btn = QPushButton('Завершить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(275, 380)
        self.btn.clicked.connect(self.close_all)

    def add_group(self):
        if self.group_gap.text() == '':
            return
        self.user.groups.append(self.group_gap.text())
        self.group_gap.setText('')

    def user_init(self):
        self.user.email = self.email_gap.text()
        self.user.email.join(list(filter(lambda x: x.isalpha(), self.user.email)))
        if self.user.email == '':
            return
        self.email_gap.setText('')
        self.user.barcode = self.barcode_gap.text()
        if self.user.barcode == '':
            return
        self.user.barcode = int(self.user.barcode)
        self.barcode_gap.setText('')
        self.user.groups = list(set(self.user.groups))
        self.send(self.convert_to_json())

    def convert_to_json(self):
        user_dict = {}
        user_dict['email'] = self.user.email
        user_dict['barcode'] = self.user.barcode
        user_dict['groups'] = self.user.groups
        return json.dumps(user_dict)

    def send(self, json_file):
        # отправить json_file нового пользователя на сервер
        pass

    def close_all(self):
        sys.exit(app.exec_())


class Group():
    def __init__(self):
        self.name = ''
        self.members = []


class NewGroup(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 450, 400)
        self.setWindowTitle('Новая группа')

        self.group = Group()

        self.name_label = QLabel(self)
        self.name_label.setText('Название:')
        self.name_label.move(80, 30)

        self.name_gap = QLineEdit(self)
        self.name_gap.move(80, 70)

        self.member_label = QLabel(self)
        self.member_label.setText('По одному введите email участников группы:')
        self.member_label.move(80, 130)

        self.member_gap = QLineEdit(self)
        self.member_gap.move(80, 170)

        self.add_member_btn = QPushButton('Добавить участника', self)
        self.add_member_btn.resize(self.add_member_btn.sizeHint())
        self.add_member_btn.move(75, 210)
        self.add_member_btn.clicked.connect(self.add_member)

        self.btn = QPushButton('Добавить в базу', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(40, 280)
        self.btn.clicked.connect(self.group_init)

        self.btn = QPushButton('Завершить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(275, 280)
        self.btn.clicked.connect(self.close_all)

    def add_member(self):
        new_member = self.member_gap.text()
        new_member.join(list(filter(lambda x: x.isalpha(), new_member)))
        if new_member == '':
            return
        self.group.members.append(new_member)
        self.member_gap.setText('')

    def group_init(self):
        self.group.name = self.name_gap.text()
        if self.group.name == '':
            return
        self.name_gap.setText('')
        self.group.members = list(set(self.group.members))
        self.send(self.convert_to_json())

    def convert_to_json(self):
        group_dict = {}
        group_dict['name'] = self.group.name
        group_dict['members'] = self.group.members
        return json.dumps(group_dict)

    def send(self, json_file):
        # отправить json_file новой группы на сервер
        pass

    def close_all(self):
        sys.exit(app.exec_())


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 400)

        self.btn_user = QPushButton('Добавить пользователей', self)
        self.btn_user.resize(self.btn_user.sizeHint())
        self.btn_user.move(50, 50)
        self.btn_user.clicked.connect(self.new_user)

        self.btn_group = QPushButton('Добавить группы', self)
        self.btn_group.resize(self.btn_group.sizeHint())
        self.btn_group.move(50, 150)
        self.btn_group.clicked.connect(self.new_group)

        self.btn_event = QPushButton('Добавить события', self)
        self.btn_event.resize(self.btn_event.sizeHint())
        self.btn_event.move(50, 250)
        self.btn_event.clicked.connect(self.new_event)

    def new_user(self):
        self.open_user_wind = NewUser()
        self.open_user_wind.show()

    def new_group(self):
        self.open_group_wind = NewGroup()
        self.open_group_wind.show()

    def new_event(self):
        # вызов окна для добавления нового мероприятия
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MainWidget()
    wid.show()
    sys.exit(app.exec())
