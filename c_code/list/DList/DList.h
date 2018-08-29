#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <memory.h>

#define Ret_OK 		0
#define	Ret_Fail	1

typedef struct _DListNode
{
	struct _DListNode* prev;
	struct _DListNode* next;
	
	void* Data;
}DListNode;

typedef struct _DList
{
	DListNode* head;
	DListNode* tail;
	int nodeNum;
}DList;

typedef unsigned char u8;
typedef u8 (*DListDataPrintFunc)(void* Data);

static u8 dlist_init(DList* thiz);
static u8 dlist_insert_node_head(DList* thiz, DListNode* node);
static u8 dlist_insert_node_tail(DList* thiz, DListNode* node);
static u8 dlist_insert_node(DList* thiz, DListNode* node, DListNode* position);

static u8 dlist_delete_node(DList* thiz, DListNode* node);
static u8 dlist_get_node(DList* thiz, void* pData);
static u8 dlist_print(DList* thiz, DListDataPrintFunc print);