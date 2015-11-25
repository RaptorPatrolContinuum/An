#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define _CRT_SECURE_NO_WARNINGS
#include <process.h>

/*
types:
int
double
float
void
string
==
char 	1 byte 	-128 to 127 or 0 to 255
unsigned char 	1 byte 	0 to 255
signed char 	1 byte 	-128 to 127
int 	2 or 4 bytes 	-32,768 to 32,767 or -2,147,483,648 to 2,147,483,647
unsigned int 	2 or 4 bytes 	0 to 65,535 or 0 to 4,294,967,295
short 	2 bytes 	-32,768 to 32,767
unsigned short 	2 bytes	0 to 65,535
long 	4 bytes 	-2,147,483,648 to 2,147,483,647
unsigned long 	4 bytes 	0 to 4,294,967,295

float 	4 byte 	1.2E-38 to 3.4E+38 	6 decimal places
double 	8 byte 	2.3E-308 to 1.7E+308 	15 decimal places
long double 	10 byte 	3.4E-4932 to 1.1E+4932 	19 decimal places



int main(void){
    FILE *DataSet;
    DataSet=fopen("TextTest.txt", "r");
    printf("What does it look like? \n",DataSet);
    }
*/


int main(void){
    char str[] = "Hello";
    printf("What does it look like? \n", str);
    scanf("");
    }


