
import cv2
import numpy as np
import math


True_Value = 0

red = 1
blue = 0
color = blue

def Get_Value():
    return True_Value

def Blak_White(img):

    black = 0
    white = 0
    if img is not None:

        # print("img.shape=",img.shape)

        ratio = img.shape[0] / 50.0
        rate = img.shape[1] / img.shape[0]


        # print("rate=", rate)
        if rate < 0.4 or rate >2 :
            print("rate=",rate)
            return 0
        Len = rate * 20.0
        img = img.copy()
        # print("len=",int(Len))
        img = cv2.resize(img, (int(Len), 20))
        # cv2.imshow("img",img)


        # cv2.imshow("img", img)
        x, y = img.shape
        # print("x=",x,"y=",y)
   
        for i in range(x):
            for j in range(y):
                if img[i, j] == 0:
                    black += 1
                else:
                    white += 1



    if white>(black/10):
        return 1
    else:return 0



def Video_Init(color):

    cap = cv2.VideoCapture()
    cap.open(0)
    if not cap.isOpened():
        print("Failed to open camera")
        exit()
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        exit()

 
    lower_red = np.array([-2, 43, 46])
    upper_red = np.array([12, 255, 255])
    lower_red_1 = np.array([168, 43, 46])
    upper_red_1 = np.array([182, 255, 255])
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([90, 255, 255])
    lower_yellow = np.array([23, 43, 46])
    upper_yellow = np.array([37, 255, 255])
    lower_blue = np.array([93, 43, 46])
    upper_blue = np.array([123, 255, 255])




    
    while(True):
        flag = 0
        flag_blue = 1
        flag_red = 1
        flag_color = 0
        while(flag != 1 ):
            # cv2.waitKey(10)
            if color == blue:
                if flag_blue == 1 :

                    ref, frame = cap.read()
                    ratio = frame.shape[0] / 500.0
                    rate = frame.shape[1] / frame.shape[0]
                    Len = rate * 500.0
                    orig = frame.copy()
                    frame = cv2.resize(frame, (int(Len), 500))
                    # print(frame.shape)

                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


                    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
                    gray = mask_blue
                    gray = cv2.bitwise_not(gray)


                    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


                    contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]

                    rectangles = []
                    diff = []
                    diff_min = 99999
                    x = y = w = h = 0
                    flag = 0
                    for i in range(len(contours)):
           
                        if len(contours[i]) < 4:
                            continue
                        area = cv2.contourArea(contours[i])
                        if (area > 1000) & (area < 35000):
                            flag = 1
                            x, y, w, h = cv2.boundingRect(contours[i])
                            # print("area = ", area)
                            ho, s, v = hsv[y + int(h / 2), x + int(w / 2)]
                            diff = math.sqrt(
                                (abs(100 - ho) * abs(100 - ho) + abs(169 - s) * abs(169 - s) + abs(123 - v) * abs(159 - v)))
                            # print("diff = ", diff)
                            if diff < diff_min:
                                x_min = x
                                y_min = y
                                w_min = w
                                h_min = h

                    if flag == 0:
                        flag_blue = 0
                    else:
                        flag_blue = 1
                    # cv2.imshow("frame", frame)

                if flag_blue == 0 :
 
                    ref, frame = cap.read()
                    ratio = frame.shape[0] / 500.0
                    rate = frame.shape[1] / frame.shape[0]
                    Len = rate * 500.0
                    orig = frame.copy()
                    frame = cv2.resize(frame, (int(Len), 500))
                    # print(frame.shape)


                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


                    mask_red = cv2.inRange(hsv, lower_red, upper_red)
                    mask_red_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
                    gray = mask_red + mask_red_1


                    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

                    contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]


                    rectangles = []
                    diff = []
                    diff_min = 99999
                    x = y = w = h = 0
                    flag = 0
                    for i in range(len(contours)):
      
                        if len(contours[i]) < 4:
                            continue
                        area = cv2.contourArea(contours[i])
                        if (area > 1000) & (area < 35000):
                            flag = 1
                            x, y, w, h = cv2.boundingRect(contours[i])
                            # print("area = ", area)
                            ho, s, v = hsv[y + int(h / 2), x + int(w / 2)]
                            diff = math.sqrt(
                                (abs(173 - ho) * abs(173 - ho) + abs(253 - s) * abs(253 - s) + abs(138 - v) * abs(138 - v)))
                            # print("diff = ", diff)
                            if diff < diff_min:
                                x_min = x
                                y_min = y
                                w_min = w
                                h_min = h
                
                    if flag == 0:
                        flag_blue = 0
                        flag_color = 0
                    else:
                        flag_blue = 1
                        flag_color = 1
                    # cv2.imshow("frame", frame)

            if color == red:
                if flag_red == 1:

                    ref, frame = cap.read()
                    ratio = frame.shape[0] / 500.0
                    rate = frame.shape[1] / frame.shape[0]
                    Len = rate * 500.0
                    orig = frame.copy()
                    frame = cv2.resize(frame, (int(Len), 500))
                    # print(frame.shape)


                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     
                    mask_red = cv2.inRange(hsv, lower_red, upper_red)
                    mask_red_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
                    gray = mask_red + mask_red_1


                    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

                    contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]

          
                    rectangles = []
                    diff = []
                    diff_min = 99999
                    x = y = w = h = 0
                    flag = 0
                    for i in range(len(contours)):

                        if len(contours[i]) < 4:
                            continue
                        area = cv2.contourArea(contours[i])
                        if (area > 1000) & (area < 35000):
                            flag = 1
                            x, y, w, h = cv2.boundingRect(contours[i])
                            # print("area = ", area)
                            ho, s, v = hsv[y + int(h / 2), x + int(w / 2)]
                            diff = math.sqrt(
                                (abs(173 - ho) * abs(173 - ho) + abs(253 - s) * abs(253 - s) + abs(138 - v) * abs(138 - v)))
                            # print("diff = ", diff)
                            if diff < diff_min:
                                x_min = x
                                y_min = y
                                w_min = w
                                h_min = h

                    if flag == 0:
                        flag_red = 0
                    else:
                        flag_red = 1

                if flag_red == 0:

                    ref, frame = cap.read()
                    ratio = frame.shape[0] / 500.0
                    rate = frame.shape[1] / frame.shape[0]
                    Len = rate * 500.0
                    orig = frame.copy()
                    frame = cv2.resize(frame, (int(Len), 500))
                    # print(frame.shape)


                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

           
                    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
                    gray = mask_blue
                    gray = cv2.bitwise_not(gray)

           
                    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

              
                    contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]

             
                    rectangles = []
                    diff = []
                    diff_min = 99999
                    x = y = w = h = 0
                    flag = 0
                    for i in range(len(contours)):
                 
                        if len(contours[i]) < 4:
                            continue
                        area = cv2.contourArea(contours[i])
                        if (area > 1000) & (area < 35000):
                            flag = 1
                            x, y, w, h = cv2.boundingRect(contours[i])
                            # print("area = ", area)
                            ho, s, v = hsv[y + int(h / 2), x + int(w / 2)]
                            diff = math.sqrt(
                                (abs(100 - ho) * abs(100 - ho) + abs(169 - s) * abs(169 - s) + abs(123 - v) * abs(159 - v)))
                            # print("diff = ", diff)
                            if diff < diff_min:
                                x_min = x
                                y_min = y
                                w_min = w
                                h_min = h

                    if flag == 0:
                        flag_red = 0
                        flag_color = 0
                    else:
                        flag_red = 1
                        flag_color = 1



      
        # print("diff_min = ", diff_min)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.imshow("frame", frame)
        # print(frame.shape)
        # print(x,y,w,h)

        flag_truth = 0
        if color == blue :
            if flag_color == 1 :
                flag_truth = 0
            else:flag_truth = 1
        elif color == red :
            if flag_color == 1 :
                flag_truth = 0
            else:flag_truth = 1
        if flag_truth == 1 :
     
            new_frame = frame.copy()
            new_frame = new_frame[y + 3:y + h - 3, x + 3:x + w - 3]
            ratio = new_frame.shape[0] / 500.0
            rate = new_frame.shape[1] / new_frame.shape[0]
            Len = rate * 500.0
            new_frame = new_frame.copy()
            new_frame = cv2.resize(new_frame,(int(Len),500))
            new_frame = new_frame[20:-20, 20:-20]
            # cv2.imshow("new_frame", new_frame)
            # print("new_frame.shape",new_frame.shape)


            hsv = cv2.cvtColor(new_frame, cv2.COLOR_BGR2HSV)
            # print("hsv.shape = ",hsv.shape)


            flag_rate = 1
   
            if flag_rate == 1:
   
                mask_green = cv2.inRange(hsv, lower_green, upper_green)
                # ShapeDetection(mask_green)
                # mask_green = mask_green[20:-20, 200:-200]
                # cv2.imshow("mask_green", mask_green)
                # print("mask_green.shape = ", mask_green.shape)
                print("Green_BW")
                flag_rate = Blak_White(mask_green)
                # print(mask_green.shape)
                # print("flag_rate=",flag_rate)
                if flag_rate == 1:
                    if color == red:
                        flag_truth = 1
                    if color == blue:
                        flag_truth = 0
                else :
                    flag_truth = 0

          
            if flag_rate != 1:
                mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

                # ShapeDetection(mask_yellow)
                # mask_yellow = mask_yellow[20:-20, 200:-200]
                # cv2.imshow("mask_yellow", mask_yellow)
       
                print("Yellow_WB")
                flag_rate = Blak_White(mask_yellow)
                print("flag_rate=", flag_rate)
                if flag_rate == 1:
                    if color == red:
                        flag_truth = 0
                    if color == blue:
                        flag_truth = 1
                else :
                    flag_truth = 0

        if flag_truth == 1:
            True_Value = 1
 
            # print(True_Value)
            # return True_Value
        else:
            True_Value = 0
       
            # print(True_Value)
            # return True_Value
        # cv2.imshow("frame", frame)
        # cv2.imshow("mask_green", mask_green)
        # cv2.imshow("mask_yellow", mask_yellow)
        cv2.waitKey(50)
Video_Init(blue)
t = Get_Value()