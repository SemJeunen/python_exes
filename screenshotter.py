import pyautogui, os, datetime,time


if os.path.exists("screenshots") != True:
    os.mkdir("screenshots")

for i in range(0,10):
    screenshot = pyautogui.screenshot()
    screenshot.save(f"screenshots/{datetime.date.today()}-{i}.png")
    time.sleep(60)

os.system("git checkout -b 'log'")
os.system("git add .")
os.system("git commit -m 'screenshot-result'")
os.system("git push --set-upstream origin 'log'")
os.system("git push")