// program to print array elements
#include <stdio.h>
int main()
{
    int array[30];
    int max = 0;
    int n;
    printf("Enter the elements of the array: ");
    for (int i = 1; i <= 10; i++)
    {
        scanf("%d", &array[i]);
    }

    for (int i = 1; i <= 10; i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
    }
    printf("The elements of the array are: ");
    for (int i = 1; i <= 10; i++)
    {
        printf("%d\n", array[i]);
    }
    printf("The maximum element in the array is: %d\n", max);
    return 0;
}