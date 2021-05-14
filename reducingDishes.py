'''
with every iteration we are serving more and more dishes, and then calculating the satisfaction
'''

def reducingDishes(self,satisfaction):
    satisfaction = sorted(satisfaction,reverse=True)

    summi,result=0,0

    for val in satisfaction:
        summi += val
        if summi<0:
            break
        result += summi
    return result