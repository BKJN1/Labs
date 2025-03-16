import pygame
import os

pygame.init()

screen_width, screen_height = 1000, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

music_dir = "Lab 7/n2/musics"  
playlist = [os.path.join(music_dir, song) for song in os.listdir(music_dir) if song.endswith(".mp3")]
current_track = 0

pygame.mixer.music.load(playlist[current_track])

def display_interface():
    screen.fill(WHITE) 

    controls_text = small_font.render("Controls: P (Play)  |  S (Stop)  |  N (Next)  |  B (Previous)", True, BLACK)
    screen.blit(controls_text, (20, 20))

    track_text = font.render(f"Now Playing: {os.path.basename(playlist[current_track])}", True, BLACK)
    screen.blit(track_text, (20, 80))

    status_text = small_font.render("Press Q to Quit", True, GRAY)
    screen.blit(status_text, (20, 150))
    pygame.display.flip()



def play_music():
    pygame.mixer.music.play()
    display_interface()

def stop_music():
    pygame.mixer.music.stop()
    display_interface()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    play_music()

display_interface()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:  
                stop_music()
            elif event.key == pygame.K_n: 
                next_track()
            elif event.key == pygame.K_b:  
                previous_track()
            elif event.key == pygame.K_q:  
                running = False

    display_interface()

pygame.quit()
print("Music player closed.")