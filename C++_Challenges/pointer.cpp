#include <iostream>
using namespace std;

/**
* Task: The function is declared with a void return type, so there is no value to return. 
* Modify the values in memory so that a contains their sum and b contains their absoluted difference.
* a' = a + b
* b' = |a - b|
*/

void update(int *a,int *b) {
    int sum, abs;
    
    sum = *a + *b;
    if(*a - *b > 0){
        abs = *a - *b;
    }else{
        abs = -(*a - *b);
    }
    
    *a = sum;
    *b = abs;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}