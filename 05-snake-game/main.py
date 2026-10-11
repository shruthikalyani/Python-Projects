import pygame

import random

import math

import sys



pygame.init()

WIDTH = 1100

HEIGHT = 760

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("SNAKE.EXE // MYSPACE EDITION")

clock = pygame.time.Clock()



BG_DARK = (18, 17, 42)

BG_PURPLE = (34, 27, 66)



GB_DARK = (35, 55, 48)

GB_MID = (88, 112, 79)

GB_LIGHT = (174, 190, 118)

GB_SCREEN = (202, 215, 151)

# Main UI

NAVY = (24, 31, 67)

NAVY_DARK = (12, 16, 38)

CYAN = (91, 221, 238)

CYAN_LIGHT = (177, 246, 255)

LAVENDER = (181, 144, 226)

LAVENDER_LIGHT = (224, 201, 246)

PINK = (244, 143, 211)

PINK_LIGHT = (255, 193, 232)

SILVER = (156, 168, 184)

SILVER_LIGHT = (238, 242, 246)

SILVER_DARK = (82, 91, 108)

BLACK = (8, 9, 13)

TEXT = (241, 246, 248)

TEXT_MUTED = (151, 173, 194)

GREEN = (121, 235, 163)

GRID = (169, 181, 175)

GRID_LIGHT = (190, 201, 188)

#
def make_font(size, bold=False):

    candidates = [

        "Trebuchet MS",

        "Verdana",

        "Arial",

        "Courier New",

        "DejaVu Sans"

    ]

    for name in candidates:

        result = pygame.font.SysFont(

            name,

            size,

            bold=bold

        )

        if result:

            return result

    return pygame.font.Font(None, size)

FONT_HUGE = make_font(42, True)

FONT_TITLE = make_font(27, True)

FONT_MEDIUM = make_font(18, True)

FONT_SMALL = make_font(13)

FONT_TINY = make_font(10)

FONT_PIXEL = make_font(16, True)

FONT_DIGITAL = make_font(25, True)

# ============================================================

# GAME BOARD

# ============================================================

BOARD_X = 205

BOARD_Y = 166

CELL = 20

COLS = 32

ROWS = 25

BOARD_W = COLS * CELL

BOARD_H = ROWS * CELL


MENU = "menu"

PLAYING = "playing"

PAUSED = "paused"

GAME_OVER = "game_over"

game_state = MENU

snake = []

previous_snake = []

direction = (1, 0)

next_direction = (1, 0)

food = (0, 0)

score = 0

high_score = 0

move_timer = 0

animation_time = 0

MOVE_TIME_START = 105

MOVE_TIME_MIN = 55


def draw_gradient(surface, rect, top, bottom):

    x, y, width, height = rect

    for row in range(height):

        ratio = row / max(1, height - 1)

        colour = (

            int(top[0] * (1 - ratio) + bottom[0] * ratio),

            int(top[1] * (1 - ratio) + bottom[1] * ratio),

            int(top[2] * (1 - ratio) + bottom[2] * ratio)

        )

        pygame.draw.line(

            surface,

            colour,

            (x, y + row),

            (x + width, y + row)

        )

def draw_text(

    message,

    position,

    font_object,

    colour,

    anchor="topleft"

):

    image = font_object.render(

        message,

        True,

        colour

    )

    rect = image.get_rect()

    setattr(rect, anchor, position)

    screen.blit(image, rect)

def center_text(

    message,

    x,

    y,

    font_object,

    colour

):

    draw_text(

        message,

        (x, y),

        font_object,

        colour,

        "center"

    )

def panel(

    rect,

    top_colour,

    bottom_colour,

    border_colour,

    radius=14

):

    draw_gradient(

        screen,

        rect,

        top_colour,

        bottom_colour

    )

    pygame.draw.rect(

        screen,

        border_colour,

        rect,

        2,

        border_radius=radius

    )



def draw_background():

    draw_gradient(

        screen,

        (0, 0, WIDTH, HEIGHT),

        BG_PURPLE,

        BG_DARK

    )



    pygame.draw.circle(

        screen,

        (54, 38, 83),

        (85, 110),

        100

    )

    pygame.draw.circle(

        screen,

        (43, 32, 75),

        (1010, 630),

        150

    )


    random.seed(12)

    for _ in range(70):

        x = random.randrange(WIDTH)

        y = random.randrange(HEIGHT)

        size = random.choice([1, 1, 2])

        pygame.draw.rect(

            screen,

            (87, 89, 135),

            (x, y, size, size)

        )

    random.seed()

