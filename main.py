# main.py

import tkinter as tk
from text_analysis import analyze_text
from text_to_speech import text_to_speech_pygame
from gtts import lang

# Print the list of supported languages
print(lang.tts_langs())

def on_speak():
    text = entry.get()
    analysis_result = analyze_text(text)
    input_lang_code = lang_var_input.get()  # Language for input text
    output_lang_code = lang_var_output.get()  # Language for output speech

    # Use the modified text_to_speech_pygame function
    text_to_speech_pygame(text, input_lang_code, analysis_result, output_lang_code)

root = tk.Tk()
root.title("Text-to-Speech App")

tk.Label(root, text="Enter Text:").pack()
entry = tk.Entry(root, width=50)
entry.pack()

tk.Label(root, text="Select Input Language:").pack()
lang_var_input = tk.StringVar(root)
lang_var_input.set("en")  # default input language
input_languages = ["en", "es", "de", "fr", "ja", "fi", "zh-CN", "sv"]
lang_menu_input = tk.OptionMenu(root, lang_var_input, *input_languages)
lang_menu_input.pack()

tk.Label(root, text="Select Output Language:").pack()
lang_var_output = tk.StringVar(root)
lang_var_output.set("en")  # default output language
output_languages = ["en", "es", "de", "fr", "ja", "fi", "zh-CN", "sv"]
lang_menu_output = tk.OptionMenu(root, lang_var_output, *output_languages)
lang_menu_output.pack()

speak_button = tk.Button(root, text="Speak", command=on_speak)
speak_button.pack()

root.mainloop()
