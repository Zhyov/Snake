import pygame, sys, random, time
spacing = 50
while spacing >= 1:
    print()
    spacing = spacing - 1
print("Snake v0.0.3s patch-1 by LukeBlack952")
print()
print("What do you want the speed of the game to be? (Turtle | Snake | Rabbit)")
speed = input(">> ")
if speed.upper() == "TURTLE":
    speed = "Turtle"
    cspeed = 8
elif speed.upper() == "SNAKE":
    speed = "Snake"
    cspeed = 10
elif speed.upper() == "RABBIT":
    speed = "Rabbit"
    cspeed = 12
print()
print("How many apples do you want to spawn? (One | Some | Many) [DOESNT WORK JUST CHOOSE A RANDOM ONE]")
apples = input(">> ")
if apples.upper() == "ONE":
    apples = "One"
    capples = 1
elif apples.upper() == "SOME":
    apples = "Some"
    capples = 3
elif apples.upper() == "MANY":
    apples = "Many"
    capples = 5
print()
print("Grid Size? (Small | Medium | Large)")
gs = input(">> ")
if gs.upper() == "SMALL":
    gs = "Small"
    cgs = 40
elif gs.upper() == "MEDIUM":
    gs = "Medium"
    cgs = 30
elif gs.upper() == "LARGE":
    gs = "Large"
    cgs = 20
print()
scd = input("Default Snake Colors? (Yes | No) >> ")
if scd.upper() == "YES":
    scr = 0
    scg = 125
    scb = 255
elif scd.upper() == "NO":
    print("Snake Color? (RGB)")
    scr = input("Red Value >> ")
    scr = int(scr)
    if scr > 255:
        scr = 255
    scg = input("Green Value >> ")
    scg = int(scg)
    if scg > 255:
        scg = 255
    scb = input("Blue Value >> ")
    scb = int(scb)
    if scb > 255:
        scb = 255
print()
print("Theme? (Dark | Default)")
theme = input(">> ")
if theme.upper() == "DARK":
    pcr = 35
    pcg = 35
    pcb = 35

    secr = 25
    secg = 25
    secb = 25

    tcr = 255
    tcg = 255
    tcb = 255
