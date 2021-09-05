import pyautogui as aa

# i = aa.locateOnScreen()
# q = aa.center(i)
# aa.click(i)


# i = aa.locateCenterOnScreen('a.png') #한번에 센터값 추출
# aa.click(i)

#print(aa.position())
#aa.screenshot('7.png', region=(412,629,30,30)) #자동 스크린샷 제작

num7 = aa.locateCenterOnScreen('7.png')
num1 = aa.locateCenterOnScreen('1.png')

aa.click(num1)
aa.click(num7)
aa.click(num1)
aa.click(num7)
aa.click(num1)
aa.click(num7)
aa.click(num1)
aa.click(num7)
aa.click(num1)
aa.click(num7)





