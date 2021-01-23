print("I am your carbon footprint calculator. I will ask you a few questions about your household etc. that will help us calculate your footprint.")
point = 0
number_people=0


# Asking Question number 1:
number_people = int(input("How many people do you live with (if alone type 0 ): "))
if number_people == 0:
  point = point + 14
elif number_people == 1:
  point = point + 12

elif number_people == 2:
  point = point + 10

elif number_people == 3:
  point = point + 8

elif number_people == 4:
  point = point + 6

elif number_people == 5:
  point = point + 4

elif number_people >= 6:
  point = point + 2
  
# Asking qustion number 2:
size_of_house = str(input("How big is your house? (Large, Medium, Small or Apartment?): "))
if size_of_house == "Large":
  point = point + 10

elif size_of_house == "Medium":
  point = point + 7
  
elif size_of_house == "Small":
  point = point + 4 

elif size_of_house == "Apartment":
  point = point + 2

# Asking question number 3: 
food_practices = str(input("What food do you eat? (Pre-packaged, Meat daily, Meat few times per week, Vegetarian, Vegan): "))
if food_practices == "Pre-packaged":
  point = point + 12

elif food_practices == "Meat daily":
  point = point + 10

elif food_practices == "Meat few times per week":
  point = point + 8 

elif food_practices == "Vegetarian":
  point = point + 4

elif food_practices == "Vegan":
  point = point + 2

# Asking question number 4:
cleanliness = int(input("Please enter the number of trash bags emptied in a week (4, 3, 2 or 1 times?): "))
if cleanliness == 4:
  point = point + 50

elif cleanliness == 3:
  point = point + 40

elif cleanliness == 2:
  point = point + 30

elif cleanliness == 1:
  point = point + 20

if point >= 60:
  print("You have to lower your carbon usage, to know more please visit this website: https://support.worldwildlife.org/site/Advocacy?cmd=display&page=UserAction&id=994 ")

else: print("You are hurting the world a little less than most people, but try and bring your footprint as little as possible, to know more please visit this website: https://support.worldwildlife.org/site/Advocacy?cmd=display&page=UserAction&id=994 ")

print("These are your carbon points: ", point)