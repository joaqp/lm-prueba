#include <iostream>

int main (void) {
union {
    int i;
    char c[sizeof(int)];
} x;
x.i = 1;
if(x.c[0] == 1)
    printf("little-endian\n");
else    printf("big-endian\n");
}