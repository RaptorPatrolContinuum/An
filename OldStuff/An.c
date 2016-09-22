#ifdef _MSC_VER // Windows
#include <windows.h>
#include <direct.h>
#include <process.h>
#else // Linux
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#endif /*_MSC_VER*/



#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define _CRT_SECURE_NO_WARNINGS
#include <stdarg.h>
#include <string.h>
//the master function
void F( char* X, ...);

void F( char* X, ...){
    // init arg list
    va_list argList;
    // init arg list again
    va_start( argList, *X );
    //next arg:
    //va_arg ( argList, ReturnType )
    //function to open text file "properly" so I don't have to keep checking if file is not real or whatevs
    if (X == "FILEOP"){
        //ARGLIST: "FILEOP", FILEVAR, FILELOCATION, FileFormat, Readmode
        //          X , FILE* FILEVAR, STR, STR3, STR4

        FILE* FILEVAR = va_arg ( argList, char* );
        char* STR = va_arg ( argList, char* );
        char* STR2 = ".";
        char* STR3 = va_arg ( argList, char* );
        char* STR4 = va_arg ( argList, char* );
        char* result = malloc(strlen(STR)+strlen(STR2)+strlen(STR3)+1);//+1 for the zero-terminator
        strcpy(result, STR);
        strcat(result, STR2);
        strcat(result, STR3);
        FILEVAR=fopen(result, STR4);
        //if fopen fails, err msg + break
        if (FILEVAR == NULL){
            perror ("Error opening file");
            return EXIT_FAILURE;
        }
    }
    //just close the file normally
    else if (X == "FILECLOSE"){
        //ARGLIST: "FILECLOSE", FILEVAR, FILELOCATION, FileFormat, Readmode
        //          X , FILE* FILEVAR, STR, STR3, STR4

        FILE* FILEVAR = va_arg ( argList, char* );
        char* STR = va_arg ( argList, char* );
        char* STR2 = ".";
        char* STR3 = va_arg ( argList, char* );
        char* STR4 = va_arg ( argList, char* );
        char* result = malloc(strlen(STR)+strlen(STR2)+strlen(STR3)+1);//+1 for the zero-terminator
        strcpy(result, STR);
        strcat(result, STR2);
        strcat(result, STR3);
        FILEVAR=fopen(result, STR4);
        //if fopen fails, err msg + break
        if (FILEVAR == NULL){
            perror ("Error opening file");
            return EXIT_FAILURE;
        }
        fclose (FILEVAR);
    }
    //write to file func
    else if (X == "FILEWRITE"){
        //ARGLIST: "FILEWRITE", FILEVAR, FILELOCATION, FileFormat, Readmode, what to write
        //          X , FILE* FILEVAR, STR, STR3, STR4, STR5

        FILE* FILEVAR = va_arg ( argList, char* );
        char* STR = va_arg ( argList, char* );
        char* STR2 = ".";
        char* STR3 = va_arg ( argList, char* );
        char* STR4 = va_arg ( argList, char* );
        char* STR5 = va_arg ( argList, char* );
        char* result = malloc(strlen(STR)+strlen(STR2)+strlen(STR3)+1);//+1 for the zero-terminator
        strcpy(result, STR);
        strcat(result, STR2);
        strcat(result, STR3);
        FILEVAR=fopen(result, STR4);
        //if fopen fails, err msg + break
        if (FILEVAR == NULL){
            perror ("Error opening file");
            return EXIT_FAILURE;
        }
        //fwrite (buffer , sizeof(char), sizeof(buffer), pFile);
        fprintf(FILEVAR,"%s \n", STR5);
        fclose (FILEVAR);
    }
    //function to cast + make a pointer and check if malloc is bad by seeing if it returns null ptr
    //NOTE: MAKE ALL TYPES OF POINTERS AVAILABLE
    else if (X == "MPTR"){
        //ARGLIST: MPTR, ptr type, ptr
        //          X, P1, P2
        //char *ptr = malloc(sizeof(char) * some_int);
        /*

        idea: make the pointer here and output the address to the ram file, then immediately get it
        idea: write to the beginning of a file so you have to only read the top to get the latest info ??
        idea: append to the end

        char P1 = va_arg ( argList, char* );
        if(){

        }
        else{

        }



        char* ptr = va_arg ( argList, char* );
        if (ptr == NULL) {
            fprintf(stderr, "failed to allocate memory.\n");
            return EXIT_FAILURE;
    }*/
    /*
    making a pointer:
    type* varname = <what it is>

    idea:
        F("PTR", pointer type, where to output )
    NEED: FUNCTION THAT GETS LAST LINE OF A FILE
    */
    }
    //concatenate func that outputs to RAM.txt
    else if (X == "CAT"){
        //ARGLIST: CAT, *string1, *string2
        //          X, STR1, STR2
        //print the result in RAM.txt
        char* STR1 = va_arg ( argList, char* );
        char* STR2 = va_arg ( argList, char* );
        char* result = malloc(strlen(STR1)+strlen(STR2)+1);//+1 for the zero-terminator
        strcpy(result, STR1);
        strcat(result, STR2);
        //need to write to RAM here now
        F("FILEWRITE", "FILEVAR", "RAM", "txt", "a+", result);
    }
    else {
        perror ("Call to F died somehow \n");

    }
    }

int main(void){
    printf("Origin Start \n");
    spawnl( P_WAIT, "Test1.exe","child.exe", "Using spawnl", "Arg1", "Arg2", NULL );
    //F("wordseparate");
    //F("FILEOP", "INPUT", "INP", "txt", "r");
    F("FILEOP", "INPUT", "INP", "txt", "r");
    F("FILECLOSE", "INPUT", "INP", "txt", "r");

    printf("Origin End. (Press any key to exit) \n");
    scanf("");
    }

