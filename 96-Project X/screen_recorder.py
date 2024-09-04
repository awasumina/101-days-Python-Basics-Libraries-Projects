import cv2
import numpy as np # allows us to create a multidimensional arrays
from PIL import ImageGrab

def screen_recorder():
    
    # four character code(fourcc )
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))
    # 5.0 represents the frame rate 
    # other represents the resolution of your screen
    
    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        # open cv captures the image in BGR so we have to convert it into Corresponfing RGB color
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("ScreenRecoder", frame)
        out.write(frame) # write the frame in our screen
        
        if cv2.waitKey(1) == 27 : # if user presses key 'k' then recording will stop
            break  
        
    out.release()
    cv2.destroyAllWindows()  # destroy all the previously created window screen
    
screen_recorder()

