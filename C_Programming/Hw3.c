#include <stdio.h>
#include <stdlib.h>
#define MAX 50

typedef struct Person
{
	int id; 
	char firstName[MAX]; 
	char lastName[MAX]; 
	char phoneNumber[20];
}Person;

int main()
{
	int a;
	int *p;
	int **q;
	int ***r;
	a = 10;
	p = &a;
	q = &p;
	r = &q;

	char *pFriends[5];
	char **pLast;
	char **pFirst;

	printf("%d \t %d \t %d \t %d \t \n", a, *p, **q, ***r);

	//4 ways to assign a value of 20.
	//I will reset a back to 10 each time
	a = 20;
	printf("%d \n", a);
	a = 10;

	***r = 20;
	printf("%d\n", a);
	a = 10;

	**q = 20;
	printf("%d\n", a);
	a = 10;

	*p = 20;
	printf("%d\n\n", a);

	//Printign the names of my friends following program 11-10

	pFriends[0] = "Alexis Poquiz";
	pFriends[1] = "Nic P.";
	pFriends[2] = "Edgar Tello";
	pFriends[3] = "Jon Lopez";
	pFriends[4] = "Jonathan Betancourt";

	printf("Full names of Friends\n");
	pLast = pFriends + 4;
	//printf("%s\n", pDays[0]);
	
	for (pFirst = pFriends; pFirst <= pLast; pFirst++)
	{
		printf("%s\n", *pFirst);
	} 
	printf("\n\n");

	//Structure of person type with ID, First Name, Last Name, Phone
	Person pp[2];

	for (int i = 0; i < 2; i++)
	{
		printf("Enter the ID of person %d: ", i + 1);
		scanf("%d", &pp[i].id);
		printf("Enter the First Name of person %d: ", i + 1);
		scanf("%s", &pp[i].firstName);
		printf("Enter the Last Name of person %d: ", i + 1);
		scanf("%s", &pp[i].lastName);
		printf("Enrter the Phone Number of person %d: ", i + 1);
		scanf("%s", &pp[i].phoneNumber);
	}
	printf("Person ID \t\t First Name \t\t Last Name \t\t Phone Number\n");
	for (int i = 0; i < 2; i++)
	{
		printf("%-10d \t\t %-10s \t\t %-15s \t %s\n", pp[i].id, pp[i].firstName, pp[i].lastName, pp[i].phoneNumber);
	}


	return 0;
}
