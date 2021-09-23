import pygame
import random
import os

pygame.mixer.init()
pygame.init()
# define colour
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green = (0,255,0)
g_over = (23,64,241)
# Game window
screen_width=800
screen_height=550
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake 2.O")
pygame.display.update()
font=pygame.font.SysFont(None,35)
clock=pygame.time.Clock()

def text(text,color,x,y):
    '''Display text in screen'''
    screen_text=font.render(text,True,color)
    window.blit(screen_text,[x,y])

def plot_snake(window,color, snk_list, snake_size):
    '''Draw snake on window '''
    for x,y in snk_list:    
        pygame.draw.rect(window,color,[x,y,snake_size,snake_size])

def home_screen():
    window.fill((222,232,242))
    exit_game = False
    while not exit_game:
        text("Welcome to Snakes",black,275,250)
        text("Press space bar to Start Game",black,220,280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                goodbye()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("bg_music.mp3")
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

def goodbye():
    window.fill(black)
    exit_game = False
    while not exit_game:
        text("Thank You",white,350,250)
        exit_game = True
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

# game loop
def game_loop():
    # Specific Variable
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 60
    snake_size = 15
    velocity_x = 0
    velocity_y = 0
    score = 0
    init_velocity = 5
    fps = 60
    snk_length = 0
    snk_list = []
    food_x = random.randint(50, screen_width/2)
    food_y = random.randint(50, screen_height/2)
    if (not os.path.exists("high_score.txt")):
        with open("high_score.txt","w") as f:
            f.write("0")

    with open("high_score.txt","r") as f:
        hi_score = f.read()
        
    while not exit_game:
        if game_over:
            window.fill(g_over)
            text("High Score : "+ str(hi_score),green,600,15)
            text("Your Score : "+ str(score), green, 5,15)
            text("Game Over Press Enter to continue...",red,200,300)
            text("Press 'Q' to quit the game",black,480,520)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    goodbye()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        home_screen()
                    if event.key == pygame.K_q:
                        goodbye()

        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    goodbye()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = - init_velocity
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity
                    if event.key == pygame.K_q:
                        goodbye()
                    if event.key == (pygame.KMOD_ALT and pygame.K_F4):
                        goodbye()
            
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            # in this put their food in random location and increase their lenght also
            if abs(snake_x - food_x)<7 and abs(snake_y - food_y)<7:
                score += 10
                # print("Score :", score)
                food_x = random.randint(0,screen_width-10)
                food_y = random.randint(0,screen_height-10)
                snk_length += 5
                if score>int(hi_score):
                    hi_score = score
                    with open("high_score.txt","r+") as f:
                        f.write(str(hi_score))

            window.fill(black)
            text("High Score : "+ str(hi_score),blue,600,5)
            text("Press 'Q' to quit the game",red,480,520)
            text("Score : "+ str(score),blue,5,5)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            pygame.draw.rect(window, green, [food_x, food_y, snake_size, snake_size])
            plot_snake(window,white,snk_list,snake_size)
                    
            # Increase the size of snake
            if len(snk_list)>snk_length:
                del snk_list[0]
            # Game over when collision by itself 
            if head in snk_list [: -1]:
                game_over = True
                pygame.mixer.music.load("songs.mp3")
                pygame.mixer.music.play()
            # Game  over when collision in walls
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height: 
                game_over = True
                pygame.mixer.music.load("songs.mp3")
                pygame.mixer.music.play()
                # print("Game Over")


        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()
home_screen()