import platform,socket,re,uuid,json,psutil,logging
import os

#deze functie komt van: https://stackoverflow.com/questions/3103178/how-to-get-the-system-info-with-python
def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

 

with open('log.txt', 'w') as file:
    file.write(getSystemInfo())


os.system("git checkout -b 'sysinfo_log'")
os.system("git add log.txt")
os.system("git commit -m 'log'")
os.system("git push --set-upstream origin 'sysinfo_log'")
os.system("git push")