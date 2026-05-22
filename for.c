#include <stdio.h>

// int main(){
//     int n;

//     scanf("%d", &n);
//     for(int i=1; i<=n; i++){
//         printf("%d ", i*i*i);
//     }
// }

//-------------------------

// 2misol

// int main(){
//     int n;
//     scanf("%d", &n);
//     for(int i=1; i<=n; n--){
//         printf("%d ", n);
//     }
// }

// --------------------------

// 3misol
// int main(){
//     int n;
//     scanf("%d", &n);

//     for(int i=1; i<=n; i++){
//         if(i%3!=0 && i%4!=0)
//         printf("%d ", i);
//     }
//     }

//----------------------------------

// // 4misol
// int main(){
//     int n;
//     int count=0;
//     scanf("%d", &n);

//     for(int i=1; i<=n; i++){
//         if(i%2!=0)
//         count++;
//     }
//     printf("%d ", count);
//     }

//----------------------------------------

// // 5misol

// int main(){
//     int n;
//     scanf("%d", &n);

//     for(int i=1; i<=n; i++){
//         if(n%i==0){
//             printf("%d ", i);
//         }
//     }
// }

//-----------------------------

// 6misol
// int main() {
//     int a,b;
//     scanf("%d %d", &a, &b);
//     int sum = 0; 
//     for(int i = a; i <= b; i++) {
//         if(i > 0) {  
//             sum += i;
//         }
//     }

//     printf("%d", sum);
// }

//----------------------------------------

// 7misol

// #include <stdio.h>

// int main() {
//     int n,sum=0;
//     scanf("%d", &n);
//     for(int i = 1; i <= n; i++){
//         sum+=i*i;
//     }
//     printf("%d", sum);
// }

//------------------------

// 8misol
// int main() {
//     int a,b;
//     scanf("%d %d", &a, &b);

//     for(int i = a; i <= b; i++) {
//         if(i % 10 == 3 || i % 10 == 7) {
//             printf("%d ", i);
//         }
//     }
// }

//9misol
// int main() {
//     int n,sum = 0, count = 0;
//     scanf("%d", &n);
//     for(int i = 1; i <= n; i++)
//         if(i % 2 == 0){
//              sum += i; 
//              count++; 
//         }
//     int average = sum / count;
//     printf("%d\n", average);
// }

//---------------

// 10misool
// int main(){
//     int n,f=1;
//     scanf("%d", &n);
//     for(int i = 1; i <= n; i++)
//         f *= i;
//     printf("%d ", f);
// }