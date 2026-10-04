#include <stdio.h>

int main(){
		int a, b, temp;
		printf("Enter a, b:\n"); //asking for input values
		scanf("%d %d", &a, &b); //scanning the values
                temp = a, a = b, b = temp; //interchanging the values of a and b
		printf("a = %d b = %d\n", a, b); //printing the values of a and b after interchanging on screen
	return 0;
}
