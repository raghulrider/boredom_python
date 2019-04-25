#CLASSES
#Class Methods

class ProtoSem:
    
    no_of_students = 0
    points_raise = 1
    def __init__(self, name, department, team, points):
        self.name = name
        self.department = department
        self.team = team
        self.points  = int(points)
        ProtoSem.no_of_students += 1
        print("\n>> {} is added to ProtoSem.\n>> Total members in ProtoSem : {}\n".format((self.name).split()[0], ProtoSem.no_of_students))
    def info(self):
        print("\n>> {} is studying {} and currently working as Graduation Engineer Trainee @Forge, also working under under a project {}.\n>> Leader Board score of {} is {}".format(self.name, self.department, self.team,self.name, self.points))
        
    def all_raise_points(self):
        self.points = int(self.points) + int(ProtoSem.points_raise)
        print("\n>> Points Raised by {} for everyone".format(ProtoSem.points_raise))
    def raise_points(self):
        self.points = int(self.points) + int(self.points_raise)
        print("\n>> Points Raised by {}.\n>> Total points of {} : {}".format(self.points_raise, self.name, self.points))
    def points_info(self):
        print("\n{}'s Points:{}".format(self.name, self.points))
        
    @classmethod
    def from_string(cls, data_string):
        name, department, team, points = data_string.split("-")
        return cls(name, department, team, points)        
#member1 = ProtoSem("Raghul Prasad", "ECE", " Smart Insulin Pump", 0)
#member2 = ProtoSem("Kanmani", "BCA", "Online Resume Maker", 100)
member_names = {}
def addmember():
    print("\nInformation should be in this format mentioned below without any spaces\n\n                    'name-department-teamname-points' ")
    print("\nEnter 'end' to STOP registering people to ProtoSem and to enter MainMenu\n")
    flag = 0; count = 0
    while (flag != 1):
        info_string = str(input("Enter the info:"))
        count += 1
        if info_string == 'end':
            flag = 1
            print("\n{} people added\n".format(count-1))
        else:
            globals()['member%s' % count]  = ProtoSem.from_string(info_string)
            member_names[info_string.split("-")[0]] = globals()['member%s' % count] 
#member1.raise_points()
#member1.info()
#member2.info()
main_flag =0
while(main_flag != 1):
    mode = input("\nWhat to do(First Add people to ProtoSem and then use info and addpoints): \nSelect one of those:\n1.addmember\n2.info\n3.addpoints\n4.knowpoints\n5.STOP(To EXIT)\n\nEnter the Mode:")
    if mode == "addmember":
        addmember()
    elif mode == "info":
        info_flag = 0
        while (info_flag != 1):
            search_name = input(("\nWhose Info(Enter first name) or Type 'end' to enter Main Menu:"))
            if search_name == "end":
                info_flag = 1
            else:
                for name,membervalue in member_names.items():
                    if name == search_name:
                        membervalue.info()
                    else:
                        pass
    elif mode == "addpoints":
        addpoints_flag = 0
        while(addpoints_flag != 1):
            search_name1 = input(("\nType 'all' to increase points for everyone or you can use particular's name to increase points or enter 'end' to enter MainMenu\n\nEnter('all' or 'particular's name or 'end'):"))
            if search_name1 == 'end':
                addpoints_flag = 1
            else:
                if search_name1 == "all":
                    new_point = input("\nHow much to do you wanna add:")
                    ProtoSem.points_raise = new_point
                    for name4,membervalue4 in member_names.items():
                        membervalue4.all_raise_points()
                    print("\n{} Points Raised for everyone".format(new_point))
                else:
                    new_point_individual = input("\nHow much to do you wanna add to {}:".format(search_name1))
                    for name1,membervalue1 in member_names.items():
                        if name1 == search_name1:
                            membervalue1.points_raise = new_point_individual
                            membervalue1.raise_points()
                        else:
                            pass
    elif mode == "knowpoints":
        knowpoints_flag = 0
        while(knowpoints_flag !=1):
            search_name2 = input("\nWhose Points(Enter First Name) or enter 'end' to enter MainMenu:")
            if search_name2 == "end":
                knowpoints_flag = 1
            else:
                for name2,membervalue2 in member_names.items():
                    if name2 == search_name2:
                        print("Success")
                        membervalue2.points_info()
    elif mode == "STOP":
        print("\n\n                         Boom baby Bye !!!\n\n")
        main_flag = 1