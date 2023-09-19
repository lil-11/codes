#include <iostream>
using namespace std;
int main() {
    float a,b,c;
// This program is used to check if a triangle is either equilateral or isosceles or scalenes, from the length of the sides entered.
//  Using nested if/else statements
cout << "Enter the three sides of the triangle below" << endl;
cin >> a >> b >> c;

if (a == b && b == c) {
    cout << "This is an equilateral triangle" << endl;
}
else {
    if ((a != b) && (b != c) && (c != a)) {
        cout << "This is a scalenet triangle" << endl;
    }   
    else {
        cout << "This is an isosceles triangle" << endl;
        }
    }
    system("pause>0");
}