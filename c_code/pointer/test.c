
#include<stdio.h>
#include<stdlib.h>
#include<assert.h>

typedef unsigned char u8;

typedef struct _Node
{
	u8 i;
	u8 j;
}Node;

Node pMemory;

static Node* get_node()
{
	return &pMemory;
}

static u8 init_node()
{
	Node* pTem = get_node();
	pTem->i = 1;
	pTem->j = 2;
	
	return 0;
}

int main(void)
{
	init_node();
	printf("%d,%d", pMemory.i,pMemory.j);
	
	return 0;
}