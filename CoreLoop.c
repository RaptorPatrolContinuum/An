#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#define getName(var) #var

//int ArrayCheck
//takes an array to a pointer and prints out all the elements
int *ArrayCheck(char *Array, char *X);
//int PowerSet:();
int *PowerSet(int *Array);
void F(char* X, ...);

int *ArrayCheck(char *Array, char *X){
	int Arraysize = sizeof(Array)/sizeof(Array[0]);
	int i;
	//sizes are wrong:
	printf("check sizes %i %i \n", sizeof(Array),sizeof(Array[0]));
	//print the array:
	for (i = 0; i < Arraysize; i++ ){
		printf("ArrayCheck %s[%i]:%c \n",X,i,Array[i]);
		}
	}
	
int *PowerSet(int *Array){
	//need to set pointer to powerset as static:
	//static *PArray
	
	}
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
	char* STR3 = va_arg ( argList, char* );
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
	int charbasissize = sizeof(basis)/sizeof(basis[0]);
	int i;
	//clear the array:
	for (i = 0; i < charbasissize; i++ ){
		//problem: strings are char arrays and I'm trying to make char arrays of char arrays 
		//so use char*basis for strings: basis[i]="ab"
		//use char basis for single characters: basis[i]= 'a'
		//basis[i] = 'a';
		//check I didn't make a basic mistake
		printf("basis[%i]:%c \n",i,basis[i]);
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

	//WOW I fucked up the basis. Since I know what they are supposed to mean I can just keep this and keep going
	char intbasis[50];
	for (i = 0; i < 50; i++){
		intbasis[i]= i +'0';
		printf("intbasis[%i]:%c \n",i,intbasis[i]);
		}
	//get the size of intbasis
	int intbasissize = sizeof(intbasis)/sizeof(intbasis[0]);
	//get unirverse size:
	int Universesize = charbasissize + intbasissize;

	//did I fuck up
	//printf("check size of universe:%i \n", Universesize);
	
	char Universe[Universesize];
	//populate the universe:
	for (i = 0; i < Universesize; i++){
		if(i<charbasissize-1){
			Universe[i]=basis[i];
			}
		else{
		int j = i - charbasissize;
			Universe[i]=intbasis[j];
			}		 
		}
	//check Universe:
	for (i = 0; i < Universesize; i++){
		intbasis[i]=i;
		printf("Universe[%i]:%c \n",i,Universe[i]);
		}
	//check if ArrayCheck works:
	printf("check if ArrayCheck works \n");
	ArrayCheck(Universe,getName(Universe));
	char NxN[Universesize][Universesize]; 
	//PLAN:
	//now that I have NxN I just have to take the powerset of the input text, then map all of them into NxN
	//make the powerset function of an array (AKA powerset the input text AND powerset of Un X Un)
	//map the powerset into Un X Un 
		//HOW:
		//is X in P(Input) in P(Un X Un)?
			//yes: turn on (aka put a 1) that element in P (Un X Un)
			//no: 
				//1. not in there as basis element (in which case: append to basis)
				//2. not in the right powerset (in which case I PP(Un X Un) then turn i ton)
	//make the epsilon function
	//make the union function
	//


	//terminate
	fclose (FILEVAR);
	free (buffer);
	return 0;
	

}
