# 辨識人臉
# noinspection PyUnresolvedReferences
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read() # 捕捉影像資料
    print(ret, frame)

    # 顯示影像
    cv2.imshow('MyCam', frame)
    # 按下 q 離開
    # cv2.waitKey(1) 一個等待鍵盤輸入的涵式
    # 0xFF == ord('q') 獲取 q 的 ASCII
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
