#include <iostream>
#include "ElementLookup.h"

using namespace std;
int main() {
    ElementLookup lookup("periodicTable.csv");

    int choice;

    cout << "Lookup Element By\n1. Number\n2. Name\nPlease Select input: ";
    cin >> choice;

    if (choice == 1) {
        int atomicNumber;
        cout << "Please enter the Atomic Number: ";
        cin >> atomicNumber;
        lookup.lookupByNumber(atomicNumber);
    } else if (choice == 2) {
        string name;
        cout << "Please enter the Element Name: ";
        cin >> name;
        lookup.lookupByName(name);
    } else {
        cout << "Invalid choice" << endl;
    }

    return 0;
}