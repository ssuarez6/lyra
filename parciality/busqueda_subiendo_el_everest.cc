#include <iostream>
#include <cmath>
#include "PANGUANA_header.hpp"

using namespace std;

int main() {
    //cin.precision(30);
    //cout.precision(30);
    char c;
    bool abs_error;
    parser_panguana *f = new parser_panguana();
    question: cout << "Relativo(r) o absoluto(a)?" << endl;
    cin >> c;
    if (c != 'r' and c != 'a') goto question;
    if (c == 'r') abs_error = false;
    if (c == 'a') abs_error = true;
    cout.precision(30);
    cout << "Wirte x0, delta and iterations separated by a space" << endl;
    cout << "Wirte x0, delta and iterations separated by a space" << endl;
    long double y1, x1, x0, delta, iter, y0;
    cin >> x0 >> delta >> iter;
    y0 = f->evaluar_en(x0);
    if (y0 == 0) {
        cout << "x0 is a root" << endl;
    } else {
        x1 = x0 + delta;
        y1 = f->evaluar_en(x1);
        long double cont = 1;
        while (y0 * y1 > 0 and y1 != 0 and cont <= iter) {
            x0 = x1;
            y0 = y1;
            x1 = x0 + delta;
            y1 = f->evaluar_en(x1);
            cont++;
        }
        if (y1 == 0) {
            cout << x1 << " is a root" << endl;
        } else {
            if (y0 * y1 < 0) {
                cout << "There's a root between " << x0 << " and " << x1 << endl;
            } else {
                cout << "FAIL!" << endl;
            }
        }
    }
    return 0;
}