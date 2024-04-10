#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// Define the process structure
typedef struct {
    int process_id;
    int arrival_time;
    int burst_time;
    int completion_time;
    int turnaround_time;
    int waiting_time;
} Process;

// Function to sort processes based on arrival time
void sort_by_arrival_time(Process *processes, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (processes[j].arrival_time > processes[j + 1].arrival_time) {
                // Swap the processes
                Process temp = processes[j];
                processes[j] = processes[j + 1];
                processes[j + 1] = temp;
            }
        }
    }
}

// Function to implement FCFS scheduling algorithm
void fcfs_scheduling(Process *processes, int n) {
    // Sort processes by arrival time
    sort_by_arrival_time(processes, n);

    int current_time = 0;
    for (int i = 0; i < n; i++) {
        // If the process hasn't arrived yet, update the current time
        if (current_time < processes[i].arrival_time) {
            current_time = processes[i].arrival_time;
        }
        // Set completion time
        processes[i].completion_time = current_time + processes[i].burst_time;
        // Set turnaround time
        processes[i].turnaround_time = processes[i].completion_time - processes[i].arrival_time;
        // Set waiting time
        processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time;
        // Update current time
        current_time = processes[i].completion_time;
    }
}

// Function to calculate average turnaround time and average waiting time
void calculate_average_times(Process *processes, int n, float *avg_turnaround_time, float *avg_waiting_time) {
    float total_turnaround_time = 0, total_waiting_time = 0;
    for (int i = 0; i < n; i++) {
        total_turnaround_time += processes[i].turnaround_time;
        total_waiting_time += processes[i].waiting_time;
    }
    *avg_turnaround_time = total_turnaround_time / n;
    *avg_waiting_time = total_waiting_time / n;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    // Allocate memory for processes
    Process *processes = (Process *)malloc(n * sizeof(Process));

    // Input process details
    for (int i = 0; i < n; i++) {
        printf("Enter arrival time and burst time for process %d: ", i + 1);
        scanf("%d %d", &processes[i].arrival_time, &processes[i].burst_time);
        processes[i].process_id = i + 1;
    }

    // Perform FCFS scheduling
    fcfs_scheduling(processes, n);

    // Calculate average turnaround time and average waiting time
    float avg_turnaround_time, avg_waiting_time;
    calculate_average_times(processes, n, &avg_turnaround_time, &avg_waiting_time);

    // Output process details and scheduling results
    printf("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t%d\t\t%d\t\t%d\t\t%d\t\t\t%d\n", processes[i].process_id, processes[i].arrival_time,
               processes[i].burst_time, processes[i].completion_time, processes[i].turnaround_time,
               processes[i].waiting_time);
    }
    printf("\nAverage Turnaround Time: %.2f\n", avg_turnaround_time);
    printf("Average Waiting Time: %.2f\n", avg_waiting_time);

    // Free allocated memory
    free(processes);

    return 0;
}
