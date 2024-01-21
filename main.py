from HomeWorkHelper import HomeWorkHelper
from customtkinter import (
    CTk,
    CTkButton,
    CTkEntry,
    CTkFont,
    CTkImage,
    CTkLabel,
    CTkOptionMenu,
    CTkScrollableFrame,
    CTkToplevel,
    filedialog,
    set_appearance_mode,    
    set_default_color_theme,
)
import customtkinter
help = HomeWorkHelper()
links = []
def getSources():
    global links
    sourcesString = ""
    sources.configure(state="normal")
    sources.delete(0.0,"end")
    sources.configure(state="disabled")
    question = questionEntry.get()
    
    try:
        repeats = int(repeatsEntry.get())
    except:
        repeatsEntry.delete(0,len(repeatsEntry.get()))
        error.configure(text="Please enter a number")
        return
    links = help.HomeWorkHelper(question, repeats)
    #print(links)
    if len(links) == 0:
        error.configure(text="No reliable sources found. Maybe add more details?")
        return
    elif len(links) >= 3:
        links[0] = "⭐ " + links[0]
        links[1] = "⭐ " + links[1]
        links[2] = "⭐ " + links[2]
    elif len(links) >= 2:
        links[0] = "⭐ " + links[0]
        links[1] = "⭐ " + links[1]
    elif len(links) == 1:
        links[0] = "⭐ " + links[0]
    sourcesString = ""
    for link in links:
        sourcesString += str(link) + "\n"
    links = None
  #  print(links)
    sources.configure(state="normal")
    sources.insert("0.0", str(sourcesString))
    sources.configure(state="disabled")
        
        
app = customtkinter.CTk()
###################################
app.title("Homework Helper")
app.geometry("400x400")
app.grid_columnconfigure(0, weight=1)
customtkinter.set_appearance_mode("dark")
###################################
#FONTS
big = CTkFont(size=70, family="Segoe UI", weight="bold")
normal =error = CTkFont(size=20, family="Segoe UI", weight="bold")
###################################
titleLabel = customtkinter.CTkLabel(app, text="Homework Helper", fg_color="transparent", font=big)
titleLabel.grid(row=0, column=0, padx=0, pady=20)

sources = customtkinter.CTkTextbox(app, width=300)
sources.grid(row=1, column=0,)
sources.insert("0.0", " ")
sources.configure(state="disabled")

questionEntry = customtkinter.CTkEntry(app, placeholder_text="Enter your question", width=300)
questionEntry.grid(row=2, column=0, pady=20)

repeatsEntry = customtkinter.CTkEntry(app, placeholder_text="Enter how many searches should be complete", width=300)
repeatsEntry.grid(row=3, column=0,pady=10)

submitButton = customtkinter.CTkButton(app, text="Submit", command=getSources)
submitButton.grid(row=4, column=0)

error = customtkinter.CTkLabel(app, text="", fg_color="transparent",font=normal,text_color="red")
error.grid(row=5, column=0)
###################################
app.mainloop()
