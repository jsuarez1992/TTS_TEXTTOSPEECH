from gtts import gTTS
import pygame
import os
from googletrans import Translator, LANGUAGES

def translate_word(word, input_lang_code, output_lang_code):
    translator = Translator()
    translation = translator.translate(word, src=input_lang_code, dest=output_lang_code)
    return translation.text

def text_to_speech_pygame(text, input_lang_code, analysis_result, output_lang_code):
    translated_text = translate_word(text, input_lang_code, output_lang_code)

    output_tts = gTTS(text=translated_text, lang=output_lang_code, slow=analysis_result['rate'] == 'slow')
    output_filename = 'temp_output_audio.mp3'
    output_tts.save(output_filename)

    pygame.mixer.init()
    pygame.mixer.music.load(output_filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

    # Remove temporary file
    os.remove(output_filename)
