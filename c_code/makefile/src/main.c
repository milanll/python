#include <stdio.h>
#include "method.h"

int main(void)
{
	int i = 1, j = 2, m = 3, n =4, result = 0;
	
	result = add(i,j);
	printf("i+j=%d\n", result);
	
	result = sub(m,n);
	printf("m-n=%d\n", result);
	
	return 0;
}