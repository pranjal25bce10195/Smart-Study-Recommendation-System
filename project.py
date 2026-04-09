import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import tkinter as tk
from tkinter import messagebox

# Dataset
data = {
    "Math": [40, 80, 30, 90, 50, 60],
    "Physics": [70, 50, 40, 85, 60, 55],
    "Hours": [2, 3, 1, 4, 2, 3],
    "Weak": ["Math", "Physics", "Math", "None", "Math", "Physics"]
}

df = pd.DataFrame(data)

X = df[["Math", "Physics", "Hours"]]
y = df["Weak"]

model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction function
def predict():
    try:
        math = int(entry_math.get())
        physics = int(entry_physics.get())
        hours = int(entry_hours.get())

        result = model.predict([[math, physics, hours]])[0]

        if result == "Math":
            output = "Weak Subject: Math\nRecommendation: Practice daily."
        elif result == "Physics":
            output = "Weak Subject: Physics\nRecommendation: Focus on numericals."
        else:
            output = "Great! No weak subject."

        result_label.config(text=output)

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# GUI window
root = tk.Tk()
root.title("Smart Study Recommendation System")
root.geometry("400x300")

tk.Label(root, text="Enter Math Marks").pack()
entry_math = tk.Entry(root)
entry_math.pack()

tk.Label(root, text="Enter Physics Marks").pack()
entry_physics = tk.Entry(root)
entry_physics.pack()

tk.Label(root, text="Enter Study Hours").pack()
entry_hours = tk.Entry(root)
entry_hours.pack()

tk.Button(root, text="Get Recommendation", command=predict).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
