from itertools import count

from matplotlib.style import available

def checkout(items, cost):
    AddCart=[]
    price=0
    if len(items)==0:
        return 0
    else:
        for i in items:
            if i not in AddCart:
                AddCart.append(i)
                if i=="A":
                    count_A=items.count(i)
                    A3group = count_A//3
                    remain_A= count_A%3
                    price += A3group*130 + remain_A*50

                elif i=="B":
                    count_B=items.count(i)
                    B2group = count_B//2
                    remain_B= count_B%2
                    price += B2group*45 + remain_B*30

                else:
                    try:
                        price +=items.count(i)*cost[i]
                    except:
                        print("Item not present in dict")
            else:
                continue
    return price

cost = {
    "A":50,
    "B":30,
    "C":20,
    "D":15
}

items=input()
TotalCost=checkout(items, cost)
print(TotalCost)
