money = input("How much money do you have? ")
if money < 50000:
    print "You cannot buy an iPhone, minimum value should be 50000"
else:
    x = money / 50000 
    print "You can buy", x, "iPhones"
    y = money%50000 
    Wii  = 20000
    z = Wii - y
    print "You need an additional", z, "php to buy a Wii"
