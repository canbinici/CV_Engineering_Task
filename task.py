
import cv2

def function(main_image, small_image):

    image = cv2.imread(main_image)
    sub_image = cv2.imread(small_image)
    h, w = image.shape[:2]
    s_h, s_w = sub_image.shape[:2]
    
    histogram = cv2.calcHist([sub_image], [0], None, [256], [0, 256])
    
    for i in range((h-s_h+1)):
        for j in range((w-s_w+1)):
        
            roi = image[0 + i:s_h + i, 0 + j:s_w + j]
            histogram_temp = cv2.calcHist([roi], [0], None, [256], [0, 256])
            number1 = 0 + i
            number2 = s_h + i
            number3 = 0 + j
            number4 = s_w + j
            filename = '%d-%d.row & %d-%d.column.png' % (number1, number2, number3, number4)
        
            hist_histtemp = cv2.compareHist(histogram, histogram_temp, cv2.HISTCMP_CORREL)
        
            if hist_histtemp == 1:
                print(filename)
                cv2.imwrite(filename, roi)
                break
        
        
function('StarMap.png', 'Small_area.png')

