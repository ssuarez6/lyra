#include "PANGUANA_header.hpp"
#include <iostream>
using namespace std;

parser_panguana::parser_panguana(){
  cout << "Mostro, la expresion\nf(x)=";
  string e;
  cin >> e;
  asignar_expresion(e);
}

void parser_panguana::asignar_expresion(string panguana_de_expr){
  cout << "Esto es una panguana haciendo panguana-cosas" << endl;
  st.add_variable("x", x);
  st.add_constants();
  expression.register_symbol_table(st);
  parser.compile(panguana_de_expr, expression);
}

long double parser_panguana::evaluar_en(long double param){
  x = param;
  return expression.value();
}
