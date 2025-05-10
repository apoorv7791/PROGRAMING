// program to print array elements
// and sort them in ascending order
#include <stdio.h>
int main()
{
    int array[30];
    int n;
    printf("Enter the number of elements in the array:");
    scanf("%d", &n);
    printf("Enter the elements of the array:");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (array[i] > array[j])
            {
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
    printf("The elements of the array in ascending order are:");
    for (int i = 0; i < n; i++)
    {
        printf("%d\n", array[i]);
    }
    return 0;
}