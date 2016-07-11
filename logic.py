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


########################################################        

class configConnection(generalProgramSettings):
    

    def __init__(self):
        self.update_program_path();
        self.update_config_file();

        #self._local_conf = self.get_config_from_file(self.get_config_file_path())
        #if not self._local_conf:
        self._local_conf = self.set_config_localy();
            #self.write_config_to_file(self.get_config_file_path(), self._local_conf);
            
            
    ##
    ## Operations with config from/with file of configuration
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## 

    def get_config_from_file(self, CONF):
	    '''
            Считывает файл настроек, и записывает в список
        '''
	    try:
	        self.confFile = open(CONF, 'r')
	        self.config = [line.strip() for line in confFile]
	        return self.config
	    except Exception:
	        return None
    

    def write_config_to_file(self, CONFIG_FILE_PATH, CONF_LIST_FROM_UI): 
        '''
            Записывает значения конфигурации
            в файл по пути CONFIG_FILE_PATH
        '''
        ### Открываем файл настроек
        self.confFile = open(self.get_config_file_path(), 'w')
        for dev in CONF_LIST_FROM_UI:
            self.confFile.write(dev + "\n")

    ##
    ## Operations with config localy in RAM
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
    def set_config_localy(self):

        print(WHERE_IS_FROM_DIR)
    ##########    from_dir = self.from_dir_choose()
        from_dir = "/home/kolya/MY"
        to_dir   = "/home/kolya/NEWPROJ"
        print(WHERE_IS_TO_DIR)
    ##########    to_dir   = self.to_dir_choose()
        
        return [from_dir, to_dir]
            
    
    def get_local_config(self):
        return self._local_conf;
    


    ##
    ## Choosing from/to destinations
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
    def from_dir_choose(self):
        return ui.io.simple_input()

    def to_dir_choose(self):
        return ui.io.simple_input()   
     


########################################################


class unsynch_files:
   
    def synch_all_files(self, FROM, TO):
        '''
        Функция синхронизирования
        '''
        os.chdir(FROM)
        print("Поиск несинхронизированных объектов...")
        FROMFiles = self.list_files(FROM)
        TOFiles   = self.list_files(TO)
       
        synFiles = self.unsynch_files(FROMFiles, TOFiles)
        print("Синхронизация...")
        os.chdir(FROM)
        for sf in synFiles:
            print("Синхронизация: ", sf)
            name = sf[1:]
            try:
                shutil.copyfile(sf, TO+name)
            except FileNotFoundError:
                dirPosition = name.rfind('/')
                thisDir = name[:dirPosition:]
                os.mkdir(TO+thisDir)
                shutil.copyfile(sf, TO+name)

        print("Синхронизация завершенна.\n\n")



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
        print("Собираю список файлов...")
        os.chdir(filesPath)
        filesList = []
        
        for location, dirs, files in os.walk("."):
            for nm in files:
                filesList.append(os.path.join(location, nm))
        
        return filesList
#########################################################

	    
	        
