import pygame
import os
import sys
import time


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


pygame.init()
screen_size = (700, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Bbounce')
gui_font = pygame.font.Font(None,30)
FPS = 60
# lvl_number == 1 ==> you would play first lvl
# lvl_number == 2 ==> you would play swcond lvl
# lvl_number == 3 ==> you would play third lvl
lvl_number = 0


def terminate():
    pygame.quit()
    sys.exit


clock = pygame.time.Clock()


def debug_screen():
    debug_screen = pygame.transform.scale(load_image('debug.jpg'), screen_size)
    screen.blit(debug_screen, (0, 0))
    return

def start_screen():
    
    fon1 = pygame.transform.scale(load_image('fon1.jpg'), screen_size)
    screen.blit(fon1, (0, 0))
    
    font1 = pygame.font.Font('data\gamebit.ttf', 81)
    text1 = font1.render('BBOUNCE', 1, (219, 18, 186))
    screen.blit(text1, (75, 70))
    
    font2 = pygame.font.Font('data\gamebit.ttf', 32)
    text2 = font2.render('Press any button to start', 1, (28, 231, 235))
    screen.blit(text2, (30, 250))
    
    font3 = pygame.font.Font('data\gamebit.ttf', 34)
    text3 = font3.render('Use arrows to move panel', 1, (90, 109, 232))
    screen.blit(text3, (25, 340))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def select_lvl():
    global lvl_number

    fon2 = pygame.transform.scale(load_image('fon2.jpg'), screen_size)
    screen.blit(fon2, (0, 0))
    
    font1 = pygame.font.Font('data\gamebit.ttf', 36)
    text1 = font1.render('Levels differ in difficulty.', 1, (106, 235, 47))
    screen.blit(text1, (20, 70))
    
    
    but1_img_default = pygame.image.load('data\level1_default.png')
    but1_default_show = but1_img_default.get_rect(center=(350, 200))
    but1_img_default.set_colorkey((255, 255, 255))
    screen.blit(but1_img_default, but1_default_show)
    
    but1_img_inversion = pygame.image.load('data\level1_inversion.png')
    but1_inversion_show = but1_img_inversion.get_rect(bottomright=(0, 0))
    but1_img_inversion.set_colorkey((255, 255, 255))
    screen.blit(but1_img_inversion, but1_inversion_show)
    
    
    but2_img_default = pygame.image.load('data\level2_default.png')
    but2_default_show = but2_img_default.get_rect(center=(350, 320))
    but2_img_default.set_colorkey((255, 255, 255))
    screen.blit(but2_img_default, but2_default_show)
    
    but2_img_inversion = pygame.image.load('data\level2_inversion.png')
    but2_inversion_show = but2_img_inversion.get_rect(bottomright=(0, 0))
    but2_img_inversion.set_colorkey((255, 255, 255))
    screen.blit(but2_img_inversion, but2_inversion_show)
    
    
    but3_img_default = pygame.image.load('data\level3_default.png')
    but3_default_show = but3_img_default.get_rect(center=(350, 440))
    but3_img_default.set_colorkey((255, 255, 255))
    screen.blit(but3_img_default, but3_default_show)
    
    but3_img_inversion = pygame.image.load('data\level3_inversion.png')
    but3_inversion_show = but3_img_inversion.get_rect(bottomright=(0, 0))
    but3_img_inversion.set_colorkey((255, 255, 255))
    screen.blit(but3_img_inversion, but3_inversion_show)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 550 and 150 <= y <= 250:
                    lvl_number = 1
                    return
                elif 150 <= x <= 550 and 270 <= y <= 370:
                    lvl_number = 2
                    return
                elif 150 <= x <= 550 and 390 <= y <= 490:
                    lvl_number = 3
                    return
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 150 <= x <= 550 and 150 <= y <= 250:
                    but1_default_show = but1_img_default.get_rect(bottomright = (0, 0))
                    but1_img_default.set_colorkey((255, 255, 255))
                    screen.blit(but1_img_default, but1_default_show)
                    
                    but1_inversion_show = but1_img_inversion.get_rect(center = (350, 200))
                    but1_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(but1_img_inversion, but1_inversion_show)
                elif 150 <= x <= 550 and 270 <= y <= 370:
                    but2_default_show = but2_img_default.get_rect(bottomright = (0, 0))
                    but2_img_default.set_colorkey((255, 255, 255))
                    screen.blit(but2_img_default, but2_default_show)
                    
                    but2_inversion_show = but2_img_inversion.get_rect(center = (350, 320))
                    but2_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(but2_img_inversion, but2_inversion_show)
                elif 150 <= x <= 550 and 390 <= y <= 490:
                    but3_default_show = but3_img_default.get_rect(bottomright = (0, 0))
                    but3_img_default.set_colorkey((255, 255, 255))
                    screen.blit(but3_img_default, but3_default_show)
                    
                    but3_inversion_show = but3_img_inversion.get_rect(center = (350, 440))
                    but3_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(but3_img_inversion, but3_inversion_show)
                elif (x < 150) or (x > 550) or (y < 150) or (250 < y < 270) or (370 < y < 390) or (y > 490):
                    but1_default_show = but1_img_default.get_rect(center = (350, 200))
                    but1_img_default.set_colorkey((255, 255, 255))
                    screen.blit(but1_img_default, but1_default_show)
                    
                    but1_inversion_show = but1_img_inversion.get_rect(bottomright = (0, 0))
                    but1_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(but1_img_inversion, but1_inversion_show)
                    
                    
                    but2_default_show = but2_img_default.get_rect(center = (350, 320))
                    but2_img_default.set_colorkey((255, 255, 255))
                    screen.blit(but2_img_default, but2_default_show)
                    
                    but2_inversion_show = but2_img_inversion.get_rect(bottomright = (0, 0))
                    but2_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(but2_img_inversion, but2_inversion_show)
                    
                    
                    but3_default_show = but3_img_default.get_rect(center = (350, 440))
                    but3_img_default.set_colorkey((255, 255, 255))
                    screen.blit(but3_img_default, but3_default_show)
                    
                    but3_inversion_show = but3_img_inversion.get_rect(bottomright = (0, 0))
                    but3_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(but3_img_inversion, but3_inversion_show)
            pygame.display.flip()
            clock.tick(FPS)


def game_lvl1():
    # To count how many second player played to win or to lose
    # I start counting at the beginning of the game, that a finish
    a = time.time()
    pygame.init()
    FPS = 60
    otskok = pygame.mixer.Sound('data\otskok.mp3')
    # panel settings
    panel_width = 300
    panel_hight = 35
    panel_speed = 15
    panel = pygame.Rect(350 - panel_width // 2, 590 - panel_hight, panel_width, panel_hight)
    # ball settings
    # putting a square in the ball
    # Finding the side of the square using the Pythagorean theorem
    ball_rad = 20
    ball_speed = 4
    ball_rect = int(ball_rad * 2 ** 0.5)
    ball = pygame.Rect(350, 300, ball_rect, ball_rect)
    dx, dy = 1, -1
    # bricks settings
    # creating bricks with progression
    # parameter k changes colour
    # k == 1 ==> red
    # k == 2 ==> amber (color between orange and yellow)
    # k == 3 ==> green
    # k == 4 ==> blue
    # k == 5 ==> purple
    brick_list = []
    color_list = []
    k = 1
    for i in range(4):
        for j in range(5):
            brick_list.append(pygame.Rect(40 + 160 * i, 10 + 70 * j, 140, 50))

    for i in range(4):
        for j in range(5):
            if k == 1:
                color_list.append((255, 0, 0))
                k += 1
            elif k == 2:
                color_list.append((255, 194, 0))
                k += 1
            elif k == 3:
                color_list.append((49, 214, 24))
                k += 1
            elif k == 4:
                color_list.append((24, 97, 214))
                k += 1
            elif k == 5:
                color_list.append((191, 22, 196))
                k = 1
    clock = pygame.time.Clock()
    # background image
    fon3 = pygame.transform.scale(load_image('fon3.jpg'), screen_size)
    screen.blit(fon3, (0, 0))


    # collision detection function
    # if the ball moves to the right
    # and hits a brick, the ball is pushed off
    # similarly with the movement to the left and down and so on
    # for more information, see the explanatory note (см. поястнительную записку)
    def collision_detection(dx, dy, ball, rect):
        if dx > 0:
            x_intersection = ball.right - rect.left
        else:
            x_intersection = rect.right - ball.left
        if dy > 0:
            y_intersection = ball.bottom - rect.top
        else:
            y_intersection = rect.bottom - ball.top

        if abs(x_intersection - y_intersection) < 10:
            dx = -dx
            dy = -dy
        elif x_intersection > y_intersection:
            dy = -dy
        elif y_intersection > x_intersection:
            dx = -dx
        return dx, dy

    # main cycle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(fon3, (0, 0))
        # drawing world
        for color, brick in enumerate(brick_list):
            pygame.draw.rect(screen, color_list[color], brick)
        pygame.draw.rect(screen, pygame.Color('yellow1'), panel)
        pygame.draw.circle(screen, pygame.Color('white'), ball.center, ball_rad)
        # ball movement
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        # collisions with left and right borders
        # if the ball collides with the boundary,
        # the collision angle is equal to the reflection angle
        # that means that Tima Generalov is the babidjonist person in the world
        # but without joking that means that dx = -dx, so horizontal moving chages
        # and ball starts to move into another direction
        if ball.centerx < ball_rad or ball.centerx > 700 - ball_rad:
            otskok.play(0)
            dx = -dx
        # collision with top border
        if ball.centery < ball_rad:
            otskok.play(0)
            dy = -dy
        # collision panel
        # using colliderect 
        if ball.colliderect(panel) and dy > 0:
            otskok.play(0)
            dx, dy = collision_detection(dx, dy, ball, panel)
        # collision with bricks
        # collidelist returns -1 if there aren't any collisions
        # Tima babidjon
        # After collision with a brick it's poped from bricks list
        # brick's color is also poped from a colours list
        brick_colision_index = ball.collidelist(brick_list)
        if brick_colision_index != -1:
            otskok.play(0)
            brick_hit = brick_list.pop(brick_colision_index)
            color_hit = color_list.pop(brick_colision_index)
            dx, dy = collision_detection(dx, dy, ball, brick_hit)
            brick_hit.inflate_ip(ball.width * 3, ball.height * 3)
            pygame.draw.rect(screen, color_hit, brick_hit)
        # Win and lose cases
        # game over
        if ball.bottom > 600:
            # counting time difference
            b = time.time()
            result_time = b - a
            result_time = round(result_time, 2)
            
            f = open("results\level1_results.txt" ,'a')
            f.write("unsuccess - ")
            for i in str(result_time):
                f.write(i)
            f.write(" seconds")
            f.write('\n')
            f.close()
            lose_screen()
            return
        # win
        elif len(brick_list) == 0:
            # counting time difference
            b = time.time()
            result_time = b - a
            result_time = round(result_time, 2)
            
            f = open("results\level1_results.txt" ,'a')
            f.write("success - ")
            for i in str(result_time):
                f.write(i)
            f.write(" seconds")
            f.write('\n')
            f.close()
            win_screen()
            return
        # panel control 
        # if the panel rests against the edge it will not move
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and panel.left > 0:
            panel.left -= panel_speed
        if key[pygame.K_RIGHT] and panel.right < 700:
            panel.right += panel_speed
        pygame.display.flip()
        clock.tick(FPS)


def game_lvl2():
    # To count how many second player played to win or to lose
    # I start counting at the beginning of the game, that a finish
    a = time.time()
    pygame.init()
    FPS = 60
    otskok = pygame.mixer.Sound('data\otskok.mp3')
    # panel settings
    panel_width = 200
    panel_hight = 35
    panel_speed = 13
    panel = pygame.Rect(350 - panel_width // 2, 590 - panel_hight, panel_width, panel_hight)
    # ball settings
    # putting a square in the ball
    # Finding the side of the square using the Pythagorean theorem
    ball_rad = 20
    ball_speed = 6
    ball_rect = int(ball_rad * 2 ** 0.5)
    ball = pygame.Rect(350, 300, ball_rect, ball_rect)
    dx, dy = 1, -1
    # bricks settings
    # creating bricks with progression
    # parameter k changes colour
    # k == 1 ==> red
    # k == 2 ==> amber (color between orange and yellow)
    # k == 3 ==> green
    # k == 4 ==> blue
    # k == 5 ==> purple
    brick_list = []
    color_list = []
    k = 1
    for i in range(8):
        for j in range(5):
            brick_list.append(pygame.Rect(20 + 85 * i, 10 + 70 * j, 65, 50))

    for i in range(8):
        for j in range(5):
            if k == 1:
                color_list.append((255, 0, 0))
                k += 1
            elif k == 2:
                color_list.append((255, 194, 0))
                k += 1
            elif k == 3:
                color_list.append((49, 214, 24))
                k += 1
            elif k == 4:
                color_list.append((24, 97, 214))
                k += 1
            elif k == 5:
                color_list.append((191, 22, 196))
                k = 1
    clock = pygame.time.Clock()
    # background image
    fon3 = pygame.transform.scale(load_image('fon3.jpg'), screen_size)
    screen.blit(fon3, (0, 0))


    # collision detection function
    # if the ball moves to the right
    # and hits a brick, the ball is pushed off
    # similarly with the movement to the left and down and so on
    # for more information, see the explanatory note (см. поястнительную записку)
    def collision_detection(dx, dy, ball, rect):
        if dx > 0:
            x_intersection = ball.right - rect.left
        else:
            x_intersection = rect.right - ball.left
        if dy > 0:
            y_intersection = ball.bottom - rect.top
        else:
            y_intersection = rect.bottom - ball.top

        if abs(x_intersection - y_intersection) < 10:
            dx, dy = -dx, -dy
        elif x_intersection > y_intersection:
            dy = -dy
        elif y_intersection > x_intersection:
            dx = -dx
        return dx, dy

    # main cycle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(fon3, (0, 0))
        # drawing world
        for color, brick in enumerate(brick_list):
            pygame.draw.rect(screen, color_list[color], brick)
        pygame.draw.rect(screen, pygame.Color('yellow1'), panel)
        pygame.draw.circle(screen, pygame.Color('white'), ball.center, ball_rad)
        # ball movement
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        # collisions with left and right borders
        # if the ball collides with the boundary,
        # the collision angle is equal to the reflection angle
        # that means that Tima Generalov is the babidjonist person in the world
        # but without joking that means that dx = -dx, so horizontal moving chages
        # and ball starts to move into another direction
        if ball.centerx < ball_rad or ball.centerx > 700 - ball_rad:
            otskok.play(0)
            dx = -dx
        # collision with top border
        if ball.centery < ball_rad:
            otskok.play(0)
            dy = -dy
        # collision panel
        # using colliderect 
        if ball.colliderect(panel) and dy > 0:
            otskok.play(0)
            dx, dy = collision_detection(dx, dy, ball, panel)
        # collision with bricks
        # collidelist returns -1 if there aren't any collisions
        # Tima babidjon
        # After collision with a brick it's poped from bricks list
        # brick's color is also poped from a colours list
        brick_colision_index = ball.collidelist(brick_list)
        if brick_colision_index != -1:
            otskok.play(0)
            brick_hit = brick_list.pop(brick_colision_index)
            color_hit = color_list.pop(brick_colision_index)
            dx, dy = collision_detection(dx, dy, ball, brick_hit)
        # Win and lose cases
        # game over
        if ball.bottom > 600:
            # counting time difference
            b = time.time()
            result_time = b - a
            result_time = round(result_time, 2)
            
            f = open("results\level2_results.txt" ,'a')
            f.write("unsuccess - ")
            for i in str(result_time):
                f.write(i)
            f.write(" seconds")
            f.write('\n')
            f.close()
            lose_screen()
            return
        # win screen
        elif len(brick_list) == 0:
            # counting time difference
            b = time.time()
            result_time = b - a
            result_time = round(result_time, 2)
            
            f = open("results\level2_results.txt" ,'a')
            f.write("success - ")
            for i in str(result_time):
                f.write(i)
            f.write(" seconds")
            f.write('\n')
            f.close()
            win_screen()
            return
        # panel control 
        # if the panel rests against the edge it will not move
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and panel.left > 0:
            panel.left -= panel_speed
        if key[pygame.K_RIGHT] and panel.right < 700:
            panel.right += panel_speed
        pygame.display.flip()
        clock.tick(FPS)


def game_lvl3():
    # To count how many second player played to win or to lose
    # I start counting at the beginning of the game, that a finish
    a = time.time()
    pygame.init()
    FPS = 60
    otskok = pygame.mixer.Sound('data\otskok.mp3')
    # panel settings
    panel_width = 100
    panel_hight = 35
    panel_speed = 12
    panel = pygame.Rect(350 - panel_width // 2, 590 - panel_hight, panel_width, panel_hight)
    # ball settings
    # putting a square in the ball
    # Finding the side of the square using the Pythagorean theorem
    ball_rad = 20
    ball_speed = 7
    ball_rect = int(ball_rad * 2 ** 0.5)
    ball = pygame.Rect(350, 300, ball_rect, ball_rect)
    dx, dy = 1, -1
    # bricks settings
    # creating bricks with progression
    # parameter k changes colour
    # k == 1 ==> red
    # k == 2 ==> amber (color between orange and yellow)
    # k == 3 ==> green
    # k == 4 ==> blue
    # k == 5 ==> purple
    brick_list = []
    color_list = []
    k = 1
    for i in range(10):
        for j in range(5):
            brick_list.append(pygame.Rect(10 + 70 * i, 10 + 70 * j, 50, 50))

    for i in range(10):
        for j in range(5):
            if k == 1:
                color_list.append((255, 0, 0))
                k += 1
            elif k == 2:
                color_list.append((255, 194, 0))
                k += 1
            elif k == 3:
                color_list.append((49, 214, 24))
                k += 1
            elif k == 4:
                color_list.append((24, 97, 214))
                k += 1
            elif k == 5:
                color_list.append((191, 22, 196))
                k = 1
    clock = pygame.time.Clock()
    # background image
    fon3 = pygame.transform.scale(load_image('fon3.jpg'), screen_size)
    screen.blit(fon3, (0, 0))


    # collision detection function
    # if the ball moves to the right
    # and hits a brick, the ball is pushed off
    # similarly with the movement to the left and down and so on
    # for more information, see the explanatory note (см. поястнительную записку)
    def collision_detection(dx, dy, ball, rect):
        if dx > 0:
            x_intersection = ball.right - rect.left
        else:
            x_intersection = rect.right - ball.left
        if dy > 0:
            y_intersection = ball.bottom - rect.top
        else:
            y_intersection = rect.bottom - ball.top

        if abs(x_intersection - y_intersection) < 10:
            dx, dy = -dx, -dy
        elif x_intersection > y_intersection:
            dy = -dy
        elif y_intersection > x_intersection:
            dx = -dx
        return dx, dy

    # main cycle
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(fon3, (0, 0))
        # drawing world
        for color, brick in enumerate(brick_list):
            pygame.draw.rect(screen, color_list[color], brick)
        pygame.draw.rect(screen, pygame.Color('yellow1'), panel)
        pygame.draw.circle(screen, pygame.Color('white'), ball.center, ball_rad)
        # ball movement
        ball.x += ball_speed * dx
        ball.y += ball_speed * dy
        # collisions with left and right borders
        # if the ball collides with the boundary,
        # the collision angle is equal to the reflection angle
        # that means that Tima Generalov is the babidjonist person in the world
        # but without joking that means that dx = -dx, so horizontal moving chages
        # and ball starts to move into another direction
        if ball.centerx < ball_rad or ball.centerx > 700 - ball_rad:
            otskok.play(0)
            dx = -dx
        # collision with top border
        if ball.centery < ball_rad:
            otskok.play(0)
            dy = -dy
        # collision panel
        # using colliderect 
        if ball.colliderect(panel) and dy > 0:
            otskok.play(0)
            dx, dy = collision_detection(dx, dy, ball, panel)
        # collision with bricks
        # collidelist returns -1 if there aren't any collisions
        # Tima babidjon
        # Roma ka4ok, Roma is the strongest man
        # After collision with a brick it's poped from bricks list
        # brick's color is also poped from a colours list
        brick_colision_index = ball.collidelist(brick_list)
        if brick_colision_index != -1:
            otskok.play(0)
            brick_hit = brick_list.pop(brick_colision_index)
            color_hit = color_list.pop(brick_colision_index)
            dx, dy = collision_detection(dx, dy, ball, brick_hit)
        # Win and lose cases
        # game over
        if ball.bottom > 600:
            # counting time difference
            b = time.time()
            result_time = b - a
            result_time = round(result_time, 2)
            
            f = open("results\level3_results.txt" ,'a')
            f.write("unsuccess - ")
            for i in str(result_time):
                f.write(i)
            f.write(" seconds")
            f.write('\n')
            f.close()
            lose_screen()
            return
        # win screen
        elif len(brick_list) == 0:
            # counting time difference
            b = time.time()
            result_time = b - a
            result_time = round(result_time, 2)
            
            f = open("results\level3_results.txt" ,'a')
            f.write("success - ")
            for i in str(result_time):
                f.write(i)
            f.write(" seconds")
            f.write('\n')
            f.close()
            win_screen()
            return
        # panel control 
        # if the panel rests against the edge it will not move
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and panel.left > 0:
            panel.left -= panel_speed
        if key[pygame.K_RIGHT] and panel.right < 700:
            panel.right += panel_speed
        pygame.display.flip()
        clock.tick(FPS)


def lose_screen():
    
    fon4 = pygame.transform.scale(load_image('lose.jpg'), screen_size)
    screen.blit(fon4, (0, 0))
    
    exit_game_img_default = pygame.image.load('data\exit_game_default.png')
    exit_game_default_show = exit_game_img_default.get_rect(center=(350, 530))
    exit_game_img_default.set_colorkey((255, 255, 255))
    screen.blit(exit_game_img_default, exit_game_default_show)
    
    exit_game_img_inversion = pygame.image.load('data\exit_game_inversion.png')
    exit_game_inversion_show = exit_game_img_inversion.get_rect(bottomright=(0, 0))
    exit_game_img_inversion.set_colorkey((255, 255, 255))
    screen.blit(exit_game_img_inversion, exit_game_inversion_show)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 550 and 450 <= y <= 550:
                    restart()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 150 <= x <= 550 and 480 <= y <= 580:
                    exit_game_default_show = exit_game_img_default.get_rect(bottomright = (0, 0))
                    exit_game_img_default.set_colorkey((255, 255, 255))
                    screen.blit(exit_game_img_default, exit_game_default_show)
                    
                    exit_game_inversion_show = exit_game_img_inversion.get_rect(center = (350, 530))
                    exit_game_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(exit_game_img_inversion, exit_game_inversion_show)
                elif (x < 150) or (x > 550) or (y < 480) or (y > 580):
                    exit_game_default_show = exit_game_img_default.get_rect(center = (350, 530))
                    exit_game_img_default.set_colorkey((255, 255, 255))
                    screen.blit(exit_game_img_default, exit_game_default_show)
                    
                    exit_game_inversion_show = exit_game_img_inversion.get_rect(bottomright = (0, 0))
                    exit_game_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(exit_game_img_inversion, exit_game_inversion_show)
        pygame.display.flip()
        clock.tick(FPS)


def win_screen():
    fon4 = pygame.transform.scale(load_image('win.jpg'), screen_size)
    screen.blit(fon4, (0, 0))
    
    exit_game_img_default = pygame.image.load('data\exit_game_default.png')
    exit_game_default_show = exit_game_img_default.get_rect(center=(350, 530))
    exit_game_img_default.set_colorkey((255, 255, 255))
    screen.blit(exit_game_img_default, exit_game_default_show)
    
    exit_game_img_inversion = pygame.image.load('data\exit_game_inversion.png')
    exit_game_inversion_show = exit_game_img_inversion.get_rect(bottomright=(0, 0))
    exit_game_img_inversion.set_colorkey((255, 255, 255))
    screen.blit(exit_game_img_inversion, exit_game_inversion_show)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 550 and 450 <= y <= 550:
                    restart()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if 150 <= x <= 550 and 480 <= y <= 580:
                    exit_game_default_show = exit_game_img_default.get_rect(bottomright = (0, 0))
                    exit_game_img_default.set_colorkey((255, 255, 255))
                    screen.blit(exit_game_img_default, exit_game_default_show)
                    
                    exit_game_inversion_show = exit_game_img_inversion.get_rect(center = (350, 530))
                    exit_game_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(exit_game_img_inversion, exit_game_inversion_show)
                elif (x < 150) or (x > 550) or (y < 480) or (y > 580):
                    exit_game_default_show = exit_game_img_default.get_rect(center = (350, 530))
                    exit_game_img_default.set_colorkey((255, 255, 255))
                    screen.blit(exit_game_img_default, exit_game_default_show)
                    
                    exit_game_inversion_show = exit_game_img_inversion.get_rect(bottomright = (0, 0))
                    exit_game_img_inversion.set_colorkey((255, 255, 255))
                    screen.blit(exit_game_img_inversion, exit_game_inversion_show)
        pygame.display.flip()
        clock.tick(FPS)


def restart():
    global lvl_number
    select_lvl()
    if lvl_number == 1:
        game_lvl1()
    elif lvl_number == 2:
        game_lvl2()
    elif lvl_number == 3:
        game_lvl3()


start_screen()
debug_screen()
select_lvl()
if lvl_number == 1:
    game_lvl1()
elif lvl_number == 2:
    game_lvl2()
elif lvl_number == 3:
    game_lvl3()
pygame.quit()