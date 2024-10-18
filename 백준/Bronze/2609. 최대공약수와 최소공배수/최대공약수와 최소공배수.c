#include <stdio.h>
//최대공약수를 구하는 함수
int gcd(int a, int b) {
	while (b != 0) {
		int temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}

//최소공배수를 구하는 함수
int lcm(int a, int b, int gcd) {
	return (a * b) / gcd;
}

int main() {
	int a, b;
	scanf("%d %d", &a, &b);

	int gcd_value = gcd(a, b);
	int lcm_value = lcm(a, b, gcd_value);

	printf("%d\n", gcd_value);
	printf("%d\n", lcm_value);

	return 0;
}