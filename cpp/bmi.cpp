// Body Mass Index Calculator, tells you your BMI based on the height and mass entered
#include <iostream>
using namespace std;

int main () {
    float height, weight, BMI;
    cout << "Please enter your height in meters: ";
    cin >> height;
    cout << "Please enter your weight in kilograms: ";
    cin >> weight;

    BMI = (weight / (height*height));

    if (BMI < 18.5) {
        cout << "Underweight" << endl;
    }
    else {
        if  (BMI > 25) {
            cout << "Overweight" << endl;
        } 
        else {
            cout << "Normal weight" << endl;
        }
    }
    cout << "Your BMI is " << BMI << endl;
    system("pause>0");
}