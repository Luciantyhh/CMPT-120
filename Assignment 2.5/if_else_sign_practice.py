def main():

    '''ask the user for their age. If the user is 25 or older, tell them they can buy alcohol, nicotine products, and they can rent a car
        If they're 21 or older but younger than 25, tell them they can buy alcohol and nicotine products, but cannot rent a car
        If they're 18 and older but younger than 21, tell them they can only buy nicotine products in some states
        If they're less than 18, they can only purchase candy cigarettes and sody pops
    '''
    print("how old are you")
    require = ["you can buy alchol","you can buy nicotine","you can rent a car"]
    age = 25
    print(age)
    if age >= 25:
        print(require)
    if age < 24:
        print(require[0,1])
    if age < 18:
        print("you can only buy candy and soda")

  
  
  
main()
