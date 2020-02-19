//Chapter: 6 
//Problem #: book example
//Problem Description: Recursive example


#include <stdio.h> 

long factorial(int n);

int main(void) 
{

	printf("%ld\n", factorial(6));
	
	return 0;
	
} //main

 //Function to print your bname
long factorial (int n)
{
	if ( n == 0 )
	{
		return 1;
	} else 
	{
		return (n * factorial(n - 1));
	}
}
