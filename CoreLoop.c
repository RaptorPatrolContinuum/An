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
	//ARGLIST: "FILEOP", FILEVAR, FILENAME, FileFormat, Readmode
        //     X , FILE*     FILEVAR, STR,          STR2,       STR3
	}
	//initialize all the arguments:
	//	FILE* FILEVAR = va_arg ( argList, char* );
	//FILE* FILEVAR = va_arg ( argList, char* );
	char* STR = va_arg ( argList, char* );
	char* STR2 = va_arg ( argList, char* );
	char* STR3 =va_arg ( argList, char* );
	FILE* FILEVAR = fopen(strcat(STR,STR2),"r+");
	
//	FILEVAR = fopen(strcat(STR,STR2);,"r+");
	printf("opened file: %s.%s \n",STR,STR2);
}

int main(void){
	printf("Waiting for commands. \n");
	//F("FILEOP");
	//	F("FILEOP", "INPUT", "INP", "txt", "r");
	
	scanf("");
	FILE* FILEVAR;
	long lSize;
	char *buffer;
	size_t result;
	

	FILEVAR = fopen ("INP2.txt", "r");
	if (FILEVAR == NULL) {fputs ("File error", stderr);exit (1);}

	// get file size
	fseek (FILEVAR, 0, SEEK_END);
	lSize = ftell (FILEVAR);
	rewind (FILEVAR);

	//allocate memory for whole file
	buffer = (char*) malloc (sizeof(char)*lSize);
	if (buffer == NULL) {fputs ("Memory error", stderr); exit (2);}
	
	//copy file into buffer
	result = fread (buffer,1,lSize,FILEVAR);
	if (result != lSize) {fputs ("Reading error", stderr); exit(3);}

	/*the whole file is not loaded in the memory buffer*/

	//write the whole file into console to check:
	printf("checking if file is in buffer \n %s", buffer);
	printf("end \n");
	//FUCK IT FINALLY WORKED:
	//TODO:
	//construct well ordered basis
	//choice:
		//basis can be words or characters:
		//if I do characters, the map from characters > words is arbitrary
		//but if I use alphanumeric as my well ordering then it makes things slightly easier
		//if I use words: then I have to use an infinite basis of words and well ordering is "meta" info
		//PICK: characters since I don't like having metainfo hidden away from the machine

	//construct concept space
	//start doing powerset on that concept space
	//metacode:
	//have it accept console commands
	//make code more generalized
	
	//construct well ordered basis:
	//char basis[10];
	//preinitialize:
	//char basis[] = "abcdefghijklmnopqrstuvwxyz";
	char basis[] = "abcdefghijklmnopqrstuvwxyz0123456789";

	//test characters next
	int size = sizeof(basis)/sizeof(basis[0]);
	int i;
	//clear the array:
	for (i = 0; i < size; i++ ){
		//problem: strings are char arrays and I'm trying to make char arrays of char arrays 
		//WTF
		//so use char*basis for strings: basis[i]="ab"
		//use char basis for single characters: basis[i]= 'a'
		//basis[i] = 'a';
		//check I didn't make a basic mistake
		//printf("basic mistake? basis[%i]:%c \n",i,basis[i]);
		}
	//now construct the NxN array (assume that longest word is 100 char long)
	//PLAN: basis + 100 numbers
	//idea: treat each word as a transversal of the alphanumeric basis
	//problem: I have numbers as both characters AND as integers????
	//AKA: 0123456789,0123456789,10,11,12, etc....
	//idea: first part of basis is characters, next part is the numbers
	//how to differentiate??
	// character basis = first half (and know the cutoff point)
	// number basis = 2nd half
	
	// so then with the 2 bases, you can then read the file then constantly check if a char is in character basis, then if not, append
	//then after that map each morpheme, word, sentence, powerset of the text, into P(basis X basis), until you have the whole work as a single number
	//then after that, have the extra functions, like if X in concept space, or try subgraph isom of a particular function/sequence of functions then try to identify, finding curried functions 

	// FUCK WHAT HAPPENS IF THE BASIS CHANGES, every number description gets fucked in the new basis


	//terminate
	fclose (FILEVAR);
	free (buffer);
	return 0;
	

}
