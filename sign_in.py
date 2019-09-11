password = 'a12345'
i = 3
while i >= 1:
    keyword = input('请输入密码：')
    if keyword == password:
        print('登录成功！')
        break
    else:
        i = i-1
        print('密码错误！你还有', i, '次机会。')
if i == 0:
	print('你已经用完了3次输入机会，账户已锁')