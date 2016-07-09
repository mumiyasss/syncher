# -*- coding: utf-8 -*-
import ui
import constants

class general:
    def __init__(self):
        update_program_path();
        update_config_file();
        
    def update_program_path(self):
        self.PROGRAM_PATH = os.getcwd()
        
        
    def update_config_file(self):
        self.CONFIG_FILE_PATH = PROGRAM_PATH + CONFIG_FILE_NAME
        
########################################################        

class config_connetion(general):
    _conf = []
    def __init__(self):
        _conf = get_config(CONFIG_FILE_PATH)
        if not self._conf:
            self.uiList = set_config();
            write_config(CONFIG_FILE_PATH, uiList);
            self._conf  = self.uiList;
            
    
    def get_config(self, CONF): # Считывает файл настроек, и записывает в список
	   
	    try:
	        self.confFile = open(CONF, 'r')
	        self.config = [line.strip() for line in confFile]
	        return self.config
	    except Exception:
	        return None
        
    def set_config(self):
                
        print("Выберите устройство:")
        MOB = device_choose()
        
        print("Выберите директорию бэкапа:")
        PC  = backup_directory()
        
        print("Синхронизация:\n1) С компьютера на устройство\n2) С устройтва на компьютер ?")
        d = input()
        
        if (d == '1') :
            SYN_DEVICE = MOB
        elif (d == '2') :
            SYN_DEVICE = PC
       
        return [MOB, PC, SYN_DEVICE]
            
    
    def write_config(self, CONFIG_FILE_PATH, CONF_LIST_FROM_UI): # Записывает значения 
                                                  # конфигурации в файл по пути CONFIG_FILE_PATH
        ### Создаем файл настроек
        self.confFile = open(CONFIG_FILE_PATH, 'w')
        for dev in CONF_LIST_FROM_UI:
            self.confFile.write(dev + "\n")
    
    def get_conf(self):
        return _conf;
        
     


########################################################


class unsynch_files:
    #def __init__():    
    pass
#########################################################

class device:
    def __init__(self):
        os.chdir(UNIX_DEVICES_PATH)
        allDevices = os.listdir(path=".")
        
        numFolder = 0
        for device in allFiles:
            numFolder += 1;
            ui.io.simple_print(str(numFolder) + ") " + device)
            
        devChoose = ui.io.simple_input()       # device choosing 
        os.chdir(allFiles[int(devChoose) - 1])
        os.chdir('Внутренняя память')
        dev = getcwd(); # Абсолютный путь к устройству
                        # Флеш карта???
        
    def get_device(self):
        return dev;
    
    def choose_device_dir(self):    
        folder = ui.io.simple_input("Пропишите путь на устройстве: ")
        os.chdir(dev + folder)
        currentDir = os.getcwd()
        return currentDir
        
