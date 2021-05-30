import joblib

model = joblib.load("salary.pk1")

years = float(input("Enter your Exprience : "))

prediction = model.predict([[years]])

print("Your salary as per exprience : ", prediction)
