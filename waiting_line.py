#here's to generate me a number that always going up
'''class number_generator():
    def generate_number():
        self.count = 0
        self.caller = str'''
#killed this class because it makes no sense on this code
#but i am storing here just in case
def user_input():
        reset_point = 3
        count = 0 
        while True:
            #try:
                user = str(input("Tirar senha Y Cancelar N: ")).lower().strip()
                if user == "y":
                    #count in range(0,100)y  
                    user = print(f"Your current number {count}")
                    count +=1                
                if count >= reset_point:
                    print(f"Reseting counting {count}")
                    #count = 0
                    count +=1
                if user == "n": 
                    break
                else:
                     print("Digite Y ou N")
        '''except ValueError:
                 print("Para imprimir uma senha pressione Y se nao deseja pegar uma, pressione N")
            return user''' 

user_input()        
#number_generator()
