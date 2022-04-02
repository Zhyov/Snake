import pygame, sys, random, time

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

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (0, 125, 255)
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
            pygame.draw.rect(surface, (0, 125, 255), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                savedata = open("save-data.txt", "w")
                savedata.write("Date: " + time.strftime("%c") + "\nHighscore: " + str(self.highscore) + "\nScore: " + str(self.score) + "\nSpeed: " + speed + "\nApples: " + apples + "\nGrid Size: " + gs)
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
                    savedata = open("save-data.txt", "w")
                    savedata.write("Date: " + time.strftime("%c") + "\nHighscore: " + str(self.highscore) + "\nScore: " + str(self.score) + "\nSpeed: " + speed + "\nApples: " + apples + "\nGrid Size: " + gs)
                    pygame.quit()
                    sys.exit()

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
                r = pygame.Rect((x * gridsize, y*  gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface,(150, 255, 0), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (150, 240, 0), rr)

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

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace", 14)

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
        text = myfont.render("Score: {0}".format(snake.score), 1, (0, 0, 0))
        text2 = myfont.render("High Score: {0}".format(snake.highscore), 1, (0, 0, 0))
        text3 = myfont.render("Speed: " + speed, 1, (0, 0, 0))
        text4 = myfont.render("Apples: " + apples, 1, (0, 0, 0))
        text5 = myfont.render("Size: " + gs, 1, (0, 0, 0))
        screen.blit(text, (5, 55))
        screen.blit(text2, (5, 10))
        screen.blit(text3, (5, 40))
        screen.blit(text4, (5, 25))
        screen.blit(text5, (5, 70))
        pygame.display.update()

main()