import os, cv2, datetime,time

cam = cv2.VideoCapture(0)
def make_folder():
    if os.path.exists("images") != True:
        os.mkdir("images")

def take_photos():
    for i in range(0,10):
        ret, frame = cam.read()
        cv2.imwrite(f"images/{datetime.date.today()}-{i}.png", frame)
        time.sleep(60)



def push_github():
    os.system("git checkout -b 'log'")
    os.system("git add .")
    os.system("git commit -m 'image-result'")
    os.system("git push --set-upstream origin 'log'")
    os.system("git push")


make_folder()
take_photos()
push_github()