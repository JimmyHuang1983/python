import os

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

# define exe_yn 函式, next : 下個要執行的task, cmd : 下個要執行的task command
def exe_yn(next,cmd) : 
    yn = input(f"{bcolors.WARNING}!!Done,  choose y/n to continue..., next : {next} : {bcolors.RESET}").upper()
    if yn == "Y" :
        os.system(cmd)
        print("\n")
        return 
    else :
        print(f"{bcolors.FAIL}\n!!You SKIP the action : \'{next}\' !!\n {bcolors.RESET}")
        return

#list all task description
task_list = ["query GMScore version",
            "reduce to 60s",
            "setprop log.tag.rpcs VERBOSE",
            "set common_user_type to test",
            "install wearmedia apk ===no need for phone=====",
            "push mp3 file     ===no need for phone=====",
            "=========To setup fast_pair_support_toggle_for_triangle_switch============",
            "======To setup SASS======, SET fast_pair_support_smart_audio_source_switch",
            "SET FastPairFeature__sass_user_configurable",
            "SET FastPairFeature__sass_debug_notification ",
            "SET fast_pair_enable_sass_for_non_sass_peripheral",
            "===To setup SASS && Triangle integration test environemnt===,fast_pair_support_calling_switch_contains_sass_candidate on the phone ",
            "FastPairConfig__add_switch_candidate_to_peripheral_list on the watch",
            "3P 耳機 要把檢查關掉,Test for 3P headset ?  ",
            "看看做了哪些flag的改動~",
            "reboot device ? "]

#list all commands (corresponding to task order)
command_list = ["adb shell dumpsys package com.google.android.gms | grep versionName",
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "fast_pair_manual_connect_affect_duration_millis" --esa types "long" --esa values "60000" com.google.android.gms',
                'adb shell setprop log.tag.rpcs VERBOSE',
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "common_user_type" --esa types "string" --esa values "test" com.google.android.gms',
                "adb install '/home/huangjimmy/Downloads/wearmedia/base.apk'",
                "adb push '/home/huangjimmy/Downloads/wearmedia/What_about_us.mp3' /storage/emulated/0/music",
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "fast_pair_support_toggle_for_triangle_switch" --esa types "boolean" --esa values "true" com.google.android.gms',
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "fast_pair_support_smart_audio_source_switch" --esa types "boolean" --esa values "true" com.google.android.gms',
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "FastPairFeature__sass_user_configurable" --esa types "boolean" --esa values "true" com.google.android.gms',
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "FastPairFeature__sass_debug_notification" --esa types "boolean" --esa values "true" com.google.android.gms',
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "fast_pair_enable_sass_for_non_sass_peripheral" --esa types "boolean" --esa values "true" com.google.android.gms',
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "fast_pair_support_calling_switch_contains_sass_candidate" --esa types "boolean" --esa values "true" com.google.android.gms',
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "FastPairConfig__add_switch_candidate_to_peripheral_list" --esa types "boolean" --esa values "true" com.google.android.gms',
                'adb shell am broadcast -a \'com.google.android.gms.phenotype.FLAG_OVERRIDE\' --es package "com.google.android.gms.nearby" --es user "\*" --esa flags "FastPairFeature__check_peripheral_support_switch" --esa types "boolean" --esa values "false" com.google.android.gms',
                'adb shell sqlite3 /data/data/com.google.android.gms/databases/phenotype.db \\\'\'SELECT name, printf("%s%s%s%s%s", intVal, case boolVal when 0 then "FALSE" when 1 then "TRUE" else "" end, floatVal, stringVal, extensionVal) AS value FROM FlagOverrides WHERE committed=1 AND packageName="com.google.android.gms.nearby" ORDER BY name ASC\'\\\'',
                "adb reboot"]

#main
os.system("adb devices")
os.system('adb root')

print("~~Done, ##Please choose your device, 1. watch   2. phone  3. SKIP : ")
device_type = input(f"{bcolors.WARNING}input 1, 2, or 3 for device type :{bcolors.RESET} \n")

