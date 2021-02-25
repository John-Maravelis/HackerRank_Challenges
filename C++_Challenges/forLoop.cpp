#include <iostream>
using namespace std;

/**
* Task: For each integer n in the inclusive interval [a, b]:
*       If 1 <= n <= 9, then print the English representation of it in lowercase. That is "one" for 1, "two" for 2, and so on.
*       Else if n > 9 and it is an even number, then print "even".
*       Else if n > 9 and it is an odd number, then print "odd".
*/

int main() {
    int l,m;
    cin >> l;
    cin >> m;
    for(int n = l; n <= m; n++){
        if(n == 1){
            cout << "one \n";
        }else if(n == 2){
            cout << "two \n";
        }else if(n == 3){
            cout << "three \n";
        }else if(n == 4){
            cout << "four \n";
        }else if(n == 5){
            cout << "five \n";
        }else if(n == 6){
            cout << "six \n";
        }else if(n == 7){
            cout << "seven \n";
        }else if(n == 8){
            cout << "eight \n";
        }else if(n == 9){
            cout << "nine \n";
        }else{
            if(n % 2 == 0){
                cout << "even \n";
            }else{
                cout << "odd \n";
            }
        }
    }
    return 0;
}
