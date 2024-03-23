d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300},{'item': 'item1', 'amount': 750}]
s=dict(d)
s.clear()
s["item1"] = 1150
s["item2"] = 300
print(s)


d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
d1={}
for i in d:
    if i['item'] in d1.keys():
        d1[i['item']]+=i['amount']
    else:
        d1[i['item']]=i['amount']
print(d1)  
    