#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''

class student:
    def __int__(self,name,id_number,year,major,gpa):
        self.name = name
        self.id_number = id_number
        self.year = year
        self.major = major
        self.gpa = gpa

    def honorsPG(self):
        if self.gpa >= 3.5:
            return("you made it to honors")
        else:
            return("you didnt make it")


    
    
    
    
def main():

    list = [1234,1040,8937]
    import random

    print(list)
    random_num = random.choice(list)
    print(random_num)

    if random_num == 1040:
        print("Winner")
    else:
        print("Loser")





main()
