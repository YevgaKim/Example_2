from class_game import *
import pygame
import sys
from tools import Element
from tools import Button
import random

pygame.init()
COLOR_FONT=(0,0,0)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Gallow")
bg_color=(255, 255, 255)
list_music=["music/background.mp3","music/background_2.mp3","music/background_3.mp3","music/background_4.mp3","music/background_5.mp3","music/background_6.mp3","music/background_7.mp3"]
random_music=random.choice(list_music)
pygame.mixer.music.load(random_music)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


#img of bg
stick_1= Element(screen,"images/1.png")
stick_2= Element(screen, "images/2.png")
rope=Element(screen,"images/3.png")
head=Element(screen, "images/4.png")
body=Element(screen, "images/5.png")
arm_1=Element(screen, "images/6.png")
arm_2=Element(screen, "images/7.png")
foot_1=Element(screen, "images/8.png")
foot_2=Element(screen, "images/9.png")
eyes=Element(screen, "images/10.png")


width=35
height=30
color_b=(0, 0, 0)
q_b= Button(screen,width,height,color_b)
w_b= Button(screen,width,height,color_b)
e_b= Button(screen,width,height,color_b)
r_b= Button(screen,width,height,color_b)
t_b= Button(screen,width,height,color_b)
y_b= Button(screen,width,height,color_b)
u_b= Button(screen,width,height,color_b)
i_b= Button(screen,width,height,color_b)
o_b= Button(screen,width,height,color_b)
p_b= Button(screen,width,height,color_b)
p1_b= Button(screen,width,height,color_b)
p2_b= Button(screen,width,height,color_b)
a_b= Button(screen,width,height,color_b)
s_b= Button(screen,width,height,color_b)
d_b= Button(screen,width,height,color_b)
f_b= Button(screen,width,height,color_b)
g_b= Button(screen,width,height,color_b)
h_b= Button(screen,width,height,color_b)
j_b= Button(screen,width,height,color_b)
k_b= Button(screen,width,height,color_b)
l_b= Button(screen,width,height,color_b)
l1_b= Button(screen,width,height,color_b)
l2_b= Button(screen,width,height,color_b)
z_b= Button(screen,width,height,color_b)
x_b= Button(screen,width,height,color_b)
c_b= Button(screen,width,height,color_b)
v_b= Button(screen,width,height,color_b)
b_b= Button(screen,width,height,color_b)
n_b= Button(screen,width,height,color_b)
m_b= Button(screen,width,height,color_b)
m1_b= Button(screen,width,height,color_b)
m2_b= Button(screen,width,height,color_b)

#buttons "Home","Reset" and "Hints"
dom = Element(screen,"images/dom.png")
dom_b= Button(screen,80,80,(0, 0, 0))
pere = Element(screen,"images/pere.png")
pere_b= Button(screen,80,80,(0, 0, 0))
hint = Element(screen, "images/hint.png")
hint_b= Button(screen,25,25)
hint_random=Element(screen,"images/random.png")
hint_random_b= Button(screen,90,90)
hint_letter=Element(screen,"images/letter.png")
hint_first_b= Button(screen,90,90)
hint_last_b= Button(screen,90,90)

#FONT
ARIAL_35=pygame.font.SysFont("arial",35)
ARIAL_40=pygame.font.SysFont("arial",40)
ARIAL_45=pygame.font.SysFont("arial",45)
ARIAL_50=pygame.font.SysFont("arial",50)
ARIAL_80=pygame.font.SysFont("arial",80)


    
def reboot_keyboard():
    keyboard = [q_b,w_b,e_b,r_b,t_b,y_b,u_b,i_b,o_b,p_b,p1_b,p2_b,
                a_b,s_b,d_b,f_b,g_b,h_b,j_b,k_b,l_b,l1_b,l2_b,
                z_b,x_b,c_b,v_b,b_b,n_b,m_b,m1_b,m2_b
                ]
    for i in keyboard:
        i.counter=0
    
