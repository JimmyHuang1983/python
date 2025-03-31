import os
import re
import subprocess
import time
import datetime

def print_option(lable, text):
    """以黃色顯示數字，後面文字無顏色"""
    print(f"\033[33m{lable} \033[0m {text}")



def get_screen_resolution():
    """取得設備螢幕解析度"""
    try:
        result = os.popen("adb shell wm size").read()
        match = result.strip().split(":")[-1].strip().split("x")
        return int(match[0]), int(match[1])
    except Exception as e:
        print(f"Error occurred while getting screen resolution: {e}")
        return None, None

def tap_at_coordinates(x, y, times):
    """在指定座標點擊多次"""
    for i in range(times):
        print(f"Tapping at ({x}, {y}) - Tap {i + 1}/{times}")
        os.system(f"adb shell input tap {x} {y}")
        time.sleep(0.1)  # 每次點擊間隔 0.2 秒

def create_alarms():
    user_input = input("Enter the start time for alarms (HH:MM, 24-hour format): ").strip()
    timex = input("How many alarm do you want to add?")
    os.system("adb root")
    time.sleep(1)
    os.system("adb shell settings put system screen_off_timeout 1800000")
    
    try:
        # Parse user input
        hour, minute = map(int, user_input.split(":"))
        now = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
    except ValueError:
        print("Invalid time format. Please enter in HH:MM format.")
        return

    print(f"Starting from {now.strftime('%H:%M')}...")
    for i in range(1, int(timex)+1):
        time.sleep(10)
        alarm_time = now + datetime.timedelta(minutes=i)
        hour, minute = alarm_time.hour, alarm_time.minute
        
        # Determine if alarm is one-time or recurring
        if i % 2 == 0:  # Even alarms are recurring (e.g., Monday, Tuesday, Wednesday)
            days = "1,2,3,4,5,6,7"
            command = f"adb shell am start -a android.intent.action.SET_ALARM --ez android.intent.extra.alarm.SKIP_UI true --ei android.intent.extra.alarm.HOUR {hour} --ei android.intent.extra.alarm.MINUTES {minute} --eia android.intent.extra.alarm.DAYS {days} "
        else:  # Odd alarms are one-time
            command = f"adb shell am start -a android.intent.action.SET_ALARM --ez android.intent.extra.alarm.SKIP_UI true --ei android.intent.extra.alarm.HOUR {hour} --ei android.intent.extra.alarm.MINUTES {minute} "

        print(f"Creating alarm {i}: {hour:02d}:{minute:02d}")
        print(command)
        os.system(command)
def adb_pull_file():
    file_base = "tmp"
    file_ext = ".png"
    counter = 0

    # Check if "tmp.png" exists first
    if os.path.exists(f"{file_base}{file_ext}"):
        counter = 1
        # Find the next available filename
        while os.path.exists(f"{file_base}{counter}{file_ext}"):
            counter += 1

    # Determine the new file name
    if counter == 0:
        new_file = f"{file_base}{file_ext}"
    else:
        new_file = f"{file_base}{counter}{file_ext}"

    # Use adb to pull the file from the device
    subprocess.run(["adb", "pull", "/sdcard/tmp.png", new_file])

    print(f"File saved as {new_file}")


