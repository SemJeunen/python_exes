import os, cv2, datetime,time

cam = cv2.VideoCapture(0)
if os.path.exists("images") != True:
    os.mkdir("images")

for i in range(0,10):
    ret, frame = cam.read()
    cv2.imwrite(f"images/{datetime.date.today()}-{i}.png", frame)
    time.sleep(60)


os.system("git add .")
os.system("git commit -m 'images-result'")
os.system("git push")