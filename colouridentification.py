import cv2,time
#sys.stdin.readline()
import numpy as np
video=cv2.VideoCapture(0)
a=0
s=True
a1s=0
while(a<1):
    a = a + 1
    check,frame=video.read()
    #print(check)
    #matrix= np.array(frame.getdata()).reshape(frame.size)
    sd=1
    #print(frame.shape[0],frame.shape[1])
    if s:
        se=1
        #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        for i in range (480):
            for j in range(640):
                b,g,r=frame[i][j]
                if(r>=190 and g>=60 and g<=180 and b<=50):
                    se+=j
                    sd+=1
                else:
                    grey=r*0.33+b*0.33+g*0.33
                    frame[i][j]=grey
              
        se=se//sd   
        print(se)
    cv2.imshow("capturing",frame)
    key=cv2.waitKey()
    if key==ord('q'):
        break
print(a)
video.release()
