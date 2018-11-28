# -*- coding:utf-8 -*-
from tkinter import *
import sys, threading

class show:
    #词语list
    words = []
    len_word = 0
    
    #汉字list
    characters = []
    len_char = 0
    
    #a group of random numbers
    random_numbers = []
    
    count = 10
    j = 0
    
    
    
    def __init__(self):
        
        self.root = Tk()
        self.root.title("语文练习")
        self.root.geometry('600x400')
        ########
        self.frm = Frame(self.root)
        #Top
        Label(self.root, text="语文练习", font=('Arial', 15)).pack()
        self.load_sys()
        self.frm = Frame(self.root)
        
        #Left
        self.frm_L = Frame(self.frm)
        Button(self.frm_L, text="认字", command=self.read_word, width=10, height=2, font=('Arial', 10)).pack(side=TOP)
        Button(self.frm_L, text="默写", command=self.write_pinyin, width=10, height=2, font=('Arial', 10)).pack(side=BOTTOM)
        self.frm_L.pack(side = LEFT)

        #Right
        self.frm_R = Frame(self.frm)
        
        self.t_show_top = Text(self.frm_R, width=5, height=3, font =('Verdana',100))
        self.t_show_top.insert('1.0', '')
        self.t_show_top.pack(side=TOP)
        
        self.t_show_bottom = Text(self.frm_R, width=10, height=2, font =('Verdana',15))
        self.t_show_bottom.insert('1.0', '')
        
        #self.t_show_bottom.pack(side=BOTTOM)

        self.frm_R.pack(side=RIGHT)
        
        self.frm.pack()
        ########

    def read_word(self):
        timer_1 = threading.Timer(0.2, self.show_word)
        timer_1.start()
           
    def write_pinyin(self):
        pass
        
    def load_sys(self):
        try:
            f = open('word.txt', encoding = 'utf-8')
            for line in f:
                #'lesson_1','秋气了树叶片大飞会个'
                d = line.strip().split(',')
                #print(d)
                for w in d[1]:
                    if w != ' ':
                        self.characters.append(w)
            self.len_char = len(self.characters)
            print(self.characters)
            print(self.len_char)
            
            self.random_numbers = self.get_random()
            
        except:
            print(sys.exc_info())
        

    #breif  get m number in range 0~n
    #input  n(int)              range 0~n
    #       m(int)              get count m
    #retrun random_num(list)    [6, 34, 13, 24, 40, 39, 40, 6, 24, 27]   
    def get_random(self):
        import random
        i = 0
        random_num = []
        while(i < self.count):
            random_number = random.randint(0,self.len_char)
            if  random_number not in random_num:
                i += 1
                random_num.append(random_number)
                       
        print('\nRandom Numbers:', random_num, '\n')
        return random_num
    
    def get_char(self):
        print(self.random_numbers[self.j], self.j)
        char = self.characters[self.random_numbers[self.j] - 1]
        self.j += 1
        return char
     
    def show_word(self):
        char = self.get_char()
        self.t_show_top.delete('1.0', 'end')
        self.t_show_top.insert('1.0', char)
        
        timer = threading.Timer(2, self.show_word)
        timer.start()
        
        if self.j == self.count:
            print('Expiry!!')
            timer.cancel()
        
        
def main():
    d = show()
    mainloop()
if __name__== "__main__":
    main()
    #get_random(50, 10)
    
    
    
    