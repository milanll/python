# 指令编译器和选项
CC=gcc
CFLAGS= -std=gnu99 -Wall

# 编译控制
version = chenll

CUR_DIR = $(shell pwd)

OBJ = $(OBJ_DIR)main.o $(OBJ_DIR)add.o $(OBJ_DIR)sub.o

LIB = -lm -lpthread 

INC = -I../include/

OBJ_DIR = ../obj/

test:$(OBJ)
	$(CC) $(CFLAGS) -o test $(OBJ)

%.o:%.c
	$(CC) $(CFLAGS) $(INC) -o $(OBJ_DIR)$@ -c $<

clean:
	-rm -rf $(OBJ) test.exe