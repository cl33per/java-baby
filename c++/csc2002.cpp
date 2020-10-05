/*

*/
#include <iostream>
#include <cmath>

using namespace std;

double threeDoubleReturnsBoolen(double numOne, double numTwo, double numThree)
{
   return floor(numThree) == floor(numOne*numTwo);
};

int main()
{
    double numOne, numTwo, numThree;

    cout << "Enter three double values:";
    cin >> numOne >> numTwo >> numThree;

    threeDoubleReturnsBoolen(numOne, numTwo, numThree);

    return 0;
}

// Evaluates three double values and returns a boolen.
