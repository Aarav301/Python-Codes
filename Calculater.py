#Calculater

while True:
    ans = input("Which of the following you have to select, +, -, x, /")
    num_1 = int(input("Enter first number"))
    num_2 = int(input("Enter second number"))

    Result = 0

    if ans == "+":
        Result = num_1 + num_2
    elif ans == "-":
        Result = num_1 - num_2
    elif ans == "x":
        Result = num_1 * num_2
    elif ans == "/":
        Result = num_1 / num_2
    else:
        print ("Invalid input")
    
    print ( "=", Result)
    




    
    
    
