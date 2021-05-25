data = []
count = 0
with open('reviews.txt', 'r') as f: #'r'為讀取模式;'w'為寫入模式。 # f為當作之後用來參考的file
	for line in f:
		data.append(line.strip())   #去掉字串前後多餘空格及換行符號/n
		count += 1 #快寫法
		if count % 1000 == 0:
			print(len(data))
print(len(data))
print(data[0])
print('-----------------------------')
print(data[1])