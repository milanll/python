
/*
#include <linux/module.h>
#include <linux/init.h>
#include<linux/sched.h>
#include<linux/sem.h>
#include <linux/slab.h>
*/
#include <linux/list.h>
#include <stdio.h>

typedef struct a
{
	struct list_head TaNode;
	int 	a;
	int 	b;
}Ta;

typedef struct b
{
	struct list_head TbNode;
	int 	c;
	int 	d;
}Tb;

typedef struct c
{
	struct list_head TcNode;
	int 	e;
	int 	f;
}Tc;

int main (void)
{
	Ta A;
	Tb B;
	Tc C;
	
	LIST_HEAD_INIT(A);
	LIST_HEAD_INIT(B);
	LIST_HEAD_INIT(C);
	
	A.a = 1;
	A.b = 2;
	
	return 0;
}