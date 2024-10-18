#include <stdio.h>
int main() {
	int b1, b2, b3;
	int c, s;
	int sum = 0;
	scanf("%d%d%d%d%d", &b1, &b2, &b3, &c, &s);
	

	if (b1 < b2)
		if (b1 < b3)
			sum += b1;
	if (b2 < b1)
		if (b2 < b3)
			sum += b2;
	if (b3 < b2)
		if (b3 < b1)
			sum += b3;

	if(b1==b2)
		if(b1<b3)
			sum += b1;
	if (b1 == b3)
		if (b1 < b2)
			sum += b1;
	if (b2 == b3)
		if (b2 < b1)
			sum += b2;
	if (b1 == b2 && b1 == b3 && b2 == b3) {
		sum = 0;
		sum += b1;
	}

		

	
	
	
	
	if (c >= s)
		sum += s;
	else
		sum += c;

	

	printf("%d", sum - 50);

}