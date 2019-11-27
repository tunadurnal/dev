#include <stdio.h>
#include <stdlib.h>

void inform(int a, int b, double res)
{
    for (int i = 0; i < a + b; ++i)
    {
        printf("%.2f\n", res);
    }
}

int main()
{
    double a, b, res;
    int choice;
    char repeat;
    printf("Enter the first number: ");
    scanf("%lf", &a);
    printf("Enter the second number: ");
    scanf("%lf", &b);
    printf("Addition - 1\nSubtraction - 2\nMultiplication - 3\nDivision - 4\nRemainder of division - 5\n");
    scanf("%d", &choice);
    switch (choice)
    {
        case 1:
            res = a + b; break;
        case 2:
            res = a - b; break;
        case 3:
            res = a * b; break;
        case 4:
            res = a / b; break;
        case 5:
            res = (int) a % (int) b; break;
        default:
            printf("You've done something wrong !");
    }
    inform(a, b, res);
    printf("Would you like to calculate again (Y/y): ");
    getchar();
    repeat = getchar();
    if (repeat == 'Y' || repeat == 'y')
    {
        system("clear");
        main();
    }
    else printf("Good bye, then !");
    return 0;
}








