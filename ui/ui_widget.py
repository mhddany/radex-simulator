# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'applayout.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from ui import resources_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(986, 611)
        Widget.setStyleSheet(u"/* =========================\n"
"   Global application style\n"
"   ========================= */\n"
"QWidget {\n"
"    background-color: transparent;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #90A1B9;\n"
"}\n"
"\n"
"/* =========================\n"
"   Label color variants\n"
"   ========================= */\n"
"#versionLabel,\n"
"#hintLabel,\n"
"#subTitleLabel,\n"
"#pipelineTitleLabel {\n"
"    color: #90A1B9;\n"
"}\n"
"\n"
"/* =========================\n"
"   Accent / status text\n"
"   ========================= */\n"
"#statusMessageLabel,\n"
"#statusIcon {\n"
"    color: #6FC5F4;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* =========================\n"
"   main title (slightly larger)\n"
"   ========================= */\n"
"#mainTitleLabel,\n"
"#maintitleSimulationPage,\n"
"#maintitleResultsPage,\n"
"#maintitlePositioningPage,\n"
"#maintitleMeshingPage,\n"
"#maintitleMaterialsPage,\n"
"#maintitleGeometryPage,\n"
"#viewTitleLayout{\n"
"    font-s"
                        "ize: 14pt;\n"
"    font-weight: normal;\n"
"    color: #f1f5f9;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#viewTitleLayout{\n"
"	border-bottom:	 1px solid #314158;\n"
"}\n"
"\n"
"#graphicsView{\n"
"    border: 0px solid #314158;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/* =========================\n"
"   Subtitles (shared)\n"
"   ========================= */\n"
"#subtitleSimulationPage,\n"
"#subtitleResultsPage,\n"
"#subtitlePositioningPage,\n"
"#subtitleMeshingPage,\n"
"#subtitleMaterialsPage,\n"
"#subtitleGeometryPage,\n"
"#stlfileAlabel ,\n"
"#stlfileBlabel,\n"
"#objectALoadedIcon,\n"
"#objectBLoadedIcon,\n"
"#objectALoadedLabel,\n"
"#objectBLoadedLabel,\n"
"#readyPositioningLabel,\n"
"#readyPositioningIcon,\n"
"#mainTitleViewLabel,\n"
"#subTitleViewLabel,\n"
"#subTitleViewIcon{\n"
"    font-size: 10pt;\n"
"    font-weight: normal;\n"
"    color: #90A1B9;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"#validationGeometryLabel,\n"
"#validationPositioningLabel{\n"
"  "
                        "  font-size: 10.5pt;\n"
"    font-weight: normal;\n"
"    color: #f1f5f9;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#objectALabel,\n"
"#positionObjectALabel{\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    color: #06d3f3;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#objectBLabel,\n"
"#positionObjectBLabel{\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    color: #f18904;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/* =========================\n"
"   Common bordered containers\n"
"   ========================= */\n"
"#topLayout,\n"
"#centerLayout,\n"
"#pipelineLayout,\n"
"#viewLayout{\n"
"    border: 1px solid #314158;\n"
"    background-color: #020618;\n"
"}\n"
"\n"
"#pipelineTitleLayout{\n"
"    border-bottom: 1px solid #314158;\n"
"    border-top: 1px solid #314158;\n"
"}\n"
"\n"
"#hintLayout{\n"
"    border-top: 1px solid #314158;\n"
"}\n"
"\n"
"/* =========================\n"
"   Dark panel containers\n"
"   ========================= */\n"
"#setting"
                        "sLayout,\n"
"#simulationPageLayout,\n"
"#resultsPageLayout,\n"
"#positioningPageLayout,\n"
"#meshingPageLayout,\n"
"#materialsPageLayout,\n"
"#geometryPageLayout,\n"
"#scrollAreaWidgetContentsGeometry,\n"
"#scrollAreaWidgetContentsPositioning,\n"
"#viewLayout{\n"
"    background-color: #0f172b;\n"
"}\n"
"\n"
"\n"
"/* =========================\n"
"   Setting layout\n"
"   ========================= */\n"
"#settingsLayout {\n"
"    border: 1px solid #314158;\n"
"}\n"
"\n"
"/* =========================\n"
"	Pipeline buttons\n"
"   ========================= */\n"
"#geometryButton,\n"
"#materialsButton,\n"
"#resultsButton,\n"
"#simulationButton,\n"
"#positioningButton,\n"
"#meshingButton {\n"
"    border: none;\n"
"    background-color: #020618;   /* idle */\n"
"    color: #f1f5f9;\n"
"	padding-left: 15px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"#geometryButton{\n"
"	spacing: 5px;       /* distance between icon and text */\n"
"}\n"
"\n"
"/* Hover \u2013 slightly lighter background */\n"
"#geometryButton:hover,\n"
""
                        "#materialsButton:hover,\n"
"#resultsButton:hover,\n"
"#simulationButton:hover,\n"
"#positioningButton:hover,\n"
"#meshingButton:hover {\n"
"    background-color: #1d293d;  \n"
"    color: #f1f5f9;\n"
"	border-left: 3px solid #415c89;\n"
"}\n"
"\n"
"#geometryButton:checked ,\n"
"#materialsButton:checked ,\n"
"#resultsButton:checked ,\n"
"#simulationButton:checked ,\n"
"#positioningButton:checked ,\n"
"#meshingButton:checked  {\n"
"    background-color: #155dfc;  \n"
"    color: #f1f5f9;\n"
"	border-left: 3px solid #50a2ff;\n"
"}\n"
"\n"
"/* Pressed \u2013 slightly darker / inset feel */\n"
"#geometryButton:pressed,\n"
"#materialsButton:pressed,\n"
"#resultsButton:pressed,\n"
"#simulationButton:pressed,\n"
"#positioningButton:pressed,\n"
"#meshingButton:pressed {\n"
"    background-color: #1253df;\n"
"}\n"
"\n"
"\n"
"#uploadFileAButton,\n"
"#uploadFileBButton,\n"
"#resetPositionAButton,\n"
"#resetPositionBButton,\n"
"#validationPositionButton{\n"
"    font-weight: bold;\n"
"    border-radius: 7px;\n"
"    border"
                        ": 1px solid #314158;\n"
"\n"
"    /* Idle state */\n"
"    background-color: #314158;\n"
"    color: #f1f5f9;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"/* Hover */\n"
"#uploadFileAButton:hover,\n"
"#uploadFileBButton:hover ,\n"
"#resetPositionAButton:hover,\n"
"#resetPositionBButton:hover,\n"
"#validationPositionButton:hover{\n"
"    background-color: #3f5470;   /* slightly lighter */\n"
"    border-color: #4b6a8c;\n"
"}\n"
"\n"
"/* Pressed / clicked */\n"
"#uploadFileAButton:pressed,\n"
"#uploadFileBButton:pressed,\n"
"#resetPositionAButton:pressed,\n"
"#resetPositionBButton:pressed,\n"
"#validationPositionButton:pressed{\n"
"    background-color: #253349;   /* darker */\n"
"    border-color: #314158;\n"
"}\n"
"\n"
"/* Disabled (optional but recommended) */\n"
"#uploadFileAButton:disabled,\n"
"#uploadFileBButton:disabled,\n"
"#resetPositionAButton:disabled,\n"
"#resetPositionBButton:disabled,\n"
"#validationPositionButton:disabled{\n"
"    background-color: #1a2333;\n"
"    border-color: #1a2333;\n"
"    colo"
                        "r: #5f6f85;\n"
"}\n"
"\n"
"\n"
"/* =========================\n"
"   Status bar\n"
"   ========================= */\n"
"#statusLayout {\n"
"    border: 1px solid #314158;\n"
"    background-color: #162556;\n"
"}\n"
"\n"
"#titleSimulationPage,\n"
"#titleResultsPage,\n"
"#titlePositioningPage,\n"
"#titleMeshingPage,\n"
"#titleMaterialsPage,\n"
"#titleGeometryPage {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#settingsSimulationPage,\n"
"#settingsResultsPage,\n"
"#settingsPositioningPage,\n"
"#settingsMeshingPage,\n"
"#settingsMaterialsPage,\n"
"#settingsGeometryPage,\n"
"#frameGeometryValidation,\n"
"#framePositioningValidation{\n"
"    border-top: 1px solid #314158;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"#frameGeometryA,\n"
"#frameGeometryB,\n"
"#framePositioningA,\n"
"#framePositioningB{\n"
"	background-color: #1d293d;\n"
"	border: 1px solid #314158;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_26 = QVBoxLayout(Widget)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.MainLayout = QVBoxLayout()
        self.MainLayout.setSpacing(0)
        self.MainLayout.setObjectName(u"MainLayout")
        self.topLayout = QWidget(Widget)
        self.topLayout.setObjectName(u"topLayout")
        self.horizontalLayout_4 = QHBoxLayout(self.topLayout)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, -1, 10)
        self.mainTitleLabel = QLabel(self.topLayout)
        self.mainTitleLabel.setObjectName(u"mainTitleLabel")
        self.mainTitleLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.mainTitleLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.mainTitleLabel)

        self.subTitleLabel = QLabel(self.topLayout)
        self.subTitleLabel.setObjectName(u"subTitleLabel")
        self.subTitleLabel.setLineWidth(1)
        self.subTitleLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.subTitleLabel.setWordWrap(True)
        self.subTitleLabel.setMargin(0)

        self.verticalLayout.addWidget(self.subTitleLabel)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.versionLabel = QLabel(self.topLayout)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setMinimumSize(QSize(80, 0))
        self.versionLabel.setMaximumSize(QSize(80, 16777215))
        self.versionLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.versionLabel.setWordWrap(True)
        self.versionLabel.setMargin(20)

        self.horizontalLayout_4.addWidget(self.versionLabel)


        self.MainLayout.addWidget(self.topLayout)

        self.centerLayout = QWidget(Widget)
        self.centerLayout.setObjectName(u"centerLayout")
        self.horizontalLayout = QHBoxLayout(self.centerLayout)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pipelineLayout = QWidget(self.centerLayout)
        self.pipelineLayout.setObjectName(u"pipelineLayout")
        self.pipelineLayout.setMaximumSize(QSize(170, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.pipelineLayout)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 0, 1, 0)
        self.pipelineTitleLayout = QWidget(self.pipelineLayout)
        self.pipelineTitleLayout.setObjectName(u"pipelineTitleLayout")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pipelineTitleLayout.sizePolicy().hasHeightForWidth())
        self.pipelineTitleLayout.setSizePolicy(sizePolicy)
        self.pipelineTitleLayout.setMinimumSize(QSize(0, 50))
        self.pipelineTitleLayout.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_3 = QVBoxLayout(self.pipelineTitleLayout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 6, -1, 15)
        self.pipelineTitleLabel = QLabel(self.pipelineTitleLayout)
        self.pipelineTitleLabel.setObjectName(u"pipelineTitleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pipelineTitleLabel.sizePolicy().hasHeightForWidth())
        self.pipelineTitleLabel.setSizePolicy(sizePolicy1)
        self.pipelineTitleLabel.setMinimumSize(QSize(0, 40))
        self.pipelineTitleLabel.setMaximumSize(QSize(16777215, 40))
        self.pipelineTitleLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.pipelineTitleLabel)


        self.verticalLayout_2.addWidget(self.pipelineTitleLayout)

        self.geometryButton = QPushButton(self.pipelineLayout)
        self.geometryButton.setObjectName(u"geometryButton")
        self.geometryButton.setMinimumSize(QSize(0, 50))
        self.geometryButton.setMaximumSize(QSize(16777215, 60))
        self.geometryButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/icons/icons/cube_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.geometryButton.setIcon(icon)
        self.geometryButton.setIconSize(QSize(15, 15))
        self.geometryButton.setCheckable(True)
        self.geometryButton.setChecked(True)
        self.geometryButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.geometryButton)

        self.positioningButton = QPushButton(self.pipelineLayout)
        self.positioningButton.setObjectName(u"positioningButton")
        self.positioningButton.setMinimumSize(QSize(0, 50))
        self.positioningButton.setMaximumSize(QSize(16777215, 60))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrows_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.positioningButton.setIcon(icon1)
        self.positioningButton.setIconSize(QSize(15, 15))
        self.positioningButton.setCheckable(True)
        self.positioningButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.positioningButton)

        self.meshingButton = QPushButton(self.pipelineLayout)
        self.meshingButton.setObjectName(u"meshingButton")
        self.meshingButton.setMinimumSize(QSize(0, 50))
        self.meshingButton.setMaximumSize(QSize(16777215, 60))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/mesh_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.meshingButton.setIcon(icon2)
        self.meshingButton.setIconSize(QSize(15, 15))
        self.meshingButton.setCheckable(True)
        self.meshingButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.meshingButton)

        self.materialsButton = QPushButton(self.pipelineLayout)
        self.materialsButton.setObjectName(u"materialsButton")
        self.materialsButton.setMinimumSize(QSize(0, 50))
        self.materialsButton.setMaximumSize(QSize(16777215, 60))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/build-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.materialsButton.setIcon(icon3)
        self.materialsButton.setIconSize(QSize(15, 15))
        self.materialsButton.setCheckable(True)
        self.materialsButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.materialsButton)

        self.simulationButton = QPushButton(self.pipelineLayout)
        self.simulationButton.setObjectName(u"simulationButton")
        self.simulationButton.setMinimumSize(QSize(0, 50))
        self.simulationButton.setMaximumSize(QSize(16777215, 60))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/play_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.simulationButton.setIcon(icon4)
        self.simulationButton.setIconSize(QSize(15, 15))
        self.simulationButton.setCheckable(True)
        self.simulationButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.simulationButton)

        self.resultsButton = QPushButton(self.pipelineLayout)
        self.resultsButton.setObjectName(u"resultsButton")
        self.resultsButton.setMinimumSize(QSize(0, 50))
        self.resultsButton.setMaximumSize(QSize(16777215, 60))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/chart_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resultsButton.setIcon(icon5)
        self.resultsButton.setIconSize(QSize(15, 15))
        self.resultsButton.setCheckable(True)
        self.resultsButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.resultsButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.hintLayout = QWidget(self.pipelineLayout)
        self.hintLayout.setObjectName(u"hintLayout")
        self.verticalLayout_4 = QVBoxLayout(self.hintLayout)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.hintLabel = QLabel(self.hintLayout)
        self.hintLabel.setObjectName(u"hintLabel")
        self.hintLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.hintLabel)


        self.verticalLayout_2.addWidget(self.hintLayout)


        self.horizontalLayout.addWidget(self.pipelineLayout)

        self.settingsLayout = QWidget(self.centerLayout)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsLayout.setMinimumSize(QSize(0, 0))
        self.settingsLayout.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.settingsLayout)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 1, 0, 0)
        self.stackedWidget = QStackedWidget(self.settingsLayout)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.geometryPage = QWidget()
        self.geometryPage.setObjectName(u"geometryPage")
        self.verticalLayout_6 = QVBoxLayout(self.geometryPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.geometryPageLayout = QWidget(self.geometryPage)
        self.geometryPageLayout.setObjectName(u"geometryPageLayout")
        self.verticalLayout_7 = QVBoxLayout(self.geometryPageLayout)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.titleGeometryPage = QWidget(self.geometryPageLayout)
        self.titleGeometryPage.setObjectName(u"titleGeometryPage")
        self.titleGeometryPage.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_23 = QVBoxLayout(self.titleGeometryPage)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(15, 10, 15, 10)
        self.maintitleGeometryPage = QLabel(self.titleGeometryPage)
        self.maintitleGeometryPage.setObjectName(u"maintitleGeometryPage")
        self.maintitleGeometryPage.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.maintitleGeometryPage)

        self.subtitleGeometryPage = QLabel(self.titleGeometryPage)
        self.subtitleGeometryPage.setObjectName(u"subtitleGeometryPage")
        self.subtitleGeometryPage.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.subtitleGeometryPage)


        self.verticalLayout_7.addWidget(self.titleGeometryPage)

        self.settingsGeometryPage = QWidget(self.geometryPageLayout)
        self.settingsGeometryPage.setObjectName(u"settingsGeometryPage")
        self.verticalLayout_24 = QVBoxLayout(self.settingsGeometryPage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 1, 0, 0)
        self.scrollAreaGeometry = QScrollArea(self.settingsGeometryPage)
        self.scrollAreaGeometry.setObjectName(u"scrollAreaGeometry")
        self.scrollAreaGeometry.setWidgetResizable(True)
        self.scrollAreaWidgetContentsGeometry = QWidget()
        self.scrollAreaWidgetContentsGeometry.setObjectName(u"scrollAreaWidgetContentsGeometry")
        self.scrollAreaWidgetContentsGeometry.setGeometry(QRect(0, 0, 314, 475))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContentsGeometry)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(20, 20, 20, 20)
        self.frameGeometryA = QFrame(self.scrollAreaWidgetContentsGeometry)
        self.frameGeometryA.setObjectName(u"frameGeometryA")
        self.frameGeometryA.setMinimumSize(QSize(0, 130))
        self.frameGeometryA.setMaximumSize(QSize(16777215, 130))
        self.frameGeometryA.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameGeometryA.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frameGeometryA)
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(15, 15, 15, 15)
        self.objectALabel = QLabel(self.frameGeometryA)
        self.objectALabel.setObjectName(u"objectALabel")

        self.verticalLayout_25.addWidget(self.objectALabel)

        self.stlfileAlabel = QLabel(self.frameGeometryA)
        self.stlfileAlabel.setObjectName(u"stlfileAlabel")

        self.verticalLayout_25.addWidget(self.stlfileAlabel)

        self.uploadFileAButton = QPushButton(self.frameGeometryA)
        self.uploadFileAButton.setObjectName(u"uploadFileAButton")
        self.uploadFileAButton.setMinimumSize(QSize(0, 35))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/upload.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.uploadFileAButton.setIcon(icon6)
        self.uploadFileAButton.setIconSize(QSize(15, 12))

        self.verticalLayout_25.addWidget(self.uploadFileAButton)


        self.verticalLayout_28.addWidget(self.frameGeometryA)

        self.frameGeometryB = QFrame(self.scrollAreaWidgetContentsGeometry)
        self.frameGeometryB.setObjectName(u"frameGeometryB")
        self.frameGeometryB.setMinimumSize(QSize(0, 130))
        self.frameGeometryB.setMaximumSize(QSize(16777215, 130))
        self.frameGeometryB.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameGeometryB.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frameGeometryB)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(15, 15, 15, 15)
        self.objectBLabel = QLabel(self.frameGeometryB)
        self.objectBLabel.setObjectName(u"objectBLabel")

        self.verticalLayout_27.addWidget(self.objectBLabel)

        self.stlfileBlabel = QLabel(self.frameGeometryB)
        self.stlfileBlabel.setObjectName(u"stlfileBlabel")

        self.verticalLayout_27.addWidget(self.stlfileBlabel)

        self.uploadFileBButton = QPushButton(self.frameGeometryB)
        self.uploadFileBButton.setObjectName(u"uploadFileBButton")
        self.uploadFileBButton.setMinimumSize(QSize(0, 35))
        self.uploadFileBButton.setIcon(icon6)
        self.uploadFileBButton.setIconSize(QSize(15, 12))

        self.verticalLayout_27.addWidget(self.uploadFileBButton)


        self.verticalLayout_28.addWidget(self.frameGeometryB)

        self.frameGeometryValidation = QFrame(self.scrollAreaWidgetContentsGeometry)
        self.frameGeometryValidation.setObjectName(u"frameGeometryValidation")
        self.frameGeometryValidation.setMinimumSize(QSize(0, 130))
        self.frameGeometryValidation.setMaximumSize(QSize(16777215, 130))
        self.frameGeometryValidation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameGeometryValidation.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frameGeometryValidation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.objectALoadedLabel = QLabel(self.frameGeometryValidation)
        self.objectALoadedLabel.setObjectName(u"objectALoadedLabel")

        self.gridLayout.addWidget(self.objectALoadedLabel, 2, 1, 1, 1)

        self.objectALoadedIcon = QLabel(self.frameGeometryValidation)
        self.objectALoadedIcon.setObjectName(u"objectALoadedIcon")
        self.objectALoadedIcon.setMinimumSize(QSize(10, 10))
        self.objectALoadedIcon.setMaximumSize(QSize(10, 10))
        self.objectALoadedIcon.setPixmap(QPixmap(u":/icons/icons/uncheck_white.svg"))
        self.objectALoadedIcon.setScaledContents(True)

        self.gridLayout.addWidget(self.objectALoadedIcon, 2, 0, 1, 1)

        self.objectBLoadedIcon = QLabel(self.frameGeometryValidation)
        self.objectBLoadedIcon.setObjectName(u"objectBLoadedIcon")
        self.objectBLoadedIcon.setMinimumSize(QSize(10, 10))
        self.objectBLoadedIcon.setMaximumSize(QSize(10, 10))
        self.objectBLoadedIcon.setPixmap(QPixmap(u":/icons/icons/uncheck_white.svg"))
        self.objectBLoadedIcon.setScaledContents(True)

        self.gridLayout.addWidget(self.objectBLoadedIcon, 3, 0, 1, 1)

        self.objectBLoadedLabel = QLabel(self.frameGeometryValidation)
        self.objectBLoadedLabel.setObjectName(u"objectBLoadedLabel")

        self.gridLayout.addWidget(self.objectBLoadedLabel, 3, 1, 1, 1)

        self.readyPositioningIcon = QLabel(self.frameGeometryValidation)
        self.readyPositioningIcon.setObjectName(u"readyPositioningIcon")
        self.readyPositioningIcon.setMinimumSize(QSize(10, 10))
        self.readyPositioningIcon.setMaximumSize(QSize(10, 10))
        self.readyPositioningIcon.setPixmap(QPixmap(u":/icons/icons/uncheck_white.svg"))
        self.readyPositioningIcon.setScaledContents(True)

        self.gridLayout.addWidget(self.readyPositioningIcon, 5, 0, 1, 1)

        self.readyPositioningLabel = QLabel(self.frameGeometryValidation)
        self.readyPositioningLabel.setObjectName(u"readyPositioningLabel")

        self.gridLayout.addWidget(self.readyPositioningLabel, 5, 1, 1, 1)

        self.validationGeometryLabel = QLabel(self.frameGeometryValidation)
        self.validationGeometryLabel.setObjectName(u"validationGeometryLabel")
        self.validationGeometryLabel.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.validationGeometryLabel, 0, 0, 1, 3)


        self.verticalLayout_28.addWidget(self.frameGeometryValidation)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_2)

        self.scrollAreaGeometry.setWidget(self.scrollAreaWidgetContentsGeometry)

        self.verticalLayout_24.addWidget(self.scrollAreaGeometry)


        self.verticalLayout_7.addWidget(self.settingsGeometryPage)


        self.verticalLayout_6.addWidget(self.geometryPageLayout)

        self.stackedWidget.addWidget(self.geometryPage)
        self.meshingPage = QWidget()
        self.meshingPage.setObjectName(u"meshingPage")
        self.verticalLayout_10 = QVBoxLayout(self.meshingPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.meshingPageLayout = QWidget(self.meshingPage)
        self.meshingPageLayout.setObjectName(u"meshingPageLayout")
        self.verticalLayout_14 = QVBoxLayout(self.meshingPageLayout)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.titleMeshingPage = QWidget(self.meshingPageLayout)
        self.titleMeshingPage.setObjectName(u"titleMeshingPage")
        self.titleMeshingPage.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_21 = QVBoxLayout(self.titleMeshingPage)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(15, 10, 15, 10)
        self.maintitleMeshingPage = QLabel(self.titleMeshingPage)
        self.maintitleMeshingPage.setObjectName(u"maintitleMeshingPage")
        self.maintitleMeshingPage.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.maintitleMeshingPage)

        self.subtitleMeshingPage = QLabel(self.titleMeshingPage)
        self.subtitleMeshingPage.setObjectName(u"subtitleMeshingPage")
        self.subtitleMeshingPage.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.subtitleMeshingPage)


        self.verticalLayout_14.addWidget(self.titleMeshingPage)

        self.settingsMeshingPage = QWidget(self.meshingPageLayout)
        self.settingsMeshingPage.setObjectName(u"settingsMeshingPage")
        self.verticalLayout_35 = QVBoxLayout(self.settingsMeshingPage)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 1, 0, 0)
        self.scrollAreaPositioning_2 = QScrollArea(self.settingsMeshingPage)
        self.scrollAreaPositioning_2.setObjectName(u"scrollAreaPositioning_2")
        self.scrollAreaPositioning_2.setWidgetResizable(True)
        self.scrollAreaWidgetContentsPositioning_2 = QWidget()
        self.scrollAreaWidgetContentsPositioning_2.setObjectName(u"scrollAreaWidgetContentsPositioning_2")
        self.scrollAreaWidgetContentsPositioning_2.setGeometry(QRect(0, -12, 314, 1000))
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContentsPositioning_2)
        self.verticalLayout_34.setSpacing(15)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(20, 20, 20, 20)
        self.framePositioningA_2 = QFrame(self.scrollAreaWidgetContentsPositioning_2)
        self.framePositioningA_2.setObjectName(u"framePositioningA_2")
        self.framePositioningA_2.setMinimumSize(QSize(0, 400))
        self.framePositioningA_2.setMaximumSize(QSize(16777215, 1000))
        self.framePositioningA_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePositioningA_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.framePositioningA_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.xRotationASlider_2 = QSlider(self.framePositioningA_2)
        self.xRotationASlider_2.setObjectName(u"xRotationASlider_2")
        self.xRotationASlider_2.setMaximum(100)
        self.xRotationASlider_2.setValue(50)
        self.xRotationASlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.xRotationASlider_2, 9, 2, 1, 1)

        self.rotationPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.rotationPositionALabel_2.setObjectName(u"rotationPositionALabel_2")
        self.rotationPositionALabel_2.setMinimumSize(QSize(0, 25))
        self.rotationPositionALabel_2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.rotationPositionALabel_2, 8, 2, 1, 1)

        self.resetPositionAButton_2 = QPushButton(self.framePositioningA_2)
        self.resetPositionAButton_2.setObjectName(u"resetPositionAButton_2")
        self.resetPositionAButton_2.setMaximumSize(QSize(50, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/undo-alt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.resetPositionAButton_2.setIcon(icon7)
        self.resetPositionAButton_2.setIconSize(QSize(12, 12))

        self.gridLayout_2.addWidget(self.resetPositionAButton_2, 0, 3, 1, 1)

        self.positionObjectALabel_2 = QLabel(self.framePositioningA_2)
        self.positionObjectALabel_2.setObjectName(u"positionObjectALabel_2")

        self.gridLayout_2.addWidget(self.positionObjectALabel_2, 0, 0, 1, 3)

        self.xRotationPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.xRotationPositionALabel_2.setObjectName(u"xRotationPositionALabel_2")

        self.gridLayout_2.addWidget(self.xRotationPositionALabel_2, 9, 0, 1, 1)

        self.xTranslationASpinbox_2 = QDoubleSpinBox(self.framePositioningA_2)
        self.xTranslationASpinbox_2.setObjectName(u"xTranslationASpinbox_2")
        self.xTranslationASpinbox_2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.gridLayout_2.addWidget(self.xTranslationASpinbox_2, 5, 2, 1, 1)

        self.yTranslationUnitPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.yTranslationUnitPositionALabel_2.setObjectName(u"yTranslationUnitPositionALabel_2")
        self.yTranslationUnitPositionALabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.yTranslationUnitPositionALabel_2, 6, 3, 1, 1)

        self.yTranslationASpinbox_2 = QDoubleSpinBox(self.framePositioningA_2)
        self.yTranslationASpinbox_2.setObjectName(u"yTranslationASpinbox_2")

        self.gridLayout_2.addWidget(self.yTranslationASpinbox_2, 6, 2, 1, 1)

        self.xTranslationUnitPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.xTranslationUnitPositionALabel_2.setObjectName(u"xTranslationUnitPositionALabel_2")
        self.xTranslationUnitPositionALabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.xTranslationUnitPositionALabel_2, 5, 3, 1, 1)

        self.zRotationUnitPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.zRotationUnitPositionALabel_2.setObjectName(u"zRotationUnitPositionALabel_2")

        self.gridLayout_2.addWidget(self.zRotationUnitPositionALabel_2, 11, 3, 1, 1)

        self.yTranslationPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.yTranslationPositionALabel_2.setObjectName(u"yTranslationPositionALabel_2")

        self.gridLayout_2.addWidget(self.yTranslationPositionALabel_2, 6, 0, 1, 1)

        self.zTranslationPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.zTranslationPositionALabel_2.setObjectName(u"zTranslationPositionALabel_2")

        self.gridLayout_2.addWidget(self.zTranslationPositionALabel_2, 7, 0, 1, 1)

        self.yRotationUnitPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.yRotationUnitPositionALabel_2.setObjectName(u"yRotationUnitPositionALabel_2")
        self.yRotationUnitPositionALabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.yRotationUnitPositionALabel_2, 10, 3, 1, 1)

        self.zRotationASlider_2 = QSlider(self.framePositioningA_2)
        self.zRotationASlider_2.setObjectName(u"zRotationASlider_2")
        self.zRotationASlider_2.setValue(50)
        self.zRotationASlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.zRotationASlider_2, 11, 2, 1, 1)

        self.yRotationPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.yRotationPositionALabel_2.setObjectName(u"yRotationPositionALabel_2")

        self.gridLayout_2.addWidget(self.yRotationPositionALabel_2, 10, 0, 1, 1)

        self.xTranslationPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.xTranslationPositionALabel_2.setObjectName(u"xTranslationPositionALabel_2")

        self.gridLayout_2.addWidget(self.xTranslationPositionALabel_2, 5, 0, 1, 1)

        self.rotationPositionAIcon_2 = QLabel(self.framePositioningA_2)
        self.rotationPositionAIcon_2.setObjectName(u"rotationPositionAIcon_2")
        self.rotationPositionAIcon_2.setMinimumSize(QSize(11, 11))
        self.rotationPositionAIcon_2.setMaximumSize(QSize(11, 11))
        self.rotationPositionAIcon_2.setPixmap(QPixmap(u":/icons/icons/rotate-right.svg"))
        self.rotationPositionAIcon_2.setScaledContents(True)

        self.gridLayout_2.addWidget(self.rotationPositionAIcon_2, 8, 0, 1, 1)

        self.xRotationUnitPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.xRotationUnitPositionALabel_2.setObjectName(u"xRotationUnitPositionALabel_2")
        self.xRotationUnitPositionALabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.xRotationUnitPositionALabel_2, 9, 3, 1, 1)

        self.zRotationPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.zRotationPositionALabel_2.setObjectName(u"zRotationPositionALabel_2")

        self.gridLayout_2.addWidget(self.zRotationPositionALabel_2, 11, 0, 1, 1)

        self.zTranslationASpinbox_2 = QDoubleSpinBox(self.framePositioningA_2)
        self.zTranslationASpinbox_2.setObjectName(u"zTranslationASpinbox_2")

        self.gridLayout_2.addWidget(self.zTranslationASpinbox_2, 7, 2, 1, 1)

        self.translationPositionAIcon_2 = QLabel(self.framePositioningA_2)
        self.translationPositionAIcon_2.setObjectName(u"translationPositionAIcon_2")
        self.translationPositionAIcon_2.setMinimumSize(QSize(11, 11))
        self.translationPositionAIcon_2.setMaximumSize(QSize(11, 11))
        self.translationPositionAIcon_2.setPixmap(QPixmap(u":/icons/icons/arrows_dark.svg"))
        self.translationPositionAIcon_2.setScaledContents(True)

        self.gridLayout_2.addWidget(self.translationPositionAIcon_2, 4, 0, 1, 1)

        self.yRotationASlider_2 = QSlider(self.framePositioningA_2)
        self.yRotationASlider_2.setObjectName(u"yRotationASlider_2")
        self.yRotationASlider_2.setValue(50)
        self.yRotationASlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.yRotationASlider_2, 10, 2, 1, 1)

        self.translationPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.translationPositionALabel_2.setObjectName(u"translationPositionALabel_2")
        self.translationPositionALabel_2.setMinimumSize(QSize(0, 25))
        self.translationPositionALabel_2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_2.addWidget(self.translationPositionALabel_2, 4, 2, 1, 1)

        self.zTranslationUnitPositionALabel_2 = QLabel(self.framePositioningA_2)
        self.zTranslationUnitPositionALabel_2.setObjectName(u"zTranslationUnitPositionALabel_2")
        self.zTranslationUnitPositionALabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_2.addWidget(self.zTranslationUnitPositionALabel_2, 7, 3, 1, 1)

        self.generateMeshAButton = QPushButton(self.framePositioningA_2)
        self.generateMeshAButton.setObjectName(u"generateMeshAButton")
        self.generateMeshAButton.setMinimumSize(QSize(0, 35))
        self.generateMeshAButton.setStyleSheet(u"\n"
"background-color: #1447e6")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/warning_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generateMeshAButton.setIcon(icon8)
        self.generateMeshAButton.setIconSize(QSize(14, 14))

        self.gridLayout_2.addWidget(self.generateMeshAButton, 1, 2, 1, 1)


        self.verticalLayout_34.addWidget(self.framePositioningA_2)

        self.framePositioningB_2 = QFrame(self.scrollAreaWidgetContentsPositioning_2)
        self.framePositioningB_2.setObjectName(u"framePositioningB_2")
        self.framePositioningB_2.setMinimumSize(QSize(0, 400))
        self.framePositioningB_2.setMaximumSize(QSize(16777215, 500))
        self.framePositioningB_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePositioningB_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.framePositioningB_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(5)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(10, 0, 10, 0)
        self.xTranslationBSpinbox_2 = QDoubleSpinBox(self.framePositioningB_2)
        self.xTranslationBSpinbox_2.setObjectName(u"xTranslationBSpinbox_2")
        self.xTranslationBSpinbox_2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.gridLayout_6.addWidget(self.xTranslationBSpinbox_2, 3, 1, 1, 1)

        self.zRotationUnitPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.zRotationUnitPositionBLabel_2.setObjectName(u"zRotationUnitPositionBLabel_2")

        self.gridLayout_6.addWidget(self.zRotationUnitPositionBLabel_2, 9, 2, 1, 1)

        self.translationPositionBIcon_2 = QLabel(self.framePositioningB_2)
        self.translationPositionBIcon_2.setObjectName(u"translationPositionBIcon_2")
        self.translationPositionBIcon_2.setMinimumSize(QSize(11, 11))
        self.translationPositionBIcon_2.setMaximumSize(QSize(11, 11))
        self.translationPositionBIcon_2.setPixmap(QPixmap(u":/icons/icons/arrows_dark.svg"))
        self.translationPositionBIcon_2.setScaledContents(True)

        self.gridLayout_6.addWidget(self.translationPositionBIcon_2, 2, 0, 1, 1)

        self.resetPositionBButton_2 = QPushButton(self.framePositioningB_2)
        self.resetPositionBButton_2.setObjectName(u"resetPositionBButton_2")
        self.resetPositionBButton_2.setMaximumSize(QSize(50, 16777215))
        self.resetPositionBButton_2.setIcon(icon7)
        self.resetPositionBButton_2.setIconSize(QSize(12, 12))

        self.gridLayout_6.addWidget(self.resetPositionBButton_2, 1, 2, 1, 1)

        self.zRotationPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.zRotationPositionBLabel_2.setObjectName(u"zRotationPositionBLabel_2")

        self.gridLayout_6.addWidget(self.zRotationPositionBLabel_2, 9, 0, 1, 1)

        self.yTranslationUnitPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.yTranslationUnitPositionBLabel_2.setObjectName(u"yTranslationUnitPositionBLabel_2")
        self.yTranslationUnitPositionBLabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_6.addWidget(self.yTranslationUnitPositionBLabel_2, 4, 2, 1, 1)

        self.xTranslationPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.xTranslationPositionBLabel_2.setObjectName(u"xTranslationPositionBLabel_2")

        self.gridLayout_6.addWidget(self.xTranslationPositionBLabel_2, 3, 0, 1, 1)

        self.zTranslationUnitPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.zTranslationUnitPositionBLabel_2.setObjectName(u"zTranslationUnitPositionBLabel_2")
        self.zTranslationUnitPositionBLabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_6.addWidget(self.zTranslationUnitPositionBLabel_2, 5, 2, 1, 1)

        self.yRotationUnitPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.yRotationUnitPositionBLabel_2.setObjectName(u"yRotationUnitPositionBLabel_2")
        self.yRotationUnitPositionBLabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_6.addWidget(self.yRotationUnitPositionBLabel_2, 8, 2, 1, 1)

        self.rotationPositionbIcon_2 = QLabel(self.framePositioningB_2)
        self.rotationPositionbIcon_2.setObjectName(u"rotationPositionbIcon_2")
        self.rotationPositionbIcon_2.setMinimumSize(QSize(11, 11))
        self.rotationPositionbIcon_2.setMaximumSize(QSize(11, 11))
        self.rotationPositionbIcon_2.setPixmap(QPixmap(u":/icons/icons/rotate-right.svg"))
        self.rotationPositionbIcon_2.setScaledContents(True)

        self.gridLayout_6.addWidget(self.rotationPositionbIcon_2, 6, 0, 1, 1)

        self.yRotationBSlider_2 = QSlider(self.framePositioningB_2)
        self.yRotationBSlider_2.setObjectName(u"yRotationBSlider_2")
        self.yRotationBSlider_2.setMaximum(100)
        self.yRotationBSlider_2.setValue(50)
        self.yRotationBSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_6.addWidget(self.yRotationBSlider_2, 8, 1, 1, 1)

        self.zTranslationBSpinbox_2 = QDoubleSpinBox(self.framePositioningB_2)
        self.zTranslationBSpinbox_2.setObjectName(u"zTranslationBSpinbox_2")

        self.gridLayout_6.addWidget(self.zTranslationBSpinbox_2, 5, 1, 1, 1)

        self.zRotationBSlider_2 = QSlider(self.framePositioningB_2)
        self.zRotationBSlider_2.setObjectName(u"zRotationBSlider_2")
        self.zRotationBSlider_2.setMaximum(100)
        self.zRotationBSlider_2.setValue(50)
        self.zRotationBSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_6.addWidget(self.zRotationBSlider_2, 9, 1, 1, 1)

        self.translationPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.translationPositionBLabel_2.setObjectName(u"translationPositionBLabel_2")
        self.translationPositionBLabel_2.setMinimumSize(QSize(0, 25))
        self.translationPositionBLabel_2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_6.addWidget(self.translationPositionBLabel_2, 2, 1, 1, 1)

        self.yTranslationBSpinbox_2 = QDoubleSpinBox(self.framePositioningB_2)
        self.yTranslationBSpinbox_2.setObjectName(u"yTranslationBSpinbox_2")

        self.gridLayout_6.addWidget(self.yTranslationBSpinbox_2, 4, 1, 1, 1)

        self.xRotationPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.xRotationPositionBLabel_2.setObjectName(u"xRotationPositionBLabel_2")

        self.gridLayout_6.addWidget(self.xRotationPositionBLabel_2, 7, 0, 1, 1)

        self.positionObjectBLabel_2 = QLabel(self.framePositioningB_2)
        self.positionObjectBLabel_2.setObjectName(u"positionObjectBLabel_2")

        self.gridLayout_6.addWidget(self.positionObjectBLabel_2, 1, 0, 1, 2)

        self.rotationPositionbLabel_2 = QLabel(self.framePositioningB_2)
        self.rotationPositionbLabel_2.setObjectName(u"rotationPositionbLabel_2")
        self.rotationPositionbLabel_2.setMinimumSize(QSize(0, 25))
        self.rotationPositionbLabel_2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_6.addWidget(self.rotationPositionbLabel_2, 6, 1, 1, 1)

        self.xRotationUnitPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.xRotationUnitPositionBLabel_2.setObjectName(u"xRotationUnitPositionBLabel_2")
        self.xRotationUnitPositionBLabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_6.addWidget(self.xRotationUnitPositionBLabel_2, 7, 2, 1, 1)

        self.yTranslationPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.yTranslationPositionBLabel_2.setObjectName(u"yTranslationPositionBLabel_2")

        self.gridLayout_6.addWidget(self.yTranslationPositionBLabel_2, 4, 0, 1, 1)

        self.xRotationBSlider_2 = QSlider(self.framePositioningB_2)
        self.xRotationBSlider_2.setObjectName(u"xRotationBSlider_2")
        self.xRotationBSlider_2.setMaximum(100)
        self.xRotationBSlider_2.setValue(50)
        self.xRotationBSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_6.addWidget(self.xRotationBSlider_2, 7, 1, 1, 1)

        self.xTranslationUnitPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.xTranslationUnitPositionBLabel_2.setObjectName(u"xTranslationUnitPositionBLabel_2")
        self.xTranslationUnitPositionBLabel_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_6.addWidget(self.xTranslationUnitPositionBLabel_2, 3, 2, 1, 1)

        self.yRotationPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.yRotationPositionBLabel_2.setObjectName(u"yRotationPositionBLabel_2")

        self.gridLayout_6.addWidget(self.yRotationPositionBLabel_2, 8, 0, 1, 1)

        self.zTranslationPositionBLabel_2 = QLabel(self.framePositioningB_2)
        self.zTranslationPositionBLabel_2.setObjectName(u"zTranslationPositionBLabel_2")

        self.gridLayout_6.addWidget(self.zTranslationPositionBLabel_2, 5, 0, 1, 1)


        self.verticalLayout_34.addWidget(self.framePositioningB_2)

        self.framePositioningValidation_2 = QFrame(self.scrollAreaWidgetContentsPositioning_2)
        self.framePositioningValidation_2.setObjectName(u"framePositioningValidation_2")
        self.framePositioningValidation_2.setMinimumSize(QSize(0, 130))
        self.framePositioningValidation_2.setMaximumSize(QSize(16777215, 130))
        self.framePositioningValidation_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePositioningValidation_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.framePositioningValidation_2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.validationPositioningLabel_2 = QLabel(self.framePositioningValidation_2)
        self.validationPositioningLabel_2.setObjectName(u"validationPositioningLabel_2")
        self.validationPositioningLabel_2.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_32.addWidget(self.validationPositioningLabel_2)

        self.validationPositionButton_2 = QPushButton(self.framePositioningValidation_2)
        self.validationPositionButton_2.setObjectName(u"validationPositionButton_2")
        self.validationPositionButton_2.setMinimumSize(QSize(0, 35))
        self.validationPositionButton_2.setStyleSheet(u"\n"
"background-color: #1447e6")
        self.validationPositionButton_2.setIcon(icon8)
        self.validationPositionButton_2.setIconSize(QSize(14, 14))

        self.verticalLayout_32.addWidget(self.validationPositionButton_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_4)


        self.verticalLayout_34.addWidget(self.framePositioningValidation_2)

        self.scrollAreaPositioning_2.setWidget(self.scrollAreaWidgetContentsPositioning_2)

        self.verticalLayout_35.addWidget(self.scrollAreaPositioning_2)


        self.verticalLayout_14.addWidget(self.settingsMeshingPage)


        self.verticalLayout_10.addWidget(self.meshingPageLayout)

        self.stackedWidget.addWidget(self.meshingPage)
        self.materialsPage = QWidget()
        self.materialsPage.setObjectName(u"materialsPage")
        self.verticalLayout_8 = QVBoxLayout(self.materialsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.materialsPageLayout = QWidget(self.materialsPage)
        self.materialsPageLayout.setObjectName(u"materialsPageLayout")
        self.verticalLayout_9 = QVBoxLayout(self.materialsPageLayout)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.titleMaterialsPage = QWidget(self.materialsPageLayout)
        self.titleMaterialsPage.setObjectName(u"titleMaterialsPage")
        self.titleMaterialsPage.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_22 = QVBoxLayout(self.titleMaterialsPage)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 10, 15, 10)
        self.maintitleMaterialsPage = QLabel(self.titleMaterialsPage)
        self.maintitleMaterialsPage.setObjectName(u"maintitleMaterialsPage")
        self.maintitleMaterialsPage.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.maintitleMaterialsPage)

        self.subtitleMaterialsPage = QLabel(self.titleMaterialsPage)
        self.subtitleMaterialsPage.setObjectName(u"subtitleMaterialsPage")
        self.subtitleMaterialsPage.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.subtitleMaterialsPage)


        self.verticalLayout_9.addWidget(self.titleMaterialsPage)

        self.settingsMaterialsPage = QWidget(self.materialsPageLayout)
        self.settingsMaterialsPage.setObjectName(u"settingsMaterialsPage")

        self.verticalLayout_9.addWidget(self.settingsMaterialsPage)


        self.verticalLayout_8.addWidget(self.materialsPageLayout)

        self.stackedWidget.addWidget(self.materialsPage)
        self.simulationPage = QWidget()
        self.simulationPage.setObjectName(u"simulationPage")
        self.verticalLayout_13 = QVBoxLayout(self.simulationPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.simulationPageLayout = QWidget(self.simulationPage)
        self.simulationPageLayout.setObjectName(u"simulationPageLayout")
        self.verticalLayout_17 = QVBoxLayout(self.simulationPageLayout)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.titleSimulationPage = QWidget(self.simulationPageLayout)
        self.titleSimulationPage.setObjectName(u"titleSimulationPage")
        self.titleSimulationPage.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_18 = QVBoxLayout(self.titleSimulationPage)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(15, 10, 15, 10)
        self.maintitleSimulationPage = QLabel(self.titleSimulationPage)
        self.maintitleSimulationPage.setObjectName(u"maintitleSimulationPage")
        self.maintitleSimulationPage.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.maintitleSimulationPage)

        self.subtitleSimulationPage = QLabel(self.titleSimulationPage)
        self.subtitleSimulationPage.setObjectName(u"subtitleSimulationPage")
        self.subtitleSimulationPage.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.subtitleSimulationPage)


        self.verticalLayout_17.addWidget(self.titleSimulationPage)

        self.settingsSimulationPage = QWidget(self.simulationPageLayout)
        self.settingsSimulationPage.setObjectName(u"settingsSimulationPage")

        self.verticalLayout_17.addWidget(self.settingsSimulationPage)


        self.verticalLayout_13.addWidget(self.simulationPageLayout)

        self.stackedWidget.addWidget(self.simulationPage)
        self.resultsPage = QWidget()
        self.resultsPage.setObjectName(u"resultsPage")
        self.verticalLayout_12 = QVBoxLayout(self.resultsPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.resultsPageLayout = QWidget(self.resultsPage)
        self.resultsPageLayout.setObjectName(u"resultsPageLayout")
        self.verticalLayout_16 = QVBoxLayout(self.resultsPageLayout)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.titleResultsPage = QWidget(self.resultsPageLayout)
        self.titleResultsPage.setObjectName(u"titleResultsPage")
        self.titleResultsPage.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_19 = QVBoxLayout(self.titleResultsPage)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(15, 10, 15, 10)
        self.maintitleResultsPage = QLabel(self.titleResultsPage)
        self.maintitleResultsPage.setObjectName(u"maintitleResultsPage")
        self.maintitleResultsPage.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.maintitleResultsPage)

        self.subtitleResultsPage = QLabel(self.titleResultsPage)
        self.subtitleResultsPage.setObjectName(u"subtitleResultsPage")
        self.subtitleResultsPage.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.subtitleResultsPage)


        self.verticalLayout_16.addWidget(self.titleResultsPage)

        self.settingsResultsPage = QWidget(self.resultsPageLayout)
        self.settingsResultsPage.setObjectName(u"settingsResultsPage")

        self.verticalLayout_16.addWidget(self.settingsResultsPage)


        self.verticalLayout_12.addWidget(self.resultsPageLayout)

        self.stackedWidget.addWidget(self.resultsPage)
        self.positioningPage = QWidget()
        self.positioningPage.setObjectName(u"positioningPage")
        self.verticalLayout_11 = QVBoxLayout(self.positioningPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.positioningPageLayout = QWidget(self.positioningPage)
        self.positioningPageLayout.setObjectName(u"positioningPageLayout")
        self.verticalLayout_15 = QVBoxLayout(self.positioningPageLayout)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.titlePositioningPage = QWidget(self.positioningPageLayout)
        self.titlePositioningPage.setObjectName(u"titlePositioningPage")
        self.titlePositioningPage.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_20 = QVBoxLayout(self.titlePositioningPage)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(15, 10, 15, 10)
        self.maintitlePositioningPage = QLabel(self.titlePositioningPage)
        self.maintitlePositioningPage.setObjectName(u"maintitlePositioningPage")
        self.maintitlePositioningPage.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.maintitlePositioningPage)

        self.subtitlePositioningPage = QLabel(self.titlePositioningPage)
        self.subtitlePositioningPage.setObjectName(u"subtitlePositioningPage")
        self.subtitlePositioningPage.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.subtitlePositioningPage)


        self.verticalLayout_15.addWidget(self.titlePositioningPage)

        self.settingsPositioningPage = QWidget(self.positioningPageLayout)
        self.settingsPositioningPage.setObjectName(u"settingsPositioningPage")
        self.verticalLayout_30 = QVBoxLayout(self.settingsPositioningPage)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 1, 0, 0)
        self.scrollAreaPositioning = QScrollArea(self.settingsPositioningPage)
        self.scrollAreaPositioning.setObjectName(u"scrollAreaPositioning")
        self.scrollAreaPositioning.setWidgetResizable(True)
        self.scrollAreaWidgetContentsPositioning = QWidget()
        self.scrollAreaWidgetContentsPositioning.setObjectName(u"scrollAreaWidgetContentsPositioning")
        self.scrollAreaWidgetContentsPositioning.setGeometry(QRect(0, 0, 314, 1000))
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContentsPositioning)
        self.verticalLayout_33.setSpacing(15)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(20, 20, 20, 20)
        self.framePositioningA = QFrame(self.scrollAreaWidgetContentsPositioning)
        self.framePositioningA.setObjectName(u"framePositioningA")
        self.framePositioningA.setMinimumSize(QSize(0, 400))
        self.framePositioningA.setMaximumSize(QSize(16777215, 1000))
        self.framePositioningA.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePositioningA.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.framePositioningA)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(10, 0, 10, 0)
        self.xTranslationPositionALabel = QLabel(self.framePositioningA)
        self.xTranslationPositionALabel.setObjectName(u"xTranslationPositionALabel")

        self.gridLayout_3.addWidget(self.xTranslationPositionALabel, 2, 0, 1, 1)

        self.zTranslationASpinbox = QDoubleSpinBox(self.framePositioningA)
        self.zTranslationASpinbox.setObjectName(u"zTranslationASpinbox")

        self.gridLayout_3.addWidget(self.zTranslationASpinbox, 4, 1, 1, 1)

        self.yTranslationUnitPositionALabel = QLabel(self.framePositioningA)
        self.yTranslationUnitPositionALabel.setObjectName(u"yTranslationUnitPositionALabel")
        self.yTranslationUnitPositionALabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.yTranslationUnitPositionALabel, 3, 2, 1, 1)

        self.yTranslationASpinbox = QDoubleSpinBox(self.framePositioningA)
        self.yTranslationASpinbox.setObjectName(u"yTranslationASpinbox")

        self.gridLayout_3.addWidget(self.yTranslationASpinbox, 3, 1, 1, 1)

        self.yRotationPositionALabel = QLabel(self.framePositioningA)
        self.yRotationPositionALabel.setObjectName(u"yRotationPositionALabel")

        self.gridLayout_3.addWidget(self.yRotationPositionALabel, 8, 0, 1, 1)

        self.translationPositionALabel = QLabel(self.framePositioningA)
        self.translationPositionALabel.setObjectName(u"translationPositionALabel")
        self.translationPositionALabel.setMinimumSize(QSize(0, 25))
        self.translationPositionALabel.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_3.addWidget(self.translationPositionALabel, 1, 1, 1, 1)

        self.xTranslationASpinbox = QDoubleSpinBox(self.framePositioningA)
        self.xTranslationASpinbox.setObjectName(u"xTranslationASpinbox")
        self.xTranslationASpinbox.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.gridLayout_3.addWidget(self.xTranslationASpinbox, 2, 1, 1, 1)

        self.translationPositionAIcon = QLabel(self.framePositioningA)
        self.translationPositionAIcon.setObjectName(u"translationPositionAIcon")
        self.translationPositionAIcon.setMinimumSize(QSize(11, 11))
        self.translationPositionAIcon.setMaximumSize(QSize(11, 11))
        self.translationPositionAIcon.setPixmap(QPixmap(u":/icons/icons/arrows_dark.svg"))
        self.translationPositionAIcon.setScaledContents(True)

        self.gridLayout_3.addWidget(self.translationPositionAIcon, 1, 0, 1, 1)

        self.positionObjectALabel = QLabel(self.framePositioningA)
        self.positionObjectALabel.setObjectName(u"positionObjectALabel")

        self.gridLayout_3.addWidget(self.positionObjectALabel, 0, 0, 1, 2)

        self.xRotationPositionALabel = QLabel(self.framePositioningA)
        self.xRotationPositionALabel.setObjectName(u"xRotationPositionALabel")

        self.gridLayout_3.addWidget(self.xRotationPositionALabel, 7, 0, 1, 1)

        self.zRotationPositionALabel = QLabel(self.framePositioningA)
        self.zRotationPositionALabel.setObjectName(u"zRotationPositionALabel")

        self.gridLayout_3.addWidget(self.zRotationPositionALabel, 9, 0, 1, 1)

        self.resetPositionAButton = QPushButton(self.framePositioningA)
        self.resetPositionAButton.setObjectName(u"resetPositionAButton")
        self.resetPositionAButton.setMaximumSize(QSize(50, 16777215))
        self.resetPositionAButton.setIcon(icon7)
        self.resetPositionAButton.setIconSize(QSize(12, 12))

        self.gridLayout_3.addWidget(self.resetPositionAButton, 0, 2, 1, 1)

        self.zRotationUnitPositionALabel = QLabel(self.framePositioningA)
        self.zRotationUnitPositionALabel.setObjectName(u"zRotationUnitPositionALabel")

        self.gridLayout_3.addWidget(self.zRotationUnitPositionALabel, 9, 2, 1, 1)

        self.yTranslationPositionALabel = QLabel(self.framePositioningA)
        self.yTranslationPositionALabel.setObjectName(u"yTranslationPositionALabel")

        self.gridLayout_3.addWidget(self.yTranslationPositionALabel, 3, 0, 1, 1)

        self.rotationPositionALabel = QLabel(self.framePositioningA)
        self.rotationPositionALabel.setObjectName(u"rotationPositionALabel")
        self.rotationPositionALabel.setMinimumSize(QSize(0, 25))
        self.rotationPositionALabel.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_3.addWidget(self.rotationPositionALabel, 5, 1, 1, 1)

        self.xRotationUnitPositionALabel = QLabel(self.framePositioningA)
        self.xRotationUnitPositionALabel.setObjectName(u"xRotationUnitPositionALabel")
        self.xRotationUnitPositionALabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.xRotationUnitPositionALabel, 7, 2, 1, 1)

        self.rotationPositionAIcon = QLabel(self.framePositioningA)
        self.rotationPositionAIcon.setObjectName(u"rotationPositionAIcon")
        self.rotationPositionAIcon.setMinimumSize(QSize(11, 11))
        self.rotationPositionAIcon.setMaximumSize(QSize(11, 11))
        self.rotationPositionAIcon.setPixmap(QPixmap(u":/icons/icons/rotate-right.svg"))
        self.rotationPositionAIcon.setScaledContents(True)

        self.gridLayout_3.addWidget(self.rotationPositionAIcon, 5, 0, 1, 1)

        self.zTranslationUnitPositionALabel = QLabel(self.framePositioningA)
        self.zTranslationUnitPositionALabel.setObjectName(u"zTranslationUnitPositionALabel")
        self.zTranslationUnitPositionALabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.zTranslationUnitPositionALabel, 4, 2, 1, 1)

        self.xTranslationUnitPositionALabel = QLabel(self.framePositioningA)
        self.xTranslationUnitPositionALabel.setObjectName(u"xTranslationUnitPositionALabel")
        self.xTranslationUnitPositionALabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.xTranslationUnitPositionALabel, 2, 2, 1, 1)

        self.yRotationUnitPositionALabel = QLabel(self.framePositioningA)
        self.yRotationUnitPositionALabel.setObjectName(u"yRotationUnitPositionALabel")
        self.yRotationUnitPositionALabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_3.addWidget(self.yRotationUnitPositionALabel, 8, 2, 1, 1)

        self.zTranslationPositionALabel = QLabel(self.framePositioningA)
        self.zTranslationPositionALabel.setObjectName(u"zTranslationPositionALabel")

        self.gridLayout_3.addWidget(self.zTranslationPositionALabel, 4, 0, 1, 1)

        self.xRotationASlider = QSlider(self.framePositioningA)
        self.xRotationASlider.setObjectName(u"xRotationASlider")
        self.xRotationASlider.setMaximum(100)
        self.xRotationASlider.setValue(50)
        self.xRotationASlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.xRotationASlider, 7, 1, 1, 1)

        self.yRotationASlider = QSlider(self.framePositioningA)
        self.yRotationASlider.setObjectName(u"yRotationASlider")
        self.yRotationASlider.setValue(50)
        self.yRotationASlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.yRotationASlider, 8, 1, 1, 1)

        self.zRotationASlider = QSlider(self.framePositioningA)
        self.zRotationASlider.setObjectName(u"zRotationASlider")
        self.zRotationASlider.setValue(50)
        self.zRotationASlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.zRotationASlider, 9, 1, 1, 1)


        self.verticalLayout_33.addWidget(self.framePositioningA)

        self.framePositioningB = QFrame(self.scrollAreaWidgetContentsPositioning)
        self.framePositioningB.setObjectName(u"framePositioningB")
        self.framePositioningB.setMinimumSize(QSize(0, 400))
        self.framePositioningB.setMaximumSize(QSize(16777215, 500))
        self.framePositioningB.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePositioningB.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.framePositioningB)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(10, 0, 10, 0)
        self.xTranslationBSpinbox = QDoubleSpinBox(self.framePositioningB)
        self.xTranslationBSpinbox.setObjectName(u"xTranslationBSpinbox")
        self.xTranslationBSpinbox.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.gridLayout_4.addWidget(self.xTranslationBSpinbox, 3, 1, 1, 1)

        self.zRotationUnitPositionBLabel = QLabel(self.framePositioningB)
        self.zRotationUnitPositionBLabel.setObjectName(u"zRotationUnitPositionBLabel")

        self.gridLayout_4.addWidget(self.zRotationUnitPositionBLabel, 9, 2, 1, 1)

        self.xRotationPositionBLabel = QLabel(self.framePositioningB)
        self.xRotationPositionBLabel.setObjectName(u"xRotationPositionBLabel")

        self.gridLayout_4.addWidget(self.xRotationPositionBLabel, 7, 0, 1, 1)

        self.xTranslationUnitPositionBLabel = QLabel(self.framePositioningB)
        self.xTranslationUnitPositionBLabel.setObjectName(u"xTranslationUnitPositionBLabel")
        self.xTranslationUnitPositionBLabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.xTranslationUnitPositionBLabel, 3, 2, 1, 1)

        self.positionObjectBLabel = QLabel(self.framePositioningB)
        self.positionObjectBLabel.setObjectName(u"positionObjectBLabel")

        self.gridLayout_4.addWidget(self.positionObjectBLabel, 1, 0, 1, 2)

        self.translationPositionBIcon = QLabel(self.framePositioningB)
        self.translationPositionBIcon.setObjectName(u"translationPositionBIcon")
        self.translationPositionBIcon.setMinimumSize(QSize(11, 11))
        self.translationPositionBIcon.setMaximumSize(QSize(11, 11))
        self.translationPositionBIcon.setPixmap(QPixmap(u":/icons/icons/arrows_dark.svg"))
        self.translationPositionBIcon.setScaledContents(True)

        self.gridLayout_4.addWidget(self.translationPositionBIcon, 2, 0, 1, 1)

        self.xTranslationPositionBLabel = QLabel(self.framePositioningB)
        self.xTranslationPositionBLabel.setObjectName(u"xTranslationPositionBLabel")

        self.gridLayout_4.addWidget(self.xTranslationPositionBLabel, 3, 0, 1, 1)

        self.rotationPositionbLabel = QLabel(self.framePositioningB)
        self.rotationPositionbLabel.setObjectName(u"rotationPositionbLabel")
        self.rotationPositionbLabel.setMinimumSize(QSize(0, 25))
        self.rotationPositionbLabel.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.rotationPositionbLabel, 6, 1, 1, 1)

        self.yTranslationUnitPositionBLabel = QLabel(self.framePositioningB)
        self.yTranslationUnitPositionBLabel.setObjectName(u"yTranslationUnitPositionBLabel")
        self.yTranslationUnitPositionBLabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.yTranslationUnitPositionBLabel, 4, 2, 1, 1)

        self.rotationPositionbIcon = QLabel(self.framePositioningB)
        self.rotationPositionbIcon.setObjectName(u"rotationPositionbIcon")
        self.rotationPositionbIcon.setMinimumSize(QSize(11, 11))
        self.rotationPositionbIcon.setMaximumSize(QSize(11, 11))
        self.rotationPositionbIcon.setPixmap(QPixmap(u":/icons/icons/rotate-right.svg"))
        self.rotationPositionbIcon.setScaledContents(True)

        self.gridLayout_4.addWidget(self.rotationPositionbIcon, 6, 0, 1, 1)

        self.zTranslationBSpinbox = QDoubleSpinBox(self.framePositioningB)
        self.zTranslationBSpinbox.setObjectName(u"zTranslationBSpinbox")

        self.gridLayout_4.addWidget(self.zTranslationBSpinbox, 5, 1, 1, 1)

        self.zTranslationUnitPositionBLabel = QLabel(self.framePositioningB)
        self.zTranslationUnitPositionBLabel.setObjectName(u"zTranslationUnitPositionBLabel")
        self.zTranslationUnitPositionBLabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.zTranslationUnitPositionBLabel, 5, 2, 1, 1)

        self.yTranslationPositionBLabel = QLabel(self.framePositioningB)
        self.yTranslationPositionBLabel.setObjectName(u"yTranslationPositionBLabel")

        self.gridLayout_4.addWidget(self.yTranslationPositionBLabel, 4, 0, 1, 1)

        self.translationPositionBLabel = QLabel(self.framePositioningB)
        self.translationPositionBLabel.setObjectName(u"translationPositionBLabel")
        self.translationPositionBLabel.setMinimumSize(QSize(0, 25))
        self.translationPositionBLabel.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_4.addWidget(self.translationPositionBLabel, 2, 1, 1, 1)

        self.yTranslationBSpinbox = QDoubleSpinBox(self.framePositioningB)
        self.yTranslationBSpinbox.setObjectName(u"yTranslationBSpinbox")

        self.gridLayout_4.addWidget(self.yTranslationBSpinbox, 4, 1, 1, 1)

        self.resetPositionBButton = QPushButton(self.framePositioningB)
        self.resetPositionBButton.setObjectName(u"resetPositionBButton")
        self.resetPositionBButton.setMaximumSize(QSize(50, 16777215))
        self.resetPositionBButton.setIcon(icon7)
        self.resetPositionBButton.setIconSize(QSize(12, 12))

        self.gridLayout_4.addWidget(self.resetPositionBButton, 1, 2, 1, 1)

        self.xRotationUnitPositionBLabel = QLabel(self.framePositioningB)
        self.xRotationUnitPositionBLabel.setObjectName(u"xRotationUnitPositionBLabel")
        self.xRotationUnitPositionBLabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.xRotationUnitPositionBLabel, 7, 2, 1, 1)

        self.yRotationPositionBLabel = QLabel(self.framePositioningB)
        self.yRotationPositionBLabel.setObjectName(u"yRotationPositionBLabel")

        self.gridLayout_4.addWidget(self.yRotationPositionBLabel, 8, 0, 1, 1)

        self.zTranslationPositionBLabel = QLabel(self.framePositioningB)
        self.zTranslationPositionBLabel.setObjectName(u"zTranslationPositionBLabel")

        self.gridLayout_4.addWidget(self.zTranslationPositionBLabel, 5, 0, 1, 1)

        self.yRotationUnitPositionBLabel = QLabel(self.framePositioningB)
        self.yRotationUnitPositionBLabel.setObjectName(u"yRotationUnitPositionBLabel")
        self.yRotationUnitPositionBLabel.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.yRotationUnitPositionBLabel, 8, 2, 1, 1)

        self.zRotationPositionBLabel = QLabel(self.framePositioningB)
        self.zRotationPositionBLabel.setObjectName(u"zRotationPositionBLabel")

        self.gridLayout_4.addWidget(self.zRotationPositionBLabel, 9, 0, 1, 1)

        self.xRotationBSlider = QSlider(self.framePositioningB)
        self.xRotationBSlider.setObjectName(u"xRotationBSlider")
        self.xRotationBSlider.setMaximum(100)
        self.xRotationBSlider.setValue(50)
        self.xRotationBSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.xRotationBSlider, 7, 1, 1, 1)

        self.yRotationBSlider = QSlider(self.framePositioningB)
        self.yRotationBSlider.setObjectName(u"yRotationBSlider")
        self.yRotationBSlider.setMaximum(100)
        self.yRotationBSlider.setValue(50)
        self.yRotationBSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.yRotationBSlider, 8, 1, 1, 1)

        self.zRotationBSlider = QSlider(self.framePositioningB)
        self.zRotationBSlider.setObjectName(u"zRotationBSlider")
        self.zRotationBSlider.setMaximum(100)
        self.zRotationBSlider.setValue(50)
        self.zRotationBSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.zRotationBSlider, 9, 1, 1, 1)


        self.verticalLayout_33.addWidget(self.framePositioningB)

        self.framePositioningValidation = QFrame(self.scrollAreaWidgetContentsPositioning)
        self.framePositioningValidation.setObjectName(u"framePositioningValidation")
        self.framePositioningValidation.setMinimumSize(QSize(0, 130))
        self.framePositioningValidation.setMaximumSize(QSize(16777215, 130))
        self.framePositioningValidation.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePositioningValidation.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.framePositioningValidation)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 10, 10, 10)
        self.validationPositioningLabel = QLabel(self.framePositioningValidation)
        self.validationPositioningLabel.setObjectName(u"validationPositioningLabel")
        self.validationPositioningLabel.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_31.addWidget(self.validationPositioningLabel)

        self.validationPositionButton = QPushButton(self.framePositioningValidation)
        self.validationPositionButton.setObjectName(u"validationPositionButton")
        self.validationPositionButton.setMinimumSize(QSize(0, 35))
        self.validationPositionButton.setStyleSheet(u"\n"
"background-color: #1447e6")
        self.validationPositionButton.setIcon(icon8)
        self.validationPositionButton.setIconSize(QSize(14, 14))

        self.verticalLayout_31.addWidget(self.validationPositionButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_3)


        self.verticalLayout_33.addWidget(self.framePositioningValidation)

        self.scrollAreaPositioning.setWidget(self.scrollAreaWidgetContentsPositioning)

        self.verticalLayout_30.addWidget(self.scrollAreaPositioning)


        self.verticalLayout_15.addWidget(self.settingsPositioningPage)


        self.verticalLayout_11.addWidget(self.positioningPageLayout)

        self.stackedWidget.addWidget(self.positioningPage)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.settingsLayout)

        self.viewLayout = QWidget(self.centerLayout)
        self.viewLayout.setObjectName(u"viewLayout")
        self.verticalLayout_29 = QVBoxLayout(self.viewLayout)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(1, 1, 1, 0)
        self.viewTitleLayout = QWidget(self.viewLayout)
        self.viewTitleLayout.setObjectName(u"viewTitleLayout")
        self.horizontalLayout_3 = QHBoxLayout(self.viewTitleLayout)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mainTitleViewLabel = QLabel(self.viewTitleLayout)
        self.mainTitleViewLabel.setObjectName(u"mainTitleViewLabel")

        self.horizontalLayout_3.addWidget(self.mainTitleViewLabel)

        self.subTitleViewIcon = QLabel(self.viewTitleLayout)
        self.subTitleViewIcon.setObjectName(u"subTitleViewIcon")
        self.subTitleViewIcon.setMaximumSize(QSize(13, 13))
        self.subTitleViewIcon.setPixmap(QPixmap(u":/icons/icons/eye_small.svg"))
        self.subTitleViewIcon.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.subTitleViewIcon)

        self.subTitleViewLabel = QLabel(self.viewTitleLayout)
        self.subTitleViewLabel.setObjectName(u"subTitleViewLabel")
        self.subTitleViewLabel.setMaximumSize(QSize(140, 20))
        self.subTitleViewLabel.setScaledContents(True)
        self.subTitleViewLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.subTitleViewLabel)


        self.verticalLayout_29.addWidget(self.viewTitleLayout)

        self.vtkViewer = QVTKRenderWindowInteractor(self.viewLayout)
        self.vtkViewer.setObjectName(u"vtkViewer")

        self.verticalLayout_29.addWidget(self.vtkViewer)


        self.horizontalLayout.addWidget(self.viewLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 3)

        self.MainLayout.addWidget(self.centerLayout)

        self.statusLayout = QWidget(Widget)
        self.statusLayout.setObjectName(u"statusLayout")
        self.horizontalLayout_2 = QHBoxLayout(self.statusLayout)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, -1, -1)
        self.statusIcon = QLabel(self.statusLayout)
        self.statusIcon.setObjectName(u"statusIcon")
        self.statusIcon.setMinimumSize(QSize(14, 14))
        self.statusIcon.setMaximumSize(QSize(14, 14))
        self.statusIcon.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.statusIcon.setScaledContents(True)
        self.statusIcon.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.statusIcon)

        self.statusMessageLabel = QLabel(self.statusLayout)
        self.statusMessageLabel.setObjectName(u"statusMessageLabel")
        self.statusMessageLabel.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.statusMessageLabel)


        self.MainLayout.addWidget(self.statusLayout)

        self.MainLayout.setStretch(0, 2)
        self.MainLayout.setStretch(1, 20)
        self.MainLayout.setStretch(2, 1)

        self.verticalLayout_26.addLayout(self.MainLayout)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.mainTitleLabel.setText(QCoreApplication.translate("Widget", u"Transient Thermal Radiation Simulator", None))
        self.subTitleLabel.setText(QCoreApplication.translate("Widget", u"CAE Tool for 3D Heat Transfer Analysis", None))
        self.versionLabel.setText(QCoreApplication.translate("Widget", u"v1.0.0", None))
        self.pipelineTitleLabel.setText(QCoreApplication.translate("Widget", u"SIMULATION PIPELINE", None))
        self.geometryButton.setText(QCoreApplication.translate("Widget", u"  Geometry", None))
        self.positioningButton.setText(QCoreApplication.translate("Widget", u"  Positioning", None))
        self.meshingButton.setText(QCoreApplication.translate("Widget", u"  Meshing", None))
        self.materialsButton.setText(QCoreApplication.translate("Widget", u"  Materials", None))
        self.simulationButton.setText(QCoreApplication.translate("Widget", u"  Simulation", None))
        self.resultsButton.setText(QCoreApplication.translate("Widget", u"  Results", None))
        self.hintLabel.setText(QCoreApplication.translate("Widget", u"Complete each step to unlock the next stage.", None))
        self.maintitleGeometryPage.setText(QCoreApplication.translate("Widget", u"Step 1: Geometry", None))
        self.subtitleGeometryPage.setText(QCoreApplication.translate("Widget", u"Load STL files for both objects", None))
        self.objectALabel.setText(QCoreApplication.translate("Widget", u"Object A", None))
        self.stlfileAlabel.setText(QCoreApplication.translate("Widget", u"STL File", None))
        self.uploadFileAButton.setText(QCoreApplication.translate("Widget", u"   Select File..", None))
        self.objectBLabel.setText(QCoreApplication.translate("Widget", u"Object B", None))
        self.stlfileBlabel.setText(QCoreApplication.translate("Widget", u"STL File", None))
        self.uploadFileBButton.setText(QCoreApplication.translate("Widget", u"   Select File...", None))
        self.objectALoadedLabel.setText(QCoreApplication.translate("Widget", u"Object A loaded", None))
        self.objectBLoadedLabel.setText(QCoreApplication.translate("Widget", u"Object B loaded", None))
        self.readyPositioningLabel.setText(QCoreApplication.translate("Widget", u"Ready for positioning", None))
        self.validationGeometryLabel.setText(QCoreApplication.translate("Widget", u"Validation", None))
        self.maintitleMeshingPage.setText(QCoreApplication.translate("Widget", u"Step 3: Meshing", None))
        self.subtitleMeshingPage.setText(QCoreApplication.translate("Widget", u"Generate tetrahedral meshes for finite element analysis", None))
        self.rotationPositionALabel_2.setText(QCoreApplication.translate("Widget", u"Rotation", None))
        self.resetPositionAButton_2.setText("")
        self.positionObjectALabel_2.setText(QCoreApplication.translate("Widget", u"Object A", None))
        self.xRotationPositionALabel_2.setText(QCoreApplication.translate("Widget", u"x:", None))
        self.yTranslationUnitPositionALabel_2.setText(QCoreApplication.translate("Widget", u"m", None))
        self.xTranslationUnitPositionALabel_2.setText(QCoreApplication.translate("Widget", u"m", None))
        self.zRotationUnitPositionALabel_2.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.yTranslationPositionALabel_2.setText(QCoreApplication.translate("Widget", u"y:", None))
        self.zTranslationPositionALabel_2.setText(QCoreApplication.translate("Widget", u"z:", None))
        self.yRotationUnitPositionALabel_2.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.yRotationPositionALabel_2.setText(QCoreApplication.translate("Widget", u"y:", None))
        self.xTranslationPositionALabel_2.setText(QCoreApplication.translate("Widget", u"x:", None))
        self.rotationPositionAIcon_2.setText("")
        self.xRotationUnitPositionALabel_2.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.zRotationPositionALabel_2.setText(QCoreApplication.translate("Widget", u"z:", None))
        self.translationPositionAIcon_2.setText("")
        self.translationPositionALabel_2.setText(QCoreApplication.translate("Widget", u"Translation", None))
        self.zTranslationUnitPositionALabel_2.setText(QCoreApplication.translate("Widget", u"m", None))
        self.generateMeshAButton.setText(QCoreApplication.translate("Widget", u"Generate Mesh", None))
        self.zRotationUnitPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.translationPositionBIcon_2.setText("")
        self.resetPositionBButton_2.setText("")
        self.zRotationPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"z:", None))
        self.yTranslationUnitPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"m", None))
        self.xTranslationPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"x:", None))
        self.zTranslationUnitPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"m", None))
        self.yRotationUnitPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.rotationPositionbIcon_2.setText("")
        self.translationPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"Translation", None))
        self.xRotationPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"x:", None))
        self.positionObjectBLabel_2.setText(QCoreApplication.translate("Widget", u"Object B", None))
        self.rotationPositionbLabel_2.setText(QCoreApplication.translate("Widget", u"Rotation", None))
        self.xRotationUnitPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.yTranslationPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"y:", None))
        self.xTranslationUnitPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"m", None))
        self.yRotationPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"y:", None))
        self.zTranslationPositionBLabel_2.setText(QCoreApplication.translate("Widget", u"z:", None))
        self.validationPositioningLabel_2.setText(QCoreApplication.translate("Widget", u"Validation", None))
        self.validationPositionButton_2.setText(QCoreApplication.translate("Widget", u" Check For Overlap", None))
        self.maintitleMaterialsPage.setText(QCoreApplication.translate("Widget", u"Step 4: Materials", None))
        self.subtitleMaterialsPage.setText(QCoreApplication.translate("Widget", u"Define thermal and material parameters for each object", None))
        self.maintitleSimulationPage.setText(QCoreApplication.translate("Widget", u"Step 5: Simulation", None))
        self.subtitleSimulationPage.setText(QCoreApplication.translate("Widget", u"Configure and run the transient thermal radiation simulation", None))
        self.maintitleResultsPage.setText(QCoreApplication.translate("Widget", u"Step 6: Results", None))
        self.subtitleResultsPage.setText(QCoreApplication.translate("Widget", u"Analyze temperature evolution and heat transfer", None))
        self.maintitlePositioningPage.setText(QCoreApplication.translate("Widget", u"Step 2: Positioning", None))
        self.subtitlePositioningPage.setText(QCoreApplication.translate("Widget", u"Position and orient both objects in 3D space", None))
        self.xTranslationPositionALabel.setText(QCoreApplication.translate("Widget", u"x:", None))
        self.yTranslationUnitPositionALabel.setText(QCoreApplication.translate("Widget", u"m", None))
        self.yRotationPositionALabel.setText(QCoreApplication.translate("Widget", u"y:", None))
        self.translationPositionALabel.setText(QCoreApplication.translate("Widget", u"Translation", None))
        self.translationPositionAIcon.setText("")
        self.positionObjectALabel.setText(QCoreApplication.translate("Widget", u"Object A", None))
        self.xRotationPositionALabel.setText(QCoreApplication.translate("Widget", u"x:", None))
        self.zRotationPositionALabel.setText(QCoreApplication.translate("Widget", u"z:", None))
        self.resetPositionAButton.setText("")
        self.zRotationUnitPositionALabel.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.yTranslationPositionALabel.setText(QCoreApplication.translate("Widget", u"y:", None))
        self.rotationPositionALabel.setText(QCoreApplication.translate("Widget", u"Rotation", None))
        self.xRotationUnitPositionALabel.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.rotationPositionAIcon.setText("")
        self.zTranslationUnitPositionALabel.setText(QCoreApplication.translate("Widget", u"m", None))
        self.xTranslationUnitPositionALabel.setText(QCoreApplication.translate("Widget", u"m", None))
        self.yRotationUnitPositionALabel.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.zTranslationPositionALabel.setText(QCoreApplication.translate("Widget", u"z:", None))
        self.zRotationUnitPositionBLabel.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.xRotationPositionBLabel.setText(QCoreApplication.translate("Widget", u"x:", None))
        self.xTranslationUnitPositionBLabel.setText(QCoreApplication.translate("Widget", u"m", None))
        self.positionObjectBLabel.setText(QCoreApplication.translate("Widget", u"Object B", None))
        self.translationPositionBIcon.setText("")
        self.xTranslationPositionBLabel.setText(QCoreApplication.translate("Widget", u"x:", None))
        self.rotationPositionbLabel.setText(QCoreApplication.translate("Widget", u"Rotation", None))
        self.yTranslationUnitPositionBLabel.setText(QCoreApplication.translate("Widget", u"m", None))
        self.rotationPositionbIcon.setText("")
        self.zTranslationUnitPositionBLabel.setText(QCoreApplication.translate("Widget", u"m", None))
        self.yTranslationPositionBLabel.setText(QCoreApplication.translate("Widget", u"y:", None))
        self.translationPositionBLabel.setText(QCoreApplication.translate("Widget", u"Translation", None))
        self.resetPositionBButton.setText("")
        self.xRotationUnitPositionBLabel.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.yRotationPositionBLabel.setText(QCoreApplication.translate("Widget", u"y:", None))
        self.zTranslationPositionBLabel.setText(QCoreApplication.translate("Widget", u"z:", None))
        self.yRotationUnitPositionBLabel.setText(QCoreApplication.translate("Widget", u"0\u00b0", None))
        self.zRotationPositionBLabel.setText(QCoreApplication.translate("Widget", u"z:", None))
        self.validationPositioningLabel.setText(QCoreApplication.translate("Widget", u"Validation", None))
        self.validationPositionButton.setText(QCoreApplication.translate("Widget", u" Check For Overlap", None))
        self.mainTitleViewLabel.setText(QCoreApplication.translate("Widget", u"3D Viewer", None))
        self.subTitleViewLabel.setText(QCoreApplication.translate("Widget", u"Click and drag to rotate", None))
        self.statusMessageLabel.setText(QCoreApplication.translate("Widget", u"Ready to begin. Load geometry files to start.", None))
    # retranslateUi

