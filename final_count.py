############################################
## Import OpenCV
import numpy as np
import cv2

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
cap  =  cv2.VideoCapture("test2.mp4")
i    =  1
cin  =  0
cout =  0
pre  =  0
prei =  800
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Video_output.mp4',fourcc,2, (680,720),1)
############################################

############################################
## Video Loop
while(1):
    ## Read the image
    ret, img = cap.read()
    ## Do the processing
    if ret:
        img=img[80:,100:]
        height, width, channels = img.shape
        img = cv2.medianBlur(img,5)

        dilation = cv2.dilate(img, kernel, iterations = 4)
        img = cv2.erode(dilation, kernel, iterations = 6)

        hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
        lower = np.array([0,0,27])
        upper= np.array([200,255,255])
        mask=cv2.inRange(hsv,lower,upper)

        def iscrossin(prei,cur):
            if(prei<width/2 and cur>width/2):
                return 1
            else:
                return 0
        def iscrossout(pre,cur):
            if(prei>width/2 and cur<width/2):
                return 1
            else:
                return 0
        ret,mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
        _,contours, hierarchy = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        n=len(contours)
        cnt=0
        m=0
        img = cv2.line(img, (width/2,0), (width/2,600), (0,0,255),4)
        for i in range(1,n):
                area=cv2.contourArea(contours[i])
                # print area
                if(area>10000 and area<25000):
                    m=area
                    # print m
                    cnt=i

                    M=cv2.moments(contours[cnt])
                    cx=int(M['m10']/M['m00'])
                    cy=int(M['m01']/M['m00'])
                    
                    x,y,w,h = cv2.boundingRect(contours[cnt])
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                    cur=cx
                    if(iscrossin(prei,cur)):
                        if(abs(prei-cur)<60):
                            cout+=1
                    elif(iscrossout(pre,cur)):
                        if(abs(pre-cur)<60):
                            cin+=1
                        else:
                            a=0
                    pre=cur
                    prei=cur
        ## Show the image
        IN="IN: "+str(cin)
        OUT="OUT: "+str(cout)
        cv2.putText(img,IN, (10, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(img,OUT, (10,100),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow('image',img)
        out.write(img)
        ## End the video loop
        cv2.waitKey(1)  
    else:
        break

## Close and exit
cap.release()
cv2.destroyAllWindows()

