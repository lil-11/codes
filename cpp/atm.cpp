// This is an ATM machine in cpp
#include <iostream>
#include <string>

using namespace std;

int main () {
int cardNo, pin;
int Cardno, pinn;
int choice;
int amount;
int initialBalance = 500;
string answer;
cout << "Good day. Enter card No to be saved: ";
cin >> cardNo;
cout << "Enter pin to be saved: ";
cin >> pin;
cout << "Saving..." << endl;

system("cls");

while (true) {

cout << "Welcome to this ATM service. Enter card No to continue: ";
cin >> Cardno;
if (Cardno == cardNo) {
    cout << "1. Deposit\n";
    cout << "2. Withdraw\n";
    cout << "3. Balance\n";
    cout << "4. Exit\n";
    cout << "Please enter desired option: ";
    cin >> choice;

    switch (choice) {
        case 1: 
            cout << "Enter amount: ";
            cin >> amount;
            for (int i = 0; i < 3; i++) {
            cout << "Enter your pin: ";
            cin >> pinn;
                if (pin == pinn) {
                    initialBalance += amount;
                    cout << "You have succesfully deposited " << amount << " FCFA to your account. ";
                    cout << "Your new balance is " << initialBalance << "FCFA" <<endl;
                    break;
                }
                else 
                    {
                        cout << "Invalid PIN. Try again." << endl;
                    }
            }
            break;
        
        case 2: 
            cout << "Enter amount: ";
            cin >> amount;
            if (amount <= initialBalance) {
            for (int i = 0; i < 3; i++) {
            cout << "Enter your pin: ";
            cin >> pinn;
                if (pin == pinn) {
                    initialBalance -= amount;
                    cout << "You have succesfully withdrawn " << amount << " FCFA to your account. ";
                    cout << "Your new balance is " << initialBalance << "FCFA" <<endl;
                    break;
                }
                else 
                    {
                        cout << "Invalid PIN. Try again" << endl;
                    }
            }
            }
            else
                {
                    cout << "Insufficient funds"<<endl;
                    exit(1);
                }
            break;
            
        case 3:
            for (int i = 0; i < 3; i++) {
            cout << "Please enter your pin: ";
            cin >> pinn;
                if (pin == pinn) {
                    cout << "Your balance is " << initialBalance << " FCFA" << endl;
                }
                else
                    {
                        cout << "Wrong pin\n";
                        cout << "Try again"<<endl;
                    }
            }
            break;

        case 4:
            cout << "Thanks for using our service"<<endl;
            exit(1);
            break;

        default:
            cout << "Invalid option entered\n"; 
            break;
    }

}
else
    {
        cout << "Invalid card number\n";
    }

        cout << "Do you want to perform another transaction? (y/n): ";
        cin >> answer;
        if ((answer == "y") || (answer == "Y")) {
                cout << "----------------------------------------------------------------"<<endl;
                cout << "                                                                 "<<endl;
            continue;
        }
        else {
            exit(1);
        }
}
system("pause");
}



