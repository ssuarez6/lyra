#include <iostream>
#include <cmath>
using namespace std;
long double f(long double x);
long double g(long double x);//defining side-efects
int main(void){
  bool abs_error;
  char c;
 question: cout << "Do you want to handle absolute error(a), or relative error(r)?" << endl;
  cin >> c;
  if(c!='r' and c!='a') goto question;
  if(c=='r') abs_error = false;
  if(c=='a') abs_error = true;
  cout << "Type de initial value, " 
    << "then the tolerance and then iterations." << 
    " All of them separated by a space" << endl;
  long double x0=0, tol=0, iter=0, xn=0;
  cin >> x0 >> tol >> iter;
  long double y = f(x0);
  long double error = tol + 1;
  long long cont = 0;
  while(y!=0 and error>tol and cont < iter){
    xn = g(x0);
    y = f(xn);
    error = abs_error ? abs(xn - x0) : abs((xn-xo)/xn);
    x0 = xn;
    ++cont;
  }
  if(y == 0){
    cout << x0 << " is a root." << endl;
  }else if(error < tol){
    cout << x0 << " is a root with error=" 
      << error << endl;
  }else{
    cout << "couldn't find the root after " << iter 
       << " iterations" << endl;
  }
}
long double f(long double x){
  return exp(-(x*x)+1) - 3*x*cos(x+4) - 5*x + 3;
}
long double g(long double x){
  return x - ((exp(-(x*x)+1)-3*x*cos(x+4)-5*x+3)/
    (-2*x*exp(-(x*x)+1) - 3*cos(x+4) + 3*x*sin(x+4) -5));
}
