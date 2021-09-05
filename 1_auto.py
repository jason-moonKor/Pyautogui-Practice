import pyautogui
import time

#pyautogui.position() #현재 마우스 위치 좌표알려줌
pyautogui.moveTo(1504, 168, 1)# x좌표, y좌표, 간격(초)

#pyautogui.click(clicks=2, interval=2) #2번클릭, 2초간격
pyautogui.doubleClick() #더블클릭

time.sleep(1)
pyautogui.typewrite('Hello') #키보드를 제어하는 코드
pyautogui.typewrite(['Ctrl']) #[]안에 넣으면 키를 누를수있음
