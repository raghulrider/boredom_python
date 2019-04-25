#CLASSES First program

class ProtoSem:
    def __init__(self, name, department, team):
        self.name = name
        self.department = department
        self.team = team

    def info(self):
        return "\n{} is studying {} and currently working as Graduation Engineer Trainee @Forge, also working under under a project {}.".format(self.name, self.department, self.team)

member1 = ProtoSem("Raghul Prasad", "ECE", " Smart Insulin Pump")
member2 = ProtoSem("Kanmani", "BCA", "Online Resume Maker")

print(member1.info())