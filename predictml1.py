import os
import joblib

os.system("tput setaf 3")
print("\t\t\tMachine Learning Model !!!")
os.system("tput setaf 7")
print("\t\t-----------------------------------------")

model = joblib.load("salary.pk1")

years = float(input("Enter your Exprience : "))

prediction = model.predict([[years]])

print("Your salary as per exprience : ", prediction)
