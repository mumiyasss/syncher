#! /usr/bin/python3.5

import ui
import logic
import constants as CONST
import os

class device:
    def __init__(self):
        os.chdir(CONST.UNIX_DEVICES_PATH)
        allFiles = os.listdir(path=".")
        
        numFolder = 0
        print("Выберите ваше устройство из списка: ")
        for device in allFiles:
            numFolder += 1;
            file_path = device+'/'+CONST.INTERNAL_STORAGE+'/'+'NEXUS5.txt'
            if os.path.exists(file_path):
                ui.io.simple_print(str(numFolder) + ") " + "Google Nexus 5")
            else:
                ui.io.simple_print(str(numFolder) + ") " + device)
            
        devChoose = ui.io.simple_input()       # device choosing 
        os.chdir(allFiles[int(devChoose) - 1])
        os.chdir(CONST.INTERNAL_STORAGE)
        self.dev = os.getcwd(); # Абсолютный путь к устройству
                        # Флеш карта???

    def from_dir_choose(self):    
        folder = ui.io.simple_input(WRITE_DEVICE_DIR)
        os.chdir(dev + folder)
        currentDir = os.getcwd()
        return currentDir
     

    def get_device_path(self):
        return self.dev;
   

def main():
    new_device = device()
    path = new_device.get_device_path();


    configuration = logic.configConnection()
    session = configuration.get_local_config();
    uns = logic.unsynch_files();
    uns.synch_all_files(path+'/DCIM', '/media/kolya/KolyanHardDisk1/backup/FullNexus');
    ui.io.simple_print("That's all")
    # Настроить также работу с жестким диском

def main_CLOSED():
    #interf = ui.interface();
    # interf.conf.set_config()
    configuration = logic.configConnection()
    session = configuration.get_local_config();
    uns = logic.unsynch_files();
    uns.synch_all_files(session[0], session[1]);
    ui.io.simple_print("That's all")

    #SET_CONFIG_LOCALLY доделать

if __name__ == '__main__':
    main()
    
