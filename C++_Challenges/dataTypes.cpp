#include <iostream>
using namespace std;

/**
* Task: Print each element on a new line in the same order it was received as input. 
* Note that the floating point value should be correct up to 3 decimal places and the double to 9 decimal places.
*/

int main() {
    int d;
    long ld;
    char c;
    float f;
    double lf;
    scanf("%d %ld %c %f %lf", &d, &ld, &c, &f, &lf);
    printf("%d \n", d);
    printf("%ld \n", ld);
    printf("%c \n", c);
    printf("%f \n", f);
    printf("%lf \n", lf);
    return 0;
}
