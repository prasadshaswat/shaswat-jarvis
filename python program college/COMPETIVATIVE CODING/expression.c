#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

struct Stack
{
    int *arr;
    int top;
};

void initializeStack(struct Stack *st, int n)
{
    st->top = -1;
    st->arr = (int *)malloc(sizeof(int) * n);
}

int isEmpty(struct Stack *st)
{
    return st->top == -1;
}

void push(struct Stack *st, int element)
{
    st->top++;
    st->arr[st->top] = element;
}

int pop(struct Stack *st)
{
    if (!isEmpty(st))
    {
        int value = st->arr[st->top];
        st->top--;
        return value;
    }
    return -1; // Indicating underflow, you can handle this differently based on your requirements
}

// Postfix evaluation
int evaluatePostfix(char *expression)
{
    struct Stack st;
    int len = strlen(expression);
    initializeStack(&st, len);

    for (int i = 0; i < len; i++)
    {
        char ch = expression[i];
        if (ch >= '0' && ch <= '9')
        {
            push(&st, ch - '0');
        }
        else
        {
            int operand2 = pop(&st);
            int operand1 = pop(&st);

            switch (ch)
            {
            case '+':
                push(&st, operand1 + operand2);
                break;
            case '-':
                push(&st, operand1 - operand2);
                break;
            case '*':
                push(&st, operand1 * operand2);
                break;
            case '/':
                if (operand2 == 0)
                {
                    printf("Error: Division by zero\n");
                    return -1; // Indicating error
                }
                push(&st, operand1 / operand2);
                break;
            default:
                printf("Error: Invalid character in expression\n");
                return -1; // Indicating error
            }
        }
    }

    if (!isEmpty(&st))
        return pop(&st);
    else
    {
        printf("Error: Empty expression\n");
        return -1; // Indicating error
    }
}

// Prefix evaluation
int evaluatePrefix(char *expression)
{
    struct Stack st;
    int len = strlen(expression);
    initializeStack(&st, len);

    for (int i = len - 1; i >= 0; i--)
    {
        char ch = expression[i];
        if (ch >= '0' && ch <= '9')
        {
            push(&st, ch - '0');
        }
        else
        {
            int operand1 = pop(&st);
            int operand2 = pop(&st);

            switch (ch)
            {
            case '+':
                push(&st, operand1 + operand2);
                break;
            case '-':
                push(&st, operand1 - operand2);
                break;
            case '*':
                push(&st, operand1 * operand2);
                break;
            case '/':
                if (operand2 == 0)
                {
                    printf("Error: Division by zero\n");
                    return -1; // Indicating error
                }
                push(&st, operand1 / operand2);
                break;
            default:
                printf("Error: Invalid character in expression\n");
                return -1; // Indicating error
            }
        }
    }

    if (!isEmpty(&st))
        return pop(&st);
    else
    {
        printf("Error: Empty expression\n");
        return -1; // Indicating error
    }
}

int main()
{
    char postfixExpression[MAX_SIZE];
    char prefixExpression[MAX_SIZE];

    printf("Enter postfix expression: ");
    scanf("%s", postfixExpression);

    int resultPostfix = evaluatePostfix(postfixExpression);
    if (resultPostfix != -1)
        printf("Result (postfix): %d\n", resultPostfix);

    printf("Enter prefix expression: ");
    scanf("%s", prefixExpression);

    int resultPrefix = evaluatePrefix(prefixExpression);
    if (resultPrefix != -1)
        printf("Result (prefix): %d\n", resultPrefix);

    return 0;
}
