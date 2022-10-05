import pygame



class Element:

    def __init__(self, screen, path):
        self.screen=screen
        self.image=pygame.image.load(path)
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

    def output(self,x,y):
        self.rect.centerx=self.screen_rect.centerx-x
        self.rect.bottom=self.screen_rect.bottom-y
        self.screen.blit(self.image,self.rect)
    
    


class Button:

    def __init__(self,screen,width=0,height=0,inactive_color=(0,0,0)):
        self.width=width
        self.height=height
        self.inactive_color=inactive_color
        self.active_color=(0, 0, 255)
        self.screen=screen
        self.counter=0
    
    def draw(self,x,y,message="",pos=0,action=None):
        def print_text():
            ARIAL_45=pygame.font.SysFont("arial",45)
            text=ARIAL_45.render(message, True,(255, 255, 255))
            self.screen.blit(text, (x+pos, y))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, (0,0,0), (x, y, self.width, self.height))
            pygame.draw.rect(self.screen, self.active_color, (x-2, y-2, self.width-2, self.height-2))
            if click[0]==1 and action is not None:
                pygame.time.delay(200)
                action()
        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
        print_text()
   
    def draw_b(self,x,y,message,pos_x=9,pos_y=7): 
        def print_text(color):
            ARIAL_30=pygame.font.SysFont("arial",30)
            text=ARIAL_30.render(message, True,color)
            self.screen.blit(text, (x+pos_x, y-pos_y))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if self.counter==1:
            return False
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            color=(255,255,255)
            pygame.draw.rect(self.screen, (0,0,0), (x, y, self.width, self.height))
            if click[0]==1:
                self.counter+=1
                pygame.time.delay(200)
                return True 
        else:
            color=(0,0,0)
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            pygame.draw.rect(self.screen, (255,255,255), (x+2, y+2, self.width-4, self.height-4))
        print_text(color)

    def draw_circle(self,x,y,radius,action=None,player=None,points=0,go=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()

        if x-self.width < mouse[0] < x + self.width and y-self.height < mouse[1] < y + self.height:
            pygame.draw.circle(self.screen, (255,0,255), (x, y), radius)
            if click[0]==1 and action is not None:
                pygame.time.delay(200)
                if player!=None:
                    if action(player,points):
                        return True
                action(go)
                
        else:
            pygame.draw.circle(self.screen, (255,255,255), (x, y), radius)
        
    def draw_hint(self,x,y,message,player=None,points=0,action=None): 
        def print_text():
            ARIAL_38=pygame.font.SysFont("arial",38)
            text=ARIAL_38.render(message, True,(0,0,0))
            self.screen.blit(text, (150, 260))
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            pygame.draw.rect(self.screen, (255,0,255), (x+5, y+5, self.width-10, self.height-10))
            print_text()
            if click[0]==1:
                pygame.time.delay(200)
                if action(player,points):
                    return True
                
        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            pygame.draw.rect(self.screen, (255,255,255), (x+5, y+5, self.width-10, self.height-10))
    
    def draw_win_lose_menu(self,x,y,action=None): 
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            pygame.draw.rect(self.screen, (255,0,255), (x+5, y+5, self.width-10, self.height-10))
            if click[0]==1:
                pygame.time.delay(200)
                action()
                    
                
        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            pygame.draw.rect(self.screen, (255,255,255), (x+5, y+5, self.width-10, self.height-10))
        
    




   
