class Car: 
    def __init__(self, name, year, hp):
        self.name = name
        self.year = year
        self.hp = hp

    def print_my_car(self):
        print(
            "Name: " , self.name ,"\n",
            "Year: ", self.year,"\n",
            "HP:   " ,self.hp)
    



myCar = Car("Tesla", "2020", "600")

myCar.print_my_car()