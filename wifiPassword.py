import subprocess
import re
import time

try:
    def wifiPassExtractor():

        ssid = subprocess.check_output("netsh wlan show profiles ", shell=True).decode("utf-8")
        ssid_list = re.findall("All User Profile     :\s(.*)\r", ssid)

        pass_list = []
        for i, value in enumerate(ssid_list):
            password = subprocess.check_output(["netsh", "wlan", "show", "profile", value, "key=clear"],shell=True).decode("utf-8")
            wifi_list = re.findall("Key Content            :\s(.*)\r", password)
            pass_list.extend(wifi_list)

        wifi = dict(zip(ssid_list, pass_list))

        for ssid, password in wifi.items():
            time.sleep(1)
            print(f"WIFI-SSID : {ssid}  WIFI-PASSWORD : {password}")


    if __name__ == "__main__":
        print("""
    ░██╗░░░░░░░██╗██╗███████╗██╗    ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░██████╗
    ░██║░░██╗░░██║██║██╔════╝██║    ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ░╚██╗████╗██╔╝██║█████╗░░██║    ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║╚█████╗░
    ░░████╔═████║░╚═╝██╔══╝░░╚═╝    ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║░╚═══██╗
    ░░╚██╔╝░╚██╔╝░██╗██║░░░░░██╗    ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝██████╔╝
    ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝    ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░

        """)
        wifiPassExtractor()


except NameError as err:
    print("[!] required modules missing ")

