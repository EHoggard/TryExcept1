#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
    #print(x)

#for x in "banana":
    #print(x)

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
    #print(x)
    #if x == "banana":
        #break

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
    #if x == "banana":
        #break
    #print(x)


#count = 5
#while count > 0:
    #print(count)
    #count -= 1

#def nameoffunction(name,count):
    #print('%s called function with count %d' % (name,count))
    ##print(name * count)

#nameoffunction("Ebonnee",34)
#nameoffunction("Phillip",35)
#nameoffunction("Bailee",5)

#Dictionary Methods
#Method 1

Dictionaryone = {
    'Key1':'Value1',
    'Key2':'Value2',
    'Key3':'Value3'
}

print(Dictionaryone)

#Method 2

Dictionarytwo = {}

Dictionarytwo['key4'] = 'value4'
Dictionarytwo['key5'] = 'value5'
Dictionarytwo['key6'] = 'value6'

print(Dictionarytwo)

del Dictionarytwo["key4"]
print(Dictionarytwo)

Dictionaryone.pop('Key1')
print(Dictionaryone)

for key,value in Dictionaryone.items():
    print("I have " + key + " relating with " + value)