def draw_window():

    pygame.draw.rect(

        screen,

        (5, 5, 17),

        (31, 28, WIDTH - 62, HEIGHT - 56),

        border_radius=30

    )



    panel(

        (38, 35, WIDTH - 76, HEIGHT - 70),

        (115, 160, 194),

        (42, 67, 120),

        SILVER_LIGHT,

        28

    )



    pygame.draw.rect(

        screen,

        CYAN,

        (47, 44, WIDTH - 94, HEIGHT - 88),

        2,

        border_radius=24

    )



def draw_header():

    panel(

        (62, 58, 976, 74),

        (103, 190, 227),

        (54, 91, 154),

        SILVER_LIGHT,

        18

    )

    # shine

    pygame.draw.line(

        screen,

        CYAN_LIGHT,

        (84, 68),

        (1000, 68),

        2

    )

    draw_text(

        "Y2K",

        (88, 69),

        FONT_HUGE,

        TEXT

    )

    draw_text(

        "SNAKE.EXE",

        (222, 75),

        FONT_TITLE,

        TEXT

    )

    draw_text(

        "MYSPACE DIGITAL EDITION  /  2004",

        (224, 106),

        FONT_TINY,

        CYAN_LIGHT

    )

 

    pygame.draw.circle(

        screen,

        GREEN,

        (920, 88),

        5

    )

    draw_text(

        "ONLINE",

        (934, 81),

        FONT_SMALL,

        TEXT

    )

    # window buttons

    buttons = [

        (974, 76, CYAN, "_"),

        (1003, 76, SILVER_LIGHT, "□")

    ]

    for x, y, colour, symbol in buttons:

        pygame.draw.rect(

            screen,

            NAVY_DARK,

            (x, y, 24, 24),

            border_radius=5

        )

        pygame.draw.rect(

            screen,

            colour,

            (x + 2, y + 2, 20, 20),

            border_radius=4

        )

        center_text(

            symbol,

            x + 12,

            y + 12,

            FONT_SMALL,

            NAVY

        )



def draw_navigation():

    pygame.draw.rect(

        screen,

        (206, 222, 233),

        (62, 137, 976, 31),

        border_radius=5

    )

    tabs = [

        ("FILE", 88),

        ("EDIT", 151),

        ("VIEW", 214),

        ("PLAY", 280),

        ("FRIENDS", 347),

        ("PROFILE", 440)

    ]

    for label, x in tabs:

        draw_text(

            label,

            (x, 146),

            FONT_SMALL,

            NAVY

        )

        pygame.draw.line(

            screen,

            (136, 157, 177),

            (x + 48, 143),

            (x + 48, 163)

        )

def draw_sidebar():

    panel(

        (70, 202, 103, 420),

        (74, 92, 163),

        (30, 39, 89),

        LAVENDER,

        19

    )

    icons = [

        "✦",

        "♥",

        "★",

        "✎",

        "◈",

        "●"

    ]

    for index, icon in enumerate(icons):

        y = 217 + index * 63

        pygame.draw.rect(

            screen,

            NAVY_DARK,

            (82, y, 79, 50),

            border_radius=11

        )

        pygame.draw.rect(

            screen,

            (93, 119, 181),

            (85, y + 3, 73, 44),

            1,

            border_radius=9

        )

        center_text(

            icon,

            121,

            y + 25,

            FONT_TITLE,

            CYAN_LIGHT

        )


