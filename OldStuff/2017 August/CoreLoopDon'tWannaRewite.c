#include <stdio.h>
#include <math.h>
#include <stdlib.h>

//master func
void F(char* X, ...);

void F(char* X, ...){
	// init arg list
	va_list argList;
	// init arg list again
	va_start(argList, *X);
	//next arg:
	//va_arg (argList, ReturnType)
	//function to open text file properly so I don't have to keep checking if file is not real or whatevs
	if (X == "FILEOP"){
	//ARGLIST: "FILEOP", FILEVAR,FILELOCATION, FileFormat, Readmode,
	//	X, FILE*, FILEVAR, STR, STR3, STR4
	}
}

int main (void){
	printf("fuck I forgot everything");
} 
