# -*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox
import sys, threading, time
import pinyin
import csv
from pinyin_ import pinyin_
from read_word_txt import get_words_dict
from copy import deepcopy

class show:
    #all data
    words = {}
    len_words = 0

    # struct of word.txt
    struct = {}

    #蓝线汉字list
    characters = []
    len_char = 0
    
    #根据unit选择后的蓝线汉字list
    characters_unit = []
    len_char_unit = 0
    
    #田字格汉字list
    chinese = []
    len_chinese = 0
    
    #扩词表list
    chinese_extend = []
    len_chinese_extend = 0
    
    #根据unit选择后的扩词表listlist
    characters_extend_unit = []
    len_char_extend_unit = 0
    
    #a group of random numbers
    random_numbers = []
    random_range = 0

    #读一个汉字/词语的时长
    duration_read = 0
    #写一个汉字/拼音的时长
    duration_write = 0
    #组词时长
    duration_combine_word = 0

    #随机选择识读字词的个数
    count_read = 0
    #随机选择写汉字/拼音的个数
    count_write = 0
    #选择田字格汉字进行组词，所选汉字的个数
    count_combine_word = 0

    #struct list
    term = ['一年级（上）']
    unit_options = ['unit-all']

    #
    timer_combine_word = None

    #
    char_display = None

    def __init__(self):
        
        self.root = Tk()
        self.root.title("语文练习")
        self.root.geometry('700x600')
        self.load_sys()
        
        ########
        self.frm_L = Frame(self.root)
        
        #Top
        Label(self.root, text="语文练习", font=('Arial', 40)).pack()
        
        #Left
        self.frm_L_A = Frame(self.frm_L)
        Button(self.frm_L_A, text="识读字词", command=self.read_word, width=10, height=2, font=('Arial', 10)).pack(side=TOP)
        Button(self.frm_L_A, text="组词练习", command=self.combine_word, width=10, height=2, font=('Arial', 10)).pack()
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
        Button(self.frm_L_B_C, text="设置组词", command=self.set_combine_word, width=10, height=2, font=('Arial', 10)).pack()
        Button(self.frm_L_B_C, text="设置默写", command=self.set_write, width=10, height=2, font=('Arial', 10)).pack()
        self.frm_L_B_C.pack()

        '''
        # 学期下拉列表
        self.frm_L_B_D = Frame(self.frm_L_B)
        self.OM_unit = StringVar(self.frm_L_B_D)
        self.OM_unit.set(self.unit_options[0]) # default value
        '''

        # 单元下拉列表
        self.frm_L_B_D = Frame(self.frm_L_B)
        self.OM_unit = StringVar(self.frm_L_B_D)
        self.OM_unit.set(self.unit_options[0])  # default value
         
        #self.w = OptionMenu(self.frm_L_B_D, self.variable, "one", "two", "three")
        self.w = OptionMenu(self.frm_L_B_D, self.OM_unit, *self.unit_options)
        self.w.pack()
        self.frm_L_B_D.pack()

        self.frm_L_B.pack(side=RIGHT)
        
        self.frm_L.pack(side = LEFT)

        #Right
        self.frm_R = Frame(self.root)
        
        self.t_show_top = Text(self.frm_R, width=6, height=1, font =('楷体',100))
        self.t_show_top.insert('1.0', '')
        self.t_show_top.pack(side=TOP)
        
        self.t_show_mid = Text(self.frm_R, width=6, height=1, font =('楷体',100), fg='blue')
        self.t_show_mid.insert('1.0', '')
        self.t_show_mid.pack()
        
        #self.t_show_bottom = Text(self.frm_R, width=25, height=4, font =('Verdana',20))
        self.t_show_bottom = Text(self.frm_R, width=30, height=6, font=('New Time Roma', 20))
        self.t_show_bottom.insert('1.0', '')
        self.t_show_bottom.pack()

        self.frm_R.pack(side=RIGHT)
        #

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
        self.duration_combine_word = 5

        self.count_read = 20
        self.count_write = 10
        self.count_combine_word = 10
        
        self.words = get_words_dict('word.txt')
        self.get_words_according_to_type()

        self.get_word_struct()
        
        return

    #获取汉字列表word.txt的结构，{学期:'单元，.....'}
    def get_word_struct(self):
        l = []
        l_temp = []
        for (k, v) in self.words.items():
            l_temp.clear()

            for k1 in v.keys():
                l_temp.append(k1)

            l = deepcopy(l_temp)
            self.struct[k] = l_temp

        return

    #按'蓝线字','田字格字', '扩词表'分类
    def get_words_according_to_type(self):
        
        for (k1, v1) in self.words.items():
            #initiate unit_options
            for key in v1.keys():
                if key not in self.unit_options:
                    self.unit_options.append(key)
                    
            #读汉字和词语
            for (k2, v2) in v1.items():
                for (k3, v3) in v2.items():
                    #读入蓝线字
                    for l in v3['蓝线字']:
                        self.characters.append(l)
                    #读入田字格字    
                    for t in v3['田字格字']:
                        if t != '0':
                            self.chinese.append(t)
                    #读入扩词表        
                    k1 = v3['扩词表']
                    if k1 != '0':
                        k2 = k1.split('-') 
                        for k in k2:
                            self.chinese_extend.append(k)
                                    
        self.len_char = len(self.characters)
        #print(self.characters)
        #print(self.len_char)
                
        self.len_chinese = len(self.chinese)
        #print(self.chinese)
        #print(self.len_chinese)
                    
        self.len_chinese_extend = len(self.chinese_extend)
        #print(self.chinese_extend)
        #print(self.len_chinese_extend)
        
        return
        
    #按钮：识读字词
    def read_word(self):
        self.reset()
        self.duration = self.duration_read
        self.count = self.count_read
        self.button = 'read_word'
        self.text =self.t_show_top
        
        self.get_words_according_to_unit()
        
        if self.len_char < self.count:
            self.count = self.len_char
            
        self.random_range = self.len_char
        self.random_numbers = self.get_random()
        
        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()
        
        print(self.characters, '\n\nCharacters Length:', len(self.characters), '\n')
        
        return

    #按钮：组词
    def combine_word(self):
        self.reset()
        self.duration = 15
        self.count = self.count_combine_word
        self.button = 'combine_word'
        self.text = self.t_show_mid

        self.get_words_according_to_unit()

        if self.len_chinese < self.count:
            self.count = self.len_chinese

        self.random_range = self.len_chinese
        self.random_numbers = self.get_random()

        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()

        print(self.chinese, '\n\nChinese Length:', len(self.chinese), '\n')

        return

    #按钮：默写拼音
    def write_pinyin(self):
        self.reset()
        self.duration = self.duration_write
        self.count = self.count_write
        self.button = 'write_pinyin'
        self.text = self.t_show_mid
        
        self.get_words_according_to_unit()
        
        if self.len_char < self.count:
            self.count = self.len_char

        self.random_range = self.len_char
        self.random_numbers = self.get_random()
        
        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()
        
        print(self.characters, '\n\nCharacters Length:', len(self.characters), '\n')
        
        return

    #按钮：默写汉字
    def write_chinese(self):
        self.reset()
        self.duration = 25
        self.count = self.count_write
        self.button = 'write_chinese'
        self.text = self.t_show_bottom
        
        self.get_words_according_to_unit()
        
        if self.len_chinese_extend < self.count:
            self.count = self.len_chinese_extend
            
        self.random_range = self.len_chinese_extend
        self.random_numbers = self.get_random()
        
        self.timer = threading.Timer(0.2, self.show_word)
        self.timer.start()
        
        print(self.chinese_extend, '\n\nChinese_extend Length:', len(self.chinese_extend), '\n')
        
        return

    #按钮：退出
    def exit_1(self):
        self.stop_all_timer()
        self.root.quit()

    #按钮：停止
    def stop_1(self):
        self.stop_all_timer()
        
        return
        
    def set_read(self):
        #print(type(self.count_1.get()), self.duration.get())
        self.duration_read = int(self.input_duration.get())
        self.count_read  = int(self.input_count.get())
        
        return

    def set_combine_word(self):
        self.duration_combine_word = int(self.input_duration.get())
        self.count_combine_word = int(self.input_count.get())

        return

    def set_write(self):
        #print(type(self.count_1.get()), self.duration.get())
        self.duration_write = int(self.input_duration.get())
        self.count_write  = int(self.input_count.get())
        
        return
    
    #根据下拉菜单中的unit，选择字和词语
    def get_words_according_to_unit(self):

        self.unit = self.OM_unit.get()
        
        if self.unit == 'unit-all':
            pass
        else:
            self.characters.clear()
            self.chinese.clear()
            self.chinese_extend.clear()
        
            for (k, v) in self.words.items():
                for (k1, v1) in v.items():
                    if self.unit == k1:
                        #读汉字和词语
                        for (k3, v3) in v1.items():
                            #读入蓝线字
                            for l in v3['蓝线字']:
                                self.characters.append(l)
                            #读入田字格字    
                            for t in v3['田字格字']:
                                if t != '0':
                                    self.chinese.append(t)
                            #读入扩词表        
                            k1 = v3['扩词表']
                            if k1 != '0':
                                k2 = k1.split('-') 
                                for k in k2:
                                    self.chinese_extend.append(k)
        
            self.len_char = len(self.characters)
            self.len_chinese = len(self.chinese)            
            self.len_chinese_extend = len(self.chinese_extend)
        
        return
        
    #breif  get m number in range 0~n
    #input  n(int)              range 0~n
    #       m(int)              get count m
    #retrun random_num(list)    [6, 34, 13, 24, 40, 39, 40, 6, 24, 27]   
    def get_random(self):
        import random
        i = 0
        random_num = []
        while(i < self.count):
            random_number = random.randint(0, (self.random_range - 1))
            if  (random_number) not in random_num:
                i += 1
                random_num.append(random_number)
               
        print('\nRandom Numbers:', random_num, '\nRandom Length:', len(random_num), '\n')
        
        return random_num
    
    def get_char(self):

        num = self.random_numbers[self.count_temp]
        print(num, self.count_temp)

        if self.button == 'write_chinese':
            char1 = self.chinese_extend[num]
            #char = pinyin.get(char1, delimiter = ' ')
            char = pinyin_(char1)
            print(char,char1)

        elif (self.button == 'read_word') or (self.button == 'write_pinyin'):
            char = self.characters[num]

        elif self.button == 'combine_word':
            char = self.chinese[num]

        else:
            assert(0)
        
        self.count_temp += 1
        
        return char
     
    def show_word(self):
        self.char_display = self.get_char()
        self.text.delete('1.0', 'end')
        self.text.insert('1.0', self.char_display)

        #练习字数达到设定值后，退出
        if self.count_temp == self.count:
            self.final()
            return

        #组词练习时
        if self.button == 'combine_word':
            self.t_show_bottom.delete('1.0', 'end')

            if self.timer_combine_word:
                self.timer_combine_word.cancel()

            self.timer_combine_word = threading.Timer(10, self.show_combine_word)
            self.timer_combine_word.start()

        #间隔时间后，继续显示
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.duration, self.show_word)
        self.timer.start()

        return

    def show_combine_word(self):
        for v in self.chinese_extend:
            if self.char_display in v:
                self.t_show_bottom.insert('1.0', v + ', ')

        return

    def final(self):
        self.stop_all_timer()
        time.sleep(self.duration)

        self.t_show_bottom.delete('1.0', 'end')

        # if the button is 'write_pinyin', display the words at the end.
        char_set = []
        if self.button == 'write_pinyin':
            for i in self.random_numbers:
                char_set.append(self.characters[i])
            self.t_show_bottom.insert('1.0', char_set)

            # pop message box at the end
            tkinter.messagebox.showinfo('write_pinyin', '默写拼音结束！')

        elif self.button == 'read_word':
            for i in self.random_numbers:
                char_set.append(self.characters[i])
            self.t_show_bottom.insert('1.0', char_set)

            # pop message box at the end
            tkinter.messagebox.showinfo('read_word', '认字结束！')

        elif self.button == 'write_chinese':
            print(self.random_numbers)
            for i in self.random_numbers:
                # char_set.append(pinyin_(self.chinese_extend[i]))
                self.t_show_bottom.insert('1.0', pinyin_(self.chinese_extend[i]) + ', ')

            tkinter.messagebox.showinfo('read_word', '默写汉字结束！')

        elif self.button == 'combine_word':
            tkinter.messagebox.showinfo('read_word', '组词练习结束！')

        else:
            pass

        return

    def reset(self):
        self.count_temp = 0
        
        self.t_show_top.delete('1.0', 'end')
        self.t_show_mid.delete('1.0', 'end')
        self.t_show_bottom.delete('1.0', 'end')
        
        self.stop_all_timer()
        
        return
        
    def stop_all_timer(self):
        if self.timer:
            self.timer.cancel()

        if self.timer_combine_word:
            self.timer_combine_word.cancel()

        return
            
def main():
    d = show()
    mainloop()
    
    return
    
if __name__== "__main__":
    main()
    #get_random(50, 10)
    
    
    
    
    