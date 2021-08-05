# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'localization_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import time
import random
from PyQt4 import QtCore, QtGui
from SAF.misc.couch_wrapper import CouchWrapper
from MobileApps.libs.ma_misc.str_id_localization import StringProcessor


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

if (sys.version_info <= (3, 0)):
    # Python 2 code in this block
    str = unicode



def centerForm(form):
    frameGm = form.frameGeometry()
    screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
    centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    form.move(frameGm.topLeft())

global_db_connection = None
global_results_subbed = 0

class lst_db(object):
    def __init__(self, db_info):
        self.db = CouchWrapper(db_info["url"], "lst_records" , (db_info["user"], db_info["password"]))

    def get_record_list(self):
        db_rec = self.db.getAllViewResults("get_info", "rec_list")
        rec_list = {}
        for row in db_rec.rows:
            rec_list[tuple(row.key)] = row.value
        return rec_list

    def get_record(self, os_type, project_name, rec_id):
        db_rec = self.db.getViewResultByKey("get_info", "rec_by_id", startKey=[os_type, project_name, rec_id], endKey=[os_type, project_name, rec_id])
        if len(db_rec.rows) != 1:
            print("More or less than one record with key: "  + os_type + " " + project_name + " " + rec_id)
            sys.exit()
        else:
            return db_rec.rows[0]["value"]

    def save_record(self, data):
        self.db.saveRecord(data, doc_id = data["_id"])


class WelcomeScreen(QtGui.QDialog):
    def __init__(self, parent=None):
        super(WelcomeScreen, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(640, 200))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.buttonBox.clicked.connect(self.accept)
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateColor)
        self.timer.start(500)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Welcome To LST", None))
        self.label.setText(_translate("Dialog", "Welcome to the tool. For instructions please visit\nhttps://github.azc.ext.hp.com/QAMA/MobileApps/wiki/Localization-Tool\nCreated By Jay Yang\njiurong.yang@hp.com", None))

    def updateColor(self):
        r = str(random.randint(0,255))
        g = str(random.randint(0,255))
        b = str(random.randint(0,255))
        self.label.setStyleSheet("color: rgb(" + r +", " + g + ", " + b +");")
        self.buttonBox.setStyleSheet("color: rgb(" + r +", " + g + ", " + b +");")
    def accept(self):
        self.timer.stop()
        self.close()
        main_window = MainScreen(self)
        centerForm(main_window)
        main_window.show()

