#include <stdio.h>
int main() {
    int n;
    int result;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++){
        int a, b;
        scanf("%d %d",&a,&b);
        result = a + b;
        printf("%d\n", result);
     }
    
}