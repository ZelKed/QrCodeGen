

import pyqrcode
from colorama import Fore, Back
input1 = '' 
import time
import sys
import os
os.system('cls')
os.system('title QrCodeGen - KPT - Version 2.2')


print(Fore.GREEN + ' ______                                                __                            __     ')
print(Fore.YELLOW + '/      |                                              /  |                          /  |    ')
print(Fore.LIGHTRED_EX + '$$$$$$/  _____  ____    ______    ______    ______   _$$ |_     ______   _______   _$$ |_   ')
print(Fore.YELLOW + '  $$ |  /     \/    \  /      \  /      \  /      \ / $$   |   /      \ /       \ / $$   |  ')
print(Fore.GREEN + '  $$ |  $$$$$$ $$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$/    $$$$$$  |$$$$$$$  |$$$$$$/   ')
print(Fore.CYAN + '  $$ |  $$ | $$ | $$ |$$ |  $$ |$$ |  $$ |$$ |  $$/   $$ | __  /    $$ |$$ |  $$ |  $$ | __ ')
print(Fore.BLUE + ' _$$ |_ $$ | $$ | $$ |$$ |__$$ |$$ \__$$ |$$ |        $$ |/  |/$$$$$$$ |$$ |  $$ |  $$ |/  |')
print(Fore.MAGENTA + '/ $$   |$$ | $$ | $$ |$$    $$/ $$    $$/ $$ |        $$  $$/ $$    $$ |$$ |  $$ |  $$  $$/ ')
print(Fore.RED + '$$$$$$/ $$/  $$/  $$/ $$$$$$$/   $$$$$$/  $$/          $$$$/   $$$$$$$/ $$/   $$/    $$$$/  ')
print(Fore.MAGENTA + '                      $$ |                                                                  ')
print(Fore.BLUE + '                      $$ |                                                                  ')
print(Fore.CYAN + '                      $$/                                                                   ')
answer = input(Fore.MAGENTA + "Run Color Test: y/n ") 
if answer == "y": 
    os.system('cls')
    #Begin Scherm
    print(Fore.RED + '_Color Test_', Fore.WHITE + '   Readme.txt: `This is used to check if you have the right Cmd/Terminal. This takes 10/30 seconds.`')
    input(Fore.CYAN + 'Press ENTER To Run Color Test.')
    os.system('cls')
    print('\n')
    print(Fore.RED + '  oooooooo8            o888                        ') 
    print(Fore.YELLOW + 'o888     88   ooooooo   888   ooooooo  oo oooooo   ') 
    print(Fore.GREEN +'888         888     888 888 888     888 888    888 ') 
    print(Fore.CYAN + '888o     oo 888     888 888 888     888 888        ') 
    print(Fore.BLUE + ' 888oooo88    88ooo88  o888o  88ooo88  o888o       ') 
    print('\n')
    time.sleep(0.1)
    print("Printing New Color Test:")


    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = [Fore.LIGHTRED_EX + "[■□□□□□□□□□]",Fore.LIGHTRED_EX + "[■■□□□□□□□□]",Fore.LIGHTRED_EX +  "[■■■□□□□□□□]", Fore.LIGHTRED_EX + "[■■■■□□□□□□]", Fore.LIGHTRED_EX + Fore.LIGHTRED_EX + "[■■■■■□□□□□]", Fore.RED + "[■■■■■■□□□□]", Fore.RED + "[■■■■■■■□□□]", Fore.GREEN + "[■■■■■■■■□□]", Fore.GREEN +  "[■■■■■■■■■□]",  Fore.GREEN + "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    time.sleep(3)
    os.system('cls')
    print('\n')
    print(Fore.RED + ' ______                __      ')
    print(Fore.YELLOW + '/\__  _\              /\ \__   ')
    print(Fore.GREEN + '\/_/\ \/    __    ____\ \ ,_\  ')
    print(Fore.CYAN + '   \ \ \  /__\ /    __// / //  ')
    print(Fore.BLUE + '    \ \ \/\  __//\__   \ \_ ')
    print(Fore.MAGENTA + '     \ \_\ \____\/\____/ \ \__')
    print(Fore.RED + '      \/_/\/____/\/___/   \/__/')
    print('\n')
    time.sleep(3)
    time.sleep(0.05)
    print("If You Dont See The Colors.\nPlease Use A Other Terminal!")
    time.sleep(5)
    os.system('cls')
elif answer == "n": 
    pass
else: 
    print("Run Color Test: Y/N") 




#os.system('cls')
os.system('cls')

#input(Fore.GREEN + '')
print(Fore.YELLOW + "Starting Load Process...")
time.sleep(1)
os.system('cls')
print(Fore.GREEN + "Loading...")

animation = [Fore.LIGHTRED_EX + "[■□□□□□□□□□]",Fore.LIGHTRED_EX + "[■■□□□□□□□□]",Fore.LIGHTRED_EX +  "[■■■□□□□□□□]", Fore.LIGHTRED_EX + "[■■■■□□□□□□]", Fore.LIGHTRED_EX + Fore.LIGHTRED_EX + "[■■■■■□□□□□]", Fore.RED + "[■■■■■■□□□□]", Fore.RED + "[■■■■■■■□□□]", Fore.GREEN + "[■■■■■■■■□□]", Fore.GREEN +  "[■■■■■■■■■□]",  Fore.GREEN + "[■■■■■■■■■■]"]

for i in range(len(animation)):
    try:
        time.sleep(0.4)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    except:
        print(Fore.RED + " Trying To Close...")
        

print("\n")
os.system('cls')




# Banner
print('\n\n')
print(Fore.GREEN + '   ')
print(Fore.RED + '      $$$$$$\             $$$$$$\                  $$\            $$$$$$\                         ')
print(Fore.LIGHTYELLOW_EX + '     $$  __$$\           $$  __$$\                 $$ |          $$  __$$\                        ')
print(Fore.LIGHTCYAN_EX + '     $$ /  $$ | $$$$$$\  $$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\  $$ /  \__| $$$$$$\  $$$$$$$\     ')
print(Fore.LIGHTBLUE_EX + '     $$ |  $$ |$$  __$$\ $$ |      $$  __$$\ $$  __$$ |$$  __$$\ $$ |$$$$\ $$  __$$\ $$  __$$\    ')
print(Fore.BLUE + '     $$ |  $$ |$$ |  \__|$$ |      $$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |\_$$ |$$$$$$$$ |$$ |  $$ |   ')
print(Fore.LIGHTMAGENTA_EX + '     $$ $$\$$ |$$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |$$   ____|$$ |  $$ |   ')
print(Fore.MAGENTA + '     \$$$$$$ / $$ |      \$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ \$$$$$$  |\$$$$$$$\ $$ |  $$ |   ')
print(Fore.LIGHTRED_EX + '      \___$$$\ \__|       \______/  \______/  \_______| \_______| \______/  \_______|\__|  \__|   ')
print(Fore.BLACK + '          \___|                                                                                ',Fore.BLUE+'Version',Fore.LIGHTRED_EX+'2.1',Fore.RED+'')                                                                                  


print(Fore.LIGHTMAGENTA_EX + 'Enter', Fore.LIGHTRED_EX + 'a', Fore.BLUE + 'Website Url:', Fore.LIGHTGREEN_EX + '')       
x = input(input1)
input1 = pyqrcode.create(x)
input1.svg('uca-url.svg', scale=8)
input1.eps('uca-url.eps', scale=2)
os.system('cls')
print(input1.terminal(quiet_zone=1))

print( Fore.GREEN + "Encoding Image:")

animation = [Fore.LIGHTRED_EX + "[■□□□□□□□□□]",Fore.LIGHTRED_EX + "[■■□□□□□□□□]",Fore.LIGHTRED_EX +  "[■■■□□□□□□□]", Fore.LIGHTRED_EX + "[■■■■□□□□□□]", Fore.LIGHTRED_EX + Fore.LIGHTRED_EX + "[■■■■■□□□□□]", Fore.RED + "[■■■■■■□□□□]", Fore.RED + "[■■■■■■■□□□]", Fore.GREEN + "[■■■■■■■■□□]", Fore.GREEN +  "[■■■■■■■■■□]",  Fore.GREEN + "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
os.system('cls')
print("\n")
time.sleep(5)
print('\r')
# Checkpoint
print(Fore.RED + '     $$$$$$\  $$\                           $$\       ')
print(Fore.LIGHTYELLOW_EX + '    $$  __$$\ $$ |                          $$ |      ')
print(Fore.LIGHTCYAN_EX + '    $$ /  \__|$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\ ')
print(Fore.LIGHTBLUE_EX + '    $$ |      $$  __$$\ $$  __$$\ $$  _____|$$ | $$  |')
print(Fore.BLUE + '    $$ |      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / ')
print(Fore.LIGHTMAGENTA_EX + '    $$ |  $$\ $$ |  $$ |$$   ____|$$ |      $$  _$$<  ')
print(Fore.MAGENTA + '    \$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ ')
print(Fore.LIGHTRED_EX + '     \______/ \__|  \__| \_______| \_______|\__|  \__|')
print(Fore.LIGHTRED_EX + 'For Gimp files or Website files. The Qr Code Is Generated')
print(Fore.GREEN + '')



# Loop Function                                            
while True:
    input1 = ''
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + 'Press Ctrl+C to stop\nAnother input?: ')
    x = input(input1)
    input1 = pyqrcode.create(x)
    input1.svg('uca-url.svg', scale=8)
    input1.eps('uca-url.eps', scale=2)
    print(input1.terminal(quiet_zone=1))