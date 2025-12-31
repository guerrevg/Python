"""
class LivingThings(HumanBeings,Animals):    -->Multiple Level Inheritence @(ParentA + ParentB > Child)
    isLive = True
    def CanHearSound():
        print("We Are Hear Sound")
    
class HumanBeings(LivingThings):            --->Single Level Inheritance @(Parent > Child)
    def Intelligent():
        print("Most Intelligent ? ")

class Animals(HumanBeings):                --->Multi-Level Inheritance @(Parent > Child1 > Child2)
    def Powerful():
        print("Powerful")
"""

