from os import name
import cv2
import time
import random
import dropbox
from dropbox.files import WriteMode

start_time = time.time()


def take_snapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        imageName = "image"+ str(number) + ".png"
        cv2.imwrite(imageName,frame)
        start_time = time.time()
        result = False
    return imageName
    videocaptureobject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = 'GlPcIk_3N_8AAAAAAAAAAU3GVT-Fx6IuwnqPCychv7jwhemU1mLQhieOmUAg8hyV'

    file_from = imageName
    file_to = '/test/' + imageName

    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,WriteMode.overwrite)

def main():
    while(True):
        if (time.time() - start_time >= 30):
            name = take_snapshot()
            upload_file(name)

main()