def print_menu():
    """顯示選單"""
    print_green("\n--- Welcome to the Testing Tool ---")
    print("Please select an option:")
    print_option(0, "   adb root")
    print_option(1, "   adb devices")
    print_option(2, "   Reboot device")
    print_option(3, "   Query Retail Demo (core)/ (preload)/ (attract loop) version")
    print_option(33, "  Query Retail Demo Data(datapop) / Retail Demo Media(mediapop)/ Pixel Demo(interactive) version")
    print_option(4, "   SW version")
    print_option(5, "   Query current app name & version")
    print_option(15, "  Tap on screen 15 times")
    print_option("b", "   Input command before scanning beta QR")
    print_option("blq", " Command to query bootloader locked or not")
    print_option("ss", "  Take a screenshot and pull")
    print_option("rv", "  Recording a video")
    print_option("pv", "  Pull the video")
    print_option("kiki", "Query Kiki, Astrea, aicore, aiai version")
    print_option("bl", "  Enter bootloader mode")
    print_option("fr", "  Factory Reset device")
    print_option("dl", "  Download file and music for 1.10.1 Clear and reset user-generated data")
    print_option("r", "   Catch bugreport")
    print_option("l", "   Pull persistent log")
    print_option("fslp", "adb command to show first sync log patterns")
    print_option("sota", "FOTA test pre-setup 3 commands")

    print_green("========================↓↓ Watch test tool ↓↓========================")
    print_option("ca", "  Create xx alarm for backup & restore test")
    print_option("long", "Set screen timeout to never")
    print_option("pt", "  Set Phone alarm sync phenotype flag to True")
    print_option("pf", "  Set Phone alarm sync phenotype flag to False")
    print_option("wt", "  Set Watch alarm sync phenotype flag to True")
    print_option("wf", "  Set Watch alarm sync phenotype flag to False")


    print_option("q", "   Quit")
    print("")

