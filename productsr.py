products=[]
with open('products.csv','r') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        name, price=line.strip().split(',')
        products.append([name,price])
print(products)