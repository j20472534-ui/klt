#include <stdio.h>
// 1misol

// int main(){
// int a=-10;

// while(a<=10){
//     printf("%d ", a);
//     a++;
// }
// }

//-----------------------------------
//2-misol

// int main(){
//     int n;
//     int a=1;
//     scanf("%d", &n);

//     while(a<=n){
//         printf("%d ", a);
//         a++;
//     }
// }

//-----------------------------------
//3-misol

// int main(){
//     int n;
//     int a=1;
//     scanf("%d", &n);

//     while(a<=n){
//         printf("%d ", a);
//         a=a+4;
//     }

// }

// ----------------------------------
// 4-misol
// int main() {
//     int x = 1;
//     int a;
//     int c = 0;

//     while(x <= 7) {
//         scanf("%d", &a);
//         c = c + a;
//         x++;
//     }
//     printf("%d", c);
// }

//-----------------------------------
//5-misol

int main(){
    int n;
    int c=0;
    scanf("%d", &n);

    while(n!=0){
        if(n>0){
            c=c+n;
        }
        scanf("%d", &n);
    }
        printf("%d ", c);
}

