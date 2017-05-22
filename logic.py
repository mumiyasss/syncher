# -*- coding: utf-8 -*-
import ui
import os
import shutil

from constants import *

class generalProgramSettings:
    def __init__(self):
        self.update_program_path();
        self.update_config_file();
        


    def update_program_path(self):
        self.PROGRAM_PATH = os.getcwd()
                
    def update_config_file(self):
        self.CONFIG_FILE_PATH = self.PROGRAM_PATH + CONFIG_FILE_NAME


    def get_program_path(self):
        return self.PROGRAM_PATH

    def get_config_file_path(self):
        return self.CONFIG_FILE_PATH;
        

class configConnection(generalProgramSettings):
    
    def __init__(self):
        self.update_program_path();
        self.update_config_file();

        self._local_conf = self.get_config_from_file(self.get_config_file_path())
        if not self._local_conf:
            self._local_conf = self.set_config_localy();
            self.write_config_to_file(self.get_config_file_path(), self._local_conf);
            exit(0)
            
            
    ##
    ## Operations with config from/with file of configuration
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 

    def get_config_from_file(self, CONF):
	    '''
            Считывает файл настроек, и записывает в список
        '''
	    try:
	        self.confFile = open(CONF, 'r')
	        self.config = [line.strip() for line in self.confFile]
	        return self.config
	    except Exception:
	        return None
    

    def write_config_to_file(self, CONFIG_FILE_PATH, CONF_LIST_FROM_UI): 
        '''
            Записывает значения конфигурации
            в файл по пути CONFIG_FILE_PATH
        '''
        ### Открываем файл настроек
        self.confFile = open(CONFIG_FILE_PATH, 'w')
        for dev in CONF_LIST_FROM_UI:
            self.confFile.write(dev + "\n")

    def set_config_localy(self):
        '''
            Operations with config localy in RAM
        '''
        ui.io.simple_print(WHERE_IS_FROM_DIR)
        from_dir = self.from_dir_choose()
        ui.io.simple_print(WHERE_IS_TO_DIR)
        to_dir   = self.to_dir_choose()
        
        return [from_dir, to_dir]
                
    def get_local_config(self):
        return self._local_conf;

    ##
    ## Choosing from/to destinations
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
    def from_dir_choose(self):
        '''
            Choosing from/to destinations
        '''
        return ui.io.simple_input()

    def to_dir_choose(self):
        return ui.io.simple_input()   
    

class unsynch_files:
   
    def synch_all_files(self, FROM, TO):
        '''
        Функция синхронизирования
        '''
        os.chdir(FROM)
        ui.io.simple_print(SEARCHING_UNSYNCHRONIZED_OBJECTS_FROM)
        FROMFiles = self.list_files(FROM)
        ui.io.simple_print(SEARCHING_UNSYNCHRONIZED_OBJECTS_TO)
        TOFiles   = self.list_files(TO)
       
        synFiles = self.unsynch_files(FROMFiles, TOFiles)
        ui.io.simple_print(SYNCHRONIZATION_STARTED)
        os.chdir(FROM)
        for sf in synFiles:
            ui.io.simple_print(FILE_SYNCHING, sf)
            name = sf[1:]
            try:
                shutil.copyfile(sf, TO+name)
            except FileNotFoundError:
                dirPosition = name.rfind('/')
                thisDir = name[:dirPosition:]
                os.mkdir(TO+thisDir)
                shutil.copyfile(sf, TO+name)

        ui.io.simple_print(SYNCHRONIZATION_FINISHED)


    # Выбирает несинхронизированные объекты
    def unsynch_files(self, FROMFiles, TOFiles):
        unsynched = []
        for m in FROMFiles:
            b = True
            for p in TOFiles:
                if (m == p):
                    b = False
            if b == True:
                unsynched += [m]
            
        return unsynched

    # Возвращает список всех файлов в данной директории
    def list_files(self, filesPath):
        os.chdir(filesPath)
        filesList = []
        
        for location, dirs, files in os.walk("."):
            for nm in files:
                filesList.append(os.path.join(location, nm))
        
        return filesList

	    
	        
