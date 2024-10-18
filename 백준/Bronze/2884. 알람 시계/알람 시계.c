#include <stdio.h>

int main() {
    int H, M, m;

    scanf("%d%d", &H, &M);

    m = M - 45;

    if (m < 0) {
        H--;
        m += 60;

        if (H < 0) {
            H += 24;
        }

    }

    printf("%d %d", H, m);

    return 0;
}
