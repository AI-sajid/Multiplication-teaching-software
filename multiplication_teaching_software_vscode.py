
import tkinter as tk
from tkinter import ttk
# translator module
from googletrans import Translator
#modules for image
from tkinter import *
from PIL import Image, ImageTk
from os import path
import os
#module for random integers for the questions
from random import randint


def study():
    global new_width,new_height
    global multiplication_table_image
    global current_image_label # Making the image label a global variable so it can be accessed later
    # Functionality for "study" button
    main_frame.place_forget()
    study_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    # Functionality for the image of multiplication table
    multiplication_table_image = Image.open("Multiplication_table.jpg")

    new_width = 800     #changing the height and width of the image
    new_height = 500
    resized_image = multiplication_table_image.resize((new_width, new_height), Image.Resampling.LANCZOS) #
    
    image_tk= ImageTk.PhotoImage(resized_image) 
    image_label = tk.Label(study_frame, text="",image = image_tk)
    image_label.image = image_tk
    image_label.place(x=250,y=100)
    
    current_image_label = image_label


def exit_study():
    global current_image_label #This variable can be used outside this function as well
    study_frame.place_forget()  # hides study frame, N.B : study frame contains the multiplication table
    main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    current_image_label.place_forget() #hides the image
    current_image_label.destroy()

def multiplication_table(): 
    global new_image_label #
    study_frame.place_forget()  # hides study frame
    multiplication_table_frame.place(relx=0, rely=0, relwidth=1, relheight=1)# N.B multiplication_table_frame contains the multiplication tips

    multiplication_tips_image = Image.open("multiplication_tips.png")

    image_new_width = 600
    image_new_height = 400

    changed_image = multiplication_tips_image.resize((image_new_width,image_new_height), Image.Resampling.LANCZOS)

    multiplication_tips_image_tk= ImageTk.PhotoImage(changed_image) 
    multiplication_tips_image_label = tk.Label(root, text="",image =  multiplication_tips_image_tk)
    multiplication_tips_image_label.image =  multiplication_tips_image_tk
    multiplication_tips_image_label.place(x=350,y=100)

    new_image_label= multiplication_tips_image_label

    
def exit_multiplication_table():
    global new_image_label  
    multiplication_table_frame.place_forget()
    study_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    new_image_label.place_forget()
    new_image_label.destroy()
    
    
def quiz():
    # Functionality for "Quiz" button
    main_frame.place_forget()
    quiz_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

def exit_quiz():  # functionality to exit from the Quiz frame
    quiz_frame.place_forget()
    main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

def easy(): 
    quiz_frame.place_forget()
    easy_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    generate_easy_questions()

def exit_easy():
    easy_frame.place_forget()
    quiz_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

def medium():
    quiz_frame.place_forget()
    medium_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    generate_medium_questions()
def exit_medium():
    medium_frame.place_forget()
    quiz_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

def hard():
    quiz_frame.place_forget()
    hard_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    generate_hard_questions
def exit_hard():
    hard_frame.place_forget()
    quiz_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

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
    easy_frame.configure(bg=color)
    medium_frame.configure(bg=color)
    hard_frame.configure(bg=color)


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
    set_background_color("white")# changes bg colour to white

def set_dark_mode():
    set_background_color("black")# changes bg colour to black

def translate_gui(language):
    # Functionality to translate all GUI text elements
    translator = Translator()
    
    # List of all text elements to be translated
    text_elements = [
        label_title, buttons_study, buttons_quiz, button_settings,
        label_settings_title, button_language, button_background,
        button_exit_settings, label_change_background, label_background_text,
        radio_light_mode, radio_dark_mode, button_exit_background_settings,
        label_language_title, combobox_language, button_exit_language_settings,
        label_study, button_exit_study, button_multiplication_table,
        label_multiplication_table, button_exit_multiplication_table,
        label_quiz, button_exit_quiz, button_easy, button_medium, button_hard,
        label_easy, button_exit_easy,submit_button
    ]
    
    for element in text_elements:
        #checking whether the elemnt is a label or button widget
    
        if isinstance(element, (tk.Label, tk.Button)):
            # the translator translates the text element according to the selected destination of the language
            translated_text = translator.translate(element["text"], dest=language).text
             # update the text with translated text
            element.config(text=translated_text)
            # checking whether the combobox is a widget
        elif isinstance(element, ttk.Combobox):
            translated_values = [translator.translate(value, dest=language).text for value in element["values"]]
            #Update hte values of combobox with the translated values
            element.config(values=translated_values)
