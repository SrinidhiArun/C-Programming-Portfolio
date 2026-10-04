#include <stdio.h>

int main(){
		int a, b, c, sum;
		printf("Sum = %d\n", (sum = (a = 5, b = 6, c = 7, a + b + c)));
	return 0;
}