class MainScreen(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainScreen, self).__init__(parent)
        self.setupUi(self)
        self.setupConnection()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(590, 700)
        MainWindow.setMinimumSize(QtCore.QSize(590, 700))
        MainWindow.setMaximumSize(QtCore.QSize(590, 700))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(110, 30))
        self.label.setMaximumSize(QtCore.QSize(110, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.connectionStatusLbl = QtGui.QLabel(self.centralwidget)
        self.connectionStatusLbl.setMinimumSize(QtCore.QSize(80, 30))
        self.connectionStatusLbl.setMaximumSize(QtCore.QSize(80, 30))
        self.connectionStatusLbl.setStyleSheet(_fromUtf8("color: red;"))
        self.connectionStatusLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.connectionStatusLbl.setObjectName(_fromUtf8("connectionStatusLbl"))
        self.horizontalLayout.addWidget(self.connectionStatusLbl)
        self.connectBtn = QtGui.QPushButton(self.centralwidget)
        self.connectBtn.setMinimumSize(QtCore.QSize(70, 30))
        self.connectBtn.setMaximumSize(QtCore.QSize(70, 30))
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.horizontalLayout.addWidget(self.connectBtn)
        self.irrCB = QtGui.QCheckBox(self.centralwidget)
        self.irrCB.setMinimumSize(QtCore.QSize(160, 30))
        self.irrCB.setMaximumSize(QtCore.QSize(160, 30))
        self.irrCB.setObjectName(_fromUtf8("irrCB"))
        self.horizontalLayout.addWidget(self.irrCB)
        self.refreshBtn = QtGui.QPushButton(self.centralwidget)
        self.refreshBtn.setEnabled(False)
        self.refreshBtn.setMinimumSize(QtCore.QSize(85, 30))
        self.refreshBtn.setMaximumSize(QtCore.QSize(85, 30))
        self.refreshBtn.setObjectName(_fromUtf8("refreshBtn"))
        self.horizontalLayout.addWidget(self.refreshBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.recTreeView = QtGui.QTreeWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recTreeView.sizePolicy().hasHeightForWidth())
        self.recTreeView.setSizePolicy(sizePolicy)
        self.recTreeView.setStyleSheet(_fromUtf8("color: rgb(red;)"))
        self.recTreeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.recTreeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.recTreeView.setAlternatingRowColors(False)
        self.recTreeView.setItemsExpandable(False)
        self.recTreeView.setObjectName(_fromUtf8("recTreeView"))
        self.recTreeView.header().setDefaultSectionSize(120)
        self.recTreeView.header().setMinimumSectionSize(80)
        self.recTreeView.header().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.recTreeView)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.reviewRunBtn = QtGui.QPushButton(self.centralwidget)
        self.reviewRunBtn.setEnabled(False)
        self.reviewRunBtn.setObjectName(_fromUtf8("reviewRunBtn"))
        self.horizontalLayout_2.addWidget(self.reviewRunBtn)
        self.exitBtn = QtGui.QPushButton(self.centralwidget)
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.horizontalLayout_2.addWidget(self.exitBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuNew_Run = QtGui.QMenu(self.menubar)
        self.menuNew_Run.setObjectName(_fromUtf8("menuNew_Run"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
     
        self.newRunMI = QtGui.QAction(MainWindow)
        self.newRunMI.setObjectName(_fromUtf8("newRunAndroidMI"))
        self.loadRunAndroidMI = QtGui.QAction(MainWindow)
        self.loadRunAndroidMI.setObjectName(_fromUtf8("loadRunAndroidMI"))
        self.menuNew_Run.addAction(self.newRunMI)
        self.menubar.addAction(self.menuNew_Run.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Localization Str ID Tester", None))
        self.label.setText(_translate("MainWindow", "Data Base Status: ", None))
        self.connectionStatusLbl.setText(_translate("MainWindow", "Disconnected", None))
        self.connectBtn.setText(_translate("MainWindow", "Connect", None))
        self.irrCB.setText(_translate("MainWindow", "Include Reviewed Rec", None))
        self.refreshBtn.setText(_translate("MainWindow", "Refresh", None))
        self.recTreeView.headerItem().setText(0, _translate("MainWindow", "OS", None))
        self.recTreeView.headerItem().setText(1, _translate("MainWindow", "Project", None))
        self.recTreeView.headerItem().setText(2, _translate("MainWindow", "ID", None))
        self.recTreeView.headerItem().setText(3, _translate("MainWindow", "Recorded Time", None))
        self.recTreeView.headerItem().setText(4, _translate("MainWindow", "Reviewed", None))
        self.recTreeView.setColumnWidth(0, 80)
        self.recTreeView.setColumnWidth(1, 80)
        self.recTreeView.setColumnWidth(2, 80)
        self.recTreeView.setColumnWidth(3, 150)

        self.reviewRunBtn.setText(_translate("MainWindow", "Review Run", None))
        self.exitBtn.setText(_translate("MainWindow", "Exit", None))
        self.menuNew_Run.setTitle(_translate("MainWindow", "New Run", None))
        self.newRunMI.setText(_translate("MainWindow", "New Run", None))
        self.newRunMI.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.loadRunAndroidMI.setText(_translate("MainWindow", "Android", None))



    def setupConnection(self):
        self.newRunMI.triggered.connect(self.openNewAndroidRunWindow)
        self.refreshBtn.clicked.connect(self.reloadTreeWidget)
        self.recTreeView.itemSelectionChanged.connect(self.toggleReviewRunBtn)
        self.connectBtn.clicked.connect(self.establishDBConnection)
        self.exitBtn.clicked.connect(self.exitProgram)
        self.reviewRunBtn.clicked.connect(self.openReviewForm)


    def exitProgram(self):
        sys.exit()

    def openReviewForm(self):
        self.hide()
        recId = str(self.recTreeView.selectedItems()[0].text(2))
        osType = str(self.recTreeView.selectedItems()[0].text(0))
        projectName = str(self.recTreeView.selectedItems()[0].text(1))
        reviewRunWindow = RunReviewWindow(recId, projectName, osType, self)
        centerForm(reviewRunWindow)
        reviewRunWindow.show()

    def establishDBConnection(self):
        global global_db_connection
        if global_db_connection is None:       
            db_info = {"url": "http://hppsrv2:5984/", "user":"service", "password":"service"}
            global_db_connection = lst_db(db_info)

        self.connectionStatusLbl.setText("Connected")
        self.connectionStatusLbl.setStyleSheet("color: green;")
        self.refreshBtn.setEnabled(True)

    def reloadTreeWidget(self):
        rec_list = global_db_connection.get_record_list()
        self.recTreeView.clear()
        reviewed = self.irrCB.isChecked()
        for key, value in rec_list.items():
            if value[1] and not reviewed:
                continue
            item = QtGui.QTreeWidgetItem(self.recTreeView)
            item.setText(0, key[1])
            item.setText(1, key[2])
            item.setText(2, key[0])
            item.setText(3, value[0])
            item.setText(4, str(value[1]))

    def toggleReviewRunBtn(self):
        if self.recTreeView.selectedItems():
            self.reviewRunBtn.setEnabled(True)
        else:
            self.reviewRunBtn.setEnabled(False)

    def openNewAndroidRunWindow(self):
        new_run_android = NewRunAndroidScreen(self)
        centerForm(new_run_android)
        new_run_android.show()

class NewRunAndroidScreen(QtGui.QDialog):
    def __init__(self, parent=None):
        super(NewRunAndroidScreen, self).__init__(parent)
        self.parent = parent
        self.project_dict = {"ios":["HP Smart"], "android": ["HP Smart", "HPPS", "Mopria"], "other": ["Medallia"]} 
        self.setupUi(self)
        self.setupConnection()


    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(960, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(960, 250))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 250))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.osTypeLbl = QtGui.QLabel(Dialog)
        self.osTypeLbl.setMinimumSize(QtCore.QSize(200, 30))
        self.osTypeLbl.setMaximumSize(QtCore.QSize(200, 30))
        self.osTypeLbl.setObjectName(_fromUtf8("osTypeLbl"))
        self.horizontalLayout_5.addWidget(self.osTypeLbl)
        self.osTypeCbb = QtGui.QComboBox(Dialog)
        self.osTypeCbb.addItems(["android", "ios", "other"])
        self.osTypeCbb.setObjectName(_fromUtf8("osTypeCbb"))
        self.osTypeCbb.setCurrentIndex(0)
        self.osTypeCbb.setEditable(True)
        self.osTypeCbb.lineEdit().setReadOnly(True)
        self.osTypeCbb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_5.addWidget(self.osTypeCbb)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(200, 30))
        self.label_4.setMaximumSize(QtCore.QSize(200, 30))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.projectCbb = QtGui.QComboBox(Dialog)
        self.projectCbb.addItems(self.project_dict[str(self.osTypeCbb.currentText()).lower()])
        self.projectCbb.setObjectName(_fromUtf8("projectCbb"))
        self.projectCbb.setCurrentIndex(0)
        self.projectCbb.setEditable(True)
        self.projectCbb.lineEdit().setReadOnly(True)
        self.projectCbb.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_4.addWidget(self.projectCbb)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_3 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(200, 30))
        self.label_3.setMaximumSize(QtCore.QSize(200, 30))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.specDirPathTxt = QtGui.QLabel(Dialog)
        self.specDirPathTxt.setMinimumSize(QtCore.QSize(0, 30))
        self.specDirPathTxt.setMaximumSize(QtCore.QSize(16777215, 30))
        self.specDirPathTxt.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))

        self.specDirPathTxt.setText(_fromUtf8(""))
        self.specDirPathTxt.setObjectName(_fromUtf8("specDirPathTxt"))
        self.horizontalLayout.addWidget(self.specDirPathTxt)
        self.openSpecDirBtn = QtGui.QPushButton(Dialog)
        self.openSpecDirBtn.setMaximumSize(QtCore.QSize(130, 30))
        self.openSpecDirBtn.setObjectName(_fromUtf8("openSpecDirBtn"))
        self.horizontalLayout.addWidget(self.openSpecDirBtn)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        self.label_2.setMaximumSize(QtCore.QSize(200, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pkgLocationTxt = QtGui.QTextEdit(Dialog)
        self.pkgLocationTxt.setMinimumSize(QtCore.QSize(0, 30))
        self.pkgLocationTxt.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pkgLocationTxt.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))
        self.pkgLocationTxt.setObjectName(_fromUtf8("pkgLocationTxt"))
        self.horizontalLayout_2.addWidget(self.pkgLocationTxt)
        self.openPkgDirBtn = QtGui.QPushButton(Dialog)
        self.openPkgDirBtn.setMinimumSize(QtCore.QSize(130, 30))
        self.openPkgDirBtn.setMaximumSize(QtCore.QSize(130, 30))
        self.openPkgDirBtn.setObjectName(_fromUtf8("openPkgDirBtn"))
        self.horizontalLayout_2.addWidget(self.openPkgDirBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.testRunCkb = QtGui.QCheckBox(Dialog)
        self.testRunCkb.setMinimumSize(QtCore.QSize(100, 35))
        self.testRunCkb.setMaximumSize(QtCore.QSize(100, 35))
        self.testRunCkb.setChecked(True)
        self.testRunCkb.setObjectName(_fromUtf8("testRunCkb"))
        self.horizontalLayout_3.addWidget(self.testRunCkb)
        self.runTestBtn = QtGui.QPushButton(Dialog)
        self.runTestBtn.setObjectName(_fromUtf8("runTestBtn"))
        self.horizontalLayout_3.addWidget(self.runTestBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "New Run", None))
        self.osTypeLbl.setText(_translate("Dialog", "Platform Selection: ", None))
        self.label_3.setText(_translate("Dialog", "Spec Folder Location: ", None))
        self.openSpecDirBtn.setText(_translate("Dialog", "Select Folder", None))
        self.openPkgDirBtn.setText(_translate("Dialog", "Select File", None))

        self.label_2.setText(_translate("Dialog", "PKG Location (URL or File Path) : ", None))
        self.label_4.setText(_translate("Dialog", "Project Name:", None))

        self.testRunCkb.setText(_translate("Dialog", "Test Run", None))
        self.runTestBtn.setText(_translate("Dialog", "Run Test", None))

    def setupConnection(self):
        self.openSpecDirBtn.clicked.connect(self.openSpecDirBtnClicked)
        self.openPkgDirBtn.clicked.connect(self.openPkgDirBtnClicked)

        self.osTypeCbb.currentIndexChanged.connect(self.update_project_cbb)
        self.runTestBtn.clicked.connect(self.runTest)

    def update_project_cbb(self):
        self.projectCbb.clear()
        self.projectCbb.addItems(self.project_dict[str(self.osTypeCbb.currentText()).lower()])
        self.newRunFormChange()

    def newRunFormChange(self):
        if str(self.projectCbb.currentText()) == "Medallia":
            self.label_2.setText("Source JSON location: ")
            self.label_3.setText("Spec File Location: ")
            self.openSpecDirBtn.setText("Select File")
        else:
            self.label_2.setText("PKG Location (URL or File Path) : ")
            self.label_3.setText("Spec Folder Location: ")
            self.openSpecDirBtn.setText("Select Folder")


    def openPkgDirBtnClicked(self):
        file_path = str(QtGui.QFileDialog.getOpenFileName(self, "Select File"))
        if file_path != "":
            self.pkgLocationTxt.setText(str(file_path))

    def openSpecDirBtnClicked(self):
        if str(self.projectCbb.currentText()) == "Medallia":
            dir_path = str(QtGui.QFileDialog.getOpenFileName(self, "Select File"))
        else:
            dir_path = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if dir_path != "":
            self.specDirPathTxt.setText(str(dir_path))

    def runTest(self):
        global global_db_connection
        sp = StringProcessor(str(self.osTypeCbb.currentText()), global_db_connection.db)
        self.openSpecDirBtn.setEnabled(False)
        self.runTestBtn.setEnabled(False)
        self.pkgLocationTxt.setEnabled(False)
        self.testRunCkb.setEnabled(False)
        results = sp.new_run(str(self.projectCbb.currentText()), str(self.pkgLocationTxt.toPlainText()), str(self.specDirPathTxt.text()), test_run=self.testRunCkb.isChecked())
        if type(results) is dict:
            infoPopUp = TestRunInfoPopUp(self)
            centerForm(infoPopUp)
            infoPopUp.setupFormData(results)
            infoPopUp.show()
        self.openSpecDirBtn.setEnabled(True)
        self.runTestBtn.setEnabled(True)
        self.pkgLocationTxt.setEnabled(True)
        self.testRunCkb.setEnabled(True)
        if not self.testRunCkb.isChecked():
            finished = QtGui.QMessageBox(self.parent)
            finished.setIcon(QtGui.QMessageBox.Information)
            finished.setText("Test run complete")
            finished.setWindowTitle("Finished!")
            finished.setStandardButtons(QtGui.QMessageBox.Ok)
            finished.exec_()
            self.close()
        self.parent.reloadTreeWidget()

