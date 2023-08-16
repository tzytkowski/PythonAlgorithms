class FIGHTER:
    def __init__(self, name, heavyweight, middleweight, lightweight, nationality):
        self.name = name
        self.heavyweight = heavyweight
        self.middleweight = middleweight
        self.lightweight = lightweight
        self.nationality = nationality
        self.skill = skill

fighters1 = [FIGHTER('Fedor', True, False, False, "Russian", "Elite"),
            FIGHTER('Jon Jones', True, True, False, "American", "Elite"),
            FIGHTER("Francis Ngannou", True, False, False, "African", "High"),
            FIGHTER("Chuck Liddell", False, True, False, "American", "Very High"),
            FIGHTER("Anderson Silva", self , False, True, False, "Brazilian", "Elite"),
            FIGHTER("Vitor Belfort", True, True, False, "Brazilian", "High")]

fighters2 = [FIGHTER('BJ Penn', True, True, True, "Hawaiian", "Elite"),
            FIGHTER('GSP', False, True, False, "Canadian", "Elite"),
            FIGHTER('Colby Covington', False, False, True, "American", "Very High"),
            FIGHTER("Nick Diaz", False, True, True, "American", "Very High"),
            FIGHTER("Robbie Lawler", False, True, True, "American", "Very High"),
            FIGHTER("Jorge Masvidal", False, True, "True", "Cuban", "High")]

index = 1;
# Comparing fighters nationalites
while index in range(len(fighters1)):
    for i in range(len(fighters2)):
        if fighters1[index].nationality == fighters2[i].nationality:
            print(fighters1[index].name, "and", fighters2[i].name, "are both", fighters1[index].nationality)
        elif fighters1[index].nationality != fighters2[i].nationality:
            print(fighters1[index].name, "and", fighters2[i].name, "are not the same nationality")
        if fighters1[index].skill == fighters2[i].skill:
            print("Both", fighters1[index].name, "and", fighters2[i].name, "both have a(n)", fighters2[i].skill, "skillset",)
            if fighters1[index].heavyweight == True and fighters2[i].heavyweight == True:
                print("and are able to fight each other")
            else fighters1[index].heavyweight == True and fighters2[i].heavyweight == False:
                print(' but cannot fight eachother')
        # End if statements


    

    
    
 



               