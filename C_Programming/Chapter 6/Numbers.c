//Gonzalo Betancourt
//CSCI 1320.2
//Date: 11/05/2-19
//Assignment # Program III
//Program can run in Windows, Mac or Linux
//Files included: main, header files, input/output, executible, etc..
//Purpose: The purpose of the program is to make a loop showing how the numbers 1 - 9
	//decrement by 1 each line.
//Input: There is no data inputs for this program
//Preconditions: The only preconditions to ot make sure we create the FILE
//Output: 
			/*
			123456789
			12345678
			1234567
			123456
			12345
			1234
			123
			12
			1
				*/
//Postconditions: None
//Algorithm: make the loop that iterates 9 times
//				 make another loop ot iterate one less the line and printe the numbers 
//					1 through less than current line
//				 Show the output
// 			 Write the output to MyOutput.txt file				  
//Error: In case the file cant be opened I y will get an error message
//Example: seen above
//History:


#include <stdio.h>
#include <stdlib.h>

void printNumbs();
void writeNumbs();

int main(void) 
{

	int numbrArray[1000];  
	FILE *spData;
 	
 	spData = fopen("MyOutput.txt", "w");
 	if ( spData == NULL)
 	{
 	   printf("Could not open file\n");
 		exit(100);
 	}

	printNumbs();
	writeNumbs(spData);


	return 0;
	
}

//Function that prints the numbers 1-9
void printNumbs()
{
	for (int line = 9; line >= 1; line--)
	{
		for (int num = 1; num <= line; num++)
		{
			printf("%d", num);
		}

		printf("\n");
	}

	printf("\n");
   
	
	return;
}

//writes output to the file MyOutput.txt
void writeNumbs(spData)
{
	for (int line = 9; line >= 1; line--)
	{
		for (int num = 1; num <= line; num++)
		{
			fprintf(spData, "%d", num);
		}

		fprintf(spData, "\n");
	}
   fclose(spData);
	
	return;
}
