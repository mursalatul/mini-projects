#ifndef ELEMENT_LOOKUP_H
#define ELEMENT_LOOKUP_H

#include "AVLTree.h"
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <functional>
using namespace std;

class ElementInfo {
public:
    string name;
    string symbol;
    int atomicNumber;
    double atomicWeight;

    ElementInfo(string n, string s, int num, double weight) : name(n), symbol(s), atomicNumber(num), atomicWeight(weight) {}

    // Define operator< to compare ElementInfo objects by atomicNumber
    bool operator<(const ElementInfo& other) const {
        return atomicNumber < other.atomicNumber;
    }
};

// Element Lookup Class
class ElementLookup {
private:
    AVLTree<ElementInfo> elements;

public:
    ElementLookup(string filename);
    void lookupByNumber(int atomicNumber);
    void lookupByName(string name);
};

ElementLookup::ElementLookup(string filename) {
    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file " << filename << endl;
        return;
    }

    string line;
    getline(file, line); // skip header line
    while (getline(file, line)) {
        stringstream ss(line);
        string name, symbol;
        int atomicNumber;
        double atomicWeight;

        getline(ss, name, ',');
        getline(ss, symbol, ',');
        ss >> atomicNumber;
        ss.ignore(); // ignore comma
        ss >> atomicWeight;

        ElementInfo element(name, symbol, atomicNumber, atomicWeight);
        elements.insert(element);
    }
    file.close();
}

void ElementLookup::lookupByNumber(int atomicNumber) {
    try {
        ElementInfo element = elements.search(atomicNumber);
        cout << "Atomic Number: " << element.atomicNumber << ", Name: " << element.name << ", Symbol: " << element.symbol
             << ", Atomic Weight: " << element.atomicWeight << endl;
    } catch (...) {
        cerr << "Element not found" << endl;
    }
}

void ElementLookup::lookupByName(string name) {
    // Perform an in-order traversal of the AVL tree
    function<void(AVLNode<ElementInfo>*)> inOrderTraversal = [&](AVLNode<ElementInfo>* node) {
        if (node == nullptr)
            return;
        inOrderTraversal(node->left);
        if (node->data.name == name) {
            cout << "Atomic Number: " << node->data.atomicNumber << ", Name: " << node->data.name << ", Symbol: " << node->data.symbol
                 << ", Atomic Weight: " << node->data.atomicWeight << endl;
            return;
        }
        inOrderTraversal(node->right);
    };

    // Start the traversal from the root of the AVL tree
    inOrderTraversal(elements.getRoot());
}

#endif // ELEMENT_LOOKUP_H
