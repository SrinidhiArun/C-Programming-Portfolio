#include <stdio.h>

int main()
{
	char ch;
	printf("Enter a letter:\n");
	scanf(" %c", &ch);
	switch(ch)
	{
		case 'A':
		case 'E':
		case 'I':
		case 'O':
		case 'U':	
		case 'a': 
		case 'e': 
		case 'i': 
		case 'o': 
		case 'u': printf("%c is a vowel\n", ch);
			  break;
		default: printf("%c is a consonant\n", ch);
	}
	return 0;
}
