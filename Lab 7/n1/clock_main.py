import pygame
import sys
import datetime

pygame.init()

WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock_face = pygame.image.load("Lab 7/n1/images/clock.png")   
hand_minute = pygame.image.load("Lab 7/n1/images/leftarm.png")   
hand_second = pygame.image.load("Lab 7/n1/images/rightarm.png")   

center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    print(minutes)
    print(seconds)
    print("----")
    minute_angle = -(minutes * 6)-49     
    second_angle = -(seconds * 6)+60     

    rotated_minute = pygame.transform.rotate(hand_minute, minute_angle)
    rotated_second = pygame.transform.rotate(hand_second, second_angle)

    face_rect = clock_face.get_rect(center=(center_x, center_y))
    minute_rect = rotated_minute.get_rect(center=(center_x, center_y))
    second_rect = rotated_second.get_rect(center=(center_x, center_y))

    screen.fill((255, 255, 255))           
    screen.blit(clock_face, face_rect)     
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()