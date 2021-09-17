from tkinter import * #import von Tkinter für die GUI

root = Tk() #  Biblothek

root.title("bot")

root.geometry("400x500")

main_menu = Menu(root) #erstellt eine main menu leiste

file_menu = Menu(root)
file_menu.add_command(label="New...")
file_menu.add_command(label="Save as..")
file_menu.add_command(label="Exit")


main_menu.add_cascade(label="File", menu = file_menu) #  anheften an file
main_menu.add_command(label="Edite")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

# chat window----------------------------------------
chatwindow = Text(root, bd=1, bg="black", width = 50, height = 8)
chatwindow.place(x=6, y=6, height=399, width=399)

 #  nachrichten fenster---------------------------------------
messagewindow = Text(root, bg="grey", width = 30, height=4)# einstellung der elemtparameter (position höhe weite etc...)
messagewindow.place(x=80, y=405, height= 70, width=400)


 #Button----------------------------------------------
button = Button(root, text="Senden", bg="green", activebackground="light green", width=6, height=5)
button.place(x=6, y=405, height=70, width=75)
root.mainloop()

