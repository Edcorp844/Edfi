import time
import sys
import os
import platform
import subprocess
import re

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def clear():
    if platform == 'Linux':
        os.system("clear")
    else:
        os.system("cls")

clear()
def display_style(T):
    for i in T + '':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1. /100)
        

def cmd():
    if platform == "Linux":
        pass
    else:
        command_output = subprocess.run(["netsh", "wlan", "show","profile"], capture_output = True).stdout.decode()
        profile_names = (re.findall("All User Profile     :(.*)\r", command_output))
        wifi_list = list()

        if len(profile_names) != 0:
            for name in profile_names:
                wifi_profile = dict()
                profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()

                if re.search("Security key           :Absent", profile_info):
                    continue
                else:
                    wifi_profile["ssid"] = name
                    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output= True).stdout.decode()
                    password = re.search("Key Content            :(.*\r)", profile_info_pass)

                    if password == None:
                        wifi_profile["password"] = None
                    else:
                        wifi_profile["password"] = password[1]

                    wifi_list.append(wifi_profile)

        for x in range(len(wifi_list)):
            print(P+"", wifi_list[x])

def banner():
    print (G+'''Product of Edson corperations (EDCORP).'''+O+"|")
    print (O+'''_______________________________________|''')
    
    
    display_style(O+'''
   ################################################
   ##            ___   _                         ##
   ##            |_ `__| __ __ __ ___            ##
   ##            |__[__|[__[__]| '|__].          ##
   ##                            _|              ##
   ################################################                            
     ''')   
    print("")
    print (G +'''  .;'                     `;,    ''')
    print (G +''' .;'  ,;'             `;,  `;,   ''')
    print (G +'''.;'  ,;'  ,;'     `;,  `;, `;,  ''')
    print (G +'''::   ::   :  ''' + GR+'''( )'''+G +'''   :    ::  :: '''+C +"Edcorp get wifi passwords.")
    print (G +''':.  ':.  ':. ''' + GR + '''/_\\'''+ G+'''  ,:'  ,:  .:''')
    print (G +''':.  ':.    '''+ GR +''' /___\\'''+ G + "    ,:'  ,")
    print (G + "  ':.      " + GR + "/_____\\" + G + "      ,:'")
    print (G + "          " + GR + "/       \\" + G + "        ")
    cmd()

banner()
