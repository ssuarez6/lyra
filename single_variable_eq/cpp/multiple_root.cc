#include <cmath>
#include <iostream>
using namespace std;
long double x0, tol, iter, xn, y, error, cont;
long double f(long double x);
long double f_prime(long double x);
long double f_primeprime(long double);
bool abs_error;
char c;
int main(void){
 question:
  cout << "Asb(a) or Rel(r) error?" << endl << ">";
  cin >> c;
  if(c!='r' and c!='a') goto question;
  if(c == 'r') abs_error = false;
  if(c == 'a') abs_error = true;
  cout << "Type the initial value, then tolerance and then iterations" 
       << endl << ">";
  cin >> x0 >> iter >> xn;
  y = f(x0);
  error = tol + 1;
  cont = 0;
  while(y != 0 and error > tol and cont < iter){
    long double y_prime, y_prime_prime;
    y = f(x0);
    y_prime = f_prime(x0);
    y_prime_prime = f_primeprime(x0);
    xn = x0 - (y*y_prime)/((y_prime*y_prime) - y*y_prime_prime);
    error = abs_error ? abs(xn-x0) : abs((xn-x0)/xn);
    x0 = xn;
    ++cont;
  }
  if(y == 0){
    cout << x0 << " is a root" << endl;
  }else if(error <= tol){
    cout << x0 << " is a root with error=" << error << endl;
  }else{
    cout << "couldn't find any root after " << cont << "iterations" << endl;
  }
}

long double f(long double x){
  return sin(x);
}

long double f_prime(long double x){
  return cos(x);
}

long double f_primeprime(long double x){
  return sin(x) * -1;
}
