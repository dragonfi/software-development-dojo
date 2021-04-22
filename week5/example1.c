#include "stdio.h"

unsigned int a = 100;
int b = -100;

unsigned int c = 100;
long d = -1000;

// uint16_t f = 10;
// int32_t g = 10;

size_t h = 10;

inline int add(int a, int b) {
    return a + b;
}

int main() {
    if (a > b) {
        printf("100 is bigger than -100\n");
    } else {
        printf("100 is smaller than -100\n");
    }

    long _a = a;
    long _b = b;

    if (_a > _b) {
        printf("100 is bigger than -100\n");
    } else {
        printf("100 is smaller than -100\n");
    }

    //static_cast<long>(a);
    //dynamic_cast<long>(a);
    //reinterpret_cast<long>(a);
    if ((long)a > (long)b) {
        printf("100 is bigger than -100\n");
    } else {
        printf("100 is smaller than -100\n");
    }

    printf("%d", add(a, b));
    return 0;
}
