# -*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox
import sys, threading
import pinyin
import csv as _csv

class show:
    #词语list
    words = []
    len_word = 0
    
    #蓝线汉字list
    characters = []
    len_char = 0
    
    #田字格汉字list
    chinese = []
    len_chinese = 0
    
    #扩词表list
    chinese_extend = []
    len_chinese_extend = 0
    
    #a group of random numbers
    random_numbers = []
    random_range = 0
    
    def __init__(self):
        
        self.root = Tk()
        self.root.title("语文练习")
        self.root.geometry('700x500')
        self.load_sys()
        
        ########
        self.frm = Frame(self.root)
        
        #Top
        Label(self.root, text="语文练习", font=('Arial', 40)).pack()
        
        #Left
        self.frm_L = Frame(self.frm)
        self.frm_L_A = Frame(self.frm_L)
        Button(self.frm_L_A, text="认字", command=self.read_word, width=10, height=2, font=('Arial', 10)).pack(side=TOP)
        Button(self.frm_L_A, text="默写生字", command=self.write_chinese, width=10, height=2, font=('Arial', 10)).pack()
        Button(self.frm_L_A, text="默写拼音", command=self.write_pinyin, width=10, height=2, font=('Arial', 10)).pack()
        Button(self.frm_L_A, text="停止", command=self.stop_1, width=10, height=2, font=('Arial', 10)).pack()
        Button(self.frm_L_A, text="退出", command=self.exit_1, width=10, height=2, font=('Arial', 10)).pack()
        self.frm_L_A.pack(side=RIGHT)
        
        self.frm_L_B = Frame(self.frm_L)
        self.frm_L_B_A = Frame(self.frm_L_B)
        self.input_count = StringVar()
        Entry(self.frm_L_B_A, textvariable=self.input_count, width = 5, font =('Verdana',12)).pack(side=RIGHT)
        Label(self.frm_L_B_A, text = '数量', font =('Arial',10)).pack(side = LEFT)
        self.frm_L_B_A.pack()
        
        self.frm_L_B_B = Frame(self.frm_L_B)
        self.input_duration = StringVar()
        Entry(self.frm_L_B_B, textvariable=self.input_duration, width = 5, font =('Verdana',12)).pack(side=RIGHT)
        Label(self.frm_L_B_B, text = '间隔(S)', font =('Arial',10)).pack(side = LEFT)
        self.frm_L_B_B.pack()
        
        self.frm_L_B_C = Frame(self.frm_L_B)
        Button(self.frm_L_B_C, text="设置认字", command=self.set_read, width=10, height=2, font=('Arial', 10)).pack()
        Button(self.frm_L_B_C, text="设置默写", command=self.set_write, width=10, height=2, font=('Arial', 10)).pack()
        self.frm_L_B_C.pack()
        
        self.frm_L_B.pack(side=RIGHT)
        
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
        #

        self.frm.pack()
        ########
     
    #Initiate
    def load_sys(self):
        self.timer = None
        self.button = None
        self.text = None
        
        self.duration = 0
        self.count = 0
        self.count_temp = 0
        
        self.duration_read = 3
        self.duration_write = 15
        self.count_read = 20
        self.count_write = 10
        
        try:
            f1 = open('word.txt', encoding = 'utf-8')
            for line in f1:
                #'lesson_1','秋气了树叶片大飞会个'
                d = line.strip().split(',')
                #print(d)
                #读取蓝线汉字
                for d4 in d[4]:
                    if d4 != '0' and d4 != '\t':
                        self.characters.append(d4)
                
                #读取田字格汉字
                for d5 in d[5]:
                    if d5 != '0' and d5 != '\t':
                        self.chinese.append(d5)
           
            self.len_char = len(self.characters)
            self.len_chinese = len(self.chinese)
            print(self.characters)
            print(self.len_char)
            print(self.chinese)
            print(self.len_chinese)
            
            #读取扩词表
            f2 = open('word.txt', 'r', encoding = 'utf-8')
            reader = _csv.reader(f2)
            for l in reader:
                l[6] = l[6].strip('\t')
                if l[6] != '0':
                    word_1 = l[6].split('-')
                    for w in word_1:
                        self.chinese_extend.append(w)
                    
            self.len_chinese_extend = len(self.chinese_extend)
            print(self.chinese_extend)
            print(self.len_chinese_extend)
        except:
            print(sys.exc_info())
    
    #Button         
    def read_word(self):
        self.reset()
        self.duration = self.duration_read
        self.count = self.count_read
        self.button = 'read_word'
        self.text =self.t_show_top
        self.random_range = self.len_char
        
        self.random_numbers = self.get_random()
        
        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()
           
    def write_pinyin(self):
        self.reset()
        self.duration = self.duration_write
        self.count = self.count_write
        self.button = 'write_pinyin'
        self.text = self.t_show_mid
        self.random_range = self.len_char
        
        self.random_numbers = self.get_random()
        
        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()
    
    def write_chinese(self):
        self.reset()
        self.duration = self.duration_write
        self.count = self.count_write
        self.button = 'write_chinese'
        self.text = self.t_show_bottom
        
        self.random_range = self.len_chinese_extend
        self.random_numbers = self.get_random()
        
        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()
       
    def exit_1(self):
        self.stop_timer()
        self.root.quit()
     
    def stop_1(self):
        self.stop_timer()
        
    def set_read(self):
        #print(type(self.count_1.get()), self.duration.get())
        self.duration_read = int(self.input_duration.get())
        self.count_read  = int(self.input_count.get())
    
    def set_write(self):
        #print(type(self.count_1.get()), self.duration.get())
        self.duration_write = int(self.input_duration.get())
        self.count_write  = int(self.input_count.get())

    #breif  get m number in range 0~n
    #input  n(int)              range 0~n
    #       m(int)              get count m
    #retrun random_num(list)    [6, 34, 13, 24, 40, 39, 40, 6, 24, 27]   
    def get_random(self):
        import random
        i = 0
        random_num = []
        while(i < self.count):
            random_number = random.randint(0,self.random_range)
            if  random_number not in random_num:
                i += 1
                random_num.append(random_number)
                       
        print('\nRandom Numbers:', random_num, '\n')
        return random_num
    
    def get_char(self):
        print(self.random_numbers[self.count_temp], self.count_temp)
        if self.button == 'write_chinese':
            char1 = self.chinese_extend[self.random_numbers[self.count_temp] - 1]
            char = pinyin.get(char1, delimiter = ' ')
            print(char,char1)
        elif (self.button == 'read_word') or (self.button == 'write_pinyin'):
            char = self.characters[self.random_numbers[self.count_temp] - 1]
        else:
            assert(0)
        
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
            
            #if the button is 'write_pinyin', display the words at the end.
            char_set = []
            if self.button == 'write_pinyin':
                for i in self.random_numbers:
                    char_set.append(self.characters[i - 1])
                self.t_show_bottom.insert('1.0', char_set)
                
                #pop message box at the end
                tkinter.messagebox.showinfo('write_pinyin', '默写拼音结束！')
            elif self.button == 'read_word':
                #pop message box at the end
                tkinter.messagebox.showinfo('read_word', '认字结束！')
            elif self.button == 'write_chinese':
                tkinter.messagebox.showinfo('read_word', '默写汉字结束！')
            else:
                pass
            
            
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
    
    
    
    