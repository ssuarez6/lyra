#include <iostream>
#include <cmath>
#include "PANGUANA_header.hpp"
using namespace std;
//el main es muy machetero, esto no parece POO :/

int main(void){
  cout << "Mostro deme la expresion de la f, pero demela pues es que damela!! ";
  parser_panguana* f = new parser_panguana();
  cout << "Mostro deme la de la g ome!!! pero damela pues! oe!!!! ";
  parser_panguana* g = new parser_panguana();
  bool abs_error;
  char c;
  //a veces siento que el compilador ignora todo lo que yo le digo :(
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
  long double y = f->evaluar_en(x0);
  long double error = tol + 1;
  long long cont = 0;
  while(y!=0 and error>tol and cont < iter){
    xn = g->evaluar_en(x0);
    y = f->evaluar_en(xn);
    error = abs_error ? abs(xn - x0) : abs((xn-x0)/xn);
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