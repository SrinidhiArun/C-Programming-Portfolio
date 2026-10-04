#include <stdio.h>

int main(){
	int t;
	float a, b, c, d, e;
	printf("Enter the total marks:"); // asking the user to enter the total marks
	scanf("%d", &t); // scanning the input value for total marks
	printf("Enter the marks obtained in 5 subjects:"); // asking the user to enter the marks obtained in each of the 5 subjets
	scanf("%f %f %f %f %f", &a, &b, &c, &d, &e); // scanning the input values of the 5 subject marks
	printf("The total percentage obtained by the student is: %f\n", ((a + b + c + d + e) / t) * 100 ); // printing the total percentage obtained
	return 0;
}
