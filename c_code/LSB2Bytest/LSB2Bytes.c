
#include <stdio.h>
#include <string.h>
int main(void)
{
	unsigned int Int32 = 0x1234;
	unsigned short int Short16 = 0;
	
	Short16 = Int32 & 0x00FF;
	
	printf("%x\n%d", Short16,Short16);
	
	return 1;
}