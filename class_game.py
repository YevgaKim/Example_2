import random

class Game:
    
    def __init__(self,attempts):
        self.__attempts=attempts #count of attempts
        self.__line=""
        self.__word=""
        self.__tries=0#count of attempts left
        self.hint_letter=""
        
    def random_word(self):
        """Choose one word from file"""
        with open("WordsStockRus.txt","r",encoding="utf-8") as afile:
            self.__line = next(afile)
            for num, aline in enumerate(afile, 2):
              if random.randrange(num): continue
              self.__line = aline.strip()
              self.__word=len(self.__line)*"-"
        return self.__word

    def check_tries(self):
        """used attempts counter/if the player lost"""
        if self.__tries>=self.__attempts:
            return True
    
    def open_first_letter(self):
        letter=list(self.__line)[0]
        word=list(self.__word)
        if word[0]=="-":
            for i,c in enumerate(self.__line):
                if c==letter:
                    word[i]=letter
        self.__word="".join(word)
        return self.__word
    
    def open_last_letter(self):
        letter=list(self.__line)[-1]
        word=list(self.__word)
        if word[-1]=="-":
            
            for i,c in enumerate(self.__line):
                if c==letter:
                    word[i]=letter
        self.__word="".join(word)
        return self.__word

    def open_random_letter(self):
        while True:
            letter=random.choice(list(self.__line))
            if letter in self.__word:
                continue
            word=list(self.__word)
            for i,c in enumerate(self.__line):
                if c==letter:
                    word[i]=letter
            self.__word="".join(word)
            return self.__word

    def enter_letter(self,letter):
        """letter substitution"""
        word=list(self.__word)
        if letter in self.__line:
            for i,c in enumerate(self.__line):
                if c==letter:
                    word[i]=letter
        else:
            self.__tries+=1
        self.__word="".join(word)
        return self.__word
    
    def finish_game(self):
        """if the player wins"""
        if not "-" in self.__word:
            return True
    
    @property
    def remaining_attempts(self):
        """return coun of remaining attempts"""
        return self.__attempts-self.__tries

    @property
    def tries(self):
        return self.__tries

    @property
    def line(self):
        return self.__line

    @property
    def word(self):
        return self.__word
    

        
