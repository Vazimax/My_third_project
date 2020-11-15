def multiplication_project() :
    print("Enter the first number and the last number of the multiplication table ")

    start = int(input("Enter the first number of the table :"))
    end = int(input("Enter the last number of the table :"))

    for x in range(start,end+1):
        for y in range(start,end+1):
            print(x,"X",y,"=X",x*y)
        print("------------------")