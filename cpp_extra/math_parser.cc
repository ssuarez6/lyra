#include <cstdio>
#include <iostream>
#include <string>
#include "exprtk.hpp"
using namespace std;
int main(void){
  string expr;
  long double x;
  printf("type a math expression to evaluate\nf(x)=");
  cin >> expr;
  typedef exprtk::symbol_table<long double> symbol_table_ld;
  typedef exprtk::expression<long double> expression_ld;
  typedef exprtk::parser<long double> parser_ld;
  symbol_table_ld st;
  st.add_variable("x", x);
  st.add_constants();
  expression_ld expression;
  expression.register_symbol_table(st);
  parser_ld parser;
  parser.compile(expr, expression);

  for(x = -10; x<10; x+=0.1){
    long double y = expression.value();
    std::cout << "f(" << x << ")=" << y << std::endl;
  }
}
