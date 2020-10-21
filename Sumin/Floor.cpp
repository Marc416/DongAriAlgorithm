#include <stdio.h>

int main(void){
    int floor;
    printf("쌓을 층 수를 입력하시오");
    scanf("%d", &floor);

    for(int i = 0; i < floor; i++){
        for(int j = i; j < floor - 1; j++){
            printf(" ");
        }
        for(int k = 0; k < i * 2 +1; k++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}

// 5를 입력하면 
//    *
//   ***
//  *****
// *******
//*********