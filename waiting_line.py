#here's to generate me a number that always going up
def user_input():
        #storing the values so it knows how many to generate and to reset the counting point
        reset_point = 3
        reset_value = 0
        count = 0 
        while True:
                #opening a loop so it can print as many numbers as the user input | with a limit
                user = str(input("Tirar senha Y Cancelar N: ")).lower().strip()
                match user:
                    case 'y':
                        user == "y" 
                        print(f"Your current number {count}")
                        count +=1 
                    case 'n' : 
                        user == "n"
                        print("Muito obrigado pela preferência volte sempre")
                        break
                    case _ :
                          print("Digite Y para imprimir N para cancelar")
                                              
#this is where it reset the values that's the reason why i give a value to count store a value | so it stores the reset value and then when it reaches the reset point (the limit) it calls the count as 0 basically reseting the value            
                if count >= reset_point: 
                    count = reset_value
                    # print(f"Reseting counting {reset_value}") # it's a back-end it doesn't need to print the reset point
user_input()        