我们计算BMI指数，计算一个人是否健康
BMI = 80.5/(1.75**2)
if BMI < 18.5:
	print ('过轻')
elif 25 > BMI  >18.5:
	print('正常')
elif 28 > BMI > 25:
	print('过重')
elif 32>BMI >28:
	print('偏胖')
else :
	print('严重肥胖')
