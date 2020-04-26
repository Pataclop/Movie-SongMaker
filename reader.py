from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore, QtWidgets

from PyQt5.QtCore import QDir, Qt, QUrl, QSize
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, 
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
import os
import slider

class VideoPlayer(QWidget):

    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        btnSize = QSize(16, 16)
        videoWidget = QVideoWidget()

        openButton = QPushButton("Open Video")   
        openButton.setToolTip("Open Video File")
        openButton.setStatusTip("Open Video File")
        openButton.setFixedHeight(24)
        openButton.setIconSize(btnSize)
        openButton.setFont(QFont("Noto Sans", 8))
        openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
        openButton.clicked.connect(self.abrir)

        speedButton = QPushButton("speedVideo")   
        speedButton.setToolTip("Open Video File")
        speedButton.setStatusTip("Open Video File")
        speedButton.setFixedHeight(24)
        speedButton.setIconSize(btnSize)
        speedButton.setFont(QFont("Noto Sans", 8))
        speedButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
        speedButton.clicked.connect(self.speed)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setFixedHeight(24)
        self.playButton.setIconSize(btnSize)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = slider.Slider(QtCore.Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        self.positionSlider.sliderPressed.connect(self.setPosition)
        self.positionSlider.sliderReleased.connect(self.setPosition)
        


        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Noto Sans", 7))
        self.statusBar.setFixedHeight(14)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(speedButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.statusBar)

        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.statusBar.showMessage("Ready")

    def abrir(self):

        num=0
        cmd = "ffmpeg -y -i " + "PART/" + str(num) + ".mkv " +  "-filter_complex \"[0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a]\" -map \"[v]\" -map \"[a]\" " + str(num) + ".mkv"

        #cmd = "ffmpeg -y -i "+ "PART/" + str(num) + ".mkv" + " -filter:v \"setpts=2.0*PTS\" "+ str(num) + ".mkv"
        os.system(cmd)

        player.setWindowTitle("CLONES")
        fileName = "/home/flo/tmp/Movie-SongMaker/0.mkv"

        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.play()

    def speed(self):

        num=0
        cmd = "ffmpeg -y -i " + "PART/" + str(num) + ".mkv " +  "-filter_complex \"[0:v]setpts=1.0*PTS[v];[0:a]atempo=1.0[a]\" -map \"[v]\" -map \"[a]\" " + str(num) + ".mkv"

        #cmd = "ffmpeg -y -i "+ "PART/" + str(num) + ".mkv" + " -filter:v \"setpts=2.0*PTS\" "+ str(num) + ".mkv"
        os.system(cmd)

        player.setWindowTitle("CLONES")
        fileName = "/home/flo/tmp/Movie-SongMaker/0.mkv"

        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.play()

    def play(self):
        
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.setWindowTitle("Player")
    player.resize(600, 400)
    player.show()
    sys.exit(app.exec_())