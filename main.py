# x = int(input("Please enter your first number: "))
# y = int(input("Second number please: "))
# print(x + y)

height = int(input("please enter height"))
weight = int(input(" weight"))

bmi = (weight/(height**2))*703
print('your bmi is: ' + str(bmi))

if(bmi < 20):
    print("awesome")
elif(bmi <30):
    print("need some working on")
elif(bmi < 40):
    print("better see the doc")
else:
    print("run fat boy run!") 
