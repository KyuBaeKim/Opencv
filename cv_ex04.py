#웹 서버 연결
import cv2
cap = cv2.VideoCapture('http://172.30.1.53:4747/video') # ip camera(Web cam) -mjpeg jpg 사진을 연속해서 계속 보여주는것
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)

while True:
    retval, frame = cap.read() # 프레임 캡쳐
    if not retval: break
    
    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)
    if key == 27: break     #Esc 누른 경우 루프 탈출
    
if cap.isOpened(): 
    cap.release()
    
cv2.destroyAllWindows()