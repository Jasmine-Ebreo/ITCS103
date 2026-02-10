import tkinter as tk

windows = tk.Tk()
windows.title("Jasmine's Profile")
windows.geometry("600x600")
windows.resizable(False, True)
windows.configure(bg="violet")

title = tk.Label(windows, text="Student Profile", font=("Times New Roman", 28, "bold"), fg="black", bg="violet")
title.pack(padx=10, pady=(20, 10))

def add_info(label_text):
    # 'anchor="w"' aligns the text to the West (left) inside the label widget
    label = tk.Label(windows, text=label_text, font=("Times New Roman", 18), fg="black", bg="violet", anchor="w")
    
    # 'fill="x"' makes the label stretch horizontally
    # 'padx=50' adds some room from the left edge
    label.pack(padx=50, pady=5, fill="x")

add_info("\nName: Jasmine D. Ebreo")
add_info("Age: 19 years old")
add_info("Course: BSIT")
add_info("Birthday: October 14, 2006")
add_info("Motto:")


def add_motto(label_text):
    # 'anchor="center"' aligns the text to the West (left) inside the label widget
    label = tk.Label(windows, text=label_text, font=("Times New Roman", 8), fg="black", bg="violet", anchor="center")
 
    # 'fill="x"' makes the label stretch horizontally
    # 'padx=50' adds some from the left edge
    label.pack(padx=50, pady=5, fill="x")
    
add_motto("\nDream with passion, Live with purpose")
windows.mainloop()