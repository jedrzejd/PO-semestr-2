/* 2) tablicy dynamiczna */

#include<iostream>
#include<cstdio>

using namespace std;


class Stos{
    public:
        int size, max_size;
        int *elements;

        Stos(){
            printf("Konkstruktor domyslny %d\n", this);
            this->size=0;
            this->elements = new int[3+1];
            this->max_size = 3;
        }

        Stos(int max_size){
            printf("Konstruktor init %d\n", this);
            this->size=0;
            this->elements = new int[max_size+1];
            this->max_size = max_size;
        }

        Stos(const Stos &copy){
            printf("Konstruktor kopiujacy %d\n", this);
            size = copy.size;
            max_size = copy.max_size;
            delete []elements;
            elements = new int[max_size+1];
            for(int i=0; i<size; i++){
                elements[i] = copy.elements[i];
            }
        }


        ~Stos(){
            printf("Destruktor %d\n", this);
        }


        void destroy(){
            this->size=0;
            delete []this->elements;
        }


        void push(int item){
            if( this->max_size > this->size ){
                this->elements[++this->size] = item;
                printf("Item added successfully\n");
            }
            else{
                printf("Stack is full\n");
            }
        }

        void pop(){
            if(  this->size > 0 ){
                this->size--;
                printf("Item deleted successfully\n");
            }
            else{
                printf("Stack is empty\n");
            }
        }

        int top(){
            if(this->size>0){
                return this->elements[this->size];
            }
            else{
                printf("Stack is empty\n");
                return -1;
            }
        }

        bool empty(){
            return (this->size==0);
        }

        bool full(){
            return (this->size==this->max_size);
        }

};


void f(Stos s, int a) {
    printf("f pre\n");
    s.push(a);
    printf("f post\n");
    printf("Rozmiar %d\n", s.size);
}


int main() {

    Stos first;
    // Stos third;

    first.push(1);
    first.push(2);
    f(first, 1110);
    printf("Rozmiar %d\n", first.size);
    while (!first.empty()) {
      cout <<first.top()<<endl;
      first.pop();
   }


    // first.pop();
    // first.push(10);
    // printf("%d\n", first.top());

    // printf("%d\n", first.empty());
    // printf("%d\n", first.full());
    
}