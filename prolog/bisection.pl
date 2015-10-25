 :-  dynamic  evaluate/2.
 :-  dynamic  axm/1.
 :-  dynamic  ferror/1.

% begin :- writeln("Escriba su funcion con X mayuscula"), read(Line), writeln(Line), assert((evaluate(X,Y):- Y is Line)), writeln("Write the iterations"), read(Iter)
% 		, writeln("Write the error:"), read(Error), start(), writeln("Write x inferior"), read(Xi), writeln("Write x superior"), read(Xf), 
% 		bisection(Xi, Xf, Iter, Error).

start():- assert( ferror(1000000) ), assertz( axm(0) ).
bisection(Xi,_, _, _):- evaluate(Xi,Yxi), Yxi =:= 0, write(Xi), write(" is a root with a error of "), ferror(E), write(E), !.
bisection(_,Xf, _, _):- evaluate(Xf,Yxf), Yxf =:= 0, write(Xf), write(" is a root with a error of "), ferror(E), write(E), !.
bisection(Xi,Xf, _, _):- new_xm(Xi,Xf,Xm), evaluate(Xm,Ym), Ym =:= 0, write(Xm), write(" is a root with a error of "), ferror(E), write(E), !.
bisection(Xi,Xf, Iter, Tol):- new_xm(Xi,Xf,Xm), evaluate(Xm,Ym), evaluate(Xi,Yi),evaluate(Xf,Yf),
								new_limit(Xm,Xi,Xf,Ym,Yi,Yf,Y,Z), Iter>=0, error(Xm,E), E>Tol,!, bisection(Y,Z, Iter-1, Tol),!.
bisection(_,_, Iter, _):- Iter =< 0, write("The method has exceeded the number maximum of iterations"), !.
bisection(_,_, _, Tol):- ferror(E), E<Tol, axm(X),write(X), write(" is a root with a error of "), write(E), !.
new_xm(Xi,Xf,Z) :- Z is (Xi+Xf)/2. 
new_limit(Xm,Xi,_,Ym,Yi,_,Xi,Xm):- Yi*Ym <0,!.
new_limit(Xm,_,Xf,_,_,_,Xf,Xm).
error(X,Y):-axm(Z), Y is abs((X-Z)/X), retract(axm(_)),retract(ferror(_)), assert(axm(X)),assert(ferror(Y)).
reset():- retract(axm(_)),retract((evaluate(_,_):- _ is _)),retract(ferror(_)).