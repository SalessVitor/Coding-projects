#here's to generate me a number that always going up
class number_generator():
    def generate_number(self):
        self.count = 0
        self.caller = str

    def user_input():
        reset_point = 101
        count = 0
        user = str(input("Tirar senha Y Cancelar N: ")).lower().strip()
        while True:
            try:
                if user == "Y":
                        print(f"Your current number {count}")
                        count =+ 1
                elif count >= reset_point:
                    print("Reseting counting")
                elif user == "N": 
                    break
            except ValueError:
                 print("Para imprimir uma senha pressione Y se nao deseja pegar uma, pressione N")

    user_input()        
number_generator()
