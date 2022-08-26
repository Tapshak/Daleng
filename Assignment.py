
class students:
    
    def __init__(self, first_Name, last_Name, Age) :
        
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.Age = Age
        
    def AllName(self):
        return f'\nfirst_Name: {self.first_Name}\nlast_Name: {self.last_Name}\nAge: {self.Age}\nRank:{self.Rank}'
    
    
class teacher (students):
    
    def __init__(self, first_Name, last_Name, Age, Rank,):
        # inheritting instance variable from class students 
        super().__init__(first_Name, last_Name, Age)
        self.Rank = Rank
        
T1 = teacher('Dashen', 'Zakari', 43, 13)
T2 =teacher('Musa', 'Lucky', 25, 12)

print(teacher.AllName(T1))
print(T2.AllName())
