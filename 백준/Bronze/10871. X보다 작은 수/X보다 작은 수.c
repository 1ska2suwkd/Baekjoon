#include <stdio.h>
int main() {
	int n, x;
	int com;
	scanf("%d%d", &n, &x);
	
	for (int i = 0; i < n; i++) {
		scanf("%d", &com);
		if (com < x)
			printf("%d ", com);
	}
		

	return 0;
}