from qreader import QReader
import cv2
qreader = QReader()

image = cv2.cvtColor(cv2.imread("test.png") , cv2.COLOR_BGR2RGB)

decoded_text= qreader.detect_and_decode(image = image)
print(decoded_text)