def draw_board():

    # large board shadow

    pygame.draw.rect(

        screen,

        (5, 10, 25),

        (

            BOARD_X - 13,

            BOARD_Y - 13,

            BOARD_W + 26,

            BOARD_H + 26

        ),

        border_radius=18

    )

    # silver frame

    pygame.draw.rect(

        screen,

        SILVER_LIGHT,

        (

            BOARD_X - 9,

            BOARD_Y - 9,

            BOARD_W + 18,

            BOARD_H + 18

        ),

        3,

        border_radius=15

    )

    # Game Boy screen

    pygame.draw.rect(

        screen,

        GB_DARK,

        (

            BOARD_X - 3,

            BOARD_Y - 3,

            BOARD_W + 6,

            BOARD_H + 6

        ),

        border_radius=8

    )

    pygame.draw.rect(

        screen,

        GB_SCREEN,

        (

            BOARD_X,

            BOARD_Y,

            BOARD_W,

            BOARD_H

        ),

        border_radius=5

    )

    # graph grid

    for x in range(COLS + 1):

        px = BOARD_X + x * CELL

        pygame.draw.line(

            screen,

            GRID,

            (px, BOARD_Y),

            (px, BOARD_Y + BOARD_H)

        )

    for y in range(ROWS + 1):

        py = BOARD_Y + y * CELL

        pygame.draw.line(

            screen,

            GRID,

            (BOARD_X, py),

            (BOARD_X + BOARD_W, py)

        )

    # subtle CRT scanlines

    for y in range(

        BOARD_Y,

        BOARD_Y + BOARD_H,

        6

    ):

        pygame.draw.line(

            screen,

            (181, 195, 164),

            (BOARD_X, y),

            (BOARD_X + BOARD_W, y)

        )


def draw_status_panel():

    x = 835

    y = 202

    panel(

        (x, y, 178, 420),

        (71, 91, 160),

        (28, 39, 88),

        LAVENDER,

        19

    )

    # title

    draw_text(

        "PLAYER",

        (x + 18, y + 20),

        FONT_TINY,

        CYAN_LIGHT

    )

    draw_text(

        "★  SNAKE",

        (x + 18, y + 38),

        FONT_MEDIUM,

        TEXT

    )

    # avatar

    pygame.draw.rect(

        screen,

        NAVY_DARK,

        (x + 18, y + 77, 142, 88),

        border_radius=12

    )

    pygame.draw.rect(

        screen,

        LAVENDER,

        (x + 25, y + 84, 128, 74),

        2,

        border_radius=9

    )

    # tiny snake avatar

    pygame.draw.circle(

        screen,

        SILVER_LIGHT,

        (x + 70, y + 120),

        15

    )

    pygame.draw.circle(

        screen,

        BLACK,

        (x + 70, y + 120),

        9

    )

    pygame.draw.circle(

        screen,

        SILVER,

        (x + 110, y + 120),

        8

    )

    # stats

    stats = [

        ("SCORE", f"{score:04}"),

        ("HIGH", f"{high_score:04}"),

        ("LEVEL", f"{score // 50 + 1:02}")

    ]

    for i, (label, value) in enumerate(stats):

        box_y = y + 180 + i * 63

        pygame.draw.rect(

            screen,

            NAVY_DARK,

            (x + 15, box_y, 148, 52),

            border_radius=9

        )

        draw_text(

            label,

            (x + 26, box_y + 9),

            FONT_TINY,

            TEXT_MUTED

        )

        draw_text(

            value,

            (x + 26, box_y + 23),

            FONT_DIGITAL,

            CYAN_LIGHT

        )


def draw_footer():

    pygame.draw.rect(

        screen,

        NAVY_DARK,

        (205, 688, 628, 38),

        border_radius=8

    )

    pygame.draw.rect(

        screen,

        CYAN,

        (205, 688, 628, 38),

        1,

        border_radius=8

    )

    draw_text(

        "[14:32 // 03.11.04]",

        (220, 698),

        FONT_SMALL,

        TEXT

    )

    draw_text(

        "♥  USB  ✦  WIFI",

        (410, 698),

        FONT_SMALL,

        CYAN_LIGHT

    )

    draw_text(

        "SYSTEM READY",

        (680, 698),

        FONT_SMALL,

        GREEN

    )



def cell_pixel(cell):

    return (

        BOARD_X + cell[0] * CELL,

        BOARD_Y + cell[1] * CELL

    )

def interpolated_position(old, new, amount):

    return (

        old[0] + (new[0] - old[0]) * amount,

        old[1] + (new[1] - old[1]) * amount

    )


