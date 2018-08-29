INC = -I../include/

OBJ_DIR = ../obj/

OBJ = $(OBJ_DIR)main.o $(OBJ_DIR)add.o $(OBJ_DIR)sub.o

test:$(OBJ)
	gcc -o test $(OBJ)
	
$(OBJ_DIR)main.o:main.c
	gcc $(INC) -c main.c -o $(OBJ_DIR)main.o

$(OBJ_DIR)add.o:add.c
	gcc $(INC) -c add.c -o $(OBJ_DIR)add.o
	
$(OBJ_DIR)sub.o:sub.c
	gcc $(INC) -c sub.c -o $(OBJ_DIR)sub.o

clean:
	-rm -rf test.exe $(OBJ)
	-rm -rf test.ese main.o add.o sub.o