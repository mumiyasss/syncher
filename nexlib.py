# Библиотека для unix-подобных
import os
import shutil



def synching(MOB, PC, SYN_DEVICE):
    '''
    Функция синхронизирования
    '''
    os.chdir(MOB)
    print("Поиск несинхронизированных объектов...")
    MOBFiles = list_files(MOB)
    PCFiles  = list_files(PC)
   
    synFiles = unsynch_files(MOBFiles, PCFiles, SYN_DEVICE)
    print("Синхронизация...")
    os.chdir(MOB)
    for sf in synFiles:
        print("Синхронизация: ", sf)
        name = sf[1:]
        shutil.copyfile(sf, PC+name)
    print("Синхронизация завершенна.\n\n")


def get_config(CONFIG_FILE_NAME):
    """
        Считывает файл настроек, и записывает в список 'config'
    """
    try:
        confFile = open(CONFIG_FILE_NAME, 'r')
        config = [line.strip() for line in confFile]
        return config
    except Exception:
        return None


def set_config(CONFIG_FILE_NAME):

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
    
    ### Создаем файл настроек
    confFile = open(CONFIG_FILE_NAME, 'w')
    devlist = [MOB, PC, SYN_DEVICE]
    for dev in devlist:
        confFile.write(dev + "\n")
        
    return [MOB, PC, SYN_DEVICE]



# Выбирает несинхронизированные объекты
def unsynch_files(MOBFiles, PCFiles, SYN_DEVICE):
    unsynched = []
    for m in MOBFiles:
        b = True
        for p in PCFiles:
            if (m == p):
                b = False
        if b == True:
            unsynched += [m]
        
    return unsynched



# Возвращает директорию синхронизации
def device_choose():
    os.chdir('/run/user/1000/gvfs/')
    allFiles = [] 
    allFiles = os.listdir(path=".")
        
    numFolder = 0
    for device in allFiles:

        numFolder += 1;
        print(str(numFolder) + ") " + device)
    devChoose = input()
    os.chdir(allFiles[int(devChoose) - 1])
    os.chdir('Внутренняя память')
    folder = input("Пропишите путь на устройстве: ")
    os.chdir(os.getcwd()+folder)
    currentDir = os.getcwd()
    return currentDir




# Возвращает путь директории бэкапа
def backup_directory():
    way = input()
    """
    #Создание директории бэкапа в Документах
    try:
        os.mkdir(way, mode=0o777, dir_fd = None)
    except FileNotFoundError:
        print("Не правильно задана директория")
    except OSError:
        print("Ошибка связанная с системой")  #Дополнить исключения
    """
    return way



# Возвращает список всех файлов в данной директории
def list_files(filesPath):
    print("Собираю список файлов...")
    os.chdir(filesPath)
    filesList = []
    
    for location, dirs, files in os.walk("."):
        for nm in files:
            filesList.append(os.path.join(location, nm))
    
    return filesList
