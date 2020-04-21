#include <stdio.h>
int main()
{
	int a, b;
	for (a = 1; a < 10; a++)
	{
		if (a <=5)
		{
			for (b = 1; b <= 5- a; b++)
			{
				printf(" ");
			}

			for (b > 5- a; b <5 + a; b++)
			{
				printf("*");
			}
			printf("\n");
		}

		else
		{
			for (b = 1; b <= a-5; b++)
			{
				printf(" ");
			}

			for (b > a-5; b <=14-a; b++)
			{
				printf("*");
			}
			printf("\n");
		}
			
		}
}
