#include <stdio.h>
int main() {
    int n1, n2;
    scanf("%d %d", &n1, &n2);

    printf("%d\n", n1 * (n2 % 10));
    printf("%d\n", n1 * (n2/10%10));
    printf("%d\n", n1 * (n2 / 100));
    printf("%d\n", n1 * n2);
}