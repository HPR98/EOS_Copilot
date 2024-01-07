import requests
from osc_sender import sendOSC
from util import channels_in_use

def message_handler(address, *args):
    ###########Inital showfile data############
    if address == "/eos/out/get/patch/count":
        print("received patch count")
        data_to_send = {"patch_count": str(args[0])}
        response = requests.post("http://127.0.0.1:5000/update_channel_count", json=data_to_send)

        i = 0
        for i in range(args[0]):
            sendOSC("/eos/get/patch/" + str(i))
            


    if address == "/eos/out/get/preset/count":
        print("received preset count")
        data_to_send = {"preset_count": str(args[0])}
        response = requests.post("http://127.0.0.1:5000/update_preset_count", json=data_to_send)

    if address == "/eos/out/get/cp/count":
        print("received CP count")
        data_to_send = {"cp_count": str(args[0])}
        response = requests.post("http://127.0.0.1:5000/update_cp_count", json=data_to_send)
        

    if address == "/eos/out/get/group/count":
        print("received group count")
        data_to_send = {"group_count": str(args[0])}
        response = requests.post("http://127.0.0.1:5000/update_group_count", json=data_to_send)


    ##########Get Channels_in_use##########
    if "/eos/out/get/patch" in address and "/list" in address and len(args) > 0:
        splitted_address = address.split("/")
        channel_number = splitted_address[5]
        if channel_number in channels_in_use:
            pass
        else:
            channels_in_use.append(channel_number)

        data_to_send = {"channels_in_use": channels_in_use}
        response = requests.post("http://127.0.0.1:5000/update_channels_in_use", json=data_to_send)


if __name__ == "__main__":
    pass