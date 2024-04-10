//Write a program for implementing a MINSTACK which should support operations like 
//push, pop, overflow, underflow, display  
import java.util.Scanner;
class MinStack
{
    int top=-1;
    int stack[]=new int[5];
    int min=9999;
    void push(int ele)
    {
        if(top==4)
        {
            System.out.println("Stack Overflow");
        }
        else
        {
            top++;
            stack[top]=ele;
            if(ele<min)
            {
                min=ele;
            }
        }
    }
    void pop()
    {
        if(top==-1)
        {
            System.out.println("Stack Underflow");
        }
        else
        {
            if(stack[top]==min)
            {
                min=9999;
                for(int i=0;i<top;i++)
                {
                    if(stack[i]<min)
                    {
                        min=stack[i];
                    }
                }
            }
            top--;
        }
    }
    void display()
    {
        if(top==-1)
        {
            System.out.println("Stack is Empty");
        }
        else
        {
            for(int i=top;i>=0;i--)
            {
                System.out.println(stack[i]);
            }
        }
    }
}
public class MinStackDemo
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        MinStack ms=new MinStack();
        int ch;
        do
        {
            System.out.println("1.Push\n2.Pop\n3.Display\n4.Exit");
            System.out.println("Enter your choice");
            ch=sc.nextInt();
            switch(ch)
            {
                case 1:
                    System.out.println("Enter element to push");
                    int ele=sc.nextInt();
                    ms.push(ele);
                    break;
                case 2:
                    ms.pop();
                    break;
                case 3:
                    ms.display();
                    break;
                case 4:
                    System.out.println("Exit");
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        }while(ch!=4);
    }
}
