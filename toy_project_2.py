#화면 변수 설정
import pygame
import random
#import wave

#게임 초기화
pygame.init()

#화면 너비 설정
screen_width = 720
screen_height = 470

pygame.display.set_caption('Fruit Box')

#이미지 위치
location_url = 'c:/Users/JINI/Desktop/python/'

#화면 색상 변수
screenColor_black = (0, 0, 0)
screenColor_white = (255, 255, 255)
screenColor_green = (0, 255, 0)
screenColor_red = (255, 0, 0)

#폰트 변수
large_font = pygame.font.SysFont('consolas', 24)
small_font = pygame.font.SysFont('새굴림', 24)
score_font = pygame.font.SysFont('consolas', 24)

#이미지 변수
apple_1_image = pygame.image.load(location_url + 'apple_1.png')
apple_2_image = pygame.image.load(location_url + 'apple_2.png')
apple_3_image = pygame.image.load(location_url + 'apple_3.png')
apple_4_image = pygame.image.load(location_url + 'apple_4.png')
apple_5_image = pygame.image.load(location_url + 'apple_5.png')
apple_6_image = pygame.image.load(location_url + 'apple_6.png')
apple_7_image = pygame.image.load(location_url + 'apple_7.png')
apple_8_image = pygame.image.load(location_url + 'apple_8.png')
apple_9_image = pygame.image.load(location_url + 'apple_9.png')

img = 'apple_1_image, apple_2_image, apple_3_image, apple_4_image, apple_5_image, apple_6_image, apple_7_image, apple_8_image, apple_9_image'

'''
#음악 생성
pygame.mixer.init()
pygame.mixer.music.load(location_url + 'apple_sound.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)   #무한 반복
'''

#point_sound = pygame.mixer.Sound(location_url + 'apple_sound.wav')
#point_sound.set_volume(0.5)

#화면 스크린 생성
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#w = wave.open('c:/Users/JINI/Desktop/python/apple_sound.mp3', 'r')

#기본 zero 값
default_zero = 0
default_two = 2

#화면 시메트릭
default_centerx = screen_width // 2
default_centery = screen_height // 2

#top down 기본값
default_top_down_number = -100

#공통 변수 설정
#total 점수
total_score = 0

#총 게임 시간
total_time = 10

#시작 시간 정보
#start_ticks = pygame.time.get_ticks()

#gmae over 기본 값
game_over = False
game_end = False

#pygame 기본 값
pygame_end = 0

#변수 및 배열 선언
score = 0
gameOver = False

#랜덤 이미지 생성 (변수)
'''
for i in range(img) :
    index = random.randrange(len(img))
'''
'''
def runGame() :
    x = 0
    y = 0

    running = True 
    while running:

        for event in pygame.event.get():    #이벤트 처리
            if event.type == pygame.QUIT:
                running = False

            screen.blit(img, (x, y))   #이미지 위치
            pygame.display.update()   #display 업데이트

            if (x < 680) :
                x = x + 40
            else :
                x = 0
                if y < 360 :
                    y = y + 40

     #타이머 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = small_font.render(str(int(total_time - elapsed_time)), True, screenColor_green)
    screen.blit(timer, (10, 10))

    #타이머 0초 될 시 타임아웃
    if total_time - elapsed_time <= 0 :
        print('Game Over!')
        running = False
'''


#점수
def processScore(total_score) :
    score_image = score_font.render('Score {}'.format(total_score), True, screenColor_red)
    screen.blit(score_image, (10, 10))

#게임 종료
def screenGameOver() :
    game_over_image = large_font.render('Game Over', True, screenColor_red)
    screen.blit(game_over_image, game_over_image.get_rect(centerx = default_centerx, centery = default_centery))

    score_image = small_font.render('점수 {}'.format(total_score), True, screenColor_red)
    screen.blit(score_image, score_image.get_rect(centerx = default_centerx, centery = default_centery - default_top_down_number))

    game_end = True
    return game_end

#시작화면 추가
def startGame() :
    startEnter = False
    while True :
        mainText = small_font.render('====== Fruit Box ======', True, screenColor_green)
        startText = small_font.render('시작하기 -> key A', True, screenColor_green)
        middleText = small_font.render('=====================', True, screenColor_green)

        screen.blit(mainText, mainText.get_rect(centerx = default_centerx, centery = default_centery))
        screen.blit(startText, startText.get_rect(centerx = default_centerx, centery = default_centery - default_top_down_number))
        screen.blit(middleText, middleText.get_rect(centerx = default_centerx, centery = default_centery - (default_top_down_number * default_two)))

        pygame.display.flip()

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :  
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_a :
                    startEnter = True
            elif event.type == pygame.KEYUP :
                if event.key == pygame.K_a :
                    startEnter = False

        if startEnter :
            break

#게임 루프 로직
#게임 시작
startGame()

while True :
    screen.blit()

    #변수 업데이트
    event = pygame.event.poll()    #이벤트 처리
    #게임 기본 핸들링 처리 함수

    #스코어
    processScore(total_score)

    #게임 종료 화면
    if game_end == True :
        gameOver = screenGameOver()

    #pygame.display.update()

    #FPS 프레임
    clock.tick(30)


pygame.quit()


    





'''
for i in pygame.font.get_fonts() : 
    print(i)
'''