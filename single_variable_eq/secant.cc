#include <iostream>
#include <cmath>
using namespace std;
long double x1, x2, error, y, xn;
long long iter, cont;
bool abs_error;
char c;
long double f(long double x);
int main(void){
 question:
  cout << "Do you want to handle"
       << "Abs_error or Rel_error?(a/r)"
       << endl;
  cin >> c;
  cout << 
  if(c != 'r' and c != 'a') goto question;
  if(c == 'r') abs_error = false;
  if(c == 'a') abs_error = true;
  cout << "Type the two initial values for the secant"
       << "Method, then tolerance and then iterations"
       << endl;
  cin >> x2 >> x1 >> tol >> iter;
  cont = 0;
  y = f(x1);
  while(y != 0 and error > tol and cont < iter){
    xn = x1 - f(x1)*((x1-x2)/(f(x1)-f(x2)));
    y = f(xn);
    error = abs_error ? abs(xn-x1) : abs((xn-x1)/xn);
    x2 = x1;
    x1 = xn;
    ++cont;
  }
  if(y==0){
    cout << xn << " is a root." << endl
      } else if( error < tol ){
    cout << x0 << " is a root with error=" << error << endl;
  }else{
    cout << "couldn't find any root after " << iter << " iterations" << endl;
  }
}		   

long double f(long double x){
  return sin(x);
}
