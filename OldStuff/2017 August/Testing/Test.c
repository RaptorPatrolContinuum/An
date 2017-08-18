#include <stdio.h>
#include <process.h>

int main(void)
{

  puts("Spawning child with spawnl");

  spawnl( P_WAIT, "child.exe",
    "child.exe", "Using spawnl", "Arg1", "Arg2", NULL );

  return 0;
}

/*
 * Program output:
 Spawning child with spawnl
 I am the child
 Arg 1 Using
 Arg 2 spawnl
 Arg 3 Arg1
 Arg 4 Arg2
 *
 */