def draw_snake(progress):

    for index, segment in enumerate(snake):

        if index < len(previous_snake):

            old = previous_snake[index]

        else:

            old = segment

        position = interpolated_position(

            old,

            segment,

            progress

        )

        x = BOARD_X + position[0] * CELL

        y = BOARD_Y + position[1] * CELL

        rect = pygame.Rect(

            int(x + 2),

            int(y + 2),

            CELL - 4,

            CELL - 4

        )

        # HEAD

        if index == 0:

            # chrome shadow

            pygame.draw.rect(

                screen,

                (72, 79, 91),

                rect,

                border_radius=5

            )

            # silver body

            pygame.draw.rect(

                screen,

                SILVER_LIGHT,

                (

                    rect.x,

                    rect.y,

                    rect.width,

                    rect.height - 2

                ),

                border_radius=5

            )

            # top reflection

            pygame.draw.line(

                screen,

                (255, 255, 255),

                (

                    rect.x + 4,

                    rect.y + 4

                ),

                (

                    rect.right - 5,

                    rect.y + 4

                ),

                2

            )

            # eyes based on direction

            draw_head_eyes(

                rect,

                direction

            )

        # BODY

        else:

            pygame.draw.rect(

                screen,

                BLACK,

                rect,

                border_radius=4

            )

            pygame.draw.rect(

                screen,

                (49, 52, 61),

                rect,

                1,

                border_radius=4

            )

def draw_head_eyes(rect, facing):

    if facing == (1, 0):

        eyes = [

            (rect.right - 5, rect.top + 6),

            (rect.right - 5, rect.bottom - 6)

        ]

    elif facing == (-1, 0):

        eyes = [

            (rect.left + 5, rect.top + 6),

            (rect.left + 5, rect.bottom - 6)

        ]

    elif facing == (0, -1):

        eyes = [

            (rect.left + 6, rect.top + 5),

            (rect.right - 6, rect.top + 5)

        ]

    else:

        eyes = [

            (rect.left + 6, rect.bottom - 5),

            (rect.right - 6, rect.bottom - 5)

        ]

    for eye in eyes:

        pygame.draw.circle(

            screen,

            NAVY_DARK,

            eye,

            2

        )



def draw_food():

    x = BOARD_X + food[0] * CELL + CELL // 2

    y = BOARD_Y + food[1] * CELL + CELL // 2

    pulse = math.sin(animation_time * 0.006)

    radius = int(9 + pulse)

    # pink/cyan aura

    pygame.draw.circle(

        screen,

        (214, 164, 226),

        (x, y),

        radius + 4

    )

    # disc

    pygame.draw.circle(

        screen,

        SILVER_DARK,

        (x, y),

        radius

    )

    pygame.draw.circle(

        screen,

        SILVER_LIGHT,

        (x, y),

        radius - 2

    )

    

    pygame.draw.arc(

        screen,

        CYAN,

        (

            x - radius + 2,

            y - radius + 2,

            (radius - 2) * 2,

            (radius - 2) * 2

        ),

        math.radians(190),

        math.radians(285),

        2

    )

    pygame.draw.arc(

        screen,

        PINK,

        (

            x - radius + 2,

            y - radius + 2,

            (radius - 2) * 2,

            (radius - 2) * 2

        ),

        math.radians(290),

        math.radians(40),

        2

    )

    # center hole

    pygame.draw.circle(

        screen,

        NAVY_DARK,

        (x, y),

        2

    )


def spawn_food():

    global food

    while True:

        candidate = (

            random.randrange(COLS),

            random.randrange(ROWS)

        )

        if candidate not in snake:

            food = candidate

            return



def reset_game():

    global snake

    global previous_snake

    global direction

    global next_direction

    global score

    global move_timer

    global game_state

    center_x = COLS // 2

    center_y = ROWS // 2

    snake = [

        (center_x, center_y),

        (center_x - 1, center_y),

        (center_x - 2, center_y),

        (center_x - 3, center_y)

    ]

    previous_snake = snake.copy()

    direction = (1, 0)

    next_direction = (1, 0)

    score = 0

    move_timer = 0

    spawn_food()

    game_state = PLAYING



def move_time():

    level = score // 50

    return max(

        MOVE_TIME_MIN,

        MOVE_TIME_START - level * 7

    )



def move_snake():

    global snake

    global previous_snake

    global direction

    global score

    global high_score

    global game_state

    direction = next_direction

    previous_snake = snake.copy()

    head = snake[0]

    new_head = (

        head[0] + direction[0],

        head[1] + direction[1]

    )

    # wall

    if (

        new_head[0] < 0

        or new_head[0] >= COLS

        or new_head[1] < 0

        or new_head[1] >= ROWS

    ):

        game_state = GAME_OVER

        return

    # self

    if new_head in snake:

        game_state = GAME_OVER

        return

    snake.insert(0, new_head)

    # food

    if new_head == food:

        score += 10

        if score > high_score:

            high_score = score

        spawn_food()

    else:

        snake.pop()