def buttons_letter(player,points):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        h_1=465
        if q_b.draw_b(25,h_1,"й",pos_y=4):
            return "й"
        if w_b.draw_b(72,h_1,"ц",pos_y=8.5):
            return "ц"
        if e_b.draw_b(119,h_1,"у",pos_x=10,pos_y=9):
            return "у"
        if r_b.draw_b(166,h_1,"к",pos_x=10):
            return "к"
        if t_b.draw_b(213,h_1,"е",pos_x=9.2):
            return "е"
        if y_b.draw_b(260,h_1,"н",pos_x=9.5):
            return "н"
        if u_b.draw_b(307,h_1,"г",pos_x=12):
            return "г"
        if i_b.draw_b(354,h_1,"ш",pos_x=7):
            return "ш"
        if o_b.draw_b(401,h_1,"щ",pos_x=7):
            return "щ"
        if p_b.draw_b(448,h_1,"з",pos_x=10):
            return "з"
        if p1_b.draw_b(495,h_1,"х",pos_x=10):
            return "х"
        if p2_b.draw_b(542,h_1,"ъ"):
            return "ъ"
        h_2=510
        if a_b.draw_b(45,h_2,"ф",pos_x=7):
            return "ф"
        if s_b.draw_b(92,h_2,"ы",pos_x=8):
            return "ы"
        if d_b.draw_b(139,h_2,"в",pos_x=10):
            return "в"
        if f_b.draw_b(186,h_2,"а",pos_x=10):
            return "а"
        if g_b.draw_b(233,h_2,"п"):
            return "п"
        if h_b.draw_b(280,h_2,"р"):
            return "р"
        if j_b.draw_b(327,h_2,"о"):
            return "о"
        if k_b.draw_b(374,h_2,"л"):
            return "л"
        if l_b.draw_b(421,h_2,"д",pos_x=10):
            return "д"
        if l1_b.draw_b(468,h_2,"ж",pos_x=8):
            return "ж"
        if l2_b.draw_b(515,h_2,"э",pos_x=11):
            return "э"
        h_3=555
        if z_b.draw_b(88,h_3,"я"):
            return "я"
        if x_b.draw_b(135,h_3,"ч",pos_x=10.5):
            return "ч"
        if c_b.draw_b(182,h_3,"с"):
            return "с"
        if v_b.draw_b(229,h_3,"м"):
            return "м"
        if b_b.draw_b(276,h_3,"и"):
            return "и"
        if n_b.draw_b(323,h_3,"т",pos_x=10.5):
            return "т"
        if m_b.draw_b(370,h_3,"ь"):
            return "ь"
        if m1_b.draw_b(417,h_3,"б",pos_y=4):
            return "б"
        if m2_b.draw_b(464,h_3,"ю"):
            return "ю" 
            
        #button hint menu
        if hint_b.draw_circle(570,25,25,hint_menu,player,points):
            return player.hint_letter
        hint.output_b(-270,550)
        pygame.display.flip()
    
