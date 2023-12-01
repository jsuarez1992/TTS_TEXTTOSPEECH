from gtts import gTTS
import pygame
import os


def text_to_speech_pygame(text, lang, analysis_result):
    tts = gTTS(text=text, lang=lang, slow=analysis_result['rate'] == 'slow')
    filename = 'temp_audio.mp3'
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    os.remove(filename)