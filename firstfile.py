def load(self,filename="input.txt"):
    FILE = open(filename)
    s= FILE.read()
#    print s
#    with open(filename,"r") as f:
#        for line in f:
#            print(line.strip())
    fizz = s.split()[0]
    buzz = s.split()[1]
    e = s.split()[2]
#    print e
    i =1
    while i < int(e):
        if i%int(fizz) is 0:
            print "F"
            i+=1
        elif i%int(buzz) is 0:
            print "B"
            i += 1
        elif i%(int(fizz) and int(buzz)) is 0:
            print "FB"
            i+= 1
        else:
            print i
            i += 1
load(file)