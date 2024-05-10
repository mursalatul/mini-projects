// AVL Tree Class
#ifndef AVLTREE
#define AVLTREE

#include <cmath>
using namespace std;

template <class T>
class AVLNode {
public:
    T data;
    AVLNode<T>* left;
    AVLNode<T>* right;
    int height;

    AVLNode(T value) : data(value), left(nullptr), right(nullptr), height(1) {}
};


template <class T>
class AVLTree {
private:
    AVLNode<T>* root;

    // Helper functions
    int height(AVLNode<T>* node);
    int balanceFactor(AVLNode<T>* node); // Corrected name
    void updateHeight(AVLNode<T>* node);
    AVLNode<T>* rotateRight(AVLNode<T>* node);
    AVLNode<T>* rotateLeft(AVLNode<T>* node);
    AVLNode<T>* balance(AVLNode<T>* node);
    AVLNode<T>* insert(AVLNode<T>* node, T value);
    AVLNode<T>* minValueNode(AVLNode<T>* node);
    AVLNode<T>* deleteNode(AVLNode<T>* root, T value);

public:
    AVLTree() : root(nullptr) {}
    void insert(T value);
    void remove(T value);
    T search(int key);
    AVLNode<T>* getRoot() const { return root; }
};

template <class T>
int AVLTree<T>::height(AVLNode<T>* node) {
    if (node == nullptr)
        return 0;
    return node->height;
}

template <class T>
int AVLTree<T>::balanceFactor(AVLNode<T>* node) { // Corrected name
    if (node == nullptr)
        return 0;
    return height(node->left) - height(node->right);
}

template <class T>
void AVLTree<T>::updateHeight(AVLNode<T>* node) {
    if (node != nullptr)
        node->height = 1 + max(height(node->left), height(node->right));
}

template <class T>
AVLNode<T>* AVLTree<T>::rotateRight(AVLNode<T>* node) {
    AVLNode<T>* newRoot = node->left;
    node->left = newRoot->right;
    newRoot->right = node;
    updateHeight(node);
    updateHeight(newRoot);
    return newRoot;
}

template <class T>
AVLNode<T>* AVLTree<T>::rotateLeft(AVLNode<T>* node) {
    AVLNode<T>* newRoot = node->right;
    node->right = newRoot->left;
    newRoot->left = node;
    updateHeight(node);
    updateHeight(newRoot);
    return newRoot;
}

template <class T>
AVLNode<T>* AVLTree<T>::balance(AVLNode<T>* node) {
    updateHeight(node);
    int bfValue = balanceFactor(node); // Corrected to use balanceFactor instead of bf
    if (bfValue > 1) {
        if (balanceFactor(node->left) < 0) {
            node->left = rotateLeft(node->left);
        }
        return rotateRight(node);
    }
    if (bfValue < -1) {
        if (balanceFactor(node->right) > 0) {
            node->right = rotateRight(node->right);
        }
        return rotateLeft(node);
    }
    return node;
}


template <class T>
AVLNode<T>* AVLTree<T>::insert(AVLNode<T>* node, T value) {
    if (node == nullptr)
        return new AVLNode<T>(value);
    if (value < node->data)
        node->left = insert(node->left, value);
    else
        node->right = insert(node->right, value);
    return balance(node);
}

template <class T>
AVLNode<T>* AVLTree<T>::minValueNode(AVLNode<T>* node) {
    AVLNode<T>* current = node;
    while (current->left != nullptr)
        current = current->left;
    return current;
}

template <class T>
AVLNode<T>* AVLTree<T>::deleteNode(AVLNode<T>* root, T value) {
    if (root == nullptr)
        return root;
    if (value < root->data)
        root->left = deleteNode(root->left, value);
    else if (value > root->data)
        root->right = deleteNode(root->right, value);
    else {
        if (root->left == nullptr || root->right == nullptr) {
            AVLNode<T>* temp = root->left ? root->left : root->right;
            if (temp == nullptr) {
                temp = root;
                root = nullptr;
            } else
                *root = *temp;
            delete temp;
        } else {
            AVLNode<T>* temp = minValueNode(root->right);
            root->data = temp->data;
            root->right = deleteNode(root->right, temp->data);
        }
    }
    if (root == nullptr)
        return root;
    return balance(root);
}

template <class T>
void AVLTree<T>::insert(T value) {
    root = insert(root, value);
}

template <class T>
void AVLTree<T>::remove(T value) {
    root = deleteNode(root, value);
}

template <class T>
T AVLTree<T>::search(int key) {
    AVLNode<T>* current = root;
    while (current != nullptr) {
        if (current->data.atomicNumber == key)
            return current->data;
        else if (key < current->data.atomicNumber)
            current = current->left;
        else
            current = current->right;
    }
    throw "Element not found";
}

#endif