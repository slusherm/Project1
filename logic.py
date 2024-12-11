from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    """
    Class for the functions of a basic TV
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 9
    MIN_CHANNEL = 1
    MAX_CHANNEL = 9

    def __init__(self) -> None:
        """
        Method that sets the default TV setting
        """
        super().__init__()
        self.setupUi(self)
        self.__status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = Logic.MIN_CHANNEL
        self.button_power.setStyleSheet("color : red")

        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_channelUp.clicked.connect(lambda: self.channel_up())
        self.button_channelDown.clicked.connect(lambda: self.channel_down())
        self.button_volUp.clicked.connect(lambda: self.volume_up())
        self.button_volDown.clicked.connect(lambda: self.volume_down())
        self.button_channel1.clicked.connect(lambda: self.change_channel(1))
        self.button_channel2.clicked.connect(lambda: self.change_channel(2))
        self.button_channel3.clicked.connect(lambda: self.change_channel(3))
        self.button_channel4.clicked.connect(lambda: self.change_channel(4))
        self.button_channel5.clicked.connect(lambda: self.change_channel(5))
        self.button_channel6.clicked.connect(lambda: self.change_channel(6))
        self.button_channel7.clicked.connect(lambda: self.change_channel(7))
        self.button_channel8.clicked.connect(lambda: self.change_channel(8))
        self.button_channel9.clicked.connect(lambda: self.change_channel(9))
        self.label_chanImage = self.findChild(QLabel, "label_chanImage")
        self.label_chanImage.hide()
        self.slider_vol.setMinimum(Logic.MIN_VOLUME)
        self.slider_vol.setMaximum(Logic.MAX_VOLUME)

    def power(self) -> None:
        """
        Method that sets the TV either on or off
        """
        if self.__status:
            self.__status = False
            self.label_chanImage.hide()
            self.button_power.setStyleSheet("color : red")
            self.button_mute.setStyleSheet("color : white")
        else:
            self.__status = True
            self.label_chanImage.show()
            self.button_power.setStyleSheet("color : green")

    def mute(self) -> None:
        """
        Method that mutes or unmutes the TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.button_mute.setStyleSheet("color : white")
            else:
                self.__muted = True
                self.button_mute.setStyleSheet("color : red")
                self.slider_vol.setValue(self.__volume)

    def channel_up(self) -> None:
        """
        Method that sets the channel one higher
        """
        if self.__status:
            if self.__channel == Logic.MAX_CHANNEL:
                self.__channel = Logic.MIN_CHANNEL
            else:
                self.__channel += 1
            self.change_channel(self.__channel)

    def channel_down(self) -> None:
        """
        Method that sets the channel one lower
        """
        if self.__status:
            if self.__channel == Logic.MIN_CHANNEL:
                self.__channel = Logic.MAX_CHANNEL
            else:
                self.__channel -= 1
            self.change_channel(self.__channel)

    def change_channel(self, channel) -> None:
        """
        Method that sets the channel number to the corresponding image
        :param channel: Number of channel selected
        """
        if self.__status:
            if channel == 1: #Netflix
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan1.png"))
            if channel == 2: #HBO
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan2.png"))
            if channel == 3: #CNN
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan3.png"))
            if channel == 4: #PBS Kids
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan4.png"))
            if channel == 5: #Cartoon Network
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan5.png"))
            if channel == 6: #WOWT News
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan6.png"))
            if channel == 7: #Animal Planet
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan7.png"))
            if channel == 8: #HGTV
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan8.png"))
            if channel == 9: #Food Network
                self.label_chanImage.setPixmap(QtGui.QPixmap("chan9.png"))


    def volume_up(self) -> None:
        """
        Method that turns the volume up by 1
        """
        if self.__status:
            if self.__volume != Logic.MAX_VOLUME:
                self.__volume += 1
                self.__muted = False
                self.slider_vol.setValue(self.__volume)
                self.button_mute.setStyleSheet("color : white")


    def volume_down(self) -> None:
        """
        Method that turns the volume down by 1
        """
        if self.__status:
            if self.__volume != Logic.MIN_VOLUME:
                self.__volume -= 1
                self.__muted = False
                self.slider_vol.setValue(self.__volume)
                self.button_mute.setStyleSheet("color : white")

    def __str__(self) -> str:
        """
        Method that prints the current TV settings
        :return: TV's current settings for power, channel, and volume
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Logic.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'