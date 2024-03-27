import os # operating system

#description0 = []
#description1 = []

#n = 0

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as file: #read 也是需要相同的編碼方可讀取出正確的資料內容
		for line in file:
			if '商品,價錢' in line: #Boolean->True或是Fail 
				continue #滿足上述boolean值 Continue繼續表示直接進入'line #1'
			#a = line.split(',') # split為分割，並已',' 作為區分的指標
			#print('這是a的，line中第',n + 1, a)
			#print('----------------')
			#b = line.strip().split(',') # 注意執行順序 #1將line中移除\n；#2 再以','作為區分；#3 最後再存入 a str字串中。
			#print('這是b的，line中第',n + 1, b)
			#print('----------------')
			name, price = line.strip().split(',') # 得知透過strip()與split已','作為區分後，line已經被拆分為[0], [1]清單，我們透過name, price 宣稱 = [0], [1] 
			products.append([name, price]) #根據filename孔所投入的parameters，如product.csv。 並將檔案內容存入products清單中。
			#n += 1
	return products #程式設計上，若已有既有檔案，可表示products是有必要回傳。
	print(products)

# 使用者輸入
def user_import(products): #我們要對既有products[]要繼續新增，就必須增加"products" parameter好讓使用者能輸入
	while True: #強制進入loop環節；(boolen-> True or fail)
		name = input('商品名稱: ')
		if name == 'q':
			break # 當再商品紀錄: 輸入'q'時，會執行break 離開loop
		price = input('商品價錢: ')
		products.append([name, price]) # 完成使用者新增至products中item與price
	return products #再將"使用者新增"回傳至較新products

#印出products
def print_products(products):
	for p in products:
		print(p[0], '價格是', p[1])

#分別寫入.csv file
def write_file(filename, products): # 因為是寫入，一定包含.csv file與要寫入的內容，固需要兩個parameters
	with open(filename, 'w', encoding = 'utf-8') as file: #1 將'wp1.csv'作為file稱呼，隨著with open結束 file定義也release。 
	                                                      #2 encoding = 'utf-8 '將其內容已utf-8編碼類型寫入csv之中，
	                                                      # 當然excel內建初始設定非'utf-8'所以繁體中文會呈現???
		file.write('商品,價錢\n') # cvs row1 先寫入'商品'與'價錢' 並用comma來column區分
		for product in products:
			file.write(product[0] + ',' + product[1] + '\n')

#
def main(filename):
	filename = 'products.csv'
	products = []  # 初始化products為空列表
	if os.path.isfile(filename):
		products = read_file(filename) #"為何有products =" 因為read_file function讀取了csv內容，同時設計概內上，是要回傳並讓背景保留該資訊。
										 #為了能在同一個[]清單內結果繼續編輯，故將'products ='放置前面
		print('file exist')
	else:
		print('file unexist')
	products = user_import(products) #為了能在同一個[]清單內結果繼續編輯，故將'products ='放置前面
	print_products(products)
	write_file('products.csv',products)

main('products.csv')