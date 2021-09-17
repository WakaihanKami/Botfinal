import random

import awr

 #  Einleitung
bot = "Bot: "

print(bot +"Hallo, wie kann ich weiterhelfen?")
print(bot + "Optionen: Versandt, Kaufen, FAQ, Daten, Optionen")
print(bot +"Um das Programm zu beenden geben sie Bitte 'Exit' ein "'\n')

 #  User input-------------------------------------------------------------------------------------------------
user_input = "" #setzte den variabel wert zurück


while user_input != "Exit": #  Exit beendet das Programm
    user_input = ""
    while user_input == "": # while Schleife für neuen input
        user_input = input("Du: ")
    #print(random.choice(awr.r_aw)) #  ausgabe

    user_input = user_input.lower()  # eingabe umwandeln in lowcase
    user_words = user_input.split() #  user_wordliste erstellen die gefüllt wird (split) mit der eingabe

    for words in user_words:
        if words in awr.true_aw:
            print(bot + awr.true_aw[words]) # verweisst auf ein Dict und printet den gegeben key zum input
        else:
            print(bot + random.choice(awr.r_aw))# wenn key nicht übereinstimmt zugriff auf random string in der liste
    if user_input == "exit":
        print(bot +"Dankesehr, auf wiedersehen")
        break