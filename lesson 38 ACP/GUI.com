import tkinter as tk


window = tk.Tk()
window.geometry("400x300")
window.title("Getting Started with Widgets")
description_label = tk.Label(window, text="Enter two numbers below to calculate their product.", fg="#333", font=("Arial", 10))
description_label.pack(pady=10)
label1 = tk.Label(window, text="Enter first number:", fg="#005f73")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()
label2 = tk.Label(window, text="Enter second number:", fg="#005f73")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"The product is: {product}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers.")
calc_button = tk.Button(window, text="Calculate Product", command=calculate_product, bg="#94d2bd")
calc_button.pack(pady=10)


result_box = tk.Text(window, height=3, width=30,) bg=("#e9d8a6")
result_box.pack()
window.mainloop()
