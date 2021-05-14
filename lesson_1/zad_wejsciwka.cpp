#include<iostream>
#include<cstdio>

using namespace std;


int main() {
    int *x=new int, *y=x;
    *y = 5;
    *x = 10;
    cout << *y;
    delete x; delete y;
}