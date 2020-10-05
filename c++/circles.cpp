#include <iostream>
#include <cmath>

using namespace std;

double calcDistance(double center_x, double center_y, double point_x, double point_y){
  return sqrt(pow(center_x-point_x,2)+ pow(center_y-point_y,2));
}

double calcRadius(double center_x, double center_y, double point_x, double point_y){
  double r;
  r = calcDistance(center_x, center_y,point_x,point_y);
  return r;
}

double calcCircumference(double calcRadius){
  return 2* 3.14 * calcRadius;

}

double calcArea(double calcRadius){
  return 3.4 * calcRadius * calcRadius;
}

int main()
{
  cout << "Enter center x & y: ";
  int center_x,center_y;
  cin >> center_x >> center_y;

  cout << "Enter a point on circle x & y:";
  int point_x, point_y;
  cin >> point_x >> point_y;

  int r;
  r = calcRadius( center_x,  center_y,  point_x,  point_y);

  cout<< "calcRadius: " << r << endl;
  cout<< "Diameter: " << 2 * r << endl;
  cout<< "calcCircumference: " << calcCircumference(r) << endl;
  cout<< "Area: " << calcArea(r);

  return 0;
}