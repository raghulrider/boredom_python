#CLASSES
# Using class variables

class ProtoSem:
    
    no_of_students = 0
    points_raise = 1
    def __init__(self, name, department, team, points):
        self.name = name
        self.department = department
        self.team = team
        self.points  = points
        ProtoSem.no_of_students += 1
        print("\n>> {} is added to ProtoSem.\n>> Total members in ProtoSem : {}".format((self.name).split()[0], ProtoSem.no_of_students))
    def info(self):
        print("\n>> {} is studying {} and currently working as Graduation Engineer Trainee @Forge, also working under under a project {}.\n>> Leader Board score of {} is {}".format(self.name, self.department, self.team,self.name, self.points))
        
    def raise_points(self):
        self.points = self.points + ProtoSem.points_raise
        print("\n>> Points Raised by {}.\n>> Total points of {} : {}".format(ProtoSem.points_raise, self.name, self.points))
        
member1 = ProtoSem("Raghul Prasad", "ECE", " Smart Insulin Pump", 0)
member2 = ProtoSem("Kanmani Raghul Prasad", "BCA", "Online Resume Maker", 100)

#member1.raise_points()
member1.info()
member2.info()