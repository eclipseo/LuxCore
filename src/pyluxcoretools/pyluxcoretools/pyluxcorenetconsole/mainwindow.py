# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/david/projects/luxcorerender/LuxCore/src/pyluxcoretools/pyluxcoretools/pyluxcorenetconsole/mainwindow.ui'
#
# Created: Sun Jun  3 10:43:14 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidgetMain = QtGui.QTabWidget(self.splitter)
        self.tabWidgetMain.setObjectName("tabWidgetMain")
        self.currentJob = QtGui.QWidget()
        self.currentJob.setObjectName("currentJob")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.currentJob)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtGui.QScrollArea(self.currentJob)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -134, 742, 595))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.labelRenderCfgFileName = QtGui.QLabel(self.groupBox)
        self.labelRenderCfgFileName.setText("")
        self.labelRenderCfgFileName.setObjectName("labelRenderCfgFileName")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelRenderCfgFileName)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.labelFilmFileName = QtGui.QLabel(self.groupBox)
        self.labelFilmFileName.setText("")
        self.labelFilmFileName.setObjectName("labelFilmFileName")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.labelFilmFileName)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.labelImageFileName = QtGui.QLabel(self.groupBox)
        self.labelImageFileName.setText("")
        self.labelImageFileName.setObjectName("labelImageFileName")
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.labelImageFileName)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_8)
        self.labelWorkDirectory = QtGui.QLabel(self.groupBox)
        self.labelWorkDirectory.setText("")
        self.labelWorkDirectory.setObjectName("labelWorkDirectory")
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.labelWorkDirectory)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_9)
        self.labelStartTime = QtGui.QLabel(self.groupBox)
        self.labelStartTime.setText("")
        self.labelStartTime.setObjectName("labelStartTime")
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.labelStartTime)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_11)
        self.labelRenderingTime = QtGui.QLabel(self.groupBox)
        self.labelRenderingTime.setText("")
        self.labelRenderingTime.setObjectName("labelRenderingTime")
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.labelRenderingTime)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_12)
        self.labelSamplesPixel = QtGui.QLabel(self.groupBox)
        self.labelSamplesPixel.setText("")
        self.labelSamplesPixel.setObjectName("labelSamplesPixel")
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.labelSamplesPixel)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_10)
        self.labelSamplesSec = QtGui.QLabel(self.groupBox)
        self.labelSamplesSec.setText("")
        self.labelSamplesSec.setObjectName("labelSamplesSec")
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.labelSamplesSec)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditHaltSPP = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHaltSPP.sizePolicy().hasHeightForWidth())
        self.lineEditHaltSPP.setSizePolicy(sizePolicy)
        self.lineEditHaltSPP.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditHaltSPP.setObjectName("lineEditHaltSPP")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditHaltSPP)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditHaltTime = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHaltTime.sizePolicy().hasHeightForWidth())
        self.lineEditHaltTime.setSizePolicy(sizePolicy)
        self.lineEditHaltTime.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditHaltTime.setObjectName("lineEditHaltTime")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditHaltTime)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditFilmUpdatePeriod = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFilmUpdatePeriod.sizePolicy().hasHeightForWidth())
        self.lineEditFilmUpdatePeriod.setSizePolicy(sizePolicy)
        self.lineEditFilmUpdatePeriod.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditFilmUpdatePeriod.setObjectName("lineEditFilmUpdatePeriod")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditFilmUpdatePeriod)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditStatsPeriod = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditStatsPeriod.sizePolicy().hasHeightForWidth())
        self.lineEditStatsPeriod.setSizePolicy(sizePolicy)
        self.lineEditStatsPeriod.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditStatsPeriod.setObjectName("lineEditStatsPeriod")
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditStatsPeriod)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonForceFilmMerge = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonForceFilmMerge.setObjectName("pushButtonForceFilmMerge")
        self.gridLayout_2.addWidget(self.pushButtonForceFilmMerge, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 1)
        self.pushButtonForceFilmDownload = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonForceFilmDownload.setObjectName("pushButtonForceFilmDownload")
        self.gridLayout_2.addWidget(self.pushButtonForceFilmDownload, 0, 1, 1, 1)
        self.pushButtonFinishJob = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonFinishJob.setObjectName("pushButtonFinishJob")
        self.gridLayout_2.addWidget(self.pushButtonFinishJob, 0, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtGui.QScrollArea(self.groupBox_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 696, 76))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelRenderingImage = QtGui.QLabel(self.scrollAreaWidgetContents_4)
        self.labelRenderingImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRenderingImage.setObjectName("labelRenderingImage")
        self.gridLayout_5.addWidget(self.labelRenderingImage, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.tabWidgetMain.addTab(self.currentJob, "")
        self.queuedJobs = QtGui.QWidget()
        self.queuedJobs.setObjectName("queuedJobs")
        self.gridLayout = QtGui.QGridLayout(self.queuedJobs)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.pushButtonAddJob = QtGui.QPushButton(self.queuedJobs)
        self.pushButtonAddJob.setObjectName("pushButtonAddJob")
        self.gridLayout.addWidget(self.pushButtonAddJob, 1, 1, 1, 1)
        self.scrollAreaQueuedJobs = QtGui.QScrollArea(self.queuedJobs)
        self.scrollAreaQueuedJobs.setWidgetResizable(True)
        self.scrollAreaQueuedJobs.setObjectName("scrollAreaQueuedJobs")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 758, 374))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaQueuedJobs.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollAreaQueuedJobs, 0, 0, 1, 4)
        self.pushButtonRemovePendingJobs = QtGui.QPushButton(self.queuedJobs)
        self.pushButtonRemovePendingJobs.setObjectName("pushButtonRemovePendingJobs")
        self.gridLayout.addWidget(self.pushButtonRemovePendingJobs, 1, 2, 1, 1)
        self.tabWidgetMain.addTab(self.queuedJobs, "")
        self.nodes = QtGui.QWidget()
        self.nodes.setObjectName("nodes")
        self.gridLayout_3 = QtGui.QGridLayout(self.nodes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 3, 1, 1)
        self.pushButtonAddNode = QtGui.QPushButton(self.nodes)
        self.pushButtonAddNode.setObjectName("pushButtonAddNode")
        self.gridLayout_3.addWidget(self.pushButtonAddNode, 1, 1, 1, 1)
        self.scrollAreaNodes = QtGui.QScrollArea(self.nodes)
        self.scrollAreaNodes.setWidgetResizable(True)
        self.scrollAreaNodes.setObjectName("scrollAreaNodes")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 758, 374))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaNodes.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.scrollAreaNodes, 0, 0, 1, 4)
        self.pushButtonRefreshNodesList = QtGui.QPushButton(self.nodes)
        self.pushButtonRefreshNodesList.setObjectName("pushButtonRefreshNodesList")
        self.gridLayout_3.addWidget(self.pushButtonRefreshNodesList, 1, 2, 1, 1)
        self.tabWidgetMain.addTab(self.nodes, "")
        self.textEditLog = QtGui.QTextEdit(self.splitter)
        self.textEditLog.setUndoRedoEnabled(False)
        self.textEditLog.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.textEditLog.setReadOnly(True)
        self.textEditLog.setObjectName("textEditLog")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidgetMain.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.clickedQuit)
        QtCore.QObject.connect(self.pushButtonAddJob, QtCore.SIGNAL("clicked()"), MainWindow.clickedAddJob)
        QtCore.QObject.connect(self.lineEditHaltSPP, QtCore.SIGNAL("editingFinished()"), MainWindow.editedHaltSPP)
        QtCore.QObject.connect(self.lineEditHaltTime, QtCore.SIGNAL("editingFinished()"), MainWindow.editedHaltTime)
        QtCore.QObject.connect(self.lineEditFilmUpdatePeriod, QtCore.SIGNAL("editingFinished()"), MainWindow.editedFilmUpdatePeriod)
        QtCore.QObject.connect(self.lineEditStatsPeriod, QtCore.SIGNAL("editingFinished()"), MainWindow.editedStatsPeriod)
        QtCore.QObject.connect(self.pushButtonForceFilmMerge, QtCore.SIGNAL("clicked()"), MainWindow.clickedForceFilmMerge)
        QtCore.QObject.connect(self.pushButtonForceFilmDownload, QtCore.SIGNAL("clicked()"), MainWindow.clickedForceFilmDownload)
        QtCore.QObject.connect(self.pushButtonFinishJob, QtCore.SIGNAL("clicked()"), MainWindow.clickedFinishJob)
        QtCore.QObject.connect(self.pushButtonRemovePendingJobs, QtCore.SIGNAL("clicked()"), MainWindow.clickedRemovePendingJobs)
        QtCore.QObject.connect(self.pushButtonAddNode, QtCore.SIGNAL("clicked()"), MainWindow.clickedAddNode)
        QtCore.QObject.connect(self.pushButtonRefreshNodesList, QtCore.SIGNAL("clicked()"), MainWindow.clickedRefreshNodesList)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditHaltSPP, self.lineEditHaltTime)
        MainWindow.setTabOrder(self.lineEditHaltTime, self.lineEditFilmUpdatePeriod)
        MainWindow.setTabOrder(self.lineEditFilmUpdatePeriod, self.lineEditStatsPeriod)
        MainWindow.setTabOrder(self.lineEditStatsPeriod, self.pushButtonForceFilmDownload)
        MainWindow.setTabOrder(self.pushButtonForceFilmDownload, self.pushButtonForceFilmMerge)
        MainWindow.setTabOrder(self.pushButtonForceFilmMerge, self.pushButtonFinishJob)
        MainWindow.setTabOrder(self.pushButtonFinishJob, self.pushButtonAddJob)
        MainWindow.setTabOrder(self.pushButtonAddJob, self.pushButtonRemovePendingJobs)
        MainWindow.setTabOrder(self.pushButtonRemovePendingJobs, self.pushButtonAddNode)
        MainWindow.setTabOrder(self.pushButtonAddNode, self.tabWidgetMain)
        MainWindow.setTabOrder(self.tabWidgetMain, self.scrollAreaQueuedJobs)
        MainWindow.setTabOrder(self.scrollAreaQueuedJobs, self.scrollArea_2)
        MainWindow.setTabOrder(self.scrollArea_2, self.scrollAreaNodes)
        MainWindow.setTabOrder(self.scrollAreaNodes, self.textEditLog)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyLuxCore Tool NetConsole", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Render configuration file name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Film file name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Image file name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Work directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Start time:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Rendering time:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Samples/pixel:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Samples/sec:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Halt at samples/pixel (0 disabled):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Halt at time (in secs, 0 disabled):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Film update period (in secs):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Statistics print period (in secs):", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Commands", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonForceFilmMerge.setText(QtGui.QApplication.translate("MainWindow", "Force film merge", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonForceFilmDownload.setText(QtGui.QApplication.translate("MainWindow", "Force film download", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFinishJob.setText(QtGui.QApplication.translate("MainWindow", "Finish job", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Rendering", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRenderingImage.setText(QtGui.QApplication.translate("MainWindow", "Waiting for film download and merge", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.currentJob), QtGui.QApplication.translate("MainWindow", "Current job", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddJob.setText(QtGui.QApplication.translate("MainWindow", "Add job", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemovePendingJobs.setText(QtGui.QApplication.translate("MainWindow", "Remove pending jobs", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.queuedJobs), QtGui.QApplication.translate("MainWindow", "Queued jobs", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddNode.setText(QtGui.QApplication.translate("MainWindow", "Add node", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRefreshNodesList.setText(QtGui.QApplication.translate("MainWindow", "Refresh nodes list", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.nodes), QtGui.QApplication.translate("MainWindow", "Nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

