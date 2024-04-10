#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    pid_t child_pid;

    child_pid = fork();

    if (child_pid < 0) {
        fprintf(stderr, "Fork failed\n");
        return 1;
    } else if (child_pid == 0) {
        // Child process
        printf("Child Process: My process id is %d\n", getpid());
    } else {
        // Parent process
        printf("Parent Process: My process id is %d\n", getpid());
        printf("Child Process id is %d\n", child_pid);
    }

    return 0;
}