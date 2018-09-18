import random
import string

def numberplate():
    letters = string.ascii_uppercase
    minus_i = letters.replace("I","")
    firstnumberlist = [0,1,5,6]
    firstnumber = random.choice(firstnumberlist)
    if firstnumber in [1,5]:
        secondnumber = random.randrange(0,10)
    if firstnumber == 0:
        secondnumber = random.randrange(2,10)
    if firstnumber == 6:
        secondnumber = random.randrange(0,9)
    firstletters = ''.join([random.choice(minus_i) for n in range(0,2)])
    lastletters = ''.join([random.choice(minus_i) for n in range(0,3)])
    print('{}{}{} {}'.format(firstletters, firstnumber, secondnumber, lastletters))
    
numberplate()


def numberplate2(size=7, chars=string.ascii_uppercase.replace("I","") + string.digits):
    plate = ''.join(random.choice(chars) for x in range(size))
    print(plate)    
        
numberplate2()


import string
import random

def numberplate3():
    totalrange = list(range(2,20))+list(range(51,70))
    totalletters = 'ABCDEFGHJKLMNPRSTUVWXYZ'
    plate1 = ''.join(random.choice(totalletters) for x in range(2))
    plate2 = format(random.choice(totalrange),'02')
    plate4 = ''.join(random.choice(totalletters) for x in range(3))
    print(plate1+plate2, plate4)

numberplate3()
