import cv2


def findBiggerArea(contours):
    index = -1
    area = 0
    var_index = 0
    for contour in contours:
        if (cv2.contourArea(contour) > area):
            index = var_index
            area = cv2.contourArea(contour)
        var_index += 1
    return index


def UART_init():
    return serial.Serial(
        port='/dev/serial0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )


def UART_print(socket, msg):
    try:
        socket.write(msg.encode())
        return 1
    except:
        print("Problem on sending UART occurs")
        return -1
