#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>

void F(char* X, ...);

void F(char* X, ...){
	// init arg list
    va_list argList;
    // init arg list again
    va_start( argList, *X );
    //next arg:
    //va_arg ( argList, ReturnType )
    //function to open text file "properly" so I don't have to keep checking if file is not real or whatevs
	if (X == "FILEOP"){
	printf("tried to open file \n");
	//ARGLIST: "FILEOP", FILEVAR, FILELOCATION, FileFormat, Readmode
        //          X , FILE* FILEVAR, STR, STR3, STR4
	}
	FILE* FILEVAR = va_arg ( argList, char* );       
}

int main(void){
	printf("start! \n");
	//F("FILEOP");
	F("FILEOP", "INPUT", "INP", "txt", "r");
	printf("end \n");
	scanf("");
}
