# import tkinter as tk
# from tkinter import messagebox

# # Lists to store user data
# Name = []
# Password = []
# Contact = []
# Address = []
# UserSalaries = {}

# # Function for sign-up
# def signup():
#     def add_user():
#         N = entry_name.get()
#         P = entry_password.get()
#         C = entry_contact.get()
#         A = entry_address.get()

#         if N and P and C and A:
#             Name.append(N)
#             Password.append(P)
#             Contact.append(C)
#             Address.append(A)
#             UserSalaries[N] = 0
#             messagebox.showinfo("Success", "Sign-up successful!")
#             signup_window.destroy()
#         else:
#             messagebox.showwarning("Input Error", "All fields are required!")

#     signup_window = tk.Toplevel(root)
#     signup_window.title("Sign Up")

#     tk.Label(signup_window, text="Name").grid(row=0)
#     tk.Label(signup_window, text="Password").grid(row=1)
#     tk.Label(signup_window, text="Contact").grid(row=2)
#     tk.Label(signup_window, text="Address").grid(row=3)

#     entry_name = tk.Entry(signup_window)
#     entry_password = tk.Entry(signup_window, show='*')
#     entry_contact = tk.Entry(signup_window)
#     entry_address = tk.Entry(signup_window)

#     entry_name.grid(row=0, column=1)
#     entry_password.grid(row=1, column=1)
#     entry_contact.grid(row=2, column=1)
#     entry_address.grid(row=3, column=1)

#     tk.Button(signup_window, text='Sign Up', command=add_user).grid(row=4, column=1, pady=4)

# # Function for sign-in
# def signin():
#     def check_user():
#         Username = entry_username.get()
#         PassWord = entry_password.get()

#         if Username in Name:
#             index = Name.index(Username)
#             if Password[index] == PassWord:
#                 messagebox.showinfo("Success", "SIGN-IN SUCCESSFUL!")
#                 signin_window.destroy()
#                 open_salary_calculator()
#             else:
#                 messagebox.showerror("Error", "Incorrect password.")
#         else:
#             messagebox.showerror("Error", "Username not found.")

#     signin_window = tk.Toplevel(root)
#     signin_window.title("Sign In")

#     tk.Label(signin_window, text="User Name").grid(row=0)
#     tk.Label(signin_window, text="Password").grid(row=1)

#     entry_username = tk.Entry(signin_window)
#     entry_password = tk.Entry(signin_window, show='*')

#     entry_username.grid(row=0, column=1)
#     entry_password.grid(row=1, column=1)

#     tk.Button(signin_window, text='Sign In', command=check_user).grid(row=2, column=1, pady=4)

# # Function for the salary calculator
# def open_salary_calculator():
#     def calculate_salary():
#         name = entry_name.get()
#         phone = entry_phone.get()
#         try:
#             salary = float(entry_salary.get())
#         except ValueError:
#             messagebox.showerror("Input Error", "Salary must be a number.")
#             return

#         if name not in UserSalaries:
#             messagebox.showerror("Error", "User not found.")
#             return

#         # Example calculation
#         bonus = salary * 0.1  # 10% bonus
#         tax = salary * 0.2    # 20% tax
#         net_salary = salary + bonus - tax

#         UserSalaries[name] = salary

#         result_text = f"Name: {name}\nPhone: {phone}\nSalary: {salary}\nBonus: {bonus}\nTax: {tax}\nNet Salary: {net_salary}"
#         result_label.config(text=result_text)

#     if len(UserSalaries) >= 5:
#         messagebox.showerror("Limit Reached", "Maximum 5 users allowed.")
#         return

#     salary_window = tk.Toplevel(root)
#     salary_window.title("Salary Calculator")

#     tk.Label(salary_window, text="Name").grid(row=0)
#     tk.Label(salary_window, text="Phone").grid(row=1)
#     tk.Label(salary_window, text="Monthly Salary").grid(row=2)

#     entry_name = tk.Entry(salary_window)
#     entry_phone = tk.Entry(salary_window)
#     entry_salary = tk.Entry(salary_window)

#     entry_name.grid(row=0, column=1)
#     entry_phone.grid(row=1, column=1)
#     entry_salary.grid(row=2, column=1)

#     tk.Button(salary_window, text='Calculate', command=calculate_salary).grid(row=3, column=1, pady=4)

#     result_label = tk.Label(salary_window, text="")
#     result_label.grid(row=4, columnspan=2)

# # Main application window
# root = tk.Tk()
# root.title("Salary Calculator App")

