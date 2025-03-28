import random
import keyboard
import tkinter as tk

writenText = ""

endscreenOn= False

create_TextComponents = []
create_EndscreenComponents = []
randomText=None

window = tk.Tk()
window.geometry("1000x500")
window.title("Tastaturschreiben")

eingabe = tk.Label(window, text="", font=("Arial", 14))
eingabe.pack(pady=20)

def update_text(event):
    global writenText
    global randomText
    global endscreenOn
    
    if len(writenText)==len(randomText)-1 and writenText[-1] == randomText[-2]:
        create_Endscreen()
        endscreenOn = False
    # Hinzufügen von "_" bei Space klick
    else:
        if event.name == "space":
            writenText += " "
        elif event.name == "backspace":
            writenText = writenText[:-1]
            create_TextComponents[len(writenText)].config(fg="grey", text=randomText[len(writenText)].lower())
        elif event.name == randomText[len(writenText)].lower():
            writenText += event.name
            create_TextComponents[len(writenText)-1].config(fg="black")
        elif not event.name == randomText[len(writenText)].lower():
            writenText += event.name
            create_TextComponents[len(writenText)-1].config(fg="red", text=event.name)

        #eingabe.config(text=writenText)

def create_Text():
    global randomText
    global endscreenOn

    endscreenOn=False
    
    for component in create_EndscreenComponents:
        component.destroy()
    create_EndscreenComponents.clear()
    
    with open("DE words.txt", encoding="utf-8") as file:
        germanWords = file.read().split(" ")

    randomText = " ".join(random.choice(germanWords) for _ in range(10))

    for i, letter in enumerate(randomText):
        lbl = tk.Label(window, text=letter.lower(), font=("Arial", 14), fg="grey")
        lbl.pack(side="left", anchor="nw")
        
        create_TextComponents.append(lbl)

def create_Endscreen():
    global create_EndscreenComponents
    global writenText

    for component in create_TextComponents:
        component.destroy()
    create_TextComponents.clear()
    writenText=""

    lbl = tk.Label(window, text="WPM" , font=("Arial", 20))
    lbl.pack(side="top")

    btn = tk.Button(window, text="Restart", font=("Arial", 15), command=create_Text)
    btn.pack(pady=100, side="top")

    create_EndscreenComponents.append(lbl)
    create_EndscreenComponents.append(btn)

# funktioniert nicht fixen
# auch in endscreen tipp bar
if not endscreenOn:
    keyboard.on_press(update_text)

create_Text()
window.mainloop()
