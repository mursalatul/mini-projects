#include <iostream>
#include <sstream>
#include <stdexcept>
#include <algorithm>
#include <cctype>
#include <string>
#include <cmath>

using namespace std;

/**
 * @brief A class representing a doubly linked list.
 *
 * @tparam T The type of data stored in the list.
 */
template <typename T>
class DoublyLinkedList
{
public:
    /**
     * @brief A struct representing a node in the doubly linked list.
     */
    struct Node
    {
        T data;     ///< The data stored in the node.
        Node *prev; ///< Pointer to the previous node.
        Node *next; ///< Pointer to the next node.

        /**
         * @brief Constructs a new Node object.
         *
         * @param d The data to be stored in the node.
         */
        Node(const T &d) : data(d), prev(nullptr), next(nullptr) {}
    };

    Node *head; ///< Pointer to the first node in the list.
    Node *tail; ///< Pointer to the last node in the list.
    int size;   ///< The size of the list.

    /**
     * @brief Constructs a new DoublyLinkedList object.
     */
    DoublyLinkedList() : head(nullptr), tail(nullptr), size(0) {}

    /**
     * @brief Destroys the DoublyLinkedList object and deallocates memory.
     */
    ~DoublyLinkedList()
    {
        clear();
    }

    /**
     * @brief Adds a new node with the given value to the front of the list.
     *
     * @param value The value to be added.
     */
    void addFront(const T &value)
    {
        Node *newNode = new Node(value);
        if (head == nullptr)
        {
            head = tail = newNode;
        }
        else
        {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
        size++;
    }

    /**
     * @brief Adds a new node with the given value to the rear of the list.
     *
     * @param value The value to be added.
     */
    void addRear(const T &value)
    {
        Node *newNode = new Node(value);
        if (tail == nullptr)
        {
            head = tail = newNode;
        }
        else
        {
            newNode->prev = tail;
            tail->next = newNode;
            tail = newNode;
        }
        size++;
    }

    /**
     * @brief Inserts a new node with the given value after the specified node.
     *
     * @param prevNode The node after which the new node will be inserted.
     * @param value The value to be inserted.
     */
    void insertAfter(Node *prevNode, const T &value)
    {
        if (prevNode == nullptr)
        {
            return;
        }
        Node *newNode = new Node(value);
        newNode->prev = prevNode;
        newNode->next = prevNode->next;
        if (prevNode->next != nullptr)
        {
            prevNode->next->prev = newNode;
        }
        else
        {
            tail = newNode;
        }
        prevNode->next = newNode;
        size++;
    }

    /**
     * @brief Inserts a new node with the given value before the specified node.
     *
     * @param nextNode The node before which the new node will be inserted.
     * @param value The value to be inserted.
     */
    void insertBefore(Node *nextNode, const T &value)
    {
        if (nextNode == nullptr)
        {
            return;
        }
        Node *newNode = new Node(value);
        newNode->next = nextNode;
        newNode->prev = nextNode->prev;
        if (nextNode->prev != nullptr)
        {
            nextNode->prev->next = newNode;
        }
        else
        {
            head = newNode;
        }
        nextNode->prev = newNode;
        size++;
    }

    /**
     * @brief Removes the specified node from the list.
     *
     * @param node The node to be removed.
     */
    void remove(Node *node)
    {
        if (node == nullptr)
        {
            return;
        }
        if (node->prev != nullptr)
        {
            node->prev->next = node->next;
        }
        else
        {
            head = node->next;
        }
        if (node->next != nullptr)
        {
            node->next->prev = node->prev;
        }
        else
        {
            tail = node->prev;
        }
        delete node;
        size--;
    }

    /**
     * @brief Finds the first occurrence of the given value in the list.
     *
     * @param value The value to be found.
     * @return Node* A pointer to the node containing the value, or nullptr if not found.
     */
    Node *find(const T &value) const
    {
        Node *current = head;
        while (current != nullptr)
        {
            if (current->data == value)
            {
                return current;
            }
            current = current->next;
        }
        return nullptr;
    }

    /**
     * @brief Clears the list and deallocates memory.
     */
    void clear()
    {
        Node *current = head;
        while (current != nullptr)
        {
            Node *next = current->next;
            delete current;
            current = next;
        }
        head = tail = nullptr;
        size = 0;
    }

    /**
     * @brief Traverses the list forward and prints the data of each node.
     */
    void traverseForward() const
    {
        Node *current = head;
        while (current != nullptr)
        {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }

    /**
     * @brief Traverses the list backward and prints the data of each node.
     */
    void traverseBackward() const
    {
        Node *current = tail;
        while (current != nullptr)
        {
            std::cout << current->data << " ";
            current = current->prev;
        }
        std::cout << std::endl;
    }

    /**
     * @brief Gets the size of the list.
     *
     * @return int The size of the list.
     */
    int getSize() const
    {
        return size;
    }

    /**
     * @brief Returns the value of the top element of the list without removing it.
     *
     * @return T The value of the top element.
     * @throw std::runtime_error if the list is empty.
     */
    T peek() const
    {
        if (head == nullptr)
        {
            throw std::runtime_error("List is empty");
        }
        return head->data;
    }
};

/**
 * @brief A class representing a stack implemented using a doubly linked list.
 *
 * @tparam T The type of data stored in the stack.
 */
template <typename T>
class Stack
{
private:
    DoublyLinkedList<T> list; ///< Doubly linked list to store stack elements.

public:
    /**
     * @brief Constructs a new Stack object.
     */
    Stack() {}

    /**
     * @brief Pushes a new element onto the top of the stack.
     *
     * @param value The value to be pushed onto the stack.
     */
    void push(const T &value)
    {
        list.addFront(value);
    }

    /**
     * @brief Removes and returns the top element from the stack.
     *
     * @return T The value of the top element.
     * @throw std::runtime_error if the stack is empty.
     */
    // T pop()
    // {
    //     if (list.getSize() == 0)
    //     {
    //         throw std::runtime_error("Stack is empty");
    //     }
    //     T data = list.head->data;
    //     list.remove(list.head);
    //     return data;
    // }
    T pop()
    {
        if (list.getSize() == 0)
        {
            throw std::runtime_error("Stack is empty");
        }
        T data = list.peek();   // Get the value of the top element
        list.remove(list.head); // Remove the top element
        return data;
    }

    /**
     * @brief Returns the value of the top element of the stack without removing it.
     *
     * @return T The value of the top element.
     * @throw std::runtime_error if the stack is empty.
     */
    T peek() const
    {
        if (list.getSize() == 0)
        {
            throw std::runtime_error("Stack is empty");
        }
        return list.head->data;
    }

    /**
     * @brief Checks if the stack is empty.
     *
     * @return true if the stack is empty, false otherwise.
     */
    bool isEmpty() const
    {
        return list.getSize() == 0;
    }
};

/**
 * @brief A class representing a queue implemented using a doubly linked list.
 *
 * @tparam T The type of data stored in the queue.
 */
template <typename T>
class Queue
{
private:
    DoublyLinkedList<T> list; ///< Doubly linked list to store queue elements.

public:
    /**
     * @brief Constructs a new Queue object.
     */
    Queue() {}

    /**
     * @brief Adds a new element to the rear of the queue.
     *
     * @param value The value to be added to the queue.
     */
    void enqueue(const T &value)
    {
        list.addRear(value);
    }

    /**
     * @brief Removes and returns the front element of the queue.
     *
     * @return T The value of the front element.
     * @throw std::runtime_error if the queue is empty.
     */
    T dequeue()
    {
        if (list.getSize() == 0)
        {
            throw std::runtime_error("Queue is empty");
        }
        T data = list.head->data;
        list.remove(list.head);
        return data;
    }

    /**
     * @brief Returns the value of the front element of the queue without removing it.
     *
     * @return T The value of the front element.
     * @throw std::runtime_error if the queue is empty.
     */
    T peek() const
    {
        if (list.getSize() == 0)
        {
            throw std::runtime_error("Queue is empty");
        }
        return list.head->data;
    }
};

/**
 * @brief A class representing a Reverse Polish Notation (RPN) calculator.
 */
class RPNCalculator
{
private:
    Stack<double> stack; ///< Stack to store operands during evaluation

public:
    /**
     * @brief Evaluates the given RPN expression and returns the result.
     *
     * @param expression The RPN expression to evaluate.
     * @return double The result of the evaluation.
     * @throw std::runtime_error if there is a division by zero or if the expression is empty.
     * @throw std::invalid_argument if the expression contains an invalid operator.
     */
    double evaluate(const std::string &expression)
    {
        std::istringstream iss(expression);
        std::string token;
        while (iss >> token)
        {
            if (isNumeric(token))
            {
                stack.push(std::stod(token));
            }
            else
            {
                double operand2 = stack.pop();
                double operand1 = stack.pop();
                if (token == "+")
                {
                    stack.push(operand1 + operand2);
                }
                else if (token == "-")
                {
                    stack.push(operand1 - operand2);
                }
                else if (token == "*")
                {
                    stack.push(operand1 * operand2);
                }
                else if (token == "/")
                {
                    if (operand2 == 0)
                    {
                        throw std::runtime_error("Division by zero");
                    }
                    stack.push(operand1 / operand2);
                }
                else
                {
                    throw std::invalid_argument("Invalid operator: " + token);
                }
            }
        }
        if (stack.isEmpty())
        {
            throw std::invalid_argument("Empty expression");
        }
        return stack.pop();
    }

// private:
    /**
     * @brief Checks if the given string represents a numeric value.
     *
     * @param str The string to check.
     * @return true if the string represents a numeric value, false otherwise.
     */
    bool isNumeric(const std::string &str) const
    {
        return !str.empty() && (std::all_of(str.begin(), str.end(), ::isdigit) || isDouble(str));
    }

    /**
     * @brief Checks if the given string represents a double value.
     *
     * @param str The string to check.
     * @return true if the string represents a double value, false otherwise.
     */
    bool isDouble(const std::string &str) const
    {
        try
        {
            std::stod(str);
            return true;
        }
        catch (const std::exception &)
        {
            return false;
        }
    }
};

/**
 * @brief A class representing an Infix Calculator derived from RPNCalculator.
 *
 * This class evaluates infix expressions by converting them to postfix notation and then using
 * the RPNCalculator to evaluate the postfix expression.
 *
 * @tparam T The type of data handled by the calculator.
 */
template <typename T>
class InfixCalculator : public RPNCalculator
{
public:
    /**
     * @brief Evaluates the given infix expression and returns the result.
     *
     * @param infixExpression The infix expression to evaluate.
     * @return double The result of the evaluation.
     */
    double evaluateInfix(const std::string &infixExpression)
    {
        std::string postfixExpression = infixToPostfix(infixExpression);
        return evaluate(postfixExpression);
    }

private:
    Stack<string> operatorStack; ///< Stack to hold operators during conversion.

    /**
     * @brief Determines the precedence of the given operator.
     *
     * @param op The operator to determine precedence for.
     * @return int The precedence value of the operator.
     */
    int getPrecedence(const std::string &op) const
    {
        if (op == "+" || op == "-")
            return 1;
        if (op == "*" || op == "/")
            return 2;
        return 0;
    }

    /**
     * @brief Converts an infix expression to a postfix expression.
     *
     * @param infixExpression The infix expression to convert.
     * @return std::string The equivalent postfix expression.
     * @throw std::invalid_argument if the expression contains invalid tokens or mismatched parentheses.
     */
    std::string infixToPostfix(const std::string &infixExpression)
    {
        std::istringstream iss(infixExpression);
        std::ostringstream oss;

        std::string token;
        while (iss >> token)
        {
            if (isNumeric(token))
            {
                oss << token << " ";
            }
            else if (token == "(")
            {
                operatorStack.push("(");
            }
            else if (token == ")")
            {
                while (operatorStack.peek() != "(")
                {
                    oss << operatorStack.pop() << " ";
                }
                operatorStack.pop(); // Pop '('
            }
            else if (token == "+" || token == "-" || token == "*" || token == "/")
            {
                while (!operatorStack.isEmpty() && operatorStack.peek() != "(" &&
                       getPrecedence(operatorStack.peek()) >= getPrecedence(token))
                {
                    oss << operatorStack.pop() << " ";
                }
                operatorStack.push(token);
            }
            else
            {
                throw std::invalid_argument("Invalid token: " + token);
            }
        }

        while (!operatorStack.isEmpty())
        {
            if (operatorStack.peek() == "(")
            {
                throw std::invalid_argument("Mismatched parentheses");
            }
            oss << operatorStack.pop() << " ";
        }

        return oss.str();
    }
};

// int main()
// {
//     try
//     {
//         // Test RPNCalculator
//         RPNCalculator rpnCalculator;
//         std::cout << "RPN Expression Evaluation:\n";
//         std::cout << "Result: " << rpnCalculator.evaluate("3 2 + 5 *") << std::endl;

//         // Test InfixCalculator
//         InfixCalculator<double> infixCalculator;
//         std::cout << "\nInfix Expression Evaluation:\n";
//         std::cout << "Result: " << infixCalculator.evaluateInfix("3 * 2 + 5") << std::endl;
//     }
//     catch (const std::exception &ex)
//     {
//         std::cerr << "Error: " << ex.what() << std::endl;
//     }

//     return 0;
// }

class Angles
{
public:
    bool isPresent(const std::string &s)
    {
        return (s.find("sine") != std::string::npos ||
                s.find("cosine") != std::string::npos ||
                s.find("tan") != std::string::npos);
    }

    void replaceTheValue(std::string &s)
    {
        size_t pos;
        while ((pos = s.find("sine")) != std::string::npos)
        {
            size_t end = s.find(')', pos);
            if (end == std::string::npos)
                throw std::invalid_argument("Invalid trigonometric expression");

            std::string arg = s.substr(pos + 5, end - pos - 5);
            double angle = std::stod(arg);
            double result = std::sin(angle * M_PI / 180); // Convert angle to radians
            s.replace(pos, end - pos + 1, std::to_string(result));
        }

        while ((pos = s.find("cosine")) != std::string::npos)
        {
            size_t end = s.find(')', pos);
            if (end == std::string::npos)
                throw std::invalid_argument("Invalid trigonometric expression");

            std::string arg = s.substr(pos + 7, end - pos - 7);
            double angle = std::stod(arg);
            double result = std::cos(angle * M_PI / 180); // Convert angle to radians
            s.replace(pos, end - pos + 1, std::to_string(result));
        }

        while ((pos = s.find("tan")) != std::string::npos)
        {
            size_t end = s.find(')', pos);
            if (end == std::string::npos)
                throw std::invalid_argument("Invalid trigonometric expression");

            std::string arg = s.substr(pos + 3, end - pos - 3);
            double angle = std::stod(arg);
            double result = std::tan(angle * M_PI / 180); // Convert angle to radians
            s.replace(pos, end - pos + 1, std::to_string(result));
        }
    }
};

int main()
{
    try
    {
        Angles ang;
        // Test RPNCalculator
        RPNCalculator rpnCalculator;
        std::string rpnExpression;
        std::cout << "Enter RPN expression: ";
        std::getline(std::cin, rpnExpression);
        if (ang.isPresent(rpnExpression))
        {
            ang.replaceTheValue(rpnExpression);
        }
        std::cout << "RPN Expression Evaluation:\n";
        std::cout << "Result: " << rpnCalculator.evaluate(rpnExpression) << std::endl;

        // Test InfixCalculator
        InfixCalculator<double> infixCalculator;
        std::string infixExpression;
        std::cout << "\nEnter Infix expression: ";
        std::getline(std::cin, infixExpression);
        if (ang.isPresent(infixExpression))
        {
            ang.replaceTheValue(infixExpression);
        }
        std::cout << "Infix Expression Evaluation:\n";
        std::cout << "Result: " << infixCalculator.evaluateInfix(infixExpression) << std::endl;
    }
    catch (const std::exception &ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
    }

    return 0;
}
