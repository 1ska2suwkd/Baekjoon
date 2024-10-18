#include <stdio.h>
int main() {
	int a[9], m, n = 0;

	for (int i = 0; i < 9; i++) {
		scanf("%d", &a[i]);	
	}

	m = a[0];
	n = 1;

	for (int i = 1; i < 9; i++) {
		if (m <= a[i]) {
			m = a[i];
			n = i + 1;
		}
		
	}
	
	
	printf("%d\n%d", m, n);

	return 0;
} 
