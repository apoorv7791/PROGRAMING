// program to print the sum of elements in an array
// 1,2,3,4,5,6,7,8,9,10
// sum is 55
#include <stdio.h>
int main()
{
    int array[20];
    int sum = 0;
    int n;
    printf("Enter the elements of the array: ");
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &array[i]);
        sum += array[i];
    }
    printf("the sum of the elements of the array is: %d\n", sum);
}