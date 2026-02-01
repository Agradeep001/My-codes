import tkinter as tk
from molmass import Formula

mass=0

def calculate_mass():
    global mass
    f = molecular_formula.get()
    try:
        x = Formula(f)
        mass = x.mass
        label_result1.config(font=("Helvetica",20),text=f"{mass:.5f} g/mol", fg="black")
    except Exception:
        label_result1.config(text="Invalid Formula",font=("Helvetica",20), fg="red")

def calculate_weight_molarsolution():
    global mass
    v=float(volume.get())
    s=float(strength.get())
    e=float(equivallancy.get())
    m=mass
    try:
        weight_needed= ((m*v*s)/1000)
        label_result2.config(font=("Helvetica", 20),text=f"{weight_needed:.5f} g", fg="black")
    except Exception:
        label_result2.config(text="error",font=("Helvetica", 20), fg="red")

def calculate_weight_normalsolution():
    global mass
    v=float(volume.get())
    s=float(strength.get())
    e=float(equivallancy.get())
    m=mass
    try:
        weight_needed= ((m*v*s)/(e*1000))
        label_result3.config(font=("Helvetica",20),text=f"{weight_needed:.5f} g", fg="black")
    except Exception:
        label_result3.config(text="error",font=("Helvetica",20), fg="red")

def calculate_equivalent_weight():
    global mass
    e=float(equivallancy.get())
    m=mass
    try:
        e_weight= (m/e)
        label_result2.config(font=("Helvetica",20),text=f"{e_weight:.5f} g", fg="black")
    except Exception:
        label_result2.config(text="Invalid Formula or Equivalency.",font=("Helvetica",20), fg="red")






window = tk.Tk()
window.title("Molar Mass Calculator")
window.state("zoomed")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

root=tk.Frame(window,bg="#F0FFF0")
root.grid(row=0,column=0,sticky="nsew")

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)

label_input = tk.Label(root, font=("Helvetica",20),text="Enter Molecular Formula:",bg="#99D5F1")
label_input.grid(row=0,column=1,sticky="nsew",pady=10)

molecular_formula = tk.Entry(root,font=("Helvetica",20),bg="white")
molecular_formula.grid(row=0,column=2,sticky="nsew",pady=10)

btn_calculate = tk.Button(root,font=("Helvetica",20), text="Calculate atomic/moecular mass",bg="powderblue", command=calculate_mass)
btn_calculate.grid(row=1,column=1,sticky="nsew",columnspan=2,pady=10)

label_output_header = tk.Label(root, font=("Helvetica",20),bg="#99D5F1",text="Molecularar Mass:")
label_output_header.grid(row=2,column=1,sticky="nsew",pady=10)

label_result1 = tk.Label(root,font=("Helvetica",20),bd=1,relief="solid",bg="#B7FCB7")
label_result1.grid(row=2,column=2,sticky="nsew",pady=10)

label_input = tk.Label(root, font=("Helvetica",20),text="Enter equivalancy:",bg="#99D5F1", )
label_input.grid(row=3,column=1,sticky="nsew",pady=10)

equivallancy = tk.Entry(root,font=("Helvetica",20),bg="white")
equivallancy.grid(row=3,column=2,sticky="nsew",pady=10)

btn_calculate = tk.Button(root,font=("Helvetica",20), text="Calculate equivalent weight",bg="powderblue", command=calculate_equivalent_weight)
btn_calculate.grid(row=4,column=1,sticky="nsew",columnspan=2,pady=10)

label_output_header2 = tk.Label(root, font=("Helvetica",20),text="Equivalent weight:",bg="#99D5F1")
label_output_header2.grid(row=5,column=1,sticky="nsew", pady=10)

label_result2 = tk.Label(root,font=("Helvetica",20),bd=1,relief="solid",bg="#B7FCB7")
label_result2.grid(row=5,column=2,sticky="nsew",pady=10)

label_input = tk.Label(root, font=("Helvetica",20),text="Enter volume(ml):",bg="#99D5F1", )
label_input.grid(row=6,column=1,sticky="nsew",pady=10)

volume = tk.Entry(root,font=("Helvetica",20),bg="white")
volume.grid(row=6,column=2,sticky="nsew",pady=10)

label_input = tk.Label(root, font=("Helvetica",20),text="Enter strength(M/N):",bg="#99D5F1", )
label_input.grid(row=7,column=1,sticky="nsew",pady=10)

strength = tk.Entry(root,font=("Helvetica",20),bg="white")
strength.grid(row=7,column=2,sticky="nsew",pady=10)

btn_calculate2 = tk.Button(root,font=("Helvetica",20), text="weight for molar solution",bg="powderblue", command=calculate_weight_molarsolution)
btn_calculate2.grid(row=8,column=1,sticky="nsew",pady=10)

btn_calculate3 = tk.Button(root,font=("Helvetica",20), text="weight for normal solution",bg="powderblue", command=calculate_weight_normalsolution)
btn_calculate3.grid(row=8,column=2,sticky="nsew",pady=10)

label_output_header3 = tk.Label(root, font=("Helvetica",20),text="Needed weight is:",bg="#99D5F1")
label_output_header3.grid(row=9,column=1,sticky="nsew", pady=10)

label_result3 = tk.Label(root,font=("Helvetica",20),bd=1,relief="solid",bg="#B7FCB7")
label_result3.grid(row=9,column=2,sticky="nsew",pady=10)

label_0=tk.Label(root, font=("Helvetica",20),text="Rules:",bg="#FAB1F4")
label_0.grid(row=10,column=1,columnspan=2,sticky="nsew")

label_1=tk.Label(root, font=("Helvetica",20),text="Enter the formula in normal text format (example:H2SO4).",bg="#FAB1F4")
label_1.grid(row=11,column=1,columnspan=2,sticky="nsew")

label_2=tk.Label(root, font=("Helvetica",20),text="Calculate each data before proceeding to the next one.",bg="#FAB1F4")
label_2.grid(row=12,column=1,columnspan=2,sticky="nsew")


root.mainloop()