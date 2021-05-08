f = open("Bailee.txt", "w+")
for i in range(10):
    f.write("I love Bailee %d\r\n" % (i+1))
f.close()