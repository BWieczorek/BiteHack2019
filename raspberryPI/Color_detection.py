import cv2
import numpy as np
import detection_fun as df

cap = cv2.VideoCapture(0)

decision_counter = 0
left_turn = 0
right_turn = 0
forward = 0

serial_device = df.UART_init()

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_color = np.array([30, 40, 140])
    upper_color = np.array([55, 255, 255])

    color_mask = cv2.inRange(hsv, lower_color, upper_color)

    contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    index = df.findBiggerArea(contours)

    if index != -1:
        contour = contours[index]
        if cv2.contourArea(contour) > 300:
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 10)
            frame = cv2.circle(frame, radius=5, center=(int(x+w/2), int(y+h/2)), color=(0, 0, 255), thickness=3)
            if x+w/2 <= 150:
                left_turn += 1
            elif 150 < x+w/2 <= 490:
                forward += 1
            else:
                right_turn += 1
            decision_counter += 1
    if decision_counter >= 25:
        decision_counter = 0
        if left_turn > forward and left_turn > right_turn:
            df.UART_print(serial_device, "Turn left") #change to df.UART_send_msg
        elif forward >= left_turn and forward >= right_turn:
            df.UART_print(serial_device, "Go Forward") #change to df.UART_send_msg
        elif right_turn > forward and right_turn > left_turn:
            df.UART_print(serial_device, "Turn right")#change to df.UART_send_msg
        left_turn = 0
        forward = 0
        right_turn = 0

    frame = cv2.line(frame, (150, 0), (150, 480), color=(0, 0, 255), thickness=2)
    frame = cv2.line(frame, (490, 0), (490, 480), color=(0, 0, 255), thickness=2)
    cv2.imshow("tracking", frame)



    k = cv2.waitKey(5) & 0XFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

