#here's to generate me a number that always going up
def user_input():
        #storing the values so it knows how much to generate and to reset the counting point
        reset_point = 3
        reset_value = 0
        count = 0 
        while True:
                #opening a loop so it can print as many numbers as the user input | with a limit
                user = str(input("Tirar senha Y Cancelar N: ")).lower().strip()
                match user:
                    case user == "y": 
                             print(f"Your current number {count}")
                             count +=1 
                    case user: 
                        user == "n":

                if count >= reset_point: #this is where it reset the values that's the reason why i give a value to count store a value | so it stores the reset value and then when it reaches the reset point (the limit) it calls the count as 0 basically reseting the value
                    count = reset_value
                    print(f"Reseting counting {reset_value}")
                    
                     
                    
                    break
                else:
                     print("Digite Y ou N")
user_input()        