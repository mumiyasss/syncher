#! /usr/bin/python3.5

import ui
import logic

class device:
    
    def __init__(self):
        os.chdir(UNIX_DEVICES_PATH)
        allFiles = os.listdir(path=".")
        
        numFolder = 0
        for device in allFiles:
            numFolder += 1;
            ui.io.simple_print(str(numFolder) + ") " + device)
            
        devChoose = ui.io.simple_input()       # device choosing 
        os.chdir(allFiles[int(devChoose) - 1])
        os.chdir(INTERNAL_STORAGE)
        dev = getcwd(); # Абсолютный путь к устройству
                        # Флеш карта???

    def from_dir_choose(self):    
        folder = ui.io.simple_input(WRITE_DEVICE_DIR)
        os.chdir(dev + folder)
        currentDir = os.getcwd()
        return currentDir
     

    def get_device_path(self):
        return dev;


def main():
    #interf = ui.interface();
    # interf.conf.set_config()
    configuration = logic.configConnection()
    session = configuration.get_local_config();
    uns = logic.unsynch_files();
    uns.synch_all_files(session[0], session[1]);
    ui.io.simple_print("That's all")

if __name__ == '__main__':
    main()
    
