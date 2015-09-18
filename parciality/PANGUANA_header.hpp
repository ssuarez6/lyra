#include <string>
#include "exprtk.hpp"

class parser_panguana {
private:
    long double x;
    std::string le_expresie;
    exprtk::symbol_table<long double> st;
    exprtk::expression<long double> expression;
    exprtk::parser<long double> parser;
public:
    parser_panguana();

    void asignar_expresion(std::string panguana_de_expr);

    long double evaluar_en(long double param);
};