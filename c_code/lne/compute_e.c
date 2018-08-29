
#include <stdio.h>
#include <math.h>

int main(void)
{
#if 1
	int j = 100;
	float a, b, c;
	float E = 0;
	
	for(int n = 1; n < j; n++)
	{
		a = (float)1/n;
		b = 1 + a;
		E = pow(b, n);
		
		printf("%8f, %d\n", E, n);
	}
#endif
	return 0;
}