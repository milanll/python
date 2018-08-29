#include "DList.h"

static u8 dlist_init(DList* thiz)
{
	thiz->nodeNum = 0;
	thiz->head = thiz->tail = NULL;
	
	return Ret_OK;
}

static u8 dlist_insert_node_tail(DList* thiz, DListNode* node)
{
	assert((thiz != NULL) && (node != NULL));
	
	if(thiz->tail)
	{
		node->prev = thiz->tail;
		thiz->tail->next = node;
		thiz->head->prev = node;
		node->next = thiz->head;
		thiz->tail = node;
	}
	else	//head is null, insert first node
	{
		thiz->head = node;
		thiz->head->next = thiz->head->prev = node;
		
		thiz->tail = node;
		thiz->tail->next = thiz->tail->prev = node;
	}
	
	thiz->nodeNum++;
	
	return Ret_OK;
}

static u8 dlist_insert_node_head(DList* thiz, DListNode* node)
{
	assert((thiz != NULL) && (node != NULL));
	//DListNode** head = NULL;
	//*head = thiz->head;

	if(thiz->head)
	{
		node->next = thiz->head;
		thiz->head->prev = node;
		thiz->tail->next = node;
		node->prev = thiz->tail;
		thiz->head = node;	
	}
	else	//head is null, insert first node
	{
		thiz->head = node;
		thiz->head->next = thiz->head->prev = node;
		
		thiz->tail = node;
		thiz->tail->next = thiz->tail->prev = node;

		//printf("%d,%d",thiz->head,thiz->tail);
	}
	
	thiz->nodeNum++;
	
	return Ret_OK;
}

/**
	breif:insert a node to a list at a certain position.
	[in]thiz:the list.
	[in]node:the node to be inserted to a list.
	[in]position:the position after where a node to be inserted.
*/
static u8 dlist_insert_node(DList* thiz, DListNode* node, DListNode* position)
{
	assert((thiz != NULL) && (node != NULL) && (position != NULL));
	DListNode* iter = thiz->head;
	
	do
	{
		/* if find the position */
		if(iter == position)
		{
			node->next = position->next;
			position->next->prev = node;
			position->next = node;
			node->prev = position;
			
			if(position == thiz->head)
			{
				thiz->head = node;
			}
			else if(position == thiz->tail)
			{
				thiz->tail = node;
			}
			else
			{}
			
			break;
		}
		
		/* if not find the position in the list */
		if(iter = thiz->tail)
		{
			return Ret_Fail;
		}
		
		iter = iter->next;
	}while(iter != thiz->head);
	
	return Ret_OK;
}

static u8 dlist_print(DList* thiz, DListDataPrintFunc print)
{
	assert((thiz != NULL) && (print != NULL));
	DListNode* iter = thiz->head;
	
	do
	{
		print(iter->Data);
		iter = iter->next;
	}while(iter != thiz->head);
	
	return Ret_OK;
}

static u8 print_int(void* data)
{
	//assert(data != NULL);
	printf("%d\n", (int)data);
	return Ret_OK;
}

#if 1
int main(void)
{
	u8 u8Ret = Ret_OK;
	DListNode node[10];
	memset(&node, 0, sizeof(DListNode) * 10);
	
	DList dlist;
	u8Ret = dlist_init(&dlist);
	
	assert(u8Ret == Ret_OK);
	
	for(int i = 0; i < 10; i++)
	{
		node[i].Data = (void *)i;
		u8Ret = dlist_insert_node_head(&dlist, &node[i]);
		assert(u8Ret == Ret_OK);
	}
	
	u8Ret = dlist_print(&dlist, print_int);
	assert(u8Ret == Ret_OK);

	return Ret_OK;
}
#endif


