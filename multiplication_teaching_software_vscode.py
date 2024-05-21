import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def study():
    # Functionality for "study" button
    main_frame.place_forget()
    study_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    buttons_study.configure(image=img_study[study])
    
def exit_study():
    study_frame.place_forget()#hides study frame
    main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
def multiplication_table():
    study_frame.place_forget()#hides study frame
    multiplication_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    
def exit_multiplication_table():
    multiplication_table_frame.place_forget()
    study_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    
def quiz():
    #Functionality for "Quiz" button
    main_frame.place_forget()
    quiz_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
def exit_quiz():
    quiz_frame.place_forget()
    main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
def easy():
    quiz_frame.place_forget()
    easy_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
def exit_easy():
    easy_frame.place_forget()
    quiz_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

    
def medium():
    quiz_frame.place_forget()
    medium_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
def exit_medium():
    medium_frame.place_forget()
    quiz_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    
def hard():
    quiz_frame.place_forget()
    hard_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
def exit_hard():
    hard_frame.place_forget()
    quiz_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

    
    
def settings():
        # Functionality for "settings" button
        main_frame.place_forget()  # Hide main frame
        settings_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
      
def exit_settings():
     settings_frame.place_forget()  # Hide settings frame
     main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
def open_background_settings():
    settings_frame.place_forget()  # Hide settings frame
    background_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
def exit_background_settings():
    background_frame.place_forget()  # Hide background frame
    settings_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
def set_background_color(color):
    # Functionality to set background color
    root.configure(bg=color)
    main_frame.configure(bg=color)
    settings_frame.configure(bg=color)
    background_frame.configure(bg=color)
    language_frame.configure(bg=color)
    study_frame.configure(bg=color)
    multiplication_table_frame.configure(bg=color)
    quiz_frame.configure(bg=color)
    
def open_language_settings():
    # Functionality for "language" button in settings
    settings_frame.place_forget()  # Hide settings frame
    language_frame.place(relx=0, rely=0, relwidth=1, relheight=1)  # Show language frame

def exit_language_settings():
    # Functionality for "exit" button in language settings
    language_frame.place_forget()  # Hide language frame
    settings_frame.place(relx=0, rely=0, relwidth=1, relheight=1)  # Show settings frame

def change_language(event):
    # Functionality to change language
    selected_language = combobox_language.get()
    translate_gui(selected_language)
    print("Selected language:", selected_language)    

def set_light_mode():
    set_background_color("white")

def set_dark_mode():
    set_background_color("black")
    
def translate_gui(language):
    # Functionality to translate all GUI text elements
    translator = Translator()
    
    # List of all text elements to be translated
    text_elements = [
        label_title, buttons_study, buttons_quiz, button_settings,
        label_settings_title, button_font, button_language, button_background,
        button_exit_settings, label_change_background, label_background_text,
        radio_light_mode, radio_dark_mode, button_exit_background_settings,
        label_language_title, combobox_language, button_exit_language_settings,
        label_study, button_exit_study, button_multiplication_table,
        label_multiplication_table, button_exit_multiplication_table,
        label_quiz, button_exit_quiz, button_easy, button_medium, button_hard,
        label_easy, button_exit_easy
    ]
    
    for element in text_elements:
        if isinstance(element, (tk.Label, tk.Button)):
            translated_text = translator.translate(element["text"], dest=language).text
            element.config(text=translated_text)
        elif isinstance(element, ttk.Combobox):
            translated_values = [translator.translate(value, dest=language).text for value in element["values"]]
            element.config(values=translated_values)
def change_font():
    font_size = int(spinbox_font_size.get())
    font_style = combobox_font_style.get()
    new_font = (font_style, font_size)
    text_elements = [
        label_title, buttons_study, buttons_quiz, button_settings,
        label_settings_title, button_font, button_language, button_background,
        button_exit_settings, label_change_background, label_background_text,
        radio_light_mode, radio_dark_mode, button_exit_background_settings,
        label_language_title, combobox_language, button_exit_language_settings,
        label_study, button_exit_study, button_multiplication_table,
        label_multiplication_table, button_exit_multiplication_table,
        label_quiz, button_exit_quiz, button_easy, button_medium, button_hard,
        label_easy, button_exit_easy
    ]
    for element in text_elements:
        if isinstance(element, (tk.Label, tk.Button)):
            element.config(font=new_font)



    
#create main window
root = tk.Tk()
root.title("Multiplication teaching software")
root.geometry("800x600")

#create main frame
main_frame = tk.Frame(root)
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Create and place widgets
label_title = tk.Label(root, text="Solve and Learn Multiplication!", font=("Arial", 24))
label_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

buttons_study = tk.Button(root, text="Study",command=study,width=17, height=3)
buttons_study.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

buttons_quiz = tk.Button(root, text="Quiz",command=quiz,width=17, height=3)
buttons_quiz.place(relx=0.5, rely= 0.55,anchor=tk.CENTER)

button_settings = tk.Button(root, text="Settings", command=settings)
button_settings.place(relx=0.9, rely=0.9, anchor=tk.SE)

settings_frame = tk.Frame(root)

