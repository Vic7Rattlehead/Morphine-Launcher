# MIT License

# Copyright (c) 2025 Vic RattleHead

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, sys, shutil, json, subprocess, winreg, webbrowser
from colorama import Fore
from pathlib import Path


# VALUE
directory = str(Path.cwd())
if getattr(sys, "frozen", False):
    exe_path = sys._MEIPASS
else:
    exe_path = os.path.dirname(__file__)
cfg = {"SIZE_WIDTH": "1920",
       "SIZE_HEIGHT": "1080",
       "EXIT_AT_INGECT": True,
       "FULLSCREEN": True
    }

def record_json(open_file, value):
    try:
        with open(open_file, 'w', encoding='utf-8') as record_file:
            json.dump(value, record_file, indent=3, ensure_ascii=False)
    except:
        pass

def read_json(open_file, value):
    try:
        with open(open_file, 'r', encoding='utf-8') as read_file:
            return json.load(read_file)

    except:
        record_json(open_file, value)


os.system('title MORPHINE LAUNCHER') # window name

# create folser 'Addons'
try: 
    os.mkdir("Addons")
except: 
    pass

# load config.json // settings game
if not os.path.exists(directory + "/config.json"):
    record_json(directory + "/config.json", cfg)

cfg = read_json(directory + "/config.json", cfg)






def read_addon_json(path):
    try:
        with open(f"{directory}/{path}/Addon.json", "r", encoding='utf-8') as info_addon:
            addon = json.load(info_addon)
        info_addon.close()
        return addon
    except:
        return "ops"


def window_edit(title, text):
    print(title)
    a = input(text)
    return str(a)





def fix_game():
    app_path = directory + '\cof.exe' 
    if not os.path.exists(app_path):
        os.system('cls')
        input("cof.exe NOT DETECTED, PRESS ENTER")
        main()
    
    try:
        key_path = r"SOFTWARE\Microsoft\DirectX\UserGpuPreferences"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
            value_name = app_path
            value_data = "GpuPreference=2;"
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
        main()
    except Exception as e:
        print(f"Error: {e}\n Fix the game manually or report the bug to Vic Rattlhead!")
        input('please press enter')

# Menu selected addon
def action(name):
    try:
        os.system("cls")
        addon_info = read_addon_json("Addons/" + name)

        print(f"""  ✩{addon_info['Addon_Name']}✩
NAME: {addon_info['Addon_Name']}
AUTHOR: {addon_info['Author']}
VERSION: {addon_info['Version']}
IS ACTIVE: {addon_info["Included"]}


1) {'ENABLE' if not addon_info["Included"] else 'DISABLE'} ADDON
2) DELETE ADDON
0) MENU
    """)
        a = input('>>> ')
        if a == "1":
            if addon_info["Included"] == False:
                shutil.copytree(f'{directory}/Addons/{name}/actual/', directory, dirs_exist_ok=True)
                addon_info["Included"] = True
                record_json(f"Addons/{name}/Addon.json", addon_info)
            else:
                shutil.copytree(f'{directory}/Addons/{name}/backup/', directory, dirs_exist_ok=True)
                addon_info["Included"] = False
                record_json(f"Addons/{name}/Addon.json", addon_info)
        elif a == "2":
            shutil.copytree(f'{directory}/Addons/{name}/backup/', directory, dirs_exist_ok=True)
            shutil.rmtree(f"{directory}/Addons/{name}")
            addon_menu()
        elif a == "0":
            addon_menu()
        action(name)
    except:
        main()

# About menu
def about():
    os.system('cls')
    print(f"""   ✩ABOUT✩
VERSION EDITION - 1.0 RELEASE
DEVELOPER - VIC RATTLEHEAD 
        
""")
    input('ENTER - EXIT')
    others()

def others():
    os.system('cls')
    print("""   ✩OTHERS✩ 
1) VIC RATTLEHEAD
2) STEAM GUIDE
3) TELEGRAM
4) BOOSTY(tips)
5) ABOUT
0) MENU""")
    a = input('>>> ')
    if a == "1":
        webbrowser.open("https://steamcommunity.com/profiles/76561199180944287/")
        others()
    elif a == "2":
        webbrowser.open("https://steamcommunity.com/sharedfiles/filedetails/?id=3563497311")
        others()
    elif a == "3":
        webbrowser.open("https://t.me/+W-7nZZoAs9A2Yzdi")
        others()
    elif a == "4":
        webbrowser.open("https://boosty.to/eyeteam/donate")
        others()
    elif a == "5":
        about()
    main()

