
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:  #for loop
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) 
print('檔案讀取完了，總共有', len(data),'筆資料') 

sum_len = 0
for d in data: #每一筆資料視為d
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data),'個字')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new), '筆留言長度小於100') #在for loop做完後再印出
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),'筆留言提到good')
#good = [d for d in data if 'good' in d]
#在data裡篩選，若有提到good的則原封不動裝進去good裡
#good = [1 for d in data if 'good' in d]，意即在data裡篩選，若有提到good的，則用1替代裝進去good裡
#bad = ['bad' in d for d in data]
#'bad' in d 中結果會是true或false，故bad裡會裝有一百萬筆資料，並檢查其中若有提到bad其結果為True，沒有提到結果為False
#bad = []
#for d in data
#	bad.append.('bad' in d)
print(good[0])