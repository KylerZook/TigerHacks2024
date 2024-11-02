import pygame
import random

# Initialize pygame
pygame.init()




# Screen settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Quiz Collector")
background_image = pygame.image.load("/Users/kylerzook2005/repos/pygame/tigerhackbackgroud.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
question_image = pygame.image.load("/Users/kylerzook2005/repos/pygame/question.png")
question_image = pygame.transform.scale(question_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Game Variables
player_score = 0
highest_score = 0
time_left = 30
game_running = False

# Load font
font = pygame.font.Font(None, 36)

# Player settings
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
player_x = 100
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
player_speed = 5
player_jump = -20
is_jumping = False
velocity_y = 0
gravity = 0.6
player_image = pygame.image.load("/Users/kylerzook2005/repos/pygame/Polishcow.png")
player_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))  # Adjust the size as needed

# Platform settings
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
platform_image = pygame.image.load("/Users/kylerzook2005/repos/pygame/platform.png")
platform_image = pygame.transform.scale(platform_image, (PLATFORM_WIDTH, PLATFORM_HEIGHT))
platform_list = [
    pygame.Rect(100, SCREEN_HEIGHT - 50, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(200, SCREEN_HEIGHT - 250, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(100, SCREEN_HEIGHT - 450, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(200, SCREEN_HEIGHT - 650, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(300, SCREEN_HEIGHT - 50, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(400, SCREEN_HEIGHT - 250, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(300, SCREEN_HEIGHT - 450, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(400, SCREEN_HEIGHT - 650, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(500, SCREEN_HEIGHT - 50, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(600, SCREEN_HEIGHT - 250, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(500, SCREEN_HEIGHT - 450, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(600, SCREEN_HEIGHT - 650, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(700, SCREEN_HEIGHT - 50, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(800, SCREEN_HEIGHT - 250, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(700, SCREEN_HEIGHT - 450, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(800, SCREEN_HEIGHT - 650, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(900, SCREEN_HEIGHT - 50, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(1000, SCREEN_HEIGHT - 250, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(900, SCREEN_HEIGHT - 450, PLATFORM_WIDTH, PLATFORM_HEIGHT),
    pygame.Rect(1000, SCREEN_HEIGHT - 650, PLATFORM_WIDTH, PLATFORM_HEIGHT)
]

# Falling symbols 
symbol_list = []
symbol_speed = 3  # Initial symbol speed
speed_increase_interval = 5000  # Speed will increase every 5 seconds (5000 ms)



# Questions for quiz
questions = [
    ("Which vitamin is most commonly found in citrus fruits?", "Vitamin C", ["Vitamin A", "Vitamin C"]),
    ("What is the main ingredient in guacamole?", "Avocado", ["Tomato", "Avocado"]),
    ("Which grain is used to make traditional Italian pasta?", "Wheat", ["Rice", "Wheat"]),
    ("What is the most widely consumed meat in the world?", "Pork", ["Chicken", "Pork"]),
    ("What is tofu made from?", "Soybeans", ["Chickpeas", "Soybeans"]),
    ("Which country is the largest producer of coffee?", "Brazil", ["Colombia", "Brazil"]),
    ("What is the process of removing the outer husk of rice called?", "Milling", ["Grinding", "Milling"]),
    ("Which fruit has the highest fiber content?", "Apple", ["Banana", "Apple"]),
    ("What type of fat is found in olive oil?", "Monounsaturated fat", ["Saturated fat", "Monounsaturated fat"]),
    ("Which crop is used to produce sugar in tropical regions?", "Sugarcane", ["Corn", "Sugarcane"]),
    ("What is the most commonly grown cereal crop in the world?", "Corn", ["Rice", "Corn"]),
    ("Which nutrient is essential for photosynthesis?", "Nitrogen", ["Phosphorus", "Nitrogen"]),
    ("What agricultural practice involves rotating different crops in the same field?", "Crop rotation", ["Irrigation", "Crop rotation"]),
    ("Which plant is known as a 'legume'?", "Peanut", ["Cabbage", "Peanut"]),
    ("What is the primary ingredient in hummus?", "Chickpeas", ["Lentils", "Chickpeas"]),
    ("Which vegetable is known for its high iron content?", "Spinach", ["Carrot", "Spinach"]),
    ("Which farming technique helps conserve soil moisture?", "Mulching", ["Weeding", "Mulching"]),
    ("What is the term for animals raised on farms for food?", "Livestock", ["Wildlife", "Livestock"]),
    ("Which fruit is the largest producer in the world?", "Banana", ["Apple", "Banana"]),
    ("What is the main ingredient in traditional Japanese miso soup?", "Soybeans", ["Rice", "Soybeans"]),
    ("Which mineral is essential for bone health?", "Calcium", ["Iron", "Calcium"]),
    ("What is a common crop grown for animal feed?", "Alfalfa", ["Cabbage", "Alfalfa"]),
    ("What is the main source of protein in a vegan diet?", "Legumes", ["Chicken", "Legumes"]),
    ("Which type of agriculture involves growing only enough food to feed the farmer’s family?", "Subsistence farming", ["Commercial farming", "Subsistence farming"]),
    ("Which vegetable has a high water content and is commonly eaten in the summer?", "Cucumber", ["Potato", "Cucumber"]),
    ("What is the most common spice in the world?", "Pepper", ["Salt", "Pepper"]),
    ("Which fruit is rich in potassium and often eaten by athletes?", "Banana", ["Apple", "Banana"]),
    ("Which herb is commonly used in Italian dishes?", "Basil", ["Cilantro", "Basil"]),
    ("What is the primary nutrient found in carrots?", "Vitamin A", ["Vitamin C", "Vitamin A"])
]



# Start menu
def start_menu():
    screen.fill(WHITE)
    title_text = font.render("Python Quiz Collector", True, BLACK)
    start_text = font.render("Press ENTER to Start", True, BLACK)
    high_score_text = font.render(f"Highest Score: {highest_score}", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 200))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, 300))
    pygame.display.flip()

# Game Over function
def game_over():
    global game_running, player_score, highest_score, time_left
    game_running = False
    highest_score = max(highest_score, player_score)
    time_left = 30  # Reset time

# Ask a question
def ask_question():
    global player_score, time_left
    question, answer, options = random.choice(questions)
    question_text = font.render(question, True, WHITE)
    option1_text = font.render("1: " + options[0], True, WHITE)
    option2_text = font.render("2: " + options[1], True, WHITE)

    # Display question and options
    screen.blit(question_image, (0, 0))
    screen.blit(question_text, (50, 50))
    screen.blit(option1_text, (50, 150))
    screen.blit(option2_text, (50, 200))
    pygame.display.flip()

    # Wait for user answer, only accepting 1 or 2
    waiting_for_answer = True
    while waiting_for_answer:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2:
                    if (event.key == pygame.K_1 and options[0] == answer) or (event.key == pygame.K_2 and options[1] == answer):
                        player_score += 10
                        time_left += 5
                    else:
                        time_left -= 5
                    waiting_for_answer = False

# Main Game Function
def main_game():
    global gravity, game_running, player_x, player_y, player_speed, is_jumping, velocity_y, symbol_list, time_left, symbol_speed

    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    last_speed_increase = pygame.time.get_ticks()  # Track last speed increase time

    symbol_spawn_timer = 0

    while game_running:
        screen.blit(background_image, (0, 0))

        # Timer and Score Display
        seconds = time_left - (pygame.time.get_ticks() - start_ticks) // 1000
        if seconds <= 0:
            game_over()
        time_text = font.render(f"Time Left: {seconds}", True, BLACK)
        score_text = font.render(f"Score: {player_score}", True, BLACK)
        screen.blit(time_text, (10, 10))
        screen.blit(score_text, (10, 50))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Left
            player_x -= player_speed
        if keys[pygame.K_d]:  # Right
            player_x += player_speed
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            velocity_y = player_jump

        # Jumping and falling mechanics
        if is_jumping:
            velocity_y += gravity
            player_y += velocity_y

        # Prevent player from falling below the bottom of the screen
        if player_y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
            player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
            is_jumping = False
            velocity_y = 0

        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

        # Platform collision and dropping when moving off platform
        on_platform = False
        for platform in platform_list:
            if player_rect.colliderect(platform) and velocity_y > 0:
                player_y = platform.top - PLAYER_HEIGHT
                velocity_y = 0
                is_jumping = False
                on_platform = True

        # If not on any platform and not at the bottom, allow falling
        if not on_platform and player_y < SCREEN_HEIGHT - PLAYER_HEIGHT:
            is_jumping = True

        # Draw player and platforms
        screen.blit(player_image, (player_x, player_y))
        for platform in platform_list:
            screen.blit(platform_image, platform)

        # Increase symbol speed over time
        current_time = pygame.time.get_ticks()
        if current_time - last_speed_increase > speed_increase_interval:
            symbol_speed += 0.5  # Increase symbol speed
            player_speed += 0.5 # Increase player speed
            gravity += 0.1 # Increase gravity
            last_speed_increase = current_time

        # Spawn symbols
        symbol_spawn_timer += 1
        if symbol_spawn_timer >= 100:
            symbol_x = random.randint(0, SCREEN_WIDTH - 20)
            symbol_y = 0
            symbol_list.append(pygame.Rect(symbol_x, symbol_y, 20, 20))
            symbol_spawn_timer = 0

        # Update symbols
        for symbol in symbol_list[:]:
            symbol.y += int(symbol_speed)  # Use updated speed
            pygame.draw.rect(screen, GREEN, symbol)
            if symbol.colliderect(player_rect):
                symbol_list.remove(symbol)
                ask_question()

        pygame.display.flip()
        clock.tick(60)

# Main loop
running = True
while running:
    if not game_running:
        start_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_x, player_y = 100, SCREEN_HEIGHT - PLAYER_HEIGHT - 10
                    player_score = 0
                    game_running = True
                    symbol_list = []

    else:
        main_game()

# Quit Pygame
pygame.quit()