elif theme.upper() == "DEFAULT":
    pcr = 150
    pcg = 255
    pcb = 0

    secr = 150
    secg = 240
    secb = 0

    tcr = 0
    tcg = 0
    tcb = 0

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (scr, scg, scb)
        self.score = 0
        self.highscore = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1] + (y * gridsize)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (scr, scg, scb), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # For some reason the save file doesnt add the data
                savedata = open("save-data.txt", "w")
                savedata.write("Date: " + time.strftime("%c") + "\nHighscore: " + str(self.highscore) + "\nScore: " + str(self.score) + "\nSpeed: " + speed + "\nApples: " + apples + "\nGrid Size: " + gs)
                savedata.close()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
                elif event.key == pygame.K_q:
                    # For some reason the save file doesnt add the data
                    savedata = open("save-data.txt", "w")
                    savedata.write("Date: " + time.strftime("%c") + "\nHighscore: " + str(self.highscore) + "\nScore: " + str(self.score) + "\nSpeed: " + speed + "\nApples: " + apples + "\nGrid Size: " + gs)
                    savedata.close()
                    pygame.quit()
                    sys.exit()
                # Not working, I will probably add it on v0.0.4 or v0.0.5
                elif event.key == pygame.K_RSHIFT:
                    pygame.quit()
                    sys.exit()
                    print()
                    print("Developer Mode On")
                    print('What do you want to do? (Type "help" for the list of commands)')
                    dma = True
                    while dma == True:
                        dev = input(">> ")
                        if dev.upper() == "HELP":
                            print()
                            print("help - Shows the list of commands")
                            print("reset - Resets the game")
                            print("quit - Quits the game")
                            print("speed - Changes the game speed")
                            print("apples - Changes the amount of apples")
                            print("grid - Changes the grid size")
                            print("theme - Changes the theme")
                            print("score - Changes the score")
                            print("highscore - Changes the highscore")
                            print("color - Changes the snake color")
                            print("devmode - Turns off developer mode")
                            print()
                        elif dev.upper() == "DEVMODE":
                            print()
                            print("Developer Mode Off")
                            dma = False
                        elif dev.upper() == "RESET":
                            print()
                            print("Game Reset")
                            self.reset()
                        elif dev.upper() == "QUIT":
                            print()
                            print("Game Quit")
                            # For some reason the save file doesnt add the data
                            savedata = open("save-data.txt", "w")
                            savedata.write("Date: " + time.strftime("%c") + "\nHighscore: " + str(self.highscore) + "\nScore: " + str(self.score) + "\nSpeed: " + speed + "\nApples: " + apples + "\nGrid Size: " + gs)
                            savedata.close()
                            pygame.quit()
                            sys.exit()
                        elif dev.upper() == "SPEED":
                            print()
                            print("What do you want the speed of the game to be? (Turtle | Snake | Rabbit)")
                            speed = input(">> ")
                            if speed.upper() == "TURTLE":
                                speed = "Turtle"
                                cspeed = 8
                            elif speed.upper() == "SNAKE":
                                speed = "Snake"
                                cspeed = 10
                            elif speed.upper() == "RABBIT":
                                speed = "Rabbit"
                                cspeed = 12
                        elif dev.upper() == "APPLES":
                            print()
                            print("How many apples do you want to spawn? (One | Some | Many)")
                            apples = input(">> ")
                            if apples.upper() == "ONE":
                                apples = "One"
                                capples = 1
                            elif apples.upper() == "SOME":
                                apples = "Some"
                                capples = 3
                            elif apples.upper() == "MANY":
                                apples = "Many"
                                capples = 5
                        elif dev.upper() == "GRID":
                            print()
                            print("What do you want the grid size to be? (Small | Medium | Large)")
                            gs = input(">> ")
                            if gs.upper() == "SMALL":
                                gs = "Small"
                                cgs = 20
                            elif gs.upper() == "MEDIUM":
                                gs = "Medium"
                                cgs = 30
                            elif gs.upper() == "LARGE":
                                gs = "Large"
                                cgs = 40
                        elif dev.upper() == "SCORE":
                            print()
                            print("What do you want the score to be?")
                            score = input(">> ")
                            self.score = int(score)
                        elif dev.upper() == "HIGHSCORE":
                            print()
                            print("What do you want the highscore to be?")
                            highscore = input(">> ")
                            self.highscore = int(highscore)
                        elif dev.upper() == "COLOR":
                            print()
                            print("Snake Color? (RGB)")
                            scr = input("Red Value >> ")
                            scr = int(scr)
                            if scr > 255:
                                scr = 255
                            scg = input("Green Value >> ")
                            scg = int(scg)
                            if scg > 255:
                                scg = 255
                            scb = input("Blue Value >> ")
                            scb = int(scb)
                            if scb > 255:
                                scb = 255
                            self.color = (scr, scg, scb)
                        else:
                            print()
                            print("Command not found")
                            print()

class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 100, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width - 1) * gridsize, random.randint(0, grid_height - 1) * gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 100, 0), r, 1)

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y *  gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface,(pcr, pcg, pcb), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (secr, secg, secb), rr)

screen_width = 480
screen_height = 480

gridsize = float(cgs)
grid_width = screen_width / gridsize
grid_height = screen_height / gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

def main():
    pygame.init()

    pygame.display.set_caption("Snake v0.0.3s patch-1")
    pygame.display.set_icon(pygame.image.load("Icon/icon.ico"))

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("nunito", 22)

    while (True):
        clock.tick(cspeed)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            if snake.highscore < snake.score:
                snake.highscore = snake.score
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text1 = myfont.render("Score: {0}".format(snake.score), 1, (tcr, tcg, tcb))
        text2 = myfont.render("High Score: {0}".format(snake.highscore), 1, (tcr, tcg, tcb))
        text3 = myfont.render("Speed: " + speed, 1, (tcr, tcg, tcb))
        text4 = myfont.render("Apples: " + apples, 1, (tcr, tcg, tcb))
        text5 = myfont.render("Size: " + gs, 1, (tcr, tcg, tcb))
        screen.blit(text1, (5, 55))
        screen.blit(text2, (5, 10))
        screen.blit(text3, (5, 40))
        screen.blit(text4, (5, 25))
        screen.blit(text5, (5, 70))
        pygame.display.update()

main()
