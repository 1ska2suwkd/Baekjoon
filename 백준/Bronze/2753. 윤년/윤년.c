#include <stdio.h>
int main() {
    int year;
    int result;

    scanf("%d", &year);

    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
        result = 1;
    else
        result = 0;
    printf("%d", result);

}