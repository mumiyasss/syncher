#! /usr/bin/python3.4

import os
import shutil
import nexlib


"""
>>> import shutil # Подключаем модуль
>>> shutil.copyfile(r'/home/py/mouse.txt', r'/home/py/new-mouse.txt')
>>> # Указанный путь не будет существовать
>>> shutil.copyfile(r'/home/py/mouse.txt', r'/go/here/no.txt')
IOError: [Errno: 2] No such file or directory
'/go/here/no.txt'
"""

def main():
    global MOB
    global PC
    global SYN_DEVICE
    
    if not (nexlib.get_config(CONFIG_FILE_NAME)):
        conf = nexlib.set_config(CONFIG_FILE_NAME)
        MOB        = conf[0]
        PC         = conf[1]
        SYN_DEVICE = conf[2]
        print("Начать синхронизацию?")
        print("---------------------" +
           "\nУстройство:         " + MOB +
           "\nДиректория бэкапа:  " + PC +
           "\nСинхронизируется в: " + SYN_DEVICE)
        print("---------------------")
    else:
        conf = nexlib.get_config(CONFIG_FILE_NAME)
        MOB        = conf[0]
        PC         = conf[1]
        SYN_DEVICE = conf[2] 
        print("Начать синхронизацию?")
        print("---------------------" +
           "\nУстройство:         " + MOB +
           "\nДиректория бэкапа:  " + PC +
           "\nСинхронизируется в: " + SYN_DEVICE)
        print("---------------------")
        
        
    while True:
        answer = input("[y/n] ?... ");
        if(answer == 'y'):
            nexlib.synching(MOB, PC, SYN_DEVICE)
            main()
        elif(answer == 'n'):
            g  = nexlib.set_config(CONFIG_FILE_NAME)
            MOB = g[0]
            PC = g[1]
            SYN_DEVICE = g[2]
            main()
        else:
            print("Ошибка!")
        
    
if __name__ == '__main__':
    global programPath
    programPath = os.getcwd()
    global CONFIG_FILE_NAME
    CONFIG_FILE_NAME = programPath + '/backup.config'

    main()
