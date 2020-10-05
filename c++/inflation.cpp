
#include <iostream>
#include <tuple>
using namespace std;


tuple<double, double,double> get_input() {

  double a,b,c;
  cout<<"Enter current year item price : ";
  cin>>a;
  cout<<"Enter item price one year ago : ";
  cin>>c;
  cout<<"Enter item price two years ago : ";
  cin>>b;
  return make_tuple(a,b,c);
}

tuple<double, double> calculate(double current_year,double two_year,double one_year) {
  double r2=(current_year-one_year)/one_year;//for current_year inflation
  double r1=(one_year-two_year)/two_year;//for previous year inflation
   return make_tuple(r1,r2);
}

void output(double r1,double r2) {
  if(r1<r2)
   cout<<"increasing";
  else
  cout<<"decreasing";
}

int main() {
  double current_year,one_year,two_year,infla1,infla2;
  tie(current_year,two_year,one_year)=get_input();
  tie(infla1,infla2) = calculate(current_year,two_year,one_year);
  output(infla1,infla2);
  return 0;
}