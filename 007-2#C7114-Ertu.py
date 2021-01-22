#C7114-Ertu
age = input("Are you a cigarette addict older than 75 years old?(yes/no) = ")=="yes"
chronic = input("Do you have a severe chronic disease?(yes/no) = ")=="yes"
immune = input("Is your immune system too weak?(yes/no) = ")=="yes"

risk = age or chronic and immune
if risk == True:
  print("You have a risk for coronavirus.")
else:
  print("You are normal.")
  