import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "Math": [40, 80, 30, 90],
    "Physics": [70, 50, 40, 85],
    "Hours": [2, 3, 1, 4],
    "Weak": ["Math", "Physics", "Math", "None"]
}

df = pd.DataFrame(data)

X = df[["Math", "Physics", "Hours"]]
y = df["Weak"]

model = DecisionTreeClassifier()
model.fit(X, y)

math = int(input("Enter Math marks: "))
physics = int(input("Enter Physics marks: "))
hours = int(input("Enter study hours: "))

result = model.predict([[math, physics, hours]])

print("Weak Subject:", result[0])

if result[0] == "Math":
    print("Recommendation: Practice Math daily.")
elif result[0] == "Physics":
    print("Recommendation: Focus on Physics numericals.")
else:
    print("Great! No weak subject.")
    