from tkinter import *
from tkinter import ttk


def calculate_tip(total, tip, people):
    result = total * (tip / 100 + 1) / people
    return "{:.2f}".format(result)


def main():
    def display_result():
        person_share.insert(0, f"${calculate_tip(total.get(), tip.get(), people.get())}")

    def reset_form():
        person_share.delete(0, 'end')
        total.set(0)
        tip.set(0)
        people.set(1)

    root = Tk()
    root.minsize(500, 230)
    body = Frame()
    body.config(pady=10)

    title_label = ttk.Label(root, text="G's Tip Calculator",
                            background="black",
                            foreground="white",
                            font="Helvetica 18 bold",
                            )
    title_label.pack()
    body.pack()

    # Grid Layout
    body.rowconfigure(0, pad=10)
    body.rowconfigure(1, pad=10)
    body.rowconfigure(2, pad=10)
    body.rowconfigure(3, pad=10)
    body.rowconfigure(4, pad=10)
    body.rowconfigure(5, pad=10)
    body.rowconfigure(6, pad=10)
    body.config(padx=10)

    # Total row
    total = IntVar()
    total_label = ttk.Label(body, text="Total bill:")
    total_input = ttk.Entry(body, width=15, textvariable=total)
    total_input.bind('<FocusIn>', lambda x: total_input.selection_range(0, END))
    # ---- layout ----
    total_label.grid(row=0, column=0, sticky="w")
    total_input.grid(row=0, column=1)

    # Tip row
    tip = IntVar()
    tip_label = ttk.Label(body, text="How much tip would you like to give?")
    tip_none_radio_btn = ttk.Radiobutton(body, text="No tip", variable=tip, value=0, width=8)
    tip_10_radio_btn = ttk.Radiobutton(body, text="10%", variable=tip, value=10, width=10)
    tip_12_radio_btn = ttk.Radiobutton(body, text="12%", variable=tip, value=12, width=10)
    tip_15_radio_btn = ttk.Radiobutton(body, text="15%", variable=tip, value=15, width=10)
    tip_custom_radio_btn = ttk.Radiobutton(body, text="Custom", variable=tip, value=-1, width=10)
    # ---- layout ----
    tip_label.grid(row=1, column=0, columnspan=5, sticky="w")
    tip_none_radio_btn.grid(row=2, column=0)
    tip_10_radio_btn.grid(row=2, column=1)
    tip_12_radio_btn.grid(row=2, column=2)
    tip_15_radio_btn.grid(row=2, column=3)
    tip_custom_radio_btn.grid(row=2, column=4)

    # How many people row
    people = IntVar()
    people_input = Spinbox(body, from_=1, to=10000, textvariable=people, width=15)
    people_label = ttk.Label(body, text="How many people to split the bill?")
    # ---- layout ----
    people_label.grid(row=4, column=0, columnspan=2, sticky="w")
    people_input.grid(row=4, column=2, sticky="w")

    # Buttons row
    calculate_btn = Button(body, text="Calculate", command=display_result)
    clear_btn = Button(body, text="Clear", command=reset_form, width=8)
    # ---- layout ----
    calculate_btn.grid(row=5, column=0, columnspan=2)
    clear_btn.grid(row=5, column=2, columnspan=2)

    # Person share row
    per_person_label = ttk.Label(body, text="Each person should pay:")
    person_share = ttk.Entry(body, width=15)
    # ---- layout ----
    per_person_label.grid(row=6, column=0, columnspan=2, sticky="e")
    person_share.grid(row=6, column=2, sticky="w")

    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
