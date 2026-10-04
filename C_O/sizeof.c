#include <stdio.h>

// sizeof operator is used to make portable programs, i.e., programs that can be run on different machines. To make general code that can run on all machines, sizeof operator can be used.



int main(){
		int var;
			printf("Size of int = %ld\n", sizeof(int)); // prints the size of integer data type
			printf("Size of char = %ld\n", sizeof(char)); // prints the size of char data type
			printf("Size of float = %ld\n", sizeof(float)); // prints the size of float data type
			printf("Size of double = %ld\n", sizeof(double)); // prints the size of double data type
			printf("Size of long double = %ld\n", sizeof(long double)); // prints the size of long double data type
			printf("Size of integer constant = %ld\n", sizeof(45)); // prints the size of an integer constant
			printf("Size of var= %ld\n", sizeof(var)); // prints the size of the variable named var
	return 0;
}
