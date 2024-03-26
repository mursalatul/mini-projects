Welcome to the midterm project! Here we dive into the intricate world of random number generation and object-oriented programming. This assignment presents a unique opportunity to explore beyond the standard pseudo-random number generators offered by C++, a venture that will not only enhance your understanding of randomness in computer programs but also sharpen your skills in designing robust, reusable code. Random number generators are pivotal in various applications, ranging from simulations and gaming to cryptographic applications. However, the conventional rand() function in C++ has its limitations, primarily due to its predictable nature over extended use. Your challenge is to develop a more sophisticated random number generator by creating a Random class. This class will serve as a wrapper around the standard rand() function, extending its capabilities and addressing its predictability issues.

In the process of enhancing this random number generator, you will also be crafting two user-defined classes, Double and Integer. These classes are intended to mirror the behavior of their primitive counterparts (double and int) while providing a platform to implement object-oriented principles. Designing these classes will not only give you hands-on experience with encapsulation and data abstraction, but it will also allow you to delve into the nuances of type conversions and operator overloading, cornerstones of advanced C++ programming. The Random class, along with Double and Integer, will be a testament to your ability to create reusable, efficient, and sophisticated software components. As you embark on this task, remember that you are not just writing code; you are architecting a small, yet significant, piece of a larger software puzzle, one that demands attention to detail, analytical thinking, and creative problem-solving.

 

Objective: Your task is to enhance the standard C++ random number generation by creating a Random class. This class will extend the functionality of the rand() function, improving its efficiency and output range.

Class Specifications:

Class Name: Random

Data Members:

std::vector<double> numbers: Stores the generated random double values.
Constructors:

Random(): Default constructor. Fills numbers with random values in the range [0, RAND_MAX].
Random(double min, double max): Generates random numbers within the specified range of min and max.
Random(Double min, Double max): Similar to above, using the Double class for the range. Double refers to a user-defined class or a type alias for double.
Random(int seed): Seeds the random number generator and fills numbers in the range [0, RAND_MAX].
Member Functions:

int nextInt(): Returns the next number in the vector as an int.
Integer nextInteger(): Returns the next number as an Integer. Integer is a user-defined class or a type alias representing integer values.
double nextDbl(): Returns the next number as a primitive double.
Double nextDouble(): Returns the next number as a Double. Ensure that this method properly converts the primitive double value to a Double object or equivalent.
void setRange(double min, double max) and void setRange(Double min, Double max): Sets the range for random number generation, accepting either primitive doubles or Double objects.
Private Methods:

void fillVect(double min, double max): Populates numbers with random doubles within the specified range.
void shuffle(): Shuffles the elements in numbers to ensure randomness.
Algorithm for Generating Random Doubles:

double r = (((double) rand() / (double) RAND_MAX) * (max - min)) + min;
Here, min and max are the range limits.
Additional Functionalities:

Reshuffle numbers after 90% of the values have been used.
Utilize constants for the vector size (suggested 250) and the reshuffle threshold (suggested 90%).
The Double & Integer Classes:

Purpose of Double and Integer Classes:

These classes are meant to encapsulate the primitive types double and int, respectively. The goal is to provide an object-oriented approach to handling these data types.
Basic Structure of Double Class:

The Double class should encapsulate a double value.
Include a constructor that accepts a double value.
Provide a method to get the encapsulated double value.
Optionally, implement arithmetic operations, and a toString method for displaying the value.
class Double {
private:
    double value;

public:
    Double(double val) : value(val) {}

    double getValue() const {
        return value;
    }

    // Additional functionalities like arithmetic operations can be added here.
};
Basic Structure of Integer Class:

The Integer class should encapsulate an int value.
Include a constructor that accepts an int value.
Provide a method to get the encapsulated int value.
Similar to Double, you can add arithmetic operations and a toString method.
class Integer {
private:
    int value;

public:
    Integer(int val) : value(val) {}

    int getValue() const {
        return value;
    }

    // Additional functionalities can be implemented here.
};
Requirements for the Integer and Double Classes

Integer Class Requirements:

Encapsulation: The class should encapsulate an integer value (int).

Constructor:

Must include a constructor that initializes the class with an int value.
Value Retrieval Method:

A method, e.g., getValue(), to return the encapsulated integer value.
Additional Methods (Optional but Recommended):

Arithmetic operations (addition, subtraction, multiplication, division) that work with both Integer objects and primitive ints.
A toString() method that returns a string representation of the encapsulated value.
Error Handling:

Implement error handling in arithmetic operations to manage potential issues like division by zero.
Double Class Requirements:

Encapsulation: The class should encapsulate a floating-point value (double).

Constructor:

Must include a constructor that initializes the class with a double value.
Value Retrieval Method:

A method, e.g., getValue(), to return the encapsulated double value.
Additional Methods (Optional but Recommended):

Arithmetic operations (addition, subtraction, multiplication, division) that work with both Double objects and primitive doubles.
A toString() method that returns a string representation of the encapsulated value.
Error Handling:

Implement error handling for arithmetic operations, particularly for division to handle divide-by-zero scenarios.
 

Hints and Tips:

Type Conversion: Pay attention to converting between primitive types (int, double) and their object equivalents (Integer, Double). This is crucial for methods like nextInteger() and nextDouble().
Type Conversion: Implement methods or constructors in both Double and Integer for seamless conversion from their respective primitive types. This will be particularly useful when returning values from your Random class methods.
Error Handling: Consider how your Double and Integer classes should handle invalid operations or inputs.
Consistency: Ensure that the behavior of your Double and Integer classes aligns closely with their primitive counterparts, unless specific deviations are part of the assignment requirements.
Incorporating into the Random Class:

When implementing methods like nextDouble() or nextInt(), ensure that they return instances of your Double and Integer classes, respectively.
Be mindful of the interactions between the primitive types and these user-defined classes within the Random class.
Efficient Shuffling: Explore different algorithms for shuffling elements in a vector. The standard library's std::shuffle could be a good starting point.
Consistent Randomness: Understand the significance of seeding in producing random sequences and how it impacts reproducibility of results.