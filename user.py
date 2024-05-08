import tkinter as tk
from tkinter import messagebox
import pickle

class CreditRiskApp:
    def __init__(self, master):
        self.master = master
        master.title("Credit Risk Model Stability")

        self.label = tk.Label(master, text="Enter customer details:")
        self.label.pack()

        self.age_label = tk.Label(master, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(master)
        self.age_entry.pack()

        self.income_label = tk.Label(master, text="Income:")
        self.income_label.pack()
        self.income_entry = tk.Entry(master)
        self.income_entry.pack()

        self.debt_label = tk.Label(master, text="Debt:")
        self.debt_label.pack()
        self.debt_entry = tk.Entry(master)
        self.debt_entry.pack()

        self.predict_button = tk.Button(master, text="Predict", command=self.predict)
        self.predict_button.pack()

        # Load the trained model
        try:
            with open(r'd:\Home-Credit---Credit-Risk-Model-Stability-main\Home-Credit---Credit-Risk-Model-Stability-main\credit_model.pkl', 'rb') as file:
                self.model = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Model file not found.")

    def predict(self):
        try:
            age = float(self.age_entry.get())
            income = float(self.income_entry.get())
            debt = float(self.debt_entry.get())

            # Prepare input data for prediction
            customer_data = [[age, income, debt,Numberofopencerditloan]]

            # Predict
            prediction = self.model.predict(customer_data)

            # Display prediction
            if prediction[0] == 1:
                messagebox.showinfo("Prediction", "This customer is likely to default.")
            else:
                messagebox.showinfo("Prediction", "This customer is not likely to default.")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

def main():
    root = tk.Tk()
    app = CreditRiskApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