# Settings menu
def settings():
    os.system('cls')
    print(f"""   ✩SETTINGS✩
1) EDIT WIDTH SIZE WINDOW -> {cfg["SIZE_WIDTH"]}
2) EDIT HEIGHT SIZE WINDOW -> {cfg["SIZE_HEIGHT"]}
3) EXIT AT RUN GAME -> {cfg["EXIT_AT_INGECT"]}
4) FULLSCREEN GAME -> {cfg["FULLSCREEN"]}
0) MENU
""")
    a = str(input(">>> "))
    if a == "1":
        wh = window_edit("EDIT WIDTH SIZE WINDOW", "value: ")
        cfg["SIZE_WIDTH"] = wh
        record_json(directory + "/config.json", cfg)
        read_json(directory + "/config.json", cfg)
    elif a == "2":
        hg = window_edit("EDIT HEIGHT SIZE WINDOW", "value: ")
        cfg["SIZE_HEIGHT"] = hg
        record_json(directory + "/config.json", cfg)
        read_json(directory + "/config.json", cfg)
    elif a == "3":
        cfg["EXIT_AT_INGECT"] = not cfg["EXIT_AT_INGECT"]
        record_json(directory + "/config.json", cfg)
        read_json(directory + "/config.json", cfg)
    elif a == "4":
        cfg["FULLSCREEN"] = not cfg["FULLSCREEN"]
        record_json(directory + "/config.json", cfg)
        read_json(directory + "/config.json", cfg)
    else:
        main()
    settings()

# Run game and configuring the program with compatibility
def run_game():
    os.system('cls')
    flags = "RUNASADMIN DISABLEDXMAXIMIZEDWINDOWEDMODE WINXPSP2 HIGHDPIAWARE"
    reg_path = r"Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"
    exe_path = os.path.join(directory, "cof.exe")
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, directory + "/cof.exe", 0, winreg.REG_SZ, flags)
        print("injection... ")
        
        settings = [
            exe_path,
            "-appid", "223710",
            "-game", "CryOfFear",
            "-gl",
            "-num_edicts", "2048",
            "-heapsize", "1024000",
            "-w", cfg["SIZE_WIDTH"],
            "-h", cfg["SIZE_HEIGHT"],
            
        ]
        if cfg["FULLSCREEN"]:
            settings.append("-fullscreen")
        else:
            settings.append("-window")
        subprocess.Popen(settings, shell=True,
                           creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS,
                           stdin=subprocess.DEVNULL,
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        if cfg["EXIT_AT_INGECT"]:
            sys.exit()
        else:
            input('please press enter')
            main()
    except Exception as e:
        print(e)
        input('cof.exe NOT DETECTED, PRESS ENTER')
        main()

# Main menu
def main():
    os.system('cls')
    print(Fore.RED, """ ✩WELCOME TO MORPHINE LAUNCHER!✩
1) RUN CRY-OF-FEAR
2) OPEN DIRECTORY
3) ADDONS MANAGER
4) OTHERS
5) SETTINGS GAME AND LAUNCHER
0) EXIT LAUNCHER""")
    a = input('>>> ')
    if a == "1":
        run_game()
    elif a == "2":
        os.system(f'explorer "{directory}"')
    elif a == "3":
        addon_menu()
    elif a == "4":
        others()
    elif a == "5":
        settings()
    elif a == "0":
        sys.exit()
    main()

# List addons
def addon_menu():
    try:
        os.system('cls')
        array_addon = []

        addon_list = os.listdir(directory + "/Addons")
        
        print(" ✩ADDONS MANAGER✩")
        for id, addon in enumerate(addon_list, 1):
            print(f"{id}) {addon}")
            array_addon.append(addon)
        print("0) MENU")
        a = input(">>> ")
        if a != "0":
            if a.isdigit():
                if 0 <= int(a) - 1 < len(array_addon):
                    action(array_addon[int(a) - 1])
                else:
                    input('NO DETECTED ADDON, PRESS ENTER')
                    addon_menu()
            else:   
                input('NO DETECTED ADDON, PRESS ENTER')
                addon_menu()
        else:
            main()
    except:
        sys.exit()





if __name__ == "__main__":
    fix_game()




# Vic Rattlehead