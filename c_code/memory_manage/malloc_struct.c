# include <stdio.h>
#include  <stdlib.h>

typedef unsigned char 	u8;
typedef unsigned short 	u16;

#define NAS_MSG_BUFFER_MAX_NUM 	600

typedef struct
{
    u16 u16EsmMsgLength;
    u8 u8EsmMsgData[NAS_MSG_BUFFER_MAX_NUM];
} MSG_LTE_EMMESM_PEERMSG_IND_t;

int main(void)
{
	MSG_LTE_EMMESM_PEERMSG_IND_t * pMsg = malloc(sizeof(MSG_LTE_EMMESM_PEERMSG_IND_t));
	assert(pMsg != NULL);
	
	printf("%d",sizeof(MSG_LTE_EMMESM_PEERMSG_IND_t));
	
	free(pMsg);
	pMsg = NULL;
	
	return 0;
}

