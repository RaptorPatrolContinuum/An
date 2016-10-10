import datetime

now = datetime.datetime.now()


#2**30
for x in range(2**30):
    print(x)
final = datetime.datetime.now()
print ("Start date and time using str method of datetime object:")
print (str(now))
print ("Final date and time using str method of datetime object:")
print (str(final))

