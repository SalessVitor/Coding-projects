#here's to generate me a number that always going up
def user_input():
        reset_point = 3
        reset_value = 0
        count = 0 
        while True:
                user = str(input("Tirar senha Y Cancelar N: ")).lower().strip()
                if user == "y":
                    user = print(f"Your current number {count}")
                    count +=1 
                else:
                     print("Digite Y ou N")
                if count >= reset_point:
                    reset_value 
                    print(f"Reseting counting {reset_value}")
                if user == "n": 
                    break
user_input()        