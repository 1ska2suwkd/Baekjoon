#include <stdio.h>
#include <string.h>

int main() {
	int n[4];
	int res1,res2;
	char str[100];

	scanf("%d", &n[0]);
	scanf("%d", &n[1]);
	scanf("%d", &n[2]);

	sprintf(str, "%d%d", n[0], n[1]);
	sscanf(str, "%d", &n[3]);

	res1 = n[0] + n[1] - n[2];
	res2 = n[3] - n[2];

	printf("%d\n", res1);
	printf("%d\n", res2);

	return 0;
}