from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QStringListModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import resource
import os
import json

# ======= Main window All matrial setup here =======


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(588, 566)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#0a0211;\n"
        "border:None;")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 14))
        font = QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#d1d11f;")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hist_title = QLabel(self.centralwidget)
        self.hist_title.setObjectName(u"hist_title")
        font1 = QFont()
        font1.setPointSize(10)
        self.hist_title.setFont(font1)
        self.hist_title.setStyleSheet(u"#hist_title{\n"
        "color:white;\n"
        "border-radius:5px;\n"
        "padding:2px;\n"
        "}\n"
        "\n"
        "#hist_title:hover{\n"
        "background-color:#292929;\n"
        "}")

        self.horizontalLayout.addWidget(self.hist_title)

        self.btn_hist_clear = QPushButton(self.centralwidget)
        self.btn_hist_clear.setObjectName(u"btn_hist_clear")
        self.btn_hist_clear.setMaximumSize(QSize(70, 16777215))
        self.btn_hist_clear.setStyleSheet(u"background-color:#eef209;\n"
        "border-radius:8px;")
        icon = QIcon()
        icon.addFile(u"clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_hist_clear.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_hist_clear)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.input_fild = QLineEdit(self.centralwidget)
        self.input_fild.setObjectName(u"input_fild")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_fild.sizePolicy().hasHeightForWidth())
        self.input_fild.setSizePolicy(sizePolicy)
        self.input_fild.setMaximumSize(QSize(16777215, 100))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(18)
        self.input_fild.setFont(font2)
        self.input_fild.setStyleSheet(u"#input_fild{\n"
        "border:None;\n"
        "background-color:#0a0211;\n"
        "color:white;\n"
        "}")
        self.input_fild.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.input_fild)

        self.input_fild1 = QLineEdit(self.centralwidget)
        self.input_fild1.setObjectName(u"input_fild1")
        sizePolicy.setHeightForWidth(self.input_fild1.sizePolicy().hasHeightForWidth())
        self.input_fild1.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(18)
        self.input_fild1.setFont(font3)
        self.input_fild1.setStyleSheet(u"#input_fild1{\n"
        "border:None;\n"
        "color:white;\n"
        "}")
        self.input_fild1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.input_fild1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color:white;")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setMaximumSize(QSize(350, 16777215))
        self.listView.setStyleSheet("""
        QListView {
            background-color: #101010;
            color: white;
            font-size: 16px;
            border: none;
        }

        QListView::item {
            padding: 10px;
            color: white;
            border-bottom: 1px solid #444;
        }

        QListView::item:selected {
            background-color: #3498db;
            color: white;
        }
    """)

        self.gridLayout_2.addWidget(self.listView, 1, 1, 2, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")

# ===== Main button import here ======
        
        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        self.btn_9.setFont(font4)
        self.btn_9.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setFont(font4)
        self.btn_8.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(16)
        self.btn_add.setFont(font5)
        self.btn_add.setStyleSheet(u"QPushButton{\n"
        "background-color:#101010  ;\n"
        "color:#d1d11f;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#292929  ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_add, 2, 3, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        self.btn_sub.setFont(font5)
        self.btn_sub.setStyleSheet(u"QPushButton{\n"
        "background-color:#101010  ;\n"
        "color:#d1d11f;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#292929  ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_sub, 1, 3, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setPointSize(12)
        self.btn_div.setFont(font6)
        self.btn_div.setStyleSheet(u"QPushButton{\n"
        "background-color:#101010  ;\n"
        "color:#d1d11f;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#292929  ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_div, 0, 1, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        self.btn_backspace.setStyleSheet(u"QPushButton{\n"
        "background-color:#101010  ;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#292929  ;\n"
        "}")
        icon1 = QIcon()
        icon1.addFile(u"backspace.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_backspace, 0, 3, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy)
        self.btn_mul.setFont(font6)
        self.btn_mul.setStyleSheet(u"QPushButton{\n"
        "background-color:#101010  ;\n"
        "color:#d1d11f;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#292929  ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_mul, 0, 2, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setFont(font4)
        self.btn_3.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setFont(font4)
        self.btn_6.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setFont(font4)
        self.btn_2.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setFont(font4)
        self.btn_dot.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_dot, 4, 2, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setFont(font4)
        self.btn_0.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_allclear = QPushButton(self.centralwidget)
        self.btn_allclear.setObjectName(u"btn_allclear")
        sizePolicy.setHeightForWidth(self.btn_allclear.sizePolicy().hasHeightForWidth())
        self.btn_allclear.setSizePolicy(sizePolicy)
        self.btn_allclear.setFont(font6)
        self.btn_allclear.setStyleSheet(u"QPushButton{\n"
        "background-color:#101010  ;\n"
        "color:#d1d11f;\n"
        "}\n"
        "\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:#292929  ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_allclear, 0, 0, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setFont(font4)
        self.btn_7.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setFont(font4)
        self.btn_4.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setFont(font4)
        self.btn_1.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_mod = QPushButton(self.centralwidget)
        self.btn_mod.setObjectName(u"btn_mod")
        sizePolicy.setHeightForWidth(self.btn_mod.sizePolicy().hasHeightForWidth())
        self.btn_mod.setSizePolicy(sizePolicy)
        self.btn_mod.setFont(font4)
        self.btn_mod.setStyleSheet(u"QPushButton{\n"
        "background-color:#1D1D1D;\n"
        "color:white;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#292929 ;\n"
        "}")

        self.gridLayout.addWidget(self.btn_mod, 4, 0, 1, 1)

        self.btn_result = QPushButton(self.centralwidget)
        self.btn_result.setObjectName(u"btn_result")
        sizePolicy.setHeightForWidth(self.btn_result.sizePolicy().hasHeightForWidth())
        self.btn_result.setSizePolicy(sizePolicy)
        self.btn_result.setFont(font5)
        self.btn_result.setStyleSheet(u"QPushButton{\n"
        "background-color:#eef209;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color:#9CA000;\n"
        "}\n"
        "")

        self.gridLayout.addWidget(self.btn_result, 3, 3, 2, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 588, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.hist_title.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.btn_hist_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.input_fild.setText("")
        self.input_fild1.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_backspace.setText("")
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_allclear.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mod.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btn_result.setText(QCoreApplication.translate("MainWindow", u"=", None))
        # self.model.setStringList(QCoreApplication.translate("MainWindow", u"My list", None))
    # retranslateUi


# ===== Here accesec to main ui and button connected on main ui =======

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = QStringListModel()
        self.ui.listView.setModel(self.model)

        self.history_file = "history.json"
        self.history = []

        self.load_history()
        self.model.setStringList(self.history)

        self.result_shown = False

        

        # ===== button connected =====

        self.ui.btn_0.clicked.connect(self.btn_clicked)
        self.ui.btn_1.clicked.connect(self.btn_clicked)
        self.ui.btn_2.clicked.connect(self.btn_clicked)
        self.ui.btn_3.clicked.connect(self.btn_clicked)
        self.ui.btn_4.clicked.connect(self.btn_clicked)
        self.ui.btn_5.clicked.connect(self.btn_clicked)
        self.ui.btn_6.clicked.connect(self.btn_clicked)
        self.ui.btn_7.clicked.connect(self.btn_clicked)
        self.ui.btn_8.clicked.connect(self.btn_clicked)
        self.ui.btn_9.clicked.connect(self.btn_clicked)

        self.ui.btn_add.clicked.connect(self.btn_clicked)
        self.ui.btn_sub.clicked.connect(self.btn_clicked)
        self.ui.btn_mul.clicked.connect(self.btn_clicked)
        self.ui.btn_div.clicked.connect(self.btn_clicked)

        self.ui.btn_dot.clicked.connect(self.btn_clicked)
        self.ui.btn_mod.clicked.connect(self.btn_clicked)


        self.ui.btn_allclear.clicked.connect(self.all_clear)
        self.ui.btn_backspace.clicked.connect(self.delete)
        
        self.ui.btn_result.clicked.connect(self.calculator)


        self.ui.btn_hist_clear.clicked.connect(self.clear_hist)


    def btn_clicked(self):
        value= self.sender().text()

        if self.result_shown:
            self.ui.input_fild1.clear()
            self.result_shown = False

        self.ui.input_fild1.insert(value)

    def all_clear(self):
        self.ui.input_fild1.clear()
        self.ui.label_3.clear()

    def delete(self):
        text = self.ui.input_fild1.text()
        self.ui.input_fild1.setText(text[:-1])

#  ===== History Save in JSON =====

    def save_history(self):
        with open(self.history_file , "w") as file:
            json.dump(self.history , file , indent=4)

#  ===== History load in JSON =====
    
    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                self.history = json.load(file)


#  ===== main calculator here=====

    def calculator(self):

        input = self.ui.input_fild1.text()

        for operator in ("+","-","*","/","%"):
            if operator in input:
                value = input.split(operator)

                num1 = float(value[0])
                num2 = float(value[1])

                if num1.is_integer():
                    num1 = int(num1)
                if num2.is_integer():
                    num2 = int(num2)
                self.calculated_result(num1,operator,num2)
                break

    def calculated_result(self,num1,operator,num2):
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else :
                    result = "error"
            elif operator == "%":
                    if num2 != 0 :
                        result = num1 % num2
                    else :
                        result = "error"
            self.result_equal(result)
            if result is not None:
                self.hist_show(num1,operator,num2,result)
        except ValueError:
            self.result = "Value error"


    def result_equal(self,result):
        if isinstance(result,float) and result.is_integer():
            result = int(result)
        self.ui.label_3.setText(str(result))
        self.result_shown = True
        
#  ===== Here Show Calculation history =====

    def hist_show(self,num1,operator,num2,result):
        if result is not None:
            calculation = f"{num1} {operator} {num2} = {result}"
            self.history.append(calculation)
            self.model.setStringList(self.history)
            self.save_history()

#  ===== Here clear Calculation history =====

    def clear_hist(self):
        self.history.clear()
        self.model.setStringList(self.history)
        self.save_history()


import sys
app = QApplication(sys.argv)
window = Mainwindow()
window.show()
sys.exit(app.exec_())