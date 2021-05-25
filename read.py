data = []
count = 0
with open('reviews.txt', 'r') as f: #'r'為讀取模式;'w'為寫入模式。 # f為當作之後用來參考的file
	for line in f:
		data.append(line)   #去掉字串前後多餘空格及換行符號/n
		count += 1 #快寫法
		if count % 100000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料。')

sum_len = 0
for d in data:
		sum_len += len(d)

print("留言的平均長度是", sum_len/len(data))