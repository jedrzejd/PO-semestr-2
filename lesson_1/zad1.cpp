/* 2) tablicy dynamiczna */

#include<iostream>
#include<cstdio>

using namespace std;


struct stack{
    int size, max_size;
    int *elements;
};


void init(stack &a, int max_size){
    a.size=0;
    a.elements = new int[max_size+1];
    a.max_size = max_size;
}


void destroy(stack &a){
    a.size=0;
    delete []a.elements;
}


void push(stack &a, int item){
    if( a.max_size > a.size ){
        a.elements[++a.size] = item;
        printf("Item added successfully\n");
    }
    else{
        printf("Stack is full\n");
    }
}


void pop(stack &a){
    if(  a.size > 0 ){
        a.size--;
        printf("Item deleted successfully\n");
    }
    else{
        printf("Stack is empty\n");
    }
}


int top(stack &a){
    if(a.size>0){
        return a.elements[a.size];
    }
    else{
        printf("Stack is empty\n");
        return -1;
    }
}


bool empty(stack &a){
    return (a.size==0);
}


bool full(stack &a){
    return (a.size==a.max_size);
}


int main() {
    stack first, second;
    init(first, 3);
    init(second, 2);

    printf("%d\n", empty(first));
    printf("%d\n", full(first));

    pop(first);
    push(first, 10);
    printf("%d\n", top(first));

    printf("%d\n", empty(first));
    printf("%d\n", full(first));
    
    destroy(first);
    
    printf("%d\n", empty(first));
    printf("%d\n", full(first));

    init(second, 2);
    push(second, 1);
    push(second, 2);
    push(second, 3);
    pop(second);
    pop(second);
    pop(second);
    pop(second);
    printf("%d\n", empty(second));
    printf("%d\n", full(second));
}