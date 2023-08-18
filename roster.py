
class Roster:
    def __init__(self, name, number, height, skill):
        self.name = name
        self.number = number
        self.height = height
        self.skill = skill

players = [Roster("Cade Cunningham", 2, 6.8, "high"),
            Roster("Killian Hayes", 7, 6.5, "very low")]

players2 = [Roster("Frank Jackson", 5, 6.5, "medium"),
            Roster("Isaiah Stewart", 28, 6.9, "high"),
            Roster("Saddiq Bey", 41, 6.7, "high")]

print(players2[0].name, end=' ')
print('and his number is', players2[0].number)



class Arena:
    def __init__(self, seat_color, ice_wood):
        self.seat_color = seat_color
        self.ice_wood = ice_wood
    
        def decision(self): 
            if self.ice_wood == "ice":
                print("Hockey")
            elif self.ice_wood == "wood":
                print("Basketball")
            elif self.seat_color == "red" and self.ice_wood == "ice":
                print("Hockey")
            elif self.seat_color == "red" and self.ice_wood == "wood":
                print("Neither")
            elif self.seat_color == "black" and self.ice_wood == "ice":
                print("Neither")
            elif self.seat_color == "black" and self.ice_wood == "wood":
                print("Basketball")
            else:
                print("Neither")
     
     
Red_Wings = Arena("red", "ice")
Pistons = Arena("black", "wood")
Tigers = Arena("green", "turf")

print(Pistons.seat_color, end=' ')
print(Pistons.ice_wood)


class School:
    def __init__(self, type, courses):
        self.type = type
        self.courses = courses

    def display(self):
        print(self.type)
        print(self.courses)

    remote = "online"

class Learning(School):
    def __init__(self, type, courses, city):
        School.__init__(self, type, courses)
        self.city = city
        self.type = type
        self.courses = courses
       
    def getCity(self):
        return self.city
        """Idk"""

    def getType(self):
        return self.type

Macomb = Learning("community college", "IT", 'warren')
Oakland = Learning('university', "teaching", 'auburn hills')
Wayne = Learning('university', "business", 'detroit')
Ferris = Learning('university', "law enforcement", 'big rapids')

