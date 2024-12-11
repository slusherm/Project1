from PyQt6.QtWidgets import *
from gui import *
import os

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
        self.__prev_channel = Logic.MIN_CHANNEL
        self.__previous_volume = Logic.MIN_VOLUME

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
        self.button_prevChannel.clicked.connect(lambda: self.change_channel(self.__prev_channel))

        self.label_chanImage = self.findChild(QLabel, "label_chanImage")
        self.label_chanImage.hide()
        self.slider_vol.setMinimum(Logic.MIN_VOLUME)
        self.slider_vol.setMaximum(Logic.MAX_VOLUME)
        self.button_power.setStyleSheet("color : red")

    def power(self) -> None:
        """
        Method that sets the TV either on or off
        """
        if self.__status:
            self.__status = False
            self.label_chanImage.hide()
            self.slider_vol.setEnabled(False)
            self.button_power.setStyleSheet("color : red")
            self.button_mute.setStyleSheet("color : white")
        else:
            self.__status = True
            self.label_chanImage.show()
            self.slider_vol.setEnabled(True)
            self.button_power.setStyleSheet("color : green")
            if self.__muted:
                self.button_mute.setStyleSheet("color : red")

    def mute(self) -> None:
        """
        Method that mutes or unmutes the TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.slider_vol.setValue(self.__previous_volume)
                self.button_mute.setStyleSheet("color : white")
            else:
                self.__muted = True
                self.__previous_volume = self.slider_vol.value()
                self.button_mute.setStyleSheet("color : red")
                self.slider_vol.setValue(0)

    def channel_up(self) -> None:
        """
        Method that sets the channel one higher
        """
        if self.__status:
            self.__prev_channel = self.__channel
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
            self.__prev_channel = self.__channel
            if self.__channel == Logic.MIN_CHANNEL:
                self.__channel = Logic.MAX_CHANNEL
            else:
                self.__channel -= 1
            self.change_channel(self.__channel)

    # def previous_channel(self) -> None:
    #     """
    #     Method that switches to the previously viewed channel
    #     """
    #     if self.__status and self.__prev_channel is not None:
    #         # Swap current and previous channels
    #         current_channel = self.__channel
    #         self.change_channel(self.__prev_channel)
    #         self.__prev_channel = current_channel

    def change_channel(self, channel) -> None:
        """
        Method that sets the channel number to the corresponding image
        :param channel: Number of channel selected
        """
        if self.__status:
            # Update the previous channel before switching
            self.__prev_channel = self.__channel
            self.__channel = channel

            # Set the corresponding image
            file_path = f"chan{channel}.png"
            if os.path.exists(file_path):
                self.label_chanImage.setPixmap(QtGui.QPixmap(file_path))

    def volume_up(self) -> None:
        """
        Method that turns the volume up by 1
        """
        if self.__status:
            value = self.slider_vol.value()
            if self.__volume != Logic.MAX_VOLUME:
                self.__volume = value
                self.__volume += 1
                self.__muted = False
                self.slider_vol.setValue(self.__volume)
                self.button_mute.setStyleSheet("color : white")

    def volume_down(self) -> None:
        """
        Method that turns the volume down by 1
        """
        if self.__status:
            value = self.slider_vol.value()
            if self.__volume != Logic.MIN_VOLUME:
                self.__volume = value
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