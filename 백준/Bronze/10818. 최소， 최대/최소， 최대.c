#include <stdio.h>

int main() {
    int N;
    int max = -1000001, min = 1000001;
    int num;

    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d", &num);
        if (num > max) {
            max = num;
        }
        if (num < min) {
            min = num;
        }
    }

    printf("%d %d\n", min, max);
    return 0;
}