# tk.Button(root, text='Sign Up', command=signup).pack(pady=10)
# tk.Button(root, text='Sign In', command=signin).pack(pady=10)
# tk.Button(root, text='Exit', command=root.quit).pack(pady=10)

# root.mainloop()




import tkinter as tk
from tkinter import messagebox

# Lists to store user data
Name = []
Password = []
Contact = []
Address = []
UserSalaries = {}

# Function for sign-up
def signup():
    def add_user():
        N = entry_name.get()
        P = entry_password.get()
        C = entry_contact.get()
        A = entry_address.get()

        if N and P and C and A:
            Name.append(N)
            Password.append(P)
            Contact.append(C)
            Address.append(A)
            UserSalaries[N] = {'phone': '', 'salary': 0}
            messagebox.showinfo("Success", "Sign-up successful!")
            signup_window.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    tk.Label(signup_window, text="Name").grid(row=0)
    tk.Label(signup_window, text="Password").grid(row=1)
    tk.Label(signup_window, text="Contact").grid(row=2)
    tk.Label(signup_window, text="Address").grid(row=3)

    entry_name = tk.Entry(signup_window)
    entry_password = tk.Entry(signup_window, show='*')
    entry_contact = tk.Entry(signup_window)
    entry_address = tk.Entry(signup_window)

    entry_name.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)
    entry_contact.grid(row=2, column=1)
    entry_address.grid(row=3, column=1)

    tk.Button(signup_window, text='Sign Up', command=add_user).grid(row=4, column=1, pady=4)

# Function for sign-in
def signin():
    def check_user():
        Username = entry_username.get()
        PassWord = entry_password.get()

        if Username in Name:
            index = Name.index(Username)
            if Password[index] == PassWord:
                messagebox.showinfo("Success", "SIGN-IN SUCCESSFUL!")
                signin_window.destroy()
                open_salary_calculator(Username)
            else:
                messagebox.showerror("Error", "Incorrect password.")
        else:
            messagebox.showerror("Error", "Username not found.")

    signin_window = tk.Toplevel(root)
    signin_window.title("Sign In")

    tk.Label(signin_window, text="User Name").grid(row=0)
    tk.Label(signin_window, text="Password").grid(row=1)

    entry_username = tk.Entry(signin_window)
    entry_password = tk.Entry(signin_window, show='*')

    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    tk.Button(signin_window, text='Sign In', command=check_user).grid(row=2, column=1, pady=4)

# Function for the salary calculator
def open_salary_calculator(current_user):
    def add_salary():
        name = current_user
        phone = entry_phone.get()
        try:
            salary = float(entry_salary.get())
        except ValueError:
            messagebox.showerror("Input Error", "Salary must be a number.")
            return

        if name not in UserSalaries:
            messagebox.showerror("Error", "User not found.")
            return

        # Example calculation
        bonus = salary * 0.1  # 10% bonus
        tax = salary * 0.2    # 20% tax
        net_salary = salary + bonus - tax

        UserSalaries[name] = {'phone': phone, 'salary': salary, 'bonus': bonus, 'tax': tax, 'net_salary': net_salary}

        update_user_list()

    def update_user_list():
        user_list_text = ""
        for user, details in UserSalaries.items():
            user_list_text += f"Name: {user}, Phone: {details['phone']}, Salary: {details['salary']}, Bonus: {details['bonus']}, Tax: {details['tax']}, Net Salary: {details['net_salary']}\n"
        user_list_label.config(text=user_list_text)

    salary_window = tk.Toplevel(root)
    salary_window.title("Salary Calculator")

    tk.Label(salary_window, text="Phone").grid(row=0)
    tk.Label(salary_window, text="Monthly Salary").grid(row=1)

    entry_phone = tk.Entry(salary_window)
    entry_salary = tk.Entry(salary_window)

    entry_phone.grid(row=0, column=1)
    entry_salary.grid(row=1, column=1)

    tk.Button(salary_window, text='Add/Update Salary', command=add_salary).grid(row=2, column=1, pady=4)

    user_list_label = tk.Label(salary_window, text="")
    user_list_label.grid(row=3, columnspan=2)

    update_user_list()

# Main application window
root = tk.Tk()
root.title("Salary Calculator App")

tk.Button(root, text='Sign Up', command=signup).pack(pady=10)
tk.Button(root, text='Sign In', command=signin).pack(pady=10)
tk.Button(root, text='Exit', command=root.quit).pack(pady=10)

root.mainloop()