def execute_command(option):
    """根據使用者選擇執行對應指令"""
    clear_screen()
    if option == "0":
        print_yellow("\nExecuting: adb root")
        os.system("adb root")
    elif option == "1":
        print_yellow("\nExecuting: adb devices")
        os.system("adb devices")
    elif option == "2":
        os.system("adb reboot")
        print_green("\nReboot device")
        
    elif option == "3":
        print_yellow("\nQuery Retail Demo versions")
        print_yellow("\nRetail Demo (core) version")
        os.system('adb shell pm dump com.google.android.retaildemo | grep -E "versionName|versionCode"')
        print_yellow("\nRetail Demo Service (Preload) version")
        os.system('adb shell pm dump com.google.android.apps.retaildemo.preload |grep -E "versionName|versionCode"')
        print_yellow("\nRetail Demo attractloop version")
        os.system('adb shell pm dump com.google.android.apps.retaildemo.attractloop | grep -E "versionName|versionCode"')
    elif option == "33":
        print_yellow("\nQuery Retail (datapop) / (mediapop)/ (interactive) version")
        print_yellow("\nRetail Demo Data (datapop)(com.google.android.apps.retaildemo.datapop) version")
        os.system('adb shell pm dump com.google.android.apps.retaildemo.datapop | grep -E "versionName|versionCode"')
        print_yellow("\nRetail Demo Media (mediapop) (com.google.android.apps.retaildemo.mediapop) version")
        os.system('adb shell pm dump com.google.android.apps.retaildemo.mediapop |grep -E "versionName|versionCode"')
        print_yellow("\nPixel Demo (com.retaildemo.interactive) version")
        os.system('adb shell pm dump com.retaildemo.interactive | grep -E "versionName|versionCode"')
    elif option == "4":
        print_yellow("\nQuery SW ROM versions")
        sw_version_query()
    elif option == "5":
        print_yellow("\nQuery Now focus app name & version")
        try:
            result = subprocess.check_output(
                "adb shell dumpsys activity | grep mCurrentFocus | sed 's/.* //g' | sed 's/\\/.*//g'", 
                shell=True, 
                text=True
            ).strip()  # 去除輸出的空白

            # 將結果存到變數 app_name
            app_name = result if result else "No app found"
            version_result = subprocess.check_output(
                f"adb shell pm dump {app_name} | grep -E 'versionName|versionCode'", 
                shell=True, 
                text=True
            ).strip()

            print(f"Current foreground app package name:", end='')
            print_yellow(f"{app_name}")
            print(f"Current foreground app version :\n", end='')
            print_yellow(f"{version_result}")
        except subprocess.CalledProcessError as e:
            print("Failed to get app name. Ensure ADB is connected and working.")
            print(e)
    
    elif option == "15":
        width, height = get_screen_resolution()
        if width and height:
            # 設定點擊右下角的座標 (例如距離邊界留一些像素以防出界)
            x = width - 200  # 距離右邊緣 10px
            y = height - 200  # 距離下邊緣 10px
            tap_at_coordinates(x, y, 15)
            print("Tap 15 times done.")
        else:
            print("Failed to get screen resolution.")


    elif option == "l":
        
        os.system('adb pull /sdcard/Download ./t')
    elif option == "b":     
        os.system('adb shell settings put global device_demo_mode 1')
        print_yellow("\nadb shell settings put global device_demo_mode 1")
    elif option == "blq":     
        os.system('adb shell getprop ro.boot.flash.locked')
        print_yellow("\nadb shell getprop ro.boot.flash.locked  --> query bootloader locked or not")
    elif option == "ss":     
        os.system('adb shell /system/bin/screencap -p /sdcard/tmp.png')
        print_yellow("\nadb shell /system/bin/screencap -p /sdcard/tmp.png  --> capture a screenshot")
        adb_pull_file()
    elif option == "rv":     
        os.system('adb shell screenrecord /sdcard/test.mp4')
        print_yellow("\nadb shell screenrecord /sdcard/test.mp4  --> record a video")
    elif option == "pv":     
        os.system('adb pull sdcard/test.mp4')
        print_yellow("\nadb pull sdcard/test.mp4  --> adb pull the video")
    elif option == "kiki":     
        print_yellow("\nQuery Kiki related packages(Kiki, Astrea, aicore, aiai) versions")
        print_yellow("\nKiki version (com.google.android.apps.pixel.agent)")
        os.system('adb shell pm dump com.google.android.apps.pixel.agent | grep -E "versionName|versionCode"')
        print_yellow("\nAstrea version (com.google.android.as.oss)")
        os.system('adb shell pm dump com.google.android.as.oss |grep -E "versionName|versionCode"')
        print_yellow("\naicore version (com.google.android.aicore)")
        os.system('adb shell pm dump com.google.android.aicore | grep -E "versionName|versionCode"')
        print_yellow("\naiai version (com.google.android.as)")
        os.system('adb shell pm dump com.google.android.as | grep -E "versionName|versionCode"')
    elif option == "bl":
        print_yellow("\nEnter command 'adb reboot bootloader', wait for device to enter bootloader mode")
        os.system('adb reboot bootloader')
        
    elif option == "fr":
        print_yellow("\nEnter command 'adb reboot bootloader', wait for device to enter bootloader mode")
        os.system('adb reboot bootloader')
        print_yellow("\nPause 8 seconds")
        time.sleep(8)
        print_yellow("\nEnter command 'fastboot devices', check if device enter bootloader mode")
        os.system('fastboot devices')
        print_yellow("\nEnter command 'fastboot -w', factory reset device")
        os.system('fastboot -w')
        print_yellow("\nEnter command 'fastboot reboot', factory reset device")
        os.system('fastboot reboot')
        
    elif option == "dl":
        
        os.system('adb shell input text "http://ipv4.download.thinkbroadband.com/5MB.zip"')
        print_yellow("\nadb shell input text http://ipv4.download.thinkbroadband.com/5MB.zip")
        time.sleep(30)
        print_yellow("\nPause 30 seconds, please focus at chrome search input field")
        os.system('adb shell input text "https://dl.last.fm/static/1733207834/131211148/760a2aa28ba11204f6c5b486347a285f2da0339ed2613237f4ea19c1bc924eca/Death+Grips+-+Get+Got.mp3"')
        print_yellow("\nadb shell input text https://dl.last.fm/static/1733207834/131211148/760a2aa28ba11204f6c5b486347a285f2da0339ed2613237f4ea19c1bc924eca/Death+Grips+-+Get+Got.mp3")

    elif option == "r":
        
        os.system('adb bugreport')
        print_yellow("\nadb bugreport")
    
    elif option == "fslp":
        
        os.system('adb devices')
        print_yellow('\nInput adb logcat | grep -E "Executing|NEW_FLOW|Updated ph|GetAllConfiguration|Demo packages"')
        os.system('adb logcat | grep -E "Executing|NEW_FLOW|Updated ph|GetAllConfiguration|Demo packages"')
        

    elif option == "p":
        
        os.system('adb shell input text "\#GoogleDemoUnit\#"')
    

    elif option == "sota":
        print_yellow("\nEnter command for FOTA test pre-setup 3 commands")
        os.system('fastboot oem silentota enable')
        time.sleep(1)
        os.system('fastboot oem silentota status')
        time.sleep(1)
        os.system('fastboot oem HALT')
        time.sleep(1)

    elif option == 'ca' :
        print_yellow("\ncreate xx alarms for backup & restore test")
        create_alarms()

    elif option == 'long' :
        os.system("adb root")
        time.sleep(1)
        os.system("adb shell settings put system screen_off_timeout 1800000")
        print_yellow("\nSet screen timeout to never.")
    
    elif option == 'pt' :
        os.system("adb root")
        time.sleep(1)
        os.system("adb shell am broadcast -a 'com.google.android.gms.phenotype.FLAG_OVERRIDE' --es package com.google.android.deskclock#com.google.android.deskclock --es user '\*' --esa flags '45412303' --esa values 'true' --esa types 'boolean' --debug-log-resolution com.google.android.gms")
        print_yellow("\nSet Phone alsrm sync phenotype flag to True.")
    
    elif option == 'pf' :
        os.system("adb root")
        time.sleep(1)
        os.system("adb shell am broadcast -a 'com.google.android.gms.phenotype.FLAG_OVERRIDE' --es package com.google.android.deskclock#com.google.android.deskclock --es user '\*' --esa flags '45412303' --esa values 'false' --esa types 'boolean' --debug-log-resolution com.google.android.gms")
        print_yellow("\nSet Phone alsrm sync phenotype flag to False.")
    
    elif option == 'wt' :
        os.system("adb root")
        time.sleep(1)
        os.system("adb shell am broadcast -a 'com.google.android.gms.phenotype.FLAG_OVERRIDE' --es package com.google.android.wearable.deskclock#com.google.android.deskclock --es user '\*' --esa flags '45411528' --esa values 'true' --esa types 'boolean' --debug-log-resolution com.google.android.gms")
        print_yellow("\nSet Watch alsrm sync phenotype flag to True.")
    
    elif option == 'wf' :
        os.system("adb root")
        time.sleep(1)
        os.system("adb shell am broadcast -a 'com.google.android.gms.phenotype.FLAG_OVERRIDE' --es package com.google.android.wearable.deskclock#com.google.android.deskclock --es user '\*' --esa flags '45411528' --esa values 'false' --esa types 'boolean' --debug-log-resolution com.google.android.gms")
        print_yellow("\nSet Watch alsrm sync phenotype flag to False.")

    else:
        print_yellow("\nInvalid option. Please try again.")
    
    
        
