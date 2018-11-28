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
    
    def __init__(self):
        
        self.root = Tk()
        self.root.title("语文练习")
        self.root.geometry('700x550')
        ########
        self.frm = Frame(self.root)
        #Top
        Label(self.root, text="语文练习", font=('Arial', 40)).pack()
        self.load_sys()
        self.frm = Frame(self.root)
        
        #Left
        self.frm_L = Frame(self.frm)
        Button(self.frm_L, text="认字", command=self.read_word, width=10, height=2, font=('Arial', 10)).pack(side=TOP)
        Button(self.frm_L, text="默写生字", command=self.write_char, width=10, height=2, font=('Arial', 10)).pack()
        Button(self.frm_L, text="默写拼音", command=self.write_pinyin, width=10, height=2, font=('Arial', 10)).pack()
        Button(self.frm_L, text="停止", command=self.stop_1, width=10, height=2, font=('Arial', 10)).pack()
        Button(self.frm_L, text="退出", command=self.exit_1, width=10, height=2, font=('Arial', 10)).pack(side=BOTTOM)
        self.frm_L.pack(side = LEFT)

        #Right
        self.frm_R = Frame(self.frm)
        
        self.t_show_top = Text(self.frm_R, width=5, height=1, font =('Verdana',100))
        self.t_show_top.insert('1.0', '')
        self.t_show_top.pack(side=TOP)
        
        self.t_show_mid = Text(self.frm_R, width=5, height=1, font =('Verdana',100), fg='red')
        self.t_show_mid.insert('1.0', '')
        self.t_show_mid.pack()
        
        self.t_show_bottom = Text(self.frm_R, width=25, height=2, font =('Verdana',20))
        self.t_show_bottom.insert('1.0', '')
        self.t_show_bottom.pack()

        self.frm_R.pack(side=RIGHT)
        
        #Bottom
        '''
        self.frm_B = Frame(self.frm)
        Button(self.frm_B, text="设置", command=self.read_word, width=10, height=2, font=('Arial', 10)).pack(side = BOTTOM)
        
        self.count_1 = StringVar()
        Entry(self.frm_B, textvariable=self.count_1, width = 5, font =('Verdana',15)).pack(side=RIGHT)
        Label(self.frm_B, text = '数量', font =('Arial',12)).pack(side = TOP)
        
        self.duration = StringVar()
        Entry(self.frm_B, textvariable=self.duration, width = 5, font =('Verdana',15)).pack(side=RIGHT)
        Label(self.frm_B, text = '间隔(S)', font =('Arial',12)).pack()

        self.frm_B.pack(side=RIGHT)
        '''
        self.frm.pack()
        ########

    def read_word(self):
        self.reset()
        self.duration = 3
        self.count = 20
        self.button = 'read_word'
        self.text =self.t_show_top
        
        self.random_numbers = self.get_random()
        
        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()
           
    def write_pinyin(self):
        self.reset()
        self.duration = 12
        self.count = 10
        self.button = 'write_pinyin'
        self.text = self.t_show_mid
        
        self.random_numbers = self.get_random()
        
        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()
    
    def write_char(self):
        pass
       
    def exit_1(self):
        self.stop_timer()
        self.root.destroy()
     
    def stop_1(self):
        self.stop_timer()
        
    def load_sys(self):
        self.timer = None
        self.button = None
        self.text = None
        self.duration = 2
        
        count = 10
        count_temp = 0
        
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
        print(self.random_numbers[self.count_temp], self.count_temp)
        char = self.characters[self.random_numbers[self.count_temp] - 1]
        self.count_temp += 1
        return char
     
    def show_word(self):
        char = self.get_char()
        self.text.delete('1.0', 'end')
        self.text.insert('1.0', char)
        
        self.stop_timer()
        self.timer = threading.Timer(self.duration, self.show_word)
        self.timer.start()
        
        if self.count_temp == self.count:
            print('Expiry!!')
            self.timer.cancel()
            
            char_set = []
            if self.button == 'write_pinyin':
                for i in self.random_numbers:
                    char_set.append(self.characters[i - 1])
                self.t_show_bottom.insert('1.0', char_set)
    
    def reset(self):
        self.count_temp = 0
        
        self.t_show_top.delete('1.0', 'end')
        self.t_show_mid.delete('1.0', 'end')
        self.t_show_bottom.delete('1.0', 'end')
        
        self.stop_timer()
        
    def stop_timer(self):
        if self.timer:
            self.timer.cancel()
            
def main():
    d = show()
    mainloop()
if __name__== "__main__":
    main()
    #get_random(50, 10)
    
    
    
    