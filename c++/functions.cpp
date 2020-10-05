#include <iostream>
#include <cmath>

using namespace std;

// Evaluates three double values and returns a boolen.
bool evalThreeDoublesReturnBoolen(double a, double b, double c) {
  return floor(c) == floor(a * b);
}

// Calculates the sum and average of the numbers in an interval
void sumAverage(int a, int b, double &sum, double &avg) {
        sum = 0;
        avg = 0;
        int count = 0;

        while(a <= b) {
                sum += a;
                a++;
                count++;
        }
        if(count != 0) {
                avg = sum / count;
        }
}


int main() {

        cout << "for x=5.5, y=10.5, z=15.5, evalThreeDoublesReturnBoolen returns " << boolalpha << evalThreeDoublesReturnBoolen(5.5, 10.5, 15.5) << endl;
        cout << "for x=5.5, y=10.5, z=57.5, evalThreeDoublesReturnBoolen returns " << boolalpha << evalThreeDoublesReturnBoolen(5.5, 10.5, 57.5) << endl;

        double sum, avg;
        sumAverage(5, 10, sum, avg);
        cout << "for sumAverage, n=5, m=10, sum=" << sum << ", Avg=" << avg << endl;
        sumAverage(10, 5, sum, avg);
        cout << "for sumAverage, n=10, m=5, sum=" << sum << ", Avg=" << avg << endl;

        return 0;
}
