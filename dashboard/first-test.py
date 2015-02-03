__author__ = 'Tim'
import cv2

vc = cv2.VideoCapture()

if not vc.open(0):
    print "no cam"
    exit(1)

while cv2.waitKey(30) <= 0:
    success, img = vc.read()
    if not success:
        break

    cv2.imshow("Testcam", img)
    k = cv2.waitKey(10)
    if k == 27:
        cv2.destroyAllWindows()


