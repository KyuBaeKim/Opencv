# r을 누르면 녹화 시작
# s를 누르면 녹화 중지


from signal import pause
import cv2
from datetime import datetime
cap = cv2.VideoCapture(0) # 0번 카메라
frame_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

recorder = None # VideoWriter 객체 
recording_status = False # 녹화 중인지 여부 상태 변수

def start_record():
    global recorder, recording_status
    if recording_status: return
    start = datetime.now()
    fname = start.strftime('./data/%Y%m%d_%H%M%S.mp4') 
    recorder = cv2.VideoWriter(fname, fourcc, 20.0, frame_size) 
    print('start recoeding', fname)
    recording_status = True
    
def stop_record():
    global recorder, recording_status
    recording_status = False
    if recorder:
        recorder.release()
        recorder = None
    print('stop recoeding')

while True:
    retval, frame = cap.read() # 프레임 캡처 
    if not retval: break
    
    if recording_status: # 녹화중인 경우에만 처리 
        recorder.write(frame)
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(25)
    if key == ord('r') :
        start_record()
    elif key == ord('s'):
        stop_record() 
    elif key == 27: break # ESC
    
    
cap.release()
cv2.destroyAllWindows()
        