def sw_version_query():
    """解析 SW 版本資訊"""
    print_yellow("Fetching SW version information...\n")
    result = os.popen('adb shell getprop | grep "\\[ro\\.product\\.build\\.fingerprint\\]"').read()
    if result.strip():
        # 提取資料
        match = re.search(r'\[(?:.*?)/(.+?)/(.+)\]', result)
        if match:
            device = match.group(1)
            build = match.group(2)
            print(f"Device : {device}")
            print(f"Build  : {build}")
        else:
            print_yellow("Unable to parse SW version information.")
    else:
        print_yellow("No SW version information found. Ensure the device is connected.")

def clear_screen():
    """清除螢幕輸出"""
    os.system("clear" if os.name == "posix" else "cls")

def print_yellow(message):
    """以黃色文字顯示"""
    print(f"\033[33m{message}\033[0m")  # ANSI 編碼，33 是黃色
def print_green(message):
    """以綠色文字顯示"""
    print(f"\033[32m{message}\033[0m")  # ANSI 編碼，32 是綠色

def main():
    """主程式"""
    while True:
        print_menu()
        user_input = input("Enter your choice: ").strip()
        
        if user_input.lower() == "q":
            clear_screen()
            print_yellow("Exiting the tool. Goodbye!")
            break
        else:
            execute_command(user_input)




if __name__ == "__main__":
    main()
