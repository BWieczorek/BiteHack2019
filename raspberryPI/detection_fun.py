import cv2

def findBiggerArea(contours):
    index = -1
    area = 0
    var_index = 0
    for contour in contours:
        if(cv2.contourArea(contour) > area):
            index = var_index
            area = cv2.contourArea(contour)
        var_index += 1
    return index



