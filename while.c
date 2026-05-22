#include <stdio.h>

int main()
{
    int son;

    printf("Sonni kiriting: ");
    scanf(" %d", &son);

    switch (son)
    {
    case 0 ... 60:
        printf("%d - imtihondan yiqildingiz!", son);
        break;
    case 61 ... 100:
        printf("%d - imtihondan o'tdingiz!", son);
        break;
    default:
        printf("To'g'ri baho kiriting");
    }
}
