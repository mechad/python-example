import pygame

def play_wav(wav_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(wav_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    pygame.quit()

wav_file = "test.wav"
play_wav(wav_file)

