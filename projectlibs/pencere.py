import tkinter as tk

pencere = tk.Tk()
pencere.title("İlk UI")

lblEtiket = tk.Label(pencere, text = "Bu bir label", bd=10)
lblEtiket.pack(side=tk.LEFT,padx=50)

enGiris = tk.Entry(pencere, width=20, font=30, bg="red", fg="white", bd=0)
enGiris.pack(side=tk.LEFT,padx=10)

btnDugme = tk.Button(pencere, text="Tıkla", bg="blue", fg="red",border=10)
btnDugme.pack(side=tk.LEFT,padx=10)


pencere.geometry("600x400")

pencere.mainloop()