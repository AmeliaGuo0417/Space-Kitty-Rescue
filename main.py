import pygame
import random
import time
# Initialize pygame
pygame.init()

global user_choice 
user_choice = "play"


# Screen dimensions
screen_width = 1400
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Character image
cat_image = pygame.image.load("cutie/Cat")
cat_rect = cat_image.get_rect() 
cat_image = pygame.transform.scale(cat_image, (100, 100))

# object lists
smallList = ["Apple","Banana", "Bottle", "Skull"]
largeList = ["Rock1","Rock1","Rock1", "Rock1","Skeleton"]


# Function to generate random position on screen
def generate_random_position():
    x = random.randint(0, screen_width - cat_rect.width)
    y = random.randint(0, screen_height - cat_rect.height)
    return x, y

# function displays all space junk
def draw_junk():
    # Draw space junk

    # one random satellite
    junk_image = pygame.image.load("cutie/Satellite")
    junk_rect = junk_image.get_rect() 
    junk_rect.x, junk_rect.y = generate_random_position() 
    junk_image = pygame.transform.scale(junk_image, (600, 300))
    screen.blit(junk_image, junk_rect)

    j = 1
    while j < 8:
        junk_name = random.choice(largeList)
        junk_image = pygame.image.load("cutie/"+junk_name)
        junk_rect = junk_image.get_rect() 
        junk_rect.x, junk_rect.y = generate_random_position() 
        junk_image = pygame.transform.rotate(junk_image, random.randint(1, 360))
        if (junk_name == "Rock1"):
            junk_image = pygame.transform.scale(junk_image, (250, 250))
        else:
            junk_image = pygame.transform.scale(junk_image, (300, 250))

        # random location for junk
        screen.blit(junk_image, junk_rect)
        #print(j)
        j = j + 1
    i = 1
    while i < 30:
        junk_name = random.choice(smallList)
        junk_image = pygame.image.load("cutie/"+junk_name)
        junk_image = pygame.transform.scale(junk_image, (150, 150))
        junk_rect = junk_image.get_rect() 
        junk_rect.x, junk_rect.y = generate_random_position() 
        junk_image = pygame.transform.rotate(junk_image, random.randint(1, 360))
        # random location for junk
        screen.blit(junk_image, junk_rect)
        #print(i)
        i = i + 1

def game_with_timer(time_limit):
    start_time = time.time()  # Get current time
    score = 0 
    return start_time

# Game loop
def game(round):
   
    while (round == 1):
        screen.fill(black)
        start_image = pygame.image.load("cutie/Start")
        start_image = pygame.transform.scale(start_image, (700, 700))
        start_rect = start_image.get_rect() 
        start_rect.x = 0
        start_rect.y = 0
        # random location for junk
        screen.blit(start_image, start_rect)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() 
                if start_rect.collidepoint(mouse_pos):
                    round = 2
        
    
    if (round >=1 and round <= 3):
        # Set initial Cat position
        cat_rect.x, cat_rect.y = generate_random_position() 
    
        screen.fill(black)
        draw_junk()
        
        time_limit = 10
        start_time = game_with_timer(10)
        while time.time() - start_time < time_limit: 
    
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos() 
                        if cat_rect.collidepoint(mouse_pos):
                            print("You found Purple Cat!")
                            return True
                            #cat_rect.x, cat_rect.y = generate_random_position() 
                        else:
                            return False
    
                # Draw Cat
                screen.blit(cat_image, cat_rect)
    
                pygame.display.flip()
            
            
            #screen.fill(black)
    
            return False








        
    #  Update score based on action
        print("Current score:")
    elif (round == 4):
        stay = True
        while stay:
            screen.fill(black)
            win_image = pygame.image.load("cutie/Win")
            win_image = pygame.transform.scale(win_image, (700, 700))
            win_rect = win_image.get_rect() 
            win_rect.x = 0
            win_rect.y = 0
            # random location 
            screen.blit(win_image, win_rect)
            #pygame.display.flip()

            # cat to the right
            end_cat_image = pygame.image.load("cutie/EndCat")
            end_cat_image = pygame.transform.scale(end_cat_image, (700, 700))
            end_cat_rect = end_cat_image.get_rect() 
            end_cat_rect.x = 700
            end_cat_rect.y = 0
            screen.blit(end_cat_image, end_cat_rect)
            #pygame.display.flip()

            play_again_image = pygame.image.load("cutie/PlayAgain")
            play_again_image = pygame.transform.scale(play_again_image, (423, 262))
            play_again_rect = play_again_image.get_rect() 
            play_again_rect.x = 1000
            play_again_rect.y = 200
            screen.blit(play_again_image, play_again_rect)
            #pygame.display.flip()

            stop_image = pygame.image.load("cutie/Stop")
            stop_image = pygame.transform.scale(stop_image, (306, 140))
            stop_rect = stop_image.get_rect() 
            stop_rect.x = 1000
            stop_rect.y = 500
            screen.blit(stop_image, stop_rect)
            pygame.display.flip()

            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos() 
                    if play_again_rect.collidepoint(mouse_pos):
                        user_choice = "play"
                        return True
                    elif stop_rect.collidepoint(mouse_pos):
                        user_choice = "stop"
                        return True
        
    elif (round == 0):
        stay = True
        while stay:
            #success image display
            screen.fill(black)
            loss_image = pygame.image.load("cutie/Loss")
            loss_image = pygame.transform.scale(loss_image, (700, 700))
            loss_rect = loss_image.get_rect() 
            loss_rect.x = 0
            loss_rect.y = 0
            screen.blit(loss_image, loss_rect)
            #pygame.display.flip()

            # cat to the right
            end_cat_image = pygame.image.load("cutie/EndCat")
            end_cat_image = pygame.transform.scale(end_cat_image, (700, 700))
            end_cat_rect = end_cat_image.get_rect() 
            end_cat_rect.x = 700
            end_cat_rect.y = 0
            screen.blit(end_cat_image, end_cat_rect)
            #pygame.display.flip()


            play_again_image = pygame.image.load("cutie/PlayAgain")
            play_again_image = pygame.transform.scale(play_again_image, (423, 262))
            play_again_rect = play_again_image.get_rect() 
            play_again_rect.x = 1000
            play_again_rect.y = 200
            screen.blit(play_again_image, play_again_rect)
            #pygame.display.flip()

            stop_image = pygame.image.load("cutie/Stop")
            stop_image = pygame.transform.scale(stop_image, (306, 140))
            stop_rect = stop_image.get_rect() 
            stop_rect.x = 1000
            stop_rect.y = 500
            screen.blit(stop_image, stop_rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos() 
                    if play_again_rect.collidepoint(mouse_pos):
                        
                        return True
                    elif stop_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        return False

            
    

def main():
    rounds = 1
    if game(rounds):
        rounds = 2
        #print("You won round 1!")
        if game(rounds):
            rounds = 3
            #print("You won round 2!")
            if game(rounds):
                rounds = 4
                if game(rounds):
                    start()
                #print("You won round 3!")
                
            else:
                #print("You lost")
                rounds = 0
                if game(rounds):
                    start()
        else:
            #print("You lost")
            rounds = 0
            if game(rounds):
                start()
            

    else:
        #print("you lost")
        rounds = 0
        if game(rounds):
            start()


        
print("Time's up! Final score:") 


def start():
    if (user_choice == "play"):
        main()


if __name__ == "__main__":
    start()

    pygame.quit()