def overlay_box(title, subtitle, action):

    # dim screen

    dim = pygame.Surface(

        (WIDTH, HEIGHT),

        pygame.SRCALPHA

    )

    dim.fill((8, 8, 25, 105))

    screen.blit(dim, (0, 0))

    # card

    card = pygame.Surface(

        (520, 280),

        pygame.SRCALPHA

    )

    pygame.draw.rect(

        card,

        (26, 31, 68, 245),

        (0, 0, 520, 280),

        border_radius=25

    )

    pygame.draw.rect(

        card,

        (219, 196, 240, 255),

        (0, 0, 520, 280),

        2,

        border_radius=25

    )

    # glossy top

    pygame.draw.line(

        card,

        (146, 232, 246, 190),

        (28, 18),

        (492, 18),

        2

    )

    screen.blit(

        card,

        (290, 270)

    )

    center_text(

        title,

        550,

        330,

        FONT_HUGE,

        TEXT

    )

    center_text(

        subtitle,

        550,

        395,

        FONT_SMALL,

        CYAN_LIGHT

    )

    # button

    pygame.draw.rect(

        screen,

        (51, 75, 128),

        (425, 445, 250, 48),

        border_radius=12

    )

    pygame.draw.rect(

        screen,

        LAVENDER_LIGHT,

        (425, 445, 250, 48),

        2,

        border_radius=12

    )

    center_text(

        action,

        550,

        469,

        FONT_MEDIUM,

        TEXT

    )



def draw_menu():

    overlay_box(

        "SNAKE.EXE",

        "YOUR PROFILE IS READY.",

        "PRESS SPACE TO PLAY"

    )

    center_text(

        "ARROW KEYS  •  MOVE",

        550,

        535,

        FONT_TINY,

        TEXT_MUTED

    )


def draw_pause():

    overlay_box(

        "PAUSED",

        "SNAKE IS TAKING A LITTLE BREAK.",

        "PRESS SPACE TO RESUME"

    )



def draw_game_over():

    overlay_box(

        "GAME OVER",

        f"SCORE {score:04}  •  HIGH {high_score:04}",

        "PRESS SPACE TO RESTART"

    )


def draw(progress):

    draw_background()

    draw_window()

    draw_header()

    draw_navigation()

    draw_sidebar()

    draw_board()

    draw_status_panel()

    draw_footer()

    if game_state in (

        PLAYING,

        PAUSED,

        GAME_OVER

    ):

        draw_food()

        draw_snake(progress)

    if game_state == MENU:

        draw_menu()

    elif game_state == PAUSED:

        draw_pause()

    elif game_state == GAME_OVER:

        draw_game_over()

running = True

while running:

    dt = clock.tick(60)

    animation_time += dt

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            # MENU

            if game_state == MENU:

                if event.key == pygame.K_SPACE:

                    reset_game()

                elif event.key == pygame.K_ESCAPE:

                    running = False

            # PLAYING

            elif game_state == PLAYING:

                if event.key == pygame.K_UP:

                    if direction != (0, 1):

                        next_direction = (0, -1)

                elif event.key == pygame.K_DOWN:

                    if direction != (0, -1):

                        next_direction = (0, 1)

                elif event.key == pygame.K_LEFT:

                    if direction != (1, 0):

                        next_direction = (-1, 0)

                elif event.key == pygame.K_RIGHT:

                    if direction != (-1, 0):

                        next_direction = (1, 0)

                elif event.key == pygame.K_SPACE:

                    game_state = PAUSED

                elif event.key == pygame.K_ESCAPE:

                    game_state = MENU

            # PAUSED

            elif game_state == PAUSED:

                if event.key == pygame.K_SPACE:

                    game_state = PLAYING

                elif event.key == pygame.K_ESCAPE:

                    game_state = MENU

            # GAME OVER

            elif game_state == GAME_OVER:

                if event.key == pygame.K_SPACE:

                    reset_game()

                elif event.key == pygame.K_ESCAPE:

                    game_state = MENU


    if game_state == PLAYING:

        move_timer += dt

        interval = move_time()

        if move_timer >= interval:

            move_timer -= interval

            move_snake()



    interval = move_time()

    progress = min(

        1.0,

        move_timer / interval

    )

    # smoothstep makes movement feel less robotic

    progress = progress * progress * (3 - 2 * progress)


    draw(progress)

    pygame.display.flip()

pygame.quit()
