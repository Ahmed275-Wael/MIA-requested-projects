class Wizard:

    def __init__(self):
        self.health = 100
        self.energy = 500
        self.shield = 3
    #---------------------------------reducers----------------------------------------
    def reduceShield(self):
        self.shield -= 1
    def reduceEnergy(self,value):
        self.energy -= value
    def reduceHealth(self,value):
        self.health -= value
    #-----------------------------------getters---------------------------------------
    def getshield(self):
        return self.shield
    def getHealth(self):
        return self.health
    def getEnergy(self):
        return self.energy
    #----------------------------------fight-------------------------------------------
    def Fight(self , Voldemort, lol):
        dictV = {}
        dictH = {}
        file1 = open('spells.txt', 'r')
        lines = file1.readlines()

        for i in range(int(lines.__len__())):
            if lines[i].split()[0] == "A":
                dictH[lines[i].split()[1]] = int(lines[i].split()[2])
                dictV[lines[i].split()[1]] = int(lines[i].split()[2])
            if lines[i].split()[0] == "H":
                dictH[lines[i].split()[1]] = int(lines[i].split()[2])
            if lines[i].split()[0] == "V":
                dictV[lines[i].split()[1]] = int(lines[i].split()[2])
        while self.getHealth() > 0 and Voldemort.getHealth() > 0 and self.getEnergy() > 0 and Voldemort.getEnergy() > 0:
            print("       Harry\t\tVoldemort\n")
            print("Health:",end="")
            print(self.getHealth(),end="")
            print("\t\t\t",end="")
            print(Voldemort.getHealth())
            print("Energy:",end="")
            print(self.getEnergy(),end="")
            print("\t\t\t",end="")
            print(Voldemort.getEnergy())
            print("Enter Harry's then Voldemort's spells")
            s = input().split()
            s1 = s[0]
            s2 = s[1]
            if s1 in dictH and s2 in dictV :
                reducedHealth = dictH[s1] - dictV[s2]
                shieldActive = 0
                if self.getEnergy() < dictH[s1] or Voldemort.getEnergy() < dictV[s2]:
                    pass
                else:
                    if s1 == "sheild" and self.getshield() >= 0:
                        self.reduceShield()
                    if s2 == "sheild" and Voldemort.getshield() >= 0:
                        Voldemort.reduceShield()
                    if s1 == "sheild" and self.getshield() < 0:
                        print("Harry is out of sheilds")
                        shieldActive = 1
                    if s2 == "sheild" and Voldemort.getshield() < 0:
                        print("Voldemort is out of sheilds")
                        shieldActive = 1
                    if shieldActive != 1:
                        self.reduceEnergy(dictH[s1])
                        Voldemort.reduceEnergy(dictV[s2])

                    if reducedHealth < 0 and s1 != "sheild":
                        self.reduceHealth(abs(reducedHealth))
                    if reducedHealth > 0 and s2 != "sheild":
                        Voldemort.reduceHealth(reducedHealth)
                if self.getHealth() <= 0:
                 print("Voldemort wins")
                if Voldemort.getHealth() <= 0:
                 print("Harry wins")
            else:
                print("Why the hell are you messing with the names,MAN")

