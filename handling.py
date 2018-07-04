
try:

    a=5
    b=8976
    c=b/0
    file=open("abc.txt")
    for line in file:
        print(line)


except Exception as e:
    print("some exception occurred :",e)
    print((dir(e)))     #shows directory of e 

#except FileNotFoundError:
    #print("File not found")

#except ZeroDivisionError:
    #print("can't divide by zero")