import tkinter as tk
from text_analysis import analyze_text
from text_to_speech import text_to_speech_pygame  # Change the import statement
from gtts import lang

# Print the list of supported languages
print(lang.tts_langs())

def on_speak():
    text = entry.get()
    analysis_result = analyze_text(text)
    lang_code = lang_var.get()

    # Use the modified text_to_speech_pygame function
    text_to_speech_pygame(text, lang_code, analysis_result)

    # If you want to use advanced_text_to_speech for specific cases, uncomment the following line
    # advanced_text_to_speech(text, analysis_result)

    # If you want to use WhisperSpeech, uncomment the following line
    # use_whisperspeech(text)

    # If you want to use character_voice_tts, uncomment the following line
    # character_voice_tts(text, character_parameter)

root = tk.Tk()
root.title("Text-to-Speech App")

tk.Label(root, text="Enter Text:").pack()
entry = tk.Entry(root, width=50)
entry.pack()

tk.Label(root, text="Select Language:").pack()
lang_var = tk.StringVar(root)
lang_var.set("en")  # default language
languages = ["en", "es", "de", "fr", "ja", "fi", "zh-CN", "sv"]  # Add "fi" for Finnish
lang_menu = tk.OptionMenu(root, lang_var, *languages)
lang_menu.pack()

speak_button = tk.Button(root, text="Speak", command=on_speak)
speak_button.pack()

root.mainloop()