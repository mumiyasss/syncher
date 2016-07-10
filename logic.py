# -*- coding: utf-8 -*-
import ui
import os
from constants import *

class general:
    def __init__(self):
        update_program_path();
        update_local_config_file();
        
    def update_program_path(self):
        self.PROGRAM_PATH = os.getcwd()
        
        
    def update_local_config_file(self):
        self.CONFIG_FILE_PATH = PROGRAM_PATH + CONFIG_FILE_NAME

########################################################



class device:
    """
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
    """
    def temp_func(self):
        print("Hello");

    def from_dir_choose(self):    
        folder = ui.io.simple_input(WRITE_DEVICE_DIR)
        os.chdir(dev + folder)
        currentDir = os.getcwd()
        return currentDir
     

    def get_device_path(self):
        return dev;

        
########################################################        

class config_connection(general):
    

    _local_conf = []

    #_local_conf = []
    def __init__(self):
        _local_conf = self.get_config_from_file(CONFIG_FILE_PATH)
        if not self._local_conf:
            _local_conf = self.set_config_localy();
            write_config_to_file(CONFIG_FILE_PATH, self._local_conf);
            
            
    ##
    ## Operations with config from/with file of configuration
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 

    def get_config_from_file(self, CONF): # Считывает файл настроек, и записывает в список
	   
	    try:
	        self.confFile = open(CONF, 'r')
	        self.config = [line.strip() for line in confFile]
	        return self.config
	    except Exception:
	        return None
    

    def write_config_to_file(self, CONFIG_FILE_PATH, CONF_LIST_FROM_UI): # Записывает значения 
                                                  # конфигурации в файл по пути CONFIG_FILE_PATH
        ### Создаем файл настроек
        self.confFile = open(CONFIG_FILE_PATH, 'w')
        for dev in CONF_LIST_FROM_UI:
            self.confFile.write(dev + "\n")

    ##
    ## Operations with config localy in RAM
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
    def set_config_localy(self):
        
        # Попробую создать экземпляры класса device прямо в этом классе. 
        tempDevice = device() # для функционирования from_dir = from_dir_choose()


        print(WHERE_IS_FROM_DIR)
        from_dir = tempDevice.from_dir_choose() # КАК ВЫЗВАТЬ ФУНКЦИЮ ДРУГОГО КЛАССА?
        
        print(WHERE_IS_TO_DIR)
        to_dir  = tempDevice.to_dir_choose()
        
        return [from_dir, to_dir]
            
    
    def get_local_config(self):
        return _local_conf;
        
     


########################################################


class unsynch_files:
    #def __init__():    
    pass
#########################################################

	    
	        
