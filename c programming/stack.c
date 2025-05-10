// stack implementation using array
#include <stdio.h>
#define MAX 5 // [MAX] is the maximum size of the stack

int stack[MAX];
int top = -1;

void push(int data)
{
    if (top == MAX - 1)
    {
        printf("Stack overflow\n");
    }
    else
    {
        top++;
        stack[top] = data;
    }
}

int pop()
{
    if (top == -1)
    {
        printf("Stack underflow\n");
        return -1;
    }
    else
    {
        int data = stack[top];
        top--;
        return data;
    }
}

void peek()
{
    if (top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Top element: %d\n", stack[top]);
    }
}

void display()
{
    if (top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        for (int i = top; i >= 0; i--)
        {
            printf("%d\n", stack[i]);
        }
    }
}

int main()
{
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);
    pop();
    display();
}