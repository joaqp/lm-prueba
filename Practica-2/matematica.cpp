#include <iostream>
#include "./matematica.h" 

using namespace std;


int main (void)
{

int16_t array[5]={1, 1, 1 , 1, 1};
int n= 5;
cout << Sumar_Array (array, n) << endl;
}

int32_t Sumar_Array (int16_t* x, int16_t xn)
{
int32_t sum=0;
for(int i=0; i< xn; i++)
sum+=x[i];
return sum;
}