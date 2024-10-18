#include <stdio.h>
int main() {
	int a, b;
	scanf("%d%d", &a, &b);
	int sum = 0, div, min, mul, r;
	sum = a + b;
	min = a - b;
	mul = a * b;
	div = a / b;
	r = a % b;
	printf("%d\n%d\n%d\n%d\n%d\n", sum, min, mul, div, r);
}