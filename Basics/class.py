class Planets:
    nearSun = False #This is a class attribute
    isLifeexist = "Nope"
    power = 100

    def Power(self):
        print(self.power)

    @staticmethod #Static Method is Use when we dont use self I our code 
    def Greet():
        print("Good Morning")

Neptune = Planets()
""" 
Neptune.Power()
     Both Are Same ()
Planets.Power(Neptune)
"""
Neptune.planet = "Neptune" #This is object/instance attribute
Neptune.isLifeexist = "Not Possible" #overrite the class attribute
# Neptune.power = 900
Neptune.Greet()
print(f"{Neptune.planet} :",end="")
print(f"\n\tPower : {Neptune.power},IsLifeExitsHere : {Neptune.isLifeexist} , PlanetIsNearSun : {Neptune.nearSun}\n")

Earth = Planets()
Earth.planet = "Earth" #This is object/instance attribute
Earth.isLifeexist = "Yes" #overrite the class attribute
Earth.nearSun = True #overrite the class attribute
Earth.Greet()
print(f"{Earth.planet} :",end="")
print(f"\n\tIsLifeExitsHere : {Earth.isLifeexist} , PlanetIsNearSun : {Earth.nearSun} \n")
    


