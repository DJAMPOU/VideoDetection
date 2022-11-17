import os
import detect
import cv2 as cv
if __name__ == '__main__':

    dir = 'part1'
    count = 0
    for file in os.listdir(dir):
        print(dir, "\\", file)
        count += 1

    print('\n nombre de fichier:', count)
    for file in os.listdir(dir):
        img = cv.imread(dir+"\\"+file)
        x, y, w, h, img = detect.face(img, for_='extrat')
        if x!=-1:
            sub_img = img[y:y+h, x:x+w]
            cv.imwrite("man\\"+str(count)+".jpg", sub_img)
        count -=1
        print("\n level:", count)
        cv.imshow("test", img)
        cv.waitKey(1)