if device_type == "1":
    print("Your connected device is Watch!")
    
    yn = input(f"{bcolors.WARNING} !!Done,  choose y/n to continue..., next : install Watch GMScore : {bcolors.RESET}").upper()
    if yn == "Y" :
        os.system("adb install '/home/huangjimmy/Downloads/##GMScore/new/GmsCore_wearable_armv7_hdpi_release.apk'")
        print("\n")
    else :
        print(f"{bcolors.FAIL} \n!!You SKIP the action !!\n {bcolors.RESET}")
     
    yn = input(f"{bcolors.WARNING} !!Done,  choose y/n to continue..., next : install mobile utilities apk (for watch) : {bcolors.RESET}").upper()
    if yn == "Y" :
        os.system("adb install '/home/huangjimmy/Downloads/#old mobile utility apk/mobile_utilities.apk'")
        print("\n")
        
    else :
        print(f"{bcolors.FAIL} \n!!You SKIP the action !!\n {bcolors.RESET}")
        
elif device_type == "2" :
    print(f"Your connected device is {bcolors.OK}Phone{bcolors.RESET} !")
    phone_os = input(f"{bcolors.WARNING} !!!Please input your phone OS version : P,Q,R,S,T , MUST Uppercase!!{bcolors.RESET}\n").upper()
    print(f"Your input is {phone_os}")
   
    if phone_os == "P" : 
        print(f"!!!your OS is Andorid {bcolors.OK}P {bcolors.RESET}!!!")
        print("Start to install Android P GMScore apk...")
        os.system("adb install '/home/huangjimmy/Downloads/##GMScore/new/GmsCore_prodpi_arm64_alldpi_release.apk'")
   
    elif phone_os == "Q" :
        print(f"!!!your OS is Andorid {bcolors.OK}Q {bcolors.RESET}!!!")
        print("Start to install Android Q GMScore apk...")
        os.system("adb install '/home/huangjimmy/Downloads/##GMScore/new/GmsCore_prodpi_arm64_alldpi_release.apk'")
   
    elif phone_os == "R" :
        print(f"!!!your OS is Andorid {bcolors.OK}R {bcolors.RESET}!!!")
        print("Start to install Android R GMScore apk...")
        os.system("adb install '/home/huangjimmy/Downloads/##GMScore/new/GmsCore_prodrvc_arm64_alldpi_release.apk'")
   
    elif phone_os == "S" :
        print(f"!!!your OS is Andorid {bcolors.OK}S {bcolors.RESET}!!!")
        print("Start to install Android S GMScore apk...")
        os.system("adb install '/home/huangjimmy/Downloads/##GMScore/new/GmsCore_prodsc_arm64_alldpi_release.apk'")
        
    elif phone_os == "T" :
        print(f"!!!your OS is Andorid {bcolors.OK}T {bcolors.RESET}!!!")
        print("Start to install Android T GMScore apk...")
        os.system("adb install '/home/huangjimmy/Downloads/##GMScore/new/GmsCore_prodsc_arm64_alldpi_release.apk'")
        #os.system("adb install '/home/huangjimmy/Downloads/##GMScore/new/GmsCore_prodnext_arm64_alldpi_release.apk'")
    
    else :
        print("Not applied...")
    
    yn = input(f"{bcolors.WARNING} !!Done,  choose y/n to continue..., next : install mobile utilities apk (for phone) : {bcolors.RESET}").upper()
    if yn == "Y" :
        os.system("adb install '/home/huangjimmy/Downloads/mobile_utilities.apk'")
        print("\n")
        
    else :
        print(f"{bcolors.FAIL} \n!!You SKIP the action !!\n {bcolors.RESET}")   


else :
    print("~~Your device is others, SKIP~~")

for x in range(len(task_list)) :
    exe_yn(task_list[x],command_list[x])
    
   
    

