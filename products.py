products=[]
with open("products.csv",'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        name,price=line.strip().split(',')
        # print(s)
        products.append([name,price])
print(products)

#讓使用者輸入
while True:
    name=input("請輸入商品名稱:")
    if name=='q':
        break
    price=input("請輸入商品價格:")
    price=int(price)
    # p=[]
    # p.append(name)
    # p.append(price)
    # p=[name,price]
    products.append([name,price])
print(products)
# print(products[0][0])
#印出所有購買紀錄
for product in products:
    print(product[0],'的價格是',product[1])
#寫入檔案
with open('products.csv','w', encoding='utf-8') as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0]+','+str(p[1])+'\n')
# data=[1,3,5,7,9]
# with open("test.txt","w") as f:
#     for d in data:
#         f.write(str(d)+'\n')
#         print(d)
