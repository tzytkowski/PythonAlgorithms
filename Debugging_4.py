class FIGHTER:
    def __init__(self, name, weight, nationality, skill):
        self.name = name
        self.weight = weight
        self.nationality = nationality
        self.skill = skill

fighters1 = [FIGHTER('Fedor', "265", "Russian", "Elite"),
            FIGHTER('Jon Jones', "205", "American", "Elite"),
            FIGHTER("Francis Ngannou", "265", "African", "High"),
            FIGHTER("Chuck Liddell", "205", "American", "Very High"),
            FIGHTER("Anderson Silva", "185" , "Brazilian", "Elite"),
            FIGHTER("Vitor Belfort", "185", "Brazilian", "High")]

fighters2 = [FIGHTER('BJ Penn', "155", "Hawaiian", "Elite"),
            FIGHTER('GSP', "170", "Canadian", "Elite"),
            FIGHTER('Colby Covington', "170", "American", "Very High"),
            FIGHTER("Nick Diaz", "170", "American", "Very High"),
            FIGHTER("Robbie Lawler", "170", "American", "Very High"),
            FIGHTER("Jorge Masvidal", "170", "Cuban", "High")]

index = 1;
# Comparing fighters nationalites
while index in range(len(fighters1)):
    for i in range(len(fighters2)):
        if fighters1[index].nationality == fighters2[i].nationality:
            print(fighters1[index].name, "and", fighters2[i].name, "are both", fighters1[index].nationality)
        elif fighters1[index].nationality != fighters2[i].nationality:
            print(fighters1[index].name, "and", fighters2[i].name, "are not the same nationality")
        if fighters1[index].skill == fighters2[i].skill:
            print("Both", fighters1[index].name, "and", fighters2[i].name, "both have a(n)", fighters2[i].skill, "skillset")
            if fighters1[index].weight and fighters2[index]:
                print("and are able to fight each other")
            else fighters1[index].weight <= fighters2[index] or fighters2[index]:
                print(' but cannot fight eachother')
        # End if statements


    

    
    
 



               
