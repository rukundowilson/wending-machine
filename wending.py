#wending machine
_=input('press enter to see use regulatories:')
notice='''NOTICE
THERE is no refund try matching our disired prices
we accept 5,15 and 25 cents
'''
print(notice)
coins=[5,15,25]
current=0
cost=50
while True:
    try:
          coin=int(input("enter the coin:"))
          if coin in coins:
            current=current+coin
            print('the amount due is',current)
          else:
               print('invalid cent.try 5,15 or 25cents to proceed')
          if current==cost:
              break
          if current>=cost:
              print("the amount is over the cost")
              extra=current-cost
              print(' can derivered successfully. the cost is 50','extra amount is',extra,'cents')
              a='''the amount you inserted is beyond {} the cost 
              try inserting other coins to reach the cost to get another can'''
              current=extra
              print(a.format(extra))
              print('new amount due is',current)
    except:
        print("wrong data try 5,15 or 25cents to proceed")
print('can derivered. ',"cost",current)
        