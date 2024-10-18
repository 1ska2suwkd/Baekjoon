#include <stdio.h>
int main() {
	int n, number,cnt=0,cnt2=0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &number);
		for (int j = 2; j < 1000; j++) {
			if (number % j == 0) {
				cnt2++;
			}
		}
		if (cnt2 == 1)
			cnt++;
		cnt2 = 0;
	}
	printf("%d", cnt);
	return 0;
}