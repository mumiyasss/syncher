#! /usr/bin/python3.5

import ui
import logic

def main():
    #interf = ui.interface();
   # interf.conf.set_config()
    configuration = logic.config_connection()
    configuration.tempDevice.temp_func();


if __name__ == '__main__':
    main()
    
