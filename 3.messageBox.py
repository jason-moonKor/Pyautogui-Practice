import pyautogui as aa


# b1 = aa.alert('경고','aaa','bbb') #b1 = aa.alert(text='경고',title='aaa',button='bbb')
# print(b1)
# print(type(b1))

# b2 = aa.confirm('Test') # (text='경고',title='aaa',button=['1','2']) 버튼갯수 상관없이 넣을수있음
# print(b2)
# print(type(b2))
# if(b2 == 'OK'):   #변수안에 넣을수있는게 장점
#     print('OK입니다')

# b3 = aa.prompt(title='TITLE', default='여기에 쓰세요') #title='TITLE', default='여기에 쓰세요', text='이것은 제목'
# print(b3) #Ok를 누를때 프롬프트창에 들어가있는 텍스트가 입력됨 Cancel = None 값 들어감

b4 = aa.password('패스워드를 치세요','비밀번호 입력창',mask='$') #보기에만 안보여지고 내부상으론 똑같이 돌아가서 보안이 좋아지는건 아님
# print(b4)
# print(type(b4))
if b4 == '1234':
    print("오케이")
else:
    print("비밀번호틀림")