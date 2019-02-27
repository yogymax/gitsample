listOfElements1 = [10,20,30,40,50]
listOfElements2 = [100,200,300,400,500]

for i in range(10):
    print(i)

for item in range(5):
    print()
    for val in range(5):

            if item==0 and (val==0 or val==4):
                print('*', end='        ')
            elif  item==1 and (val==1 or val==3):
                print('*', end='        ')
            elif  item==2 and (val==2):
                print('*', end='        ')