class TestRunInfoPopUp(QtGui.QDialog):
    def __init__(self, parent=None):
        super(TestRunInfoPopUp, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName(_fromUtf8("InfoDialog"))
        InfoDialog.resize(640, 450)
        InfoDialog.setMinimumSize(QtCore.QSize(640, 450))
        InfoDialog.setMaximumSize(QtCore.QSize(640, 450))
        self.verticalLayout = QtGui.QVBoxLayout(InfoDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.totalInAPKLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.totalInAPKLbl.setFont(font)
        self.totalInAPKLbl.setText(_fromUtf8(""))
        self.totalInAPKLbl.setObjectName(_fromUtf8("totalInAPKLbl"))
        self.verticalLayout.addWidget(self.totalInAPKLbl)
        self.totalInSpecLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.totalInSpecLbl.setFont(font)
        self.totalInSpecLbl.setText(_fromUtf8(""))
        self.totalInSpecLbl.setObjectName(_fromUtf8("totalInSpecLbl"))
        self.verticalLayout.addWidget(self.totalInSpecLbl)

        self.diffTotalLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.diffTotalLbl.setFont(font)
        self.diffTotalLbl.setText(_fromUtf8(""))
        self.diffTotalLbl.setObjectName(_fromUtf8("diffTotalLbl"))
        self.verticalLayout.addWidget(self.diffTotalLbl)


        self.passedLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.passedLbl.setFont(font)
        self.passedLbl.setText(_fromUtf8(""))
        self.passedLbl.setObjectName(_fromUtf8("passedLbl"))
        self.verticalLayout.addWidget(self.passedLbl)

        self.legacyPass = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.legacyPass.setFont(font)
        self.legacyPass.setText(_fromUtf8(""))
        self.legacyPass.setObjectName(_fromUtf8("legacyPassLbl"))
        self.verticalLayout.addWidget(self.legacyPass)

        self.failedMMLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.failedMMLbl.setFont(font)
        self.failedMMLbl.setText(_fromUtf8(""))
        self.failedMMLbl.setObjectName(_fromUtf8("failedMMLbl"))
        self.verticalLayout.addWidget(self.failedMMLbl)
        self.failedLMLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.failedLMLbl.setFont(font)
        self.failedLMLbl.setText(_fromUtf8(""))
        self.failedLMLbl.setObjectName(_fromUtf8("failedLMLbl"))
        self.verticalLayout.addWidget(self.failedLMLbl)
        self.failedMSLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.failedMSLbl.setFont(font)
        self.failedMSLbl.setText(_fromUtf8(""))
        self.failedMSLbl.setObjectName(_fromUtf8("failedMSLbl"))
        self.verticalLayout.addWidget(self.failedMSLbl)


        self.failedSELbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.failedSELbl.setFont(font)
        self.failedSELbl.setText(_fromUtf8(""))
        self.failedSELbl.setObjectName(_fromUtf8("failedSELbl"))
        self.verticalLayout.addWidget(self.failedSELbl)

        self.failedLCLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.failedLCLbl.setFont(font)
        self.failedLCLbl.setText(_fromUtf8(""))
        self.failedLCLbl.setObjectName(_fromUtf8("failedLCLbl"))
        self.verticalLayout.addWidget(self.failedLCLbl)



        self.notTestLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.notTestLbl.setFont(font)
        self.notTestLbl.setText(_fromUtf8(""))
        self.notTestLbl.setObjectName(_fromUtf8("notTestLbl"))
        self.verticalLayout.addWidget(self.notTestLbl)

        self.removedLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.removedLbl.setFont(font)
        self.removedLbl.setText(_fromUtf8(""))
        self.removedLbl.setObjectName(_fromUtf8("removedLbl"))
        self.verticalLayout.addWidget(self.removedLbl)

        self.unknownLbl = QtGui.QLabel(InfoDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.unknownLbl.setFont(font)
        self.unknownLbl.setText(_fromUtf8(""))
        self.unknownLbl.setObjectName(_fromUtf8("unknownLbl"))
        self.verticalLayout.addWidget(self.unknownLbl)
        self.acceptBtn = QtGui.QDialogButtonBox(InfoDialog)
        self.acceptBtn.setOrientation(QtCore.Qt.Horizontal)
        self.acceptBtn.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.acceptBtn.setObjectName(_fromUtf8("acceptBtn"))
        self.verticalLayout.addWidget(self.acceptBtn)

        self.retranslateUi(InfoDialog)
        QtCore.QObject.connect(self.acceptBtn, QtCore.SIGNAL(_fromUtf8("accepted()")), InfoDialog.accept)
        QtCore.QObject.connect(self.acceptBtn, QtCore.SIGNAL(_fromUtf8("rejected()")), InfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        InfoDialog.setWindowTitle(_translate("InfoDialog", "Test Run Info", None))

    def setupFormData(self, data_dict):
        result_dict = data_dict["result_dict"]
        totalSpec = data_dict["spec_total"]
        diff_total = data_dict["str_id_total_diff"]
        passed = 0
        legacyPassed = 0
        notTest = 0
        removed = 0
        failedLM = 0
        failedMM = 0
        failedMS = 0
        failedSE = 0
        failedLC = 0
        unknown = 0
        totalAPK = len(result_dict.keys())
        for key, value in result_dict.items():
            if value["result"] == "failed":
                if "(legacy)" in value["reason"]:
                    failedLC += 1
                elif "[1]" in value["reason"]:
                    failedMM += 1
                elif "[2]" in value["reason"]:
                    failedLM += 1
                elif "[3]" in value["reason"]:
                    failedMS += 1
                elif "[4]" in value["reason"]:
                    failedSE += 1
                
            elif value["result"] == "passed":
                if "[2]" in value["reason"] or "[3]" in value["reason"] or "[4]" in value["reason"]:
                    legacyPassed += 1
                else:
                    passed += 1
            elif value["result"] == "not test":
                notTest += 1
            elif value["result"] == "removed":
                removed += 1
            else:
                unknown += 1
        self.totalInAPKLbl.setText("Total in pkg: " + str(totalAPK))
        self.totalInSpecLbl.setText("Total in Spec: " + str(totalSpec))
        self.diffTotalLbl.setText("Total str_id difference from previous run: " + str(diff_total))
        self.failedMMLbl.setText("Failed(string mismatch): " + str(failedMM))
        self.failedMSLbl.setText("Failed(translated in apk but str_id missing in spec): " + str(failedMS))
        self.failedLMLbl.setText("Failed(missing translation): " + str(failedLM))
        self.failedSELbl.setText("Failed(tranlation same as english): " + str(failedSE))
        self.failedLCLbl.setText("Failed(legacy): " + str(failedLC))

        self.passedLbl.setText("Passed: " + str(passed))
        self.legacyPass.setText("Passed(Legacy): " + str(legacyPassed))
        self.notTestLbl.setText("Not Test: " + str(notTest))
        self.removedLbl.setText("Removed: " + str(removed))
        self.unknownLbl.setText("Unknown: " + str(unknown))

class RunReviewWindow(QtGui.QDialog):
    def __init__(self, recId, projectName, osType, parent=None):
        super(RunReviewWindow, self).__init__(parent)
        self.parent = parent
        self.data = global_db_connection.get_record(osType, projectName, recId)
        self.showReviewed = True
        self.setupUi(self)
        self.populateLists()
        self.setupConnection()
        self.totalLbl.setText(str(len(self.data["result_str_dict"].keys())))

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowFlags(QtCore.Qt.Window) 

        Form.resize(1267, 951)
        self.gridLayout_5 = QtGui.QGridLayout(Form)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(120, 30))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.totalLbl = QtGui.QLabel(Form)
        self.totalLbl.setMaximumSize(QtCore.QSize(100, 30))
        self.totalLbl.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))
        self.totalLbl.setText(_fromUtf8(""))
        self.totalLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.totalLbl.setObjectName(_fromUtf8("totalLbl"))
        self.horizontalLayout_2.addWidget(self.totalLbl)
        self.showreviewedCbx = QtGui.QCheckBox(Form)
        self.showreviewedCbx.setMinimumSize(QtCore.QSize(120, 30))
        self.showreviewedCbx.setMaximumSize(QtCore.QSize(120, 30))
        self.showreviewedCbx.setChecked(True)
        self.showreviewedCbx.setObjectName(_fromUtf8("showreviewedCbx"))
        self.showreviewedCbx.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))

        self.horizontalLayout_2.addWidget(self.showreviewedCbx)

        self.pkgNameLbl = QtGui.QLabel(Form)
        self.pkgNameLbl.setMinimumSize(QtCore.QSize(120, 30))
        self.pkgNameLbl.setMaximumSize(QtCore.QSize(1000, 30))
        self.pkgNameLbl.setObjectName(_fromUtf8("pkgNameLbl"))
        self.pkgNameLbl.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))

        self.horizontalLayout_2.addWidget(self.pkgNameLbl)

        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tabView = QtGui.QTabWidget(Form)
        self.tabView.setEnabled(True)
        self.tabView.setMinimumSize(QtCore.QSize(960, 540))
        self.tabView.setObjectName(_fromUtf8("tabView"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollArea_5 = QtGui.QScrollArea(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName(_fromUtf8("scrollArea_5"))
        self.scrollAreaWidgetContents_5 = QtGui.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1225, 810))
        self.scrollAreaWidgetContents_5.setObjectName(_fromUtf8("scrollAreaWidgetContents_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents_5)
        self.label_3.setMinimumSize(QtCore.QSize(130, 35))
        self.label_3.setMaximumSize(QtCore.QSize(130, 35))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.failedCountLbl = QtGui.QLabel(self.scrollAreaWidgetContents_5)
        self.failedCountLbl.setMinimumSize(QtCore.QSize(100, 35))
        self.failedCountLbl.setMaximumSize(QtCore.QSize(100, 35))
        self.failedCountLbl.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))
        self.failedCountLbl.setText(_fromUtf8(""))
        self.failedCountLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.failedCountLbl.setObjectName(_fromUtf8("failedCountLbl"))
        self.horizontalLayout_5.addWidget(self.failedCountLbl)
        self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(100, 35))
        self.label_14.setMaximumSize(QtCore.QSize(100, 35))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_5.addWidget(self.label_14)
        self.failedSearchBox = QtGui.QTextEdit(self.scrollAreaWidgetContents_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.failedSearchBox.sizePolicy().hasHeightForWidth())
        self.failedSearchBox.setSizePolicy(sizePolicy)
        self.failedSearchBox.setMinimumSize(QtCore.QSize(300, 35))
        self.failedSearchBox.setMaximumSize(QtCore.QSize(700, 35))
        self.failedSearchBox.setObjectName(_fromUtf8("failedSearchBox"))
        self.horizontalLayout_5.addWidget(self.failedSearchBox)
        self.failedSearchBtn = QtGui.QPushButton(self.scrollAreaWidgetContents_5)
        self.failedSearchBtn.setMinimumSize(QtCore.QSize(100, 35))
        self.failedSearchBtn.setMaximumSize(QtCore.QSize(100, 35))
        self.failedSearchBtn.setObjectName(_fromUtf8("failedSearchBtn"))
        self.horizontalLayout_5.addWidget(self.failedSearchBtn)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.failList = QtGui.QListWidget(self.scrollAreaWidgetContents_5)
        self.failList.setObjectName(_fromUtf8("failList"))
        self.gridLayout_4.addWidget(self.failList, 1, 0, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_4.addWidget(self.scrollArea_5)
        self.tabView.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.scrollArea_3 = QtGui.QScrollArea(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1225, 810))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_4.setMinimumSize(QtCore.QSize(130, 35))
        self.label_4.setMaximumSize(QtCore.QSize(130, 35))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.unknownCountLbl = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.unknownCountLbl.setMinimumSize(QtCore.QSize(100, 35))
        self.unknownCountLbl.setMaximumSize(QtCore.QSize(100, 35))
        self.unknownCountLbl.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))
        self.unknownCountLbl.setText(_fromUtf8(""))
        self.unknownCountLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.unknownCountLbl.setObjectName(_fromUtf8("unknownCountLbl"))
        self.horizontalLayout_4.addWidget(self.unknownCountLbl)
        self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(100, 35))
        self.label_12.setMaximumSize(QtCore.QSize(100, 35))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.unknownSearchBox = QtGui.QTextEdit(self.scrollAreaWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unknownSearchBox.sizePolicy().hasHeightForWidth())
        self.unknownSearchBox.setSizePolicy(sizePolicy)
        self.unknownSearchBox.setMinimumSize(QtCore.QSize(300, 35))
        self.unknownSearchBox.setMaximumSize(QtCore.QSize(700, 35))
        self.unknownSearchBox.setObjectName(_fromUtf8("unknownSearchBox"))
        self.horizontalLayout_4.addWidget(self.unknownSearchBox)
        self.unknownSearchBtn = QtGui.QPushButton(self.scrollAreaWidgetContents_3)
        self.unknownSearchBtn.setMinimumSize(QtCore.QSize(100, 35))
        self.unknownSearchBtn.setMaximumSize(QtCore.QSize(100, 35))
        self.unknownSearchBtn.setObjectName(_fromUtf8("unknownSearchBtn"))
        self.horizontalLayout_4.addWidget(self.unknownSearchBtn)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.unknownList = QtGui.QListWidget(self.scrollAreaWidgetContents_3)
        self.unknownList.setObjectName(_fromUtf8("unknownList"))
        self.gridLayout_6.addWidget(self.unknownList, 1, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.tabView.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout = QtGui.QGridLayout(self.tab_5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea_6 = QtGui.QScrollArea(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_6.sizePolicy().hasHeightForWidth())
        self.scrollArea_6.setSizePolicy(sizePolicy)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName(_fromUtf8("scrollArea_6"))
        self.scrollAreaWidgetContents_6 = QtGui.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 1225, 810))
        self.scrollAreaWidgetContents_6.setObjectName(_fromUtf8("scrollAreaWidgetContents_6"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_6)
        self.label.setMinimumSize(QtCore.QSize(130, 35))
        self.label.setMaximumSize(QtCore.QSize(130, 35))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.passedCountLbl = QtGui.QLabel(self.scrollAreaWidgetContents_6)
        self.passedCountLbl.setMinimumSize(QtCore.QSize(100, 35))
        self.passedCountLbl.setMaximumSize(QtCore.QSize(100, 35))
        self.passedCountLbl.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))
        self.passedCountLbl.setText(_fromUtf8(""))
        self.passedCountLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.passedCountLbl.setObjectName(_fromUtf8("passedCountLbl"))
        self.horizontalLayout_3.addWidget(self.passedCountLbl)
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(100, 35))
        self.label_9.setMaximumSize(QtCore.QSize(100, 35))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.passedSearchBox = QtGui.QTextEdit(self.scrollAreaWidgetContents_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passedSearchBox.sizePolicy().hasHeightForWidth())
        self.passedSearchBox.setSizePolicy(sizePolicy)
        self.passedSearchBox.setMinimumSize(QtCore.QSize(300, 35))
        self.passedSearchBox.setMaximumSize(QtCore.QSize(700, 35))
        self.passedSearchBox.setObjectName(_fromUtf8("passedSearchBox"))
        self.horizontalLayout_3.addWidget(self.passedSearchBox)
        self.passedSearchBtn = QtGui.QPushButton(self.scrollAreaWidgetContents_6)
        self.passedSearchBtn.setMinimumSize(QtCore.QSize(100, 35))
        self.passedSearchBtn.setMaximumSize(QtCore.QSize(100, 35))
        self.passedSearchBtn.setObjectName(_fromUtf8("passedSearchBtn"))
        self.horizontalLayout_3.addWidget(self.passedSearchBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.passList = QtGui.QListWidget(self.scrollAreaWidgetContents_6)
        self.passList.setObjectName(_fromUtf8("passList"))
        self.gridLayout_2.addWidget(self.passList, 1, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout.addWidget(self.scrollArea_6, 0, 1, 1, 1)
        self.tabView.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabView, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.submitBtn = QtGui.QPushButton(Form)
        self.submitBtn.setObjectName(_fromUtf8("submitBtn"))
        self.horizontalLayout.addWidget(self.submitBtn)
        self.saveBtn = QtGui.QPushButton(Form)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.horizontalLayout.addWidget(self.saveBtn)
        self.quitBtn = QtGui.QPushButton(Form)
        self.quitBtn.setObjectName(_fromUtf8("quitBtn"))
        self.horizontalLayout.addWidget(self.quitBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabView.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Review Window", None))
        self.label_2.setText(_translate("Form", "Total Str ID in App: ", None))
        self.showreviewedCbx.setText(_translate("Form", "Show Reviewed", None))
        self.label_3.setText(_translate("Form", "Total Failed StrID:", None))
        self.label_14.setText(_translate("Form", "Search:", None))
        self.failedSearchBtn.setText(_translate("Form", "Search", None))
        self.tabView.setTabText(self.tabView.indexOf(self.tab_2), _translate("Form", "Failed", None))
        self.label_4.setText(_translate("Form", "Total Unknown StrID:", None))
        self.label_12.setText(_translate("Form", "Search:", None))
        self.unknownSearchBtn.setText(_translate("Form", "Search", None))
        self.tabView.setTabText(self.tabView.indexOf(self.tab_3), _translate("Form", "Unknown", None))
        self.label.setText(_translate("Form", "Total Passed StrID:", None))
        self.label_9.setText(_translate("Form", "Search:", None))
        self.passedSearchBtn.setText(_translate("Form", "Search", None))
        self.tabView.setTabText(self.tabView.indexOf(self.tab_5), _translate("Form", "Passed/Removed/Not Test", None))
        self.submitBtn.setText(_translate("Form", "Submit Result", None))
        self.saveBtn.setText(_translate("Form", "Save", None))
        self.quitBtn.setText(_translate("Form", "Quit", None))
        self.pkgNameLbl.setText(_translate("Form", "Pkg Name: " + self.data["pkg_source"].split("/")[-1], None))

    def closeEvent(self, event):
        self.parent.show()
        event.accept()

    def setupConnection(self):
        self.failedSearchBtn.clicked.connect(lambda : self.filterList(self.failedSearchBox, self.failList))
        self.passedSearchBtn.clicked.connect(lambda : self.filterList(self.passedSearchBox, self.passList))
        self.unknownSearchBtn.clicked.connect(lambda : self.filterList(self.unknownSearchBox, self.unknownList))
        self.saveBtn.clicked.connect(self.saveDataToDB)
        self.submitBtn.clicked.connect(self.submitDataToDB)
        self.quitBtn.clicked.connect(self.closeWindow)
        self.showreviewedCbx.clicked.connect(self.filterReviewed)

    def closeWindow(self):
        self.close()

    def filterReviewed(self):
        self.showReviewed = self.showreviewedCbx.isChecked()
        self.populateLists()

    def filterList(self, searchObj, listObj):
        for index in range(listObj.count()):
            if str(searchObj.toPlainText()) == "":
                listObj.setRowHidden(index, False)
            elif str(searchObj.toPlainText()) in str(listObj.itemWidget(listObj.item(index)).strIDLbl.text()) or \
                str(searchObj.toPlainText()) in str(listObj.itemWidget(listObj.item(index)).reasonLbl.text()):
                listObj.setRowHidden(index, False)
            else:
                listObj.setRowHidden(index, True)

    def saveDataToDB(self):
        global_db_connection.save_record(self.data)
        finished = QtGui.QMessageBox(self)
        finished.setIcon(QtGui.QMessageBox.Information)
        finished.setText("Save Record Complete!")
        finished.setWindowTitle("Finished!")
        finished.setStandardButtons(QtGui.QMessageBox.Ok)
        finished.exec_()

    def submitDataToDB(self):
        self.data["reviewed"] = True
        self.saveDataToDB()


    def refreshTabCount(self):
        self.passedCountLbl.setText(str(self.passList.count()))
        self.failedCountLbl.setText(str(self.failList.count()))
        self.unknownCountLbl.setText(str(self.unknownList.count()))

    def refreshListIndex(self, updateList):
        for lst in updateList:
            for index in range(lst.count()):
                lst.itemWidget(lst.item(index)).indexLbl.setText(str(index+1))
    
    def populateLists(self):
        self.passList.clear()
        self.failList.clear()
        self.unknownList.clear()
        pIndex = 1
        fIndex = 1
        uIndex = 1
        
        for key, value in self.data["result_str_dict"].items():
            if not self.showReviewed and value.get("reviewed", False) is not False:
                continue

            itemN = QtGui.QListWidgetItem() 
            widget = self.createListWidget(key, value)

            itemN.setSizeHint(widget.sizeHint())  

            if value["result"] == "passed" or value["result"] == "removed" or value["result"] == "not test":
                widget.indexLbl.setText(str(pIndex))
                pIndex += 1
                self.passList.addItem(itemN)
                self.passList.setItemWidget(itemN, widget)

            elif value["result"] == "failed":
                widget.indexLbl.setText(str(fIndex))
                fIndex += 1
                self.failList.addItem(itemN)
                self.failList.setItemWidget(itemN, widget)
            elif value["result"] == "unknown":
                widget.indexLbl.setText(str(uIndex))
                uIndex +=1
                self.unknownList.addItem(itemN)
                self.unknownList.setItemWidget(itemN, widget)  

        self.refreshTabCount()

    def createListWidget(self, key, value):
        widget = QtGui.QWidget()
        verticalLayout = QtGui.QVBoxLayout()
        horizontalLayout = QtGui.QHBoxLayout()

        widget.strIDLbl = QtGui.QLabel(key)
        widget.strIDLbl.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))
        widget.strIDLbl.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        widget.indexLbl = QtGui.QLabel()
        widget.indexLbl.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))
        widget.indexLbl.setMinimumSize(QtCore.QSize(40, 0))
        widget.indexLbl.setMaximumSize(QtCore.QSize(40, 16777215))

        widget.reasonLbl = QtGui.QLabel(value.get("reason", "N/A"))
        widget.reasonLbl.setStyleSheet(_fromUtf8("border:1px solid rgb(102,102,0); "))

        widget.reviewBtn = QtGui.QPushButton("Review")
        widget.reviewBtn.setMinimumSize(QtCore.QSize(100, 0))
        widget.reviewBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        if value.get("reviewed", False) is False:
            widget.reviewBtn.setStyleSheet(_fromUtf8("color: red;"))
        else:
            widget.reviewBtn.setStyleSheet(_fromUtf8("color: green;"))

        horizontalLayout.addWidget(widget.indexLbl)
        horizontalLayout.addWidget(widget.strIDLbl)
        horizontalLayout.addWidget(widget.reasonLbl)
        horizontalLayout.addWidget(widget.reviewBtn)

        verticalLayout.addLayout(horizontalLayout)
        widget.setLayout(verticalLayout)
        widget.reviewBtn.clicked.connect(lambda state, x = key: self.openStrIDView(x))
        return widget

    def openStrIDView(self, strID):
        self.hide()
        StrIDWindow = StrIDView(strID, parent=self)
        centerForm(StrIDWindow)
        StrIDWindow.show()

    def updateUI(self, strID, prevResult):
        if prevResult == "passed" or prevResult == "removed" or prevResult == "not test":
            moveFromList = self.passList
        elif prevResult == "failed":
            moveFromList = self.failList
        elif prevResult == "unknown":
            moveFromList = self.unknownList

        curResult = self.data["result_str_dict"][strID]["result"]
        for index in range(moveFromList.count()):
            lstItemWidget = moveFromList.itemWidget(moveFromList.item(index))
            if strID == str(lstItemWidget.strIDLbl.text()):
                if curResult == "passed" or curResult == "removed" or curResult == "not test":
                    moveToList = self.passList
                elif curResult == "failed":
                    moveToList = self.failList                
                elif curResult == "unknown":
                    moveToList = self.unknownList
                if moveToList != moveFromList:
                    del lstItemWidget
                    item = moveFromList.takeItem(index)
                    moveToList.addItem(item)
                    widget = self.createListWidget(strID, self.data["result_str_dict"][strID])
                    moveToList.setItemWidget(item, widget)
                    self.refreshListIndex([moveFromList, moveToList])
                else:
                    moveFromList.itemWidget(moveFromList.item(index)).reviewBtn.setStyleSheet(_fromUtf8("color: green;"))
                break
        self.refreshTabCount()



