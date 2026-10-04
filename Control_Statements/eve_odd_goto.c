#include <stdio.h>


int main()
{
	int n;
	printf("Enter a number:\n");
	if (scanf("%d", &n) != 1)
        {
            printf("Invalid input, integers only.\n");
            while (getchar() != '\n'); // clear buffer
        }
	if( n % 2 == 0 )
		goto even;
	else
		goto odd;
	
even:
	printf("%d is even", n);
	goto end;

odd:
	printf("%d is odd", n);
	goto end;

end:
	printf("\n");
	return 0;
}

