
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

#include <string.h>
#include <errno.h>
#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <dirent.h>

//#define FILE_PATH "E:\C_Test_Cygwin\Decode_Esm_Message\Code_Stream.txt"  // 文件路径
#define FILE_NAME "Code_Stream.txt"


void readFile(char *pBuffer) {
        char s[] = FILE_NAME;
        //只读打开文件
        int fd = open(s, O_RDONLY);

        if(fd == -1) {
                printf("error is %s\n", strerror(errno));
                return;
        }

        printf("sucess fd = %d\n", fd);
        char buf[100];
        memset(buf, 0, sizeof(buf));
        //read返回0表示文件读取完毕
        while(read(fd, buf, sizeof(buf) - 1) > 0) {
                //printf("%s\n", buf);
				memcpy(pBuffer, buf, sizeof(buf));
				pBuffer += sizeof(buf);
                memset(buf, 0, sizeof(buf));
        }
		
		//memcpy(pBuffer, buf, sizeof(buf));
        //printf("%s\n", buf);
        //别忘记关闭
        close(fd);
}

void DeleteBlankInArray(char *pBuffer, char *pOutBuff)
{
	char *pTemp = NULL;
	pTemp = pOutBuff;
	while(*pBuffer++ != '\0')
	{
		if(*pBuffer != ' ')
		{
			*pTemp = *pBuffer;
			printf("%c\n", *pTemp++);
			pTemp++;
		}
		
	}
	return;
}

int main()
{	
	int i = 0, j = 0;
	int lengthOfArrary = 0;
	unsigned char pTemp = 0;
	char pBuffer[512] = {0};
	char pCodeStream[512] = {0};
#if 0
	unsigned char pBuffer[] =  {0X03,0X00,0X10,0X12,0X67,0X00,0X00,0X00,0X63,0X00,0X52,0X01,0XC1,0X01,0X07,0X2C,
								0X06,0X63,0X6D,0X77,0X35,0X30,0X30,0X0D,0X72,0X6F,0X68,0X64,0X65,0X2D,0X73,0X63,
								0X68,0X77,0X61,0X72,0X7A,0X03,0X63,0X6F,0X6D,0X06,0X6D,0X6E,0X63,0X30,0X30,0X31,
								0X06,0X6D,0X63,0X63,0X30,0X30,0X31,0X04,0X67,0X70,0X72,0X73,0X05,0X01,0XC0,0XA8,
								0X30,0X81,0X5D,0X01,0X00,0X30,0X0C,0X14,0X42,0X1F,0X6B,0X96,0X10,0X40,0X62,0X2A,
								0X0A,0X20,0X00,0X32,0X05,0X81,0X27,0X15,0X80,0X80,0X21,0X0A,0X03,0X00,0X00,0X0A,
								0X81,0X06,0XC0,0XA8,0X30,0X6F,0X00,0X0D,0X04,0XC0,0XA8,0X30,0X6F,0X00,0X00
								};
#endif
	
	readFile(pBuffer);
	DeleteBlankInArray(pBuffer, pCodeStream);
	/*
	while(pCodeStream[i++] != ' ')
	{
		printf("%c\n", pCodeStream);
		if(i % 16 == 0)
		{
			printf("\n");
		}
	}
	*/
	i += 10;
	pTemp = pBuffer[i] & 0x0F;
	if(2 == pTemp)
	{
		printf("PD:  ESM\n");
	}
	
	pTemp = (pBuffer[i] >> 4) & 0x0F;
	printf("EBI:  %d\n", pTemp);
	
	i++;
	pTemp = pBuffer[i];
	printf("PTI:  %d\n", pTemp);
	
	i++;
	pTemp = pBuffer[i];
	printf("MessageType:  ");
	switch(pTemp)
	{
	case 0xc1:
		printf("Activate default EPS bearer context request\n");
		break;
	default:
		break;
	}
	return 0;
}