#include <stdio.h>

int main(){
	int a, b; // variable declaration
	printf("Enter two numbers:\n"); // asking user to input two values
        scanf("%d %d", &a, &b); // scanning the input values
	printf("%d\n", (a > b) ? (a + b) : (a - b)); // printing sum if first number is greater than seconnd number else printing the difference
	return 0;
}
