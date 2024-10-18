#include <stdio.h>

int main() {
    int cnt = 0;
    char a[1000001];

    // 공백을 포함한 문자열 입력 받기
    scanf("%[^\n]", a);

    // 문자열 순회하면서 단어 수 세기
    for (int i = 0; a[i] != '\0'; i++) {
        // 공백이 아니고, 처음이거나 이전 문자가 공백인 경우 단어 시작
        if (a[i] != ' ' && (i == 0 || a[i - 1] == ' ')) {
            cnt++;
        }
    }

    printf("%d\n", cnt);

    return 0;
}