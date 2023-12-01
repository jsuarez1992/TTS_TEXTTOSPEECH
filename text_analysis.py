import tkinter as tk
from tkinter import ttk, OptionMenu, messagebox
import pyttsx3
import langid
from langid.langid import LanguageIdentifier, model
from nltk.sentiment import SentimentIntensityAnalyzer

from text_to_speech import text_to_speech_pygame  # Assuming you have a module named text_to_speech

class SentimentAnalysisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analysis GUI")

        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()

        self.create_widgets()

    def create_widgets(self):
        # Text Input
        self.label = ttk.Label(self.root, text="Enter Text:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.text_input = tk.Text(self.root, height=5, width=40)
        self.text_input.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # Analyze Button
        self.analyze_button = ttk.Button(self.root, text="Analyze", command=self.analyze_and_speak)
        self.analyze_button.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

    def analyze_and_speak(self):
        text_to_analyze = self.text_input.get("1.0", tk.END).strip()

        if not text_to_analyze:
            self.speak("Please enter some text for analysis.")
            return

        result = self.enhanced_analyze_text(text_to_analyze)

        analysis_result = (
             f"{result['mood']}\n"
            #f"Content Type: {result['content_type']}\n"
            #f"Sentiment: {result['sentiment']}\n"
            #f"Mood: {result['mood']}\n"
            #f"Language: {result['language']}\n"
            #f"Rate: {result['rate']}"
        )

        self.speak(analysis_result)

    def enhanced_analyze_text(self, text):
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        mood = self.map_sentiment_to_mood(sentiment['compound'])

        if text.strip().endswith('?'):
            content_type = 'question'
        elif text.strip().endswith('!'):
            content_type = 'exclamation'
        else:
            content_type = 'statement'

        if content_type == 'question':
            rate = 'slow'
        elif content_type == 'exclamation' or sentiment['compound'] > 0.5:
            rate = 'fast'
        else:
            rate = 'medium'

        identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
        detected_lang, _ = identifier.classify(text)

        return {'rate': rate, 'content_type': content_type, 'sentiment': sentiment['compound'], 'mood': mood,
                'language': detected_lang}


    def map_sentiment_to_mood(self, sentiment_score):
        if sentiment_score > 0.5:
            return "You go queen."
        elif -0.5 <= sentiment_score <= 0.5:
            return "Please set a car on fire or something."
        else:
            return "Do you need a hug?"
    def speak(self, text):
        #print("Available voices:")
        #for voice in self.engine.getProperty('voices'):
            #print(voice.id)


        # Use the text-to-speech engine to speak the given text
        self.engine.setProperty('rate', 150)
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        self.engine.setProperty('voice', voice_id)
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalysisGUI(root)
    root.mainloop()
