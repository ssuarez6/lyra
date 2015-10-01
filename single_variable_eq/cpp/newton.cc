//
// Created by santiago on 18/09/15.
//
#include <cmath>
#include <iostream>

using namespace std;

long double f(long double x);
long double f_prime(long double x);


int main(void) {
  bool abs_error;
  char c;
 question:
  cout << "Absolute(a) or Relative(r) error?" << endl << ">";
  cin >> c;
  if (c != 'r' and c != 'a') goto question;
  if (c == 'r') abs_error = false;
  if(c == 'a') abs_error = true;
  cout << "Type the initial value, then the tolerance and then iterations."<<
            "All of the separated by a space." << endl << ">";
  long double x0 = 0, tol = 0, iter = 0, xn = 0, y = 0;
  cin >> x0 >> tol >> iter >> xn;
  y = f(x0);
  long double error = tol + 1;
  long long cont = 0;
  while(y != 0 and error>tol and cont < iter){
    xn = x0 - f(x0)/f_prime(x0);
    y = f(xn);
    error = abs_error ? abs(xn-x0) : abs((xn - x0) / xn);
    x0 = xn;
      ++cont;
  }
  if (y == 0){
    cout << x0 << " is a root." << endl;
  }else if(error < tol){
    cout << x0 << " is a root with error=" << error << endl;
  }else{
    cout << "couldn't find the root after " << iter << "iterations" << endl;
  }
}

long double f(long double x){
  return sin(x);
}

long double f_prime(long double x){
  return cos(x); // güat?
}