class StrIDView(QtGui.QDialog):
    def __init__(self, strID, parent=None):
        super(StrIDView, self).__init__(parent)
        self.parent = parent
        self.strID = strID
        self.pkgData = self.parent.data["apk_str_dict"].get(self.strID, {})
        self.specData = self.parent.data["spec_str_dict"].get(self.strID, {})
        self.resultData = self.parent.data["result_str_dict"][self.strID]
        self.specVersion = self.parent.data["spec_version"]
        self.langRow = {}
        self.ignoreNewLine = False
        self.setupUi(self)
        self.setupConnection()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowFlags(QtCore.Qt.Window) 
        Dialog.resize(960, 540)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(960, 540))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)

        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setMinimumSize(QtCore.QSize(200, 35))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label_2.setStyleSheet("color:orange;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0,0)

        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setMinimumSize(QtCore.QSize(200, 35))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label_3.setStyleSheet("color:green;")        
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0,3)

        self.stackViewCbb = QtGui.QCheckBox(Dialog)
        self.stackViewCbb.setMinimumSize(QtCore.QSize(120, 30))
        self.stackViewCbb.setMaximumSize(QtCore.QSize(16777215, 30))
        self.stackViewCbb.setChecked(True)
        self.stackViewCbb.setStyleSheet("margin-left:50%; margin-right:50%;")
        self.gridLayout.addWidget(self.stackViewCbb, 0, 1)

        self.newlineViewCbb = QtGui.QCheckBox(Dialog)
        self.newlineViewCbb.setMinimumSize(QtCore.QSize(120, 30))
        self.newlineViewCbb.setMaximumSize(QtCore.QSize(16777215, 30))
        self.newlineViewCbb.setChecked(False)
        self.newlineViewCbb.setStyleSheet("margin-left:50%; margin-right:50%;")
        self.gridLayout.addWidget(self.newlineViewCbb, 0, 2)

        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))


        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1045, 677))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        row = 0
        for key, value in self.pkgData.items():
            self.langRow[key] = {"row": row}
            langBtn = QtGui.QPushButton(Dialog)
            langBtn.setText(key)
            langBtn.setMinimumSize(QtCore.QSize(100, 35))
            langBtn.setMaximumSize(QtCore.QSize(100, 35))
            langBtn.setStyleSheet(_fromUtf8("color:orange;"))
            langBtn.clicked.connect(lambda state, x=key : self.openEdit(x, "apk_str_dict"))


            label = QtGui.QLabel(Dialog)
            label.setText(value)
            label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
            label.setWordWrap(True)
            label.setStyleSheet(_fromUtf8("border:1px solid rgb(255,255,255); color:orange;"))
            self.langRow[key]["left"] = label
            self.langRow[key]["leftBtn"] = langBtn
            self.gridLayout_2.addWidget(langBtn, row, 0)
            self.gridLayout_2.addWidget(label, row, 1, 1, 2)
            row += 1

        for key, value in self.specData.items():
            matchingRow = self.langRow.get(key, {}).get("row", row)
            if matchingRow == row:
                self.langRow[key] = {"row": matchingRow}

            lang2Btn = QtGui.QPushButton(Dialog)
            lang2Btn.setText(key)
            lang2Btn.setMinimumSize(QtCore.QSize(100, 35))
            lang2Btn.setMaximumSize(QtCore.QSize(100, 35))
            lang2Btn.setStyleSheet(_fromUtf8("color:green;"))
            lang2Btn.clicked.connect(lambda state, x = key: self.openEdit(x, "spec_str_dict"))

            label2 = QtGui.QLabel(Dialog)
            label2.setText(value)
            label2.setWordWrap(True)
            label2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
            label2.setStyleSheet(_fromUtf8("border:1px solid rgb(255,255,255); color:green;"))

            self.langRow[key]["right"] = label2
            self.langRow[key]["rightBtn"] = lang2Btn

            self.gridLayout_2.addWidget(lang2Btn, matchingRow, 3)
            self.gridLayout_2.addWidget(label2, matchingRow, 1, 1, 2)

            if matchingRow == row:
                row += 1       

        for key, value in self.langRow.items():
            if value.get("left", False) is False or value.get("right", False) is False:
                lang3Btn = QtGui.QPushButton(Dialog)
                lang3Btn.setText(key)
                lang3Btn.setMinimumSize(QtCore.QSize(100, 35))
                lang3Btn.setMaximumSize(QtCore.QSize(100, 35))
                lang3Btn.setStyleSheet(_fromUtf8("color:white;")) 
            else:
                continue

            if value.get("left", False) is False:
                lang3Btn.clicked.connect(lambda state, x = key: self.openEdit(x, "apk_str_dict"))
                self.langRow[key]["leftBtn"] = lang3Btn
                self.gridLayout_2.addWidget(lang3Btn, value["row"], 0)
            elif value.get("right", False) is False:
                lang3Btn.clicked.connect(lambda state, x = key: self.openEdit(x, "spec_str_dict"))
                self.langRow[key]["rightBtn"] = lang3Btn
                self.gridLayout_2.addWidget(lang3Btn, value["row"], 3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout"))

       
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.crLineEdit = QtGui.QLineEdit(Dialog)
        self.crLineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.onlyInt = QtGui.QIntValidator()
        self.crLineEdit.setValidator(self.onlyInt)
        if self.resultData.get("cr", None) is not None:
            self.crLineEdit.setText(self.resultData["cr"])

        self.horizontalLayout.addWidget(self.crLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.commentBtn = QtGui.QPushButton(Dialog)
        self.horizontalLayout_2.addWidget(self.commentBtn)

        self.resultCbb = QtGui.QComboBox(Dialog)
        self.resultCbb.addItems(["Passed", "Failed", "Unknown", "Removed", "Not Test"])
        self.resultCbb.setObjectName(_fromUtf8("resultCbb"))
        if self.resultData["result"] == "passed":
            self.resultCbb.setCurrentIndex(0)
        elif self.resultData["result"] == "failed":
            self.resultCbb.setCurrentIndex(1)            
        elif self.resultData["result"] == "unknown":
            self.resultCbb.setCurrentIndex(2)
        elif self.resultData["result"] == "removed":
            self.resultCbb.setCurrentIndex(3)
        elif self.resultData["result"] == "not test":
            self.resultCbb.setCurrentIndex(4)

        self.horizontalLayout_2.addWidget(self.resultCbb)
        self.submitBtn = QtGui.QPushButton(Dialog)
        self.horizontalLayout_2.addWidget(self.submitBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", self.strID + " | " + self.specVersion, None))
        self.label_2.setText(_translate("Dialog", "In App String", None))
        self.label_3.setText(_translate("Dialog", "Spec String", None))
        self.label_4.setText(_translate("Dialog", "Assign CR ID: ", None))
        self.stackViewCbb.setText(_translate("Dialog", "Stacked View: ", None))
        self.newlineViewCbb.setText(_translate("Dialog", "Ignore Newline: ", None))
        self.submitBtn.setText(_translate("Dialog", "Submit Result", None))
        self.commentBtn.setText(_translate("Dialog", "Comment", None))

    def closeEvent(self, event):
        self.parent.show()
        event.accept()

    def setupConnection(self):
        self.stackViewCbb.stateChanged.connect(self.redrawLabels)
        self.newlineViewCbb.stateChanged.connect(self.changeDisplayNewLine)
        self.commentBtn.clicked.connect(self.openComment)
        self.submitBtn.clicked.connect(self.submitChange)

    def openComment(self):
        commentEditWindow = CommentEditView(self.strID, parent=self)
        centerForm(commentEditWindow)
        commentEditWindow.show()

    def openEdit(self, lang, langDictName):
        strEditWindow = StrEditView(self.strID, lang, langDictName, parent=self)
        centerForm(strEditWindow)
        strEditWindow.show()        

    def changeDisplayNewLine(self):
        self.ignoreNewLine = self.newlineViewCbb.isChecked()

        for item in self.parent.data["apk_str_dict"][self.strID].keys():
            self.refreshText(item, "apk_str_dict")
        for item in self.parent.data["spec_str_dict"][self.strID].keys():
            self.refreshText(item, "spec_str_dict")

    def redrawLabels(self):
        if not self.stackViewCbb.isChecked():
            for lang, info in self.langRow.items():
                for key, value in info.items():
                    if key in ["left", "right"]:
                        self.gridLayout_2.removeWidget(value)
                    if key == "left":
                        self.gridLayout_2.addWidget(value, self.langRow[lang]["row"], 1,1 ,1)
                    elif key == "right":
                        self.gridLayout_2.addWidget(value, self.langRow[lang]["row"], 2,1,1)
        else:
            for lang, info in self.langRow.items():
                for key, value in info.items():
                    if key in ["left", "right"]:
                        self.gridLayout_2.removeWidget(value)
                    if key == "left":
                        self.gridLayout_2.addWidget(value, self.langRow[lang]["row"], 1, 1, 2)
                    elif key == "right":
                        self.gridLayout_2.addWidget(value, self.langRow[lang]["row"], 1, 1, 2)

    def submitChange(self):
        global global_results_subbed
        prevResult = self.parent.data["result_str_dict"][self.strID]["result"]
        if prevResult != str(self.resultCbb.currentText()).lower():
            self.parent.data["result_str_dict"][self.strID]["result"] = str(self.resultCbb.currentText()).lower()
            self.parent.data["result_str_dict"][self.strID]["reason"] = "[9][" + str(self.resultCbb.currentText()).lower() + "] User changed status to: " + str(self.resultCbb.currentText()).lower()
        self.parent.data["result_str_dict"][self.strID]["reviewed"] = True
        if str(self.crLineEdit.text()) != "":
            self.parent.data["result_str_dict"][self.strID]["cr"] = str(self.crLineEdit.text())
        
        self.parent.updateUI(self.strID, prevResult)
        global_results_subbed += 1
        if global_results_subbed >= 10:
            self.parent.saveDataToDB()
            global_results_subbed = 0
        self.close()

    def refreshText(self, lang, langDictName):
        if langDictName == "apk_str_dict":
            side = "left"
            styleSheet = "color:orange;"
        elif langDictName == "spec_str_dict":
            side = "right"
            styleSheet = "color:green;"

        labelText = self.parent.data[langDictName][self.strID][lang]
        if self.ignoreNewLine:
            labelText = labelText.replace("\n", "")

        if self.langRow[lang].get(side, None) is None:
            label = QtGui.QLabel(self)
            label.setText(labelText)
            label.setStyleSheet(_fromUtf8("border:1px solid rgb(255,255,255); " + styleSheet))
            self.langRow[lang][side] = label
            row = self.langRow[lang]["row"]
            stacked = self.stackViewCbb.isChecked()
            if side == "left":
                col = 1
                width = 2 if stacked else 1
            elif side == "right" and stacked:
                col = 1
                width = 2
            elif side == "right" and not stacked:
                col = 2
                width = 1
                self.gridLayout_2.addWidget(label, row, col, 1, width)
        else:
            self.langRow[lang][side].setText(labelText)
        btnKey = side + "Btn"
        self.langRow[lang][btnKey].setStyleSheet(_fromUtf8(styleSheet))


class CommentEditView(QtGui.QDialog):
    def __init__(self, strID, parent=None):
        super(CommentEditView, self).__init__(parent)
        self.parent = parent
        self.strID = strID
        self.resultData = self.parent.parent.data["result_str_dict"][self.strID]
        self.setupUi(self)
        self.setupConnection()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(580, 270)
        Dialog.setMinimumSize(QtCore.QSize(580, 270))
        Dialog.setWindowTitle(_fromUtf8("Edit: " + self.strID + " comment"))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.strTextEdit = QtGui.QTextEdit(Dialog)
        self.strTextEdit.setObjectName(_fromUtf8("strTextEdit"))
        self.strTextEdit.setText(self.resultData.get("comment", ""))

        self.gridLayout.addWidget(self.strTextEdit, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.saveBtn = QtGui.QPushButton(Dialog)
        self.saveBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.horizontalLayout.addWidget(self.saveBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.saveBtn.setText(_translate("Dialog", "Save", None))

    def setupConnection(self):
        self.saveBtn.clicked.connect(self.saveChange)

    def saveChange(self):
        self.resultData["comment"] = str(self.strTextEdit.toPlainText())
        self.close()


class StrEditView(QtGui.QDialog):
    def __init__(self, strID, lang, langDictName, parent=None):
        super(StrEditView, self).__init__(parent)
        self.parent = parent
        self.strID = strID
        self.lang = lang
        self.langDictName = langDictName
        self.actualString = self.parent.parent.data[self.langDictName].get(self.strID, {}).get(self.lang, "")
        self.setupUi(self)
        self.setupConnection()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(580, 270)
        Dialog.setMinimumSize(QtCore.QSize(580, 270))
        Dialog.setWindowTitle(_fromUtf8("Edit: " + self.strID + " for: " + self.lang))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.strTextEdit = QtGui.QTextEdit(Dialog)
        self.strTextEdit.setObjectName(_fromUtf8("strTextEdit"))
        self.strTextEdit.setText(self.actualString)

        self.gridLayout.addWidget(self.strTextEdit, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.saveBtn = QtGui.QPushButton(Dialog)
        self.saveBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.horizontalLayout.addWidget(self.saveBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.saveBtn.setText(_translate("Dialog", "Save", None))

    def setupConnection(self):
        self.saveBtn.clicked.connect(self.saveChange)

    def saveChange(self):
        if self.strTextEdit.toPlainText() != self.actualString:
            if self.parent.parent.data[self.langDictName].get(self.strID, None) is None:
                self.parent.parent.data[self.langDictName][self.strID] = {self.lang: str(self.strTextEdit.toPlainText())}
            else:
                self.parent.parent.data[self.langDictName][self.strID][self.lang] = str(self.strTextEdit.toPlainText())
            self.parent.refreshText(self.lang, self.langDictName)

        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    welcome_screen = WelcomeScreen()
    centerForm(welcome_screen)
    welcome_screen.show()
    sys.exit(app.exec_())