def generate_easy_questions():
    # Function to generate and display 20 easy multiplication questions
    global question_entries, answers
    question_entries = []
    answers = []#initialize the lists to store question labels and answer entries
    for i in range(20):
        #generating random numbers between 1 to 10
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        question_label = tk.Label(easy_frame, text=f"{num1} x {num2} =")
        question_label.grid(row=i, column=0, padx=10, pady=5)
        answer_entry = tk.Entry(easy_frame)
        answer_entry.grid(row=i, column=1, padx=10, pady=5)
        # Append the question label and answer entry to the question_entries list
        question_entries.append((question_label, answer_entry))
        answers.append(num1 * num2)

def check_easy_answers():
    correct = 0
    for i, (label, entry) in enumerate(question_entries):
        user_answer = entry.get()
        if user_answer.isdigit() and int(user_answer) == answers[i]:
            correct += 1
    result_label.config(text=f"Correct answers: {correct}/20")
    result_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def generate_medium_questions():
    global medium_question_entries, medium_answers
    medium_question_entries = []
    medium_answers = []
    for i in range(20):
        medium_num1 = randint(10, 99)
        medium_num2 = randint(1,10)
        medium_question_label = tk.Label(medium_frame, text=f"{medium_num1} x {medium_num2} =")
        medium_question_label.grid(row=i, column=0, padx=10, pady=5)
        medium_answer_entry = tk.Entry(medium_frame)
        medium_answer_entry.grid(row=i, column=1, padx=10, pady=5)
        medium_question_entries.append((medium_question_label, medium_answer_entry))
        medium_answers.append(medium_num1 * medium_num2)

def check_medium_answers():
    correct = 0
    for i, (medium_label, medium_entry) in enumerate(medium_question_entries):
        medium_user_answer = medium_entry.get()
        if medium_user_answer.isdigit() and int(medium_user_answer) == medium_answers[i]:
            correct += 1
    medium_result_label.config(text=f"Correct answers: {correct}/20")
    medium_result_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def generate_hard_questions():
    global hard_question_entries, hard_answers
    hard_question_entries = []
    hard_answers = []
    for i in range(20):
        hard_num1 = randint(100,1000)
        hard_num2 = randint(100,1000)
        hard_question_label = tk.Label(hard_frame, text=f"{hard_num1} x {hard_num2} =")
        hard_question_label.grid(row=i, column=0, padx=10, pady=5)
        hard_answer_entry = tk.Entry(hard_frame)
        hard_answer_entry.grid(row=i, column=1, padx=10, pady=5)
        hard_question_entries.append((hard_question_label, hard_answer_entry))
        hard_answers.append(hard_num1 * hard_num2)

def check_hard_answers():
    correct = 0
    for i, (hard_label, hard_entry) in enumerate(hard_question_entries):
        hard_user_answer = hard_entry.get()
        if hard_user_answer.isdigit() and int(hard_user_answer) == hard_answers[i]:
            correct += 1
    hard_result_label.config(text=f"Correct answers: {correct}/20")
    hard_result_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def zoom_in():
    global new_width,new_height,resized_image,image_tk
    new_width +=50
    new_height +=50
    resized_image = multiplication_table_image.resize((new_width,new_height),Image.Resampling.LANCZOS)
    image_tk = ImageTk.PhotoImage(resized_image)
    current_image_label.config(image=image_tk)
    current_image_label.image = image_tk
def zoom_out():
    global new_width,new_height,resized_image,image_tk
    if new_width > 50 and new_height > 50:
        new_width -=50
        new_height -=50
        resized_image = multiplication_table_image.resize((new_width,new_height),Image.Resampling.LANCZOS)
        image_tk = ImageTk.PhotoImage(resized_image)
        current_image_label.config(image=image_tk)
        current_image_label.image = image_tk


# Create main window
root = tk.Tk()
root.title("Multiplication teaching software")
root.geometry("800x600")




# Create main frame
main_frame = tk.Frame(root)
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# Create and place widgets
label_title = tk.Label(root, text="Solve and Learn Multiplication", font=("Arial", 24))
label_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

buttons_study = tk.Button(root, text="Study", command=study, width=17, height=3)
buttons_study.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

buttons_quiz = tk.Button(root, text="Quiz", command=quiz, width=17, height=3)
buttons_quiz.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

button_settings = tk.Button(root, text="Settings", command=settings)
button_settings.place(relx=0.9, rely=0.9, anchor=tk.SE)

settings_frame = tk.Frame(root)

# Create and place widgets for settings interface
label_settings_title = tk.Label(settings_frame, text="Settings", font=("Arial", 16))
label_settings_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)


button_language = tk.Button(settings_frame, text="Language", width=17, height=3, command=open_language_settings)
button_language.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button_background = tk.Button(settings_frame, text="Background", width=17, height=3, command=open_background_settings)
button_background.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

button_exit_settings = tk.Button(settings_frame, text="Exit", command=exit_settings)
button_exit_settings.place(relx=0.1, rely=0.9, anchor=tk.SW)

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

languages = ["English", "Spanish", "French", "German", "Bengali", "Arabic", "Russian", "Hindi", "Indonesian", "Portuguese", "Chinese", "Japanese", "Korean"]
combobox_language = ttk.Combobox(language_frame, values=languages)
combobox_language.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
combobox_language.bind("<<ComboboxSelected>>", change_language)

button_exit_language_settings = tk.Button(language_frame, text="Exit", command=exit_language_settings)
button_exit_language_settings.place(relx=0.1, rely=0.9, anchor=tk.SW)

study_frame = tk.Frame(root)

zoom_in_button = tk.Button(study_frame, text = "zoom in",command=zoom_in)
zoom_in_button.place(relx=0.1,rely=0.1,anchor=tk.SE)

zoom_out_button = tk.Button(study_frame, text="zoom out",command=zoom_out)
zoom_out_button.place(relx=0.9,rely=0.1,anchor=tk.SE)

# Create and place widget for study interface
label_study = tk.Label(study_frame, text="Multiplication Table", font=("Arial", 16))
label_study.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_study = tk.Button(study_frame, text="Exit", command=exit_study)
button_exit_study.place(relx=0.1, rely=0.9, anchor=tk.SW)

button_multiplication_table = tk.Button(study_frame, text="Next Page", command=multiplication_table)
button_multiplication_table.place(relx=0.9, rely=0.9, anchor=tk.SW)

multiplication_table_frame = tk.Frame(root)

label_multiplication_table = tk.Label(multiplication_table_frame, text="Multiplication Tips", font=("Arial", 16))
label_multiplication_table.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_multiplication_table = tk.Button(multiplication_table_frame, text="Exit", command=exit_multiplication_table)
button_exit_multiplication_table.place(relx=0.1, rely=0.9, anchor=tk.SW)

quiz_frame = tk.Frame(root)

label_quiz = tk.Label(quiz_frame, text="Select your difficulty", font=("Arial", 16))
label_quiz.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_quiz = tk.Button(quiz_frame, text="Exit", command=exit_quiz)
button_exit_quiz.place(relx=0.1, rely=0.9, anchor=tk.SW)

button_easy = tk.Button(quiz_frame, text="Easy", command=easy, width=17, height=3)
button_easy.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

button_medium = tk.Button(quiz_frame, text="Medium", command=medium, width=17, height=3)
button_medium.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

button_hard = tk.Button(quiz_frame, text="Hard", command=medium, width=17, height=3)
button_hard.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

easy_frame = tk.Frame(root)

label_easy = tk.Label(easy_frame, text="Type in the products", font=("Arial", 16))
label_easy.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_easy = tk.Button(easy_frame, text="Exit", command=exit_easy)
button_exit_easy.place(relx=0.5, rely=0.7, anchor=tk.SW)

submit_button = tk.Button(easy_frame, text="Submit", command=check_easy_answers)
submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# A label is created to display the result after checking answers. The text is empty initially
result_label = tk.Label(easy_frame, text="", font=("Arial", 16))


medium_frame = tk.Frame(root)
label_medium = tk.Label(medium_frame, text="Type in the products", font=("Arial", 16))
label_medium.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

submit_button = tk.Button(medium_frame, text="Submit", command=check_medium_answers)
submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

button_exit_medium = tk.Button(medium_frame, text="Exit", command=exit_medium)
button_exit_medium.place(relx=0.5, rely=0.7, anchor=tk.SW)

medium_result_label= tk.Label(medium_frame, text="", font=("Arial",16))


hard_frame = tk.Frame(root)
label_hard = tk.Label(hard_frame, text="Type in the products", font=("Arial", 16))
label_hard.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

button_exit_hard = tk.Button(hard_frame, text="Exit", command=exit_hard)
button_exit_hard.place(relx=0.1, rely=0.9, anchor=tk.SW)

submit_button = tk.Button(hard_frame, text="Submit", command=check_hard_answers)
submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

hard_result_label= tk.Label(hard_frame, text="", font=("Arial",16))

#hi guys welcome back to my new minecraft letsplay today we will be fixing piston sounds
root.mainloop()
