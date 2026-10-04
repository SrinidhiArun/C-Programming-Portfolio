#include <stdio.h>

int main(){
		int n;
		printf("Enter a number:");
		scanf("%d", &n);
		if(n < 0)
			printf("The number entered is negative\nValue of the number is: %d\n", n);
	return 0;
}
