import pyzbar.pyzbar as pyzbar
import cv2
import matplotlib.pyplot as plt

# import tensorflow as tf

# 바코드 이미지 가져오기
src = cv2.imread("/Users/deep/Ryan_Repository/OpenCV/Project/img/bh_bar.jpg")
gray =cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


plt.imshow(src)
# cv2.imshow("src", src)

plt.imshow(gray, cmap='gray')
decoded = pyzbar.decode(gray)
print(decoded)

for d in decoded:
    print(d.data.decode('utf-8'))
    print(d.type)
    x, y, w, h = d.rect


    barcode_data = d.data.decode("utf-8")
    barcode_type = d.type

    cv2.rectangle(src, (d.rect[0], d.rect[1]), (d.rect[0] + d.rect[2], d.rect[1] + d.rect[3]), (0, 0, 255), 2)

    text = '%s (%s)' % (barcode_data, barcode_type)
    cv2.putText(src, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

# plt.imshow(src)
cv2.imshow('src', src)
# cv2.imshow("gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()