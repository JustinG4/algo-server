import appscript
import time

def createSession():
    script_0 = "ssh root @170.187.143.231 && docker-compose up -d"
    appscript.app('Terminal').do_script(script_0)  # or any other command you choose

def startGUI():
    script_2 = "open -n -a 'Google Chrome' --args --new-window 'http://170.187.143.231:8080/trade'"
    appscript.app('Terminal').do_script(script_2)  # or any other command you choose

createSession()
time.sleep(5)
startGUI()