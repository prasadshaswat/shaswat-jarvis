#include <stdio.h>
#include <stdbool.h>

#define MAX_PROCESS 5
#define MAX_RESOURCE 3

int available[MAX_RESOURCE];
int maximum[MAX_PROCESS][MAX_RESOURCE];
int allocation[MAX_PROCESS][MAX_RESOURCE];
int need[MAX_PROCESS][MAX_RESOURCE];
bool finish[MAX_PROCESS];

void initialize() {
    // Initialize available resources
    for (int i = 0; i < MAX_RESOURCE; i++) {
        printf("Enter the available instances of resource %d: ", i + 1);
        scanf("%d", &available[i]);
    }

    // Initialize maximum resources for each process
    for (int i = 0; i < MAX_PROCESS; i++) {
        printf("Enter the maximum resources required for process %d: ", i + 1);
        for (int j = 0; j < MAX_RESOURCE; j++) {
            scanf("%d", &maximum[i][j]);
        }
        finish[i] = false;
    }

    // Initialize allocation and need matrices
    for (int i = 0; i < MAX_PROCESS; i++) {
        printf("Enter the resources allocated to process %d: ", i + 1);
        for (int j = 0; j < MAX_RESOURCE; j++) {
            scanf("%d", &allocation[i][j]);
            need[i][j] = maximum[i][j] - allocation[i][j];
        }
    }
}

bool isSafeState() {
    int work[MAX_RESOURCE];
    for (int i = 0; i < MAX_RESOURCE; i++) {
        work[i] = available[i];
    }

    bool finishAll;
    int i, j;
    for (i = 0; i < MAX_PROCESS; i++) {
        if (!finish[i]) {
            finishAll = true;
            for (j = 0; j < MAX_RESOURCE; j++) {
                if (need[i][j] > work[j]) {
                    finishAll = false;
                    break;
                }
            }
            if (finishAll) {
                for (j = 0; j < MAX_RESOURCE; j++) {
                    work[j] += allocation[i][j];
                }
                finish[i] = true;
                i = -1;
            }
        }
    }

    for (i = 0; i < MAX_PROCESS; i++) {
        if (!finish[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    initialize();

    if (isSafeState()) {
        printf("System is in a safe state\n");
    } else {
        printf("System is not in a safe state\n");
    }

    return 0;
}
