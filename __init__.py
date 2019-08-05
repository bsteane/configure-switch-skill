import paramiko 
import time 
import getpass 
import os 

#from host_file import network_devices 
#from config_file import host_conf
from mycroft import MycroftSkill, intent_file_handler 

__author__ = "bsteane" 

class ConfigureSwitch(MycroftSkill): 
    
    def __init__(self): 
        MycroftSkill.__init__(self) 

    @intent_file_handler('switch.configure.intent') 
    def handle_switch_configure(self, message): 
        ip = "192.168.0.200" 
        twrssh = paramiko.SSHClient() 
        twrssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        twrssh.connect(ip, port=22, username="cisco", password="cisco") 
        remote = twrssh.invoke_shell() 
        remote.send('term len 0\n')
        remote.send('en\n') 
        remote.send('cisco\n')
        remote.send('conf t\n')
        remote.send('int g0/1\n') 
        remote.send('desc ben your in\n') 
        time.sleep(1) 
        twrssh.close()
        self.speak_dialog('switch.configure') 
 
def create_skill(): 
    return ConfigureSwitch()


