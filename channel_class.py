from osc_sender import sendOSC
import time

class channel():
    def __init__(self, channel_number) -> None:
        self.channel_number = channel_number
        self.data = {"intensity": "--"}

    def set_intens(self):
        sendOSC("/eos/get/patch/" + str(self.channel_number))
        self.data["intensity"] = "30"
    

