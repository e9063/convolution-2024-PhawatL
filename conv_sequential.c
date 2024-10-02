#pragma GCC optimize ("O3")
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    clock_t start_time = clock();

    // ---- input and malloc A, F ----
    int NA, NF;
    scanf("%d %d", &NA, &NF);

    int *A = malloc(sizeof(int) * NA);
    int *F = malloc(sizeof(int) * NF);

    for (int i = 0; i < NA; i++) {
        scanf("%d", &A[i]);
    }
    for (int i = 0; i < NF; i++) {
        scanf("%d", &F[NF - i - 1]);
    }
    // ---- end input and malloc----

    // ---- computation ----
    int result_size = NA - NF + 1;
    int *R = malloc(sizeof(int) * result_size);

    for (int i = 0; i < result_size; i++) {
        int sum = 0;

        for (int j = 0; j < NF; j++) {
            sum += A[i + j] * F[j];
        }
        R[i] = sum;
    }
    // ---- end computation ----

    // ---- output ----
    for (int i = 0; i < result_size; i++) {
        printf("%d\n", R[i]);
    }
    // ---- end output ----

    // ---- free memory ----
    free(F);
    free(A);
    free(R);
    // ---- end free ----

    clock_t end_time = clock();
    double cpu_time_used = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
    printf("CPU time used: %.6f seconds\n", cpu_time_used);
    return 0;
}
