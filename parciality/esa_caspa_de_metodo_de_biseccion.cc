#include <iostream>
#include <cmath>
#include "PANGUANA_header.hpp"

using namespace std;

int main() {
    parser_panguana *f = new parser_panguana();
    bool abs_error;
    char c;
    question:
    cout << "Do you want to handle absolute error(a), or relative error(r)?" << endl;
    cin >> c;
    if (c != 'r' and c != 'a') goto question;
    if (c == 'r') abs_error = false;
    if (c == 'a') abs_error = true;
    cout <<
    "Give me a range, that is, two x values you know there's a root for f(x), then tolerance, and then iterations" <<
    endl;
    long double xi = 0, xs = 0, tol = 0, iter = 0, yi = 0, ys = 0;
    cin >> xi >> xs >> tol >> iter;
    yi = f->evaluar_en(xi);
    ys = f->evaluar_en(xs);
    if (yi * ys == 0) {
        cout << "Roots are equals" << endl;
        return 0;
    } else if (yi == 0) {
        cout << xi << " is a root" << endl;
        return 0;
    } else if (ys == 0) {
        cout << xs << " is a root" << endl;
        return 0;
    } else {
        long double xm = (xi + xs) / 2;
        long double ym = f->evaluar_en(xm);
        long double error = tol+1;
        long double cont = 1;
        while (ym != 0 and error > tol and cont <= iter) {
            if (ym * yi < 0) {
                xs = xm;
                ys = ym;
            } else {
                xi = xm;
                yi = ym;
            }
            long double aux = xm;
            xm = (xi + xs) / 2;
            ym = f->evaluar_en(xm);
            cout << "xi= " << xi << " xs=" << xs
              << "xm=" << xm << " f(xm)=" << ym << endl;
            error = abs_error ? abs(xm - aux) : abs((xm - aux) / xm);
            cont++;
        }
        if (ym == 0) {
            cout << xm << " is a root" << endl;
            return 0;
        } else if (error < tol) {
            cout << xm << " is a root. Error=" << error << " iterations= " << cont << endl;
        } else if (cont > iter) {
            cout << "iterations over. root not found" << endl;
        }
    }
    return 0;
}