# Create and place widgets for settings interface
label_settings_title = tk.Label(settings_frame, text="Settings", font=("Arial", 16))
label_settings_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_font = tk.Button(settings_frame, text="Font",width=17,height=3)
button_font.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

button_language = tk.Button(settings_frame, text="Language",width=17,height=3,command=open_language_settings)
button_language.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button_background = tk.Button(settings_frame, text="Background",width=17,height=3,command= open_background_settings)
button_background.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

button_exit_settings = tk.Button(settings_frame, text="Exit", command=exit_settings)
button_exit_settings.place(relx=0.1, rely=0.9, anchor=tk.SW)

font_styles = ["Arial", "Times New Roman", "Courier", "Verdana", "Helvetica"]
combobox_font_style = ttk.Combobox(settings_frame, values=font_styles)
combobox_font_style.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


# Create background settings frame
background_frame = tk.Frame(root)
# Create and place widgets for background settings interface
label_change_background = tk.Label(background_frame, text="Change Background", font=("Arial", 16))
label_change_background.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


label_background_text = tk.Label(background_frame, text="Do you wish to change background to:", font=("Arial", 10))
label_background_text.place(relx=0.5, rely=0.3, anchor=tk.CENTER)



radio_light_mode = tk.Radiobutton(background_frame, text="Light Mode", command=set_light_mode)
radio_light_mode.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

radio_dark_mode = tk.Radiobutton(background_frame, text="Dark Mode", command=set_dark_mode)
radio_dark_mode.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

button_exit_background_settings = tk.Button(background_frame, text="Exit", command=exit_background_settings)
button_exit_background_settings.place(relx=0.1, rely=0.9, anchor=tk.SW)

language_frame = tk.Frame(root)

# Create and place widgets for language settings interface
label_language_title = tk.Label(language_frame, text="Change Language", font=("Arial", 16))
label_language_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

languages = ["English", "Spanish", "French", "German", "Bengali" , "Arabic", "Russian", "Hindi" , "Indonesian", "Portugese", "Chinese" , "Japanese", "Korean"]
combobox_language = ttk.Combobox(language_frame, values=languages)
combobox_language.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
combobox_language.bind("<<ComboboxSelected>>", change_language)

button_exit_language_settings = tk.Button(language_frame, text="Exit", command=exit_language_settings)
button_exit_language_settings.place(relx=0.1, rely=0.9, anchor=tk.SW)

study_frame = tk.Frame(root)


#create and place widget for study interface
label_study = tk.Label(study_frame, text="Multiplication Table", font=("Arial", 16))
label_study.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_study = tk.Button(study_frame, text="Exit",command=exit_study)
button_exit_study.place(relx=0.1, rely=0.9, anchor=tk.SW)



button_multiplication_table = tk.Button(study_frame, text="Next Page", command=multiplication_table)
button_multiplication_table.place(relx=0.9,rely=0.9,anchor=tk.SW)



multiplication_table_frame=tk.Frame(root)



label_multiplication_table = tk.Label(multiplication_table_frame , text="Multiplication Tips", font=("Arial", 16))
label_multiplication_table.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_multiplication_table=tk.Button(multiplication_table_frame, text="Exit",command=exit_multiplication_table)
button_exit_multiplication_table.place(relx=0.1, rely=0.9, anchor=tk.SW)

quiz_frame=tk.Frame(root)


label_quiz=tk.Label(quiz_frame,text="Select your difficulty", font=("Arial", 16))
label_quiz.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_quiz=tk.Button(quiz_frame,text="Exit",command=exit_quiz)
button_exit_quiz.place(relx=0.1, rely=0.9, anchor=tk.SW)

button_easy=tk.Button(quiz_frame,text="Easy",command=easy,width=17,height=3)
button_easy.place(relx=0.5,rely=0.35,anchor=tk.CENTER)

button_medium=tk.Button(quiz_frame,text="Medium",command=medium,width=17,height=3)
button_medium.place(relx=0.5,rely=0.45,anchor=tk.CENTER)

button_hard=tk.Button(quiz_frame,text="Hard",command=medium,width=17,height=3)
button_hard.place(relx=0.5,rely=0.55,anchor=tk.CENTER)

easy_frame=tk.Frame(root)

label_easy=tk.Label(easy_frame,text="Type in the products",font=("Arial",16))
label_easy.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_easy=tk.Button(easy_frame,text="Exit",command=exit_easy)
button_exit_easy.place(relx=0.1, rely=0.9, anchor=tk.SW)

spinbox_font_size = tk.Spinbox(settings_frame, from_=8, to=30)
spinbox_font_size.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


medium_frame=tk.Frame(root)
label_medium=tk.Label(medium_frame,text="Type in the products",font=("Arial",16))
label_medium.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_medium=tk.Button(medium_frame,text="Exit",command=exit_medium)
button_exit_medium.place(relx=0.1,rely=0.9, anchor=tk.SW)

hard_frame=tk.Frame(root)
label_hard=tk.Label(hard_frame,text="Type in the products",font=("Arial",16))
label_hard.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_hard=tk.Button(hard_frame,text="Exit",command=exit_hard)
button_exit_hard.place(relx=0.1,rely=0.9, anchor=tk.SW)






root.mainloop()

