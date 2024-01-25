from tkinter import *

window = Tk()

window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

label1 = Label(text="Enter weight (kg):")
label1.config(pady=5)
label1.pack()

entry1 = Entry(width=10)
entry1.pack()

label2 = Label(text="Enter height (m):")
label2.config(pady=5)
label2.pack()

entry2 = Entry(width=10)
entry2.pack()

user_button = Button(text="Calculate BMI", command=lambda: button(entry1.get(), entry2.get()))
user_button.config(pady=10)
user_button.pack()

result_label = Label(text="")
result_label.pack()

def button(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        bmi = int(weight / (height * height))

        if bmi < 18.5:
            result_label.config(text=f"BMI: {bmi} and you are underweight")
        elif 18.5 <= bmi <= 24.9:
            result_label.config(text=f"BMI: {bmi} and you are normal")
        elif 25 <= bmi <= 29.9:
            result_label.config(text=f"BMI: {bmi} and you are overweight")
        else:
            result_label.config(text=f"BMI: {bmi} and you are obese.")

    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

window.mainloop()