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

main (){
	printf("Hello World! \n");
	int status = system("./nA.exe");
}
