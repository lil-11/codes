#include <iostream>
#include <string>

using namespace std;
//Use functions to store names and mark

marks_11() {
    int marks;
    for (int i = 0; i < 11; i++) {
    cout "Enter marks: ";
    cin >> marks[i];
}
}

marks_10() {
    int marks;
    for (int i = 0; i < 10; i++) {
    cout "Enter marks: ";
    cin >> marks[i];
}
}

marks_9() {
    int marks;
    for (int i = 0; i < 9; i++) {
    cout "Enter marks: ";
    cin >> marks[i];
}
}

marks_8() {
    int marks;
    for (int i = 0; i < 8; i++) {
    cout "Enter marks: ";
    cin >> marks[i];
}
}

marks_5() {
    int marks;
    for (int i = 0; i < 5; i++) {
    cout "Enter marks: ";
    cin >> marks[i];
}
}

marks_4() {
    int marks;
    for (int i = 0; i < 4; i++) {
    cout "Enter marks: ";
    cin >> marks[i];
}
}

marks_3() {
    int marks;
    for (int i = 0; i < 3; i++) {
    cout "Enter marks: ";
    cin >> marks[i];
}
}

marks_2() {
    int marks;
    for (int i = 0; i < 2; i++) {
    cout "Enter marks: ";
    cin >> marks[i];
}
}




int main() {
    string name;
    int canNo;
    int userID, userid;

    cout << "Please enter your user id to be saved: ";
    cin >> userID;
    cout << "Saving..." << endl;
    cout << "saved" << endl;
    cout << "----------------------------------------------------" << endl;

    system ("cls");
    
    for (int i = 0; i < 2; i++) {
    cout << "Please enter your user id to continue: ";
    cin >> userid;
    if (userID == userid) {
        continue;
    } 
    else {
        cout << "Invalid user id. Try again later"<< endl;
        exit(1);
    }
    }

    cout << "Welcome to this CGCE database." << endl;

    // taking/storing information about the candidate
    cout << "Enter candidate name: ";
    getline(cin, name);
    cout << "Enter candidate number: ";
    cin >> canNo;
    cin.ignore(); // Ignore the newline character left in the input buffer

    cout << "--------------------------------------------------" << endl;

  
    system("pause>0");        
    }