def starting():
    easy_b=Button(screen,140,70,(0, 128, 1))
    medium_b=Button(screen,140,70,(255, 255, 0))
    hard_b=Button(screen,140,70,(255,0,0))

    text=ARIAL_50.render("Please select a difficulty level", True,COLOR_FONT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(bg_color)
        screen.blit(text, (40, 100))
        easy_b.draw(40,300,"Easy",26,easy)
        medium_b.draw(225,300,"Medium",1,medium)
        hard_b.draw(410,300,"Hard",26,hard)
        pygame.display.flip()

def hint_menu(player,points):
    def rand_let(player,points):
        if (points-3)<3:
            return True
        else:
            with open("points.txt","w") as f:
                points-=3
                f.write(str(points))
            player.open_random_letter()
            return True
    def first_let(player,points):
        if (points-5)<5:
            return True
        else:
            with open("points.txt","w") as f:
                points-=5
                f.write(str(points))
            player.open_first_letter()
            return True
    def last_let(player,points):
        if (points-4)<4:
            return True
        else:
            with open("points.txt","w") as f:
                points-=4
                f.write(str(points))
            player.open_last_letter()
            return True
    def back_screen(player,points):
        player.word
        return True

    
    text=ARIAL_50.render("Hints", True,COLOR_FONT)
    text_2=ARIAL_35.render(str(points), True,COLOR_FONT)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if hint_b.draw_circle(570,25,25,back_screen,player,points):
            return True
        hint.output_b(-270,550)
        pygame.draw.rect(screen,(0,0,0),(100,100,400,210))
        pygame.draw.rect(screen,(255,255,255),(105,105,390,200))

        pygame.draw.rect(screen,(0,0,0),(430,110,60,40))
        pygame.draw.rect(screen,(255,255,255),(433,113,54,34))

        screen.blit(text,(255,105))
        screen.blit(text_2,(435,110))
        if hint_random_b.draw_hint(135,170,"Open random letter(3)",player,points,rand_let):
            return True
        hint_random.output_b(120,340)
        if hint_first_b.draw_hint(255,170,"   Open first letter(5)",player,points,first_let):
            return True
        hint_letter.output_b(0,350)
        if hint_last_b.draw_hint(375,170,"    Open last letter(4)",player,points,last_let):
            return True
        hint_letter.output_b(-120,350)
        pygame.display.flip()

def lose(screen,player,mode):

    text=ARIAL_40.render(player.line, False,COLOR_FONT)
    text_2=ARIAL_80.render("You lose", True, COLOR_FONT)
    text_3=ARIAL_40.render("Correct word", False, COLOR_FONT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.flip()

            dom_b.draw_win_lose_menu(35,457,action=starting)
            dom.output_b(225,75)

            pere_b.draw_win_lose_menu(485,457,action=mode)
            pere.output_b(-225,73)

            
            pygame.draw.rect(screen, (0, 0, 0), (165, 450, 270, 100))
            pygame.draw.rect(screen, (255, 255, 255), (170, 455, 260, 90))
            screen.blit(text_2,(175,450))
            pygame.draw.rect(screen,(0,0,0),(350,155,240,100))
            pygame.draw.rect(screen,(255,255,255),(355,160,230,90))
            screen.blit(text_3,(375,160))
            screen.blit(text,(470-((len(player.line)*18))/2,195))

def win(screen,scores,scores_game,points,mode):
    
    with open("scores.txt","w") as f:
        f.write(str(scores+scores_game))
    if (scores+scores_game)%100==0:
        with open("points.txt","w") as f:
            points+=5
            f.write(str(points))

    text_3=ARIAL_80.render("You win", True, COLOR_FONT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.flip()
            dom_b.draw_win_lose_menu(35,457,action=starting)
            dom.output_b(225,75)

            pere_b.draw_win_lose_menu(485,457,action=mode)
            pere.output_b(-225,73)
            pygame.draw.rect(screen, (0, 0, 0), (175, 450, 250, 100))
            pygame.draw.rect(screen, (255, 255, 255), (180, 455, 240, 90))
            screen.blit(text_3,(187,450))
 
def easy():
    player=Game(9)
    player.random_word()
    reboot_keyboard()
    with open("scores.txt","r") as f:
        scores=int(f.readline())
    
    text=ARIAL_45.render(player.word, True,COLOR_FONT)
    text_2=ARIAL_35.render(f"Scores: {str(scores)}",True,COLOR_FONT)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        with open("points.txt","r") as f:
            points=int(f.readline())
        screen.fill(bg_color)
        
        screen.blit(text, (300-((len(player.line)*20)/2), 390))
        screen.blit(text_2, (350, 7))
        
        if player.tries>=1:
            stick_1.output()
            if player.tries>=2:
                stick_2.output()
                if player.tries>=3:
                    rope.output()
                    if player.tries>=4:
                        head.output()
                        if player.tries>=5:
                            body.output()
                            if player.tries>=6:
                                arm_1.output()
                                if player.tries>=7:
                                    arm_2.output()
                                    if player.tries>=8:
                                        foot_1.output()
                                        if player.tries>=9:
                                            foot_2.output()
                                            eyes.output()
        if player.check_tries(): 
            lose(screen,player,easy)
        if player.finish_game():
            win(screen,scores,20,points,easy)
        text=ARIAL_45.render(player.enter_letter(buttons_letter(player,points)), True,COLOR_FONT)
       
def medium():
    player=Game(7)
    player.random_word()
    reboot_keyboard()
    with open("scores.txt","r") as f:
        scores=int(f.readline())
    text=ARIAL_45.render(player.word, True,COLOR_FONT)
    text_2=ARIAL_35.render(f"Scores: {str(scores)}",True,COLOR_FONT)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        with open("points.txt","r") as f:
            points=int(f.readline())
        screen.fill(bg_color)

        
        screen.blit(text, (300-((len(player.line)*20)/2), 390))
        screen.blit(text_2, (350, 7))
        
        if player.tries>=1:
            stick_1.output()
            if player.tries>=2:
                stick_2.output()
                if player.tries>=3:
                    rope.output()
                    if player.tries>=4:
                        head.output()
                        if player.tries>=5:
                            body.output()
                            if player.tries>=6:
                                arm_1.output()
                                arm_2.output()
                                if player.tries>=7:
                                    foot_1.output()
                                    foot_2.output()
                                    eyes.output()
                                    
        if player.check_tries(): 
            lose(screen,player,medium)
        if player.finish_game():
            win(screen,scores,35,points,medium)
        text=ARIAL_45.render(player.enter_letter(buttons_letter(player,points)), True,COLOR_FONT)
                        
def hard():
    player=Game(5)
    player.random_word()
    reboot_keyboard()
    with open("scores.txt","r") as f:
        scores=int(f.readline())
    text=ARIAL_45.render(player.word, True,COLOR_FONT)
    text_2=ARIAL_35.render(f"Scores: {str(scores)}",True,COLOR_FONT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        with open("points.txt","r") as f:
            points=int(f.readline())
        screen.fill(bg_color)

        
        screen.blit(text, (300-((len(player.line)*20)/2), 390))
        screen.blit(text_2, (350, 7))
       
        if player.tries>=1:
            stick_1.output()
            stick_2.output()
            rope.output()
            if player.tries>=2:
                head.output()
                if player.tries>=3:
                    body.output()
                    if player.tries>=4:
                        arm_1.output()
                        arm_2.output()
                        if player.tries>=5:
                            foot_1.output()
                            foot_2.output()
                            eyes.output()
                                    
        if player.check_tries(): 
            lose(screen,player,hard)
        if player.finish_game():
            win(screen,scores,50,points,hard)
        text=ARIAL_45.render(player.enter_letter(buttons_letter(player,points)), True,COLOR_FONT)
       
        
starting()

        
    
    
    
    





    
            



    



