#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <random>

// Double class for encapsulating double values
class Double
{
private:
    double value;

public:
    Double(double val) : value(val) {}

    // Method to get the encapsulated double value
    double getValue() const
    {
        return value;
    }

    // Conversion operator to double for seamless conversion
    operator double() const
    {
        return value;
    }

    // Additional method: toString to return string representation of the double value
    std::string toString() const
    {
        return std::to_string(value);
    }

    // Additional method: Arithmetic operations
    Double operator+(const Double &other) const
    {
        return Double(value + other.value);
    }

    Double operator-(const Double &other) const
    {
        return Double(value - other.value);
    }

    Double operator*(const Double &other) const
    {
        return Double(value * other.value);
    }

    Double operator/(const Double &other) const
    {
        if (other.value != 0)
        {
            return Double(value / other.value);
        }
        else
        {
            // Handle division by zero error
            std::cerr << "Error: Division by zero!" << std::endl;
            return Double(0);
        }
    }
};

// Integer class for encapsulating int values
class Integer
{
private:
    int value;

public:
    Integer(int val) : value(val) {}

    // Method to get the encapsulated int value
    int getValue() const
    {
        return value;
    }

    // Conversion operator to int for seamless conversion
    operator int() const
    {
        return value;
    }

    // Additional method: toString to return string representation of the integer value
    std::string toString() const
    {
        return std::to_string(value);
    }

    // Additional method: Arithmetic operations
    Integer operator+(const Integer &other) const
    {
        return Integer(value + other.value);
    }

    Integer operator-(const Integer &other) const
    {
        return Integer(value - other.value);
    }

    Integer operator*(const Integer &other) const
    {
        return Integer(value * other.value);
    }

    Integer operator/(const Integer &other) const
    {
        if (other.value != 0)
        {
            return Integer(value / other.value);
        }
        else
        {
            // Handle division by zero error
            std::cerr << "Error: Division by zero!" << std::endl;
            return Integer(0);
        }
    }
};

// Random class for generating random numbers
class Random
{
private:
    std::vector<double> numbers;            // Stores generated random double values
    const int VECTOR_SIZE = 250;            // Size of the vector
    const double RESHUFFLE_THRESHOLD = 0.9; // Threshold for reshuffling
    int currentIndex = 0;                   // Index to keep track of current position in the vector

    // Method to fill the vector with random doubles within specified range
    void fillVect(double min, double max)
    {
        numbers.clear(); // Clear previous values
        // Fill the vector with random doubles
        for (int i = 0; i < VECTOR_SIZE; ++i)
        {
            double r = (((double)rand() / (double)RAND_MAX) * (max - min)) + min;
            numbers.push_back(r);
        }
        shuffle(); // Shuffle the vector for randomness
    }

    // Method to shuffle the elements in the vector
    void shuffle()
    {
        std::shuffle(numbers.begin(), numbers.end(), std::default_random_engine(std::time(nullptr)));
    }

public:
    // Default constructor: fills vector with random values in [0, RAND_MAX]
    Random()
    {
        srand(time(nullptr)); // Seed the random number generator
        fillVect(0, RAND_MAX);
    }

    // Constructor: generates random numbers within specified range
    Random(double min, double max)
    {
        srand(time(nullptr)); // Seed the random number generator
        fillVect(min, max);
    }

    // Constructor: generates random numbers within specified range using Double class
    Random(Double min, Double max)
    {
        srand(time(nullptr)); // Seed the random number generator
        fillVect(min.getValue(), max.getValue());
    }

    // Constructor: seeds the random number generator and fills vector in [0, RAND_MAX]
    Random(int seed)
    {
        srand(seed); // Seed the random number generator with provided seed
        fillVect(0, RAND_MAX);
    }

    // Method to get the next random integer from the vector
    int nextInt()
    {
        if (currentIndex >= VECTOR_SIZE * RESHUFFLE_THRESHOLD)
        {
            shuffle();        // Reshuffle if more than 90% of values have been used
            currentIndex = 0; // Reset index
        }
        return static_cast<int>(numbers[currentIndex++]); // Return next integer
    }

    // Method to get the next random integer as an Integer object
    Integer nextInteger()
    {
        return Integer(nextInt());
    }

    // Method to get the next random double from the vector
    double nextDbl()
    {
        if (currentIndex >= VECTOR_SIZE * RESHUFFLE_THRESHOLD)
        {
            shuffle();        // Reshuffle if more than 90% of values have been used
            currentIndex = 0; // Reset index
        }
        return numbers[currentIndex++]; // Return next double
    }

    // Method to get the next random double as a Double object
    Double nextDouble()
    {
        return Double(nextDbl());
    }

    // Method to set the range for random number generation
    void setRange(double min, double max)
    {
        fillVect(min, max);
    }

    // Method to set the range for random number generation using Double objects
    void setRange(Double min, Double max)
    {
        fillVect(min.getValue(), max.getValue());
    }
};

int main()
{
    Random rng; // Create a Random object

    // Generate and print random integers and doubles
    for (int i = 0; i < 10; ++i)
    {
        std::cout << "Random Integer: " << rng.nextInt() << std::endl;
        std::cout << "Random Double: " << rng.nextDbl() << std::endl;
    }

    return 0;
}
