import os #operating system


def read_file(filename):
    products=[]
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name,price=line.strip().split(',')
            # print(s)
            products.append([name,price])
    return products
            



#讓使用者輸入
def user_input(products):
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
    return products
    # print(products[0][0])
#印出所有購買紀錄
def print_products(products):
    for product in products:
        print(product[0],'的價格是',product[1])
#寫入檔案
def write_file(filename,products):
    with open(filename,'w', encoding='utf-8') as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0]+','+str(p[1])+'\n')
# data=[1,3,5,7,9]
# with open("test.txt","w") as f:
#     for d in data:
#         f.write(str(d)+'\n')
#         print(d)
def main():
    filename='produects.csv'
    if os.path.isfile(filename):
        print("yeah!找到檔案了!")
        products=read_file(filename)
    else:
        print("找不到檔案……")
    products=user_input(products)
    print_products(products)
    write_file('produects.csv',products)
main()