// program to implement bubble sort
#include <stdio.h>
int main()
{
    int array[10];
    int n;
    printf("Enter the number of elements in the array:");
    scanf("%d", &n);
    printf("Enter the elements of the array:");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }
    // bubble sort
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (array[j] > array[j + 1])
            {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    printf("The sorted array is: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d\n", array[i]);
    }
    return 0;
}