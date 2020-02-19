//Chapter: 5
//Problem #: Class example 
//Problem Description: Calculates the letter grade based percentage 0 - 100


#include <stdio.h> 

//Function Declaration
char letterGrade(int testScore);
char grammar(char grade);

int main(void) 
{
	
	int testScore;
	char myGrade;
	char a;
	printf("Please enter your test score (0 - 100): \n");
	scanf("%d", &testScore);
	
	myGrade = letterGrade(testScore);
	a = grammar(myGrade);
	printf("The test score of %d is equivalent to a%c %c. \n", testScore, a, myGrade);

	return 0;
	
}

char letterGrade(int testScore)
{
	char grade;
	int score2 = testScore / 10;
	switch (score2)
	{
		case 10:
		case 9 : grade = 'A';
					break;
		case 8 : grade = 'B';
					break;
		case 7 : grade = 'C';
					break;
		case 6 : grade = 'D';
					break;
		default: grade = 'F';
	}
	return grade;
}

char grammar(char grade)
{
	char letter;
	if ( (grade == 'A') || (grade == 'F') )
	{
		letter = 'n';	
	} else 
		letter = letter;
		

	return letter;	
}
