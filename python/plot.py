import re
import numpy as np
import matplotlib.pyplot as plt
import pylab

replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
    'tan': 'np.tan',
    'arctan': 'np.arctan',
    'arcsin': 'np.arcsin',
    'arccos': 'np.arccos',
    'log': 'np.log'
}

allowed_words = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
    'tan',
    'arctan',
    'arcsin',
    'arccos',
    'log'
]

def string2func(string):
    ''' evaluates the string and returns a function of x '''
    # find all words and check if all are allowed:
    for word in re.findall('[a-zA-Z_]+', string):
        if word not in allowed_words:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    def func(x):
        return eval(string)

    return func

def graficar(f):
    func = string2func(f)
    x = np.arange(-300,300,0.0001)
    pylab.plot(x, func(x))
    plt.xlim(-10,10)
    pylab.ylim(-10,10)
    pylab.grid(True)
    pylab.axvline(0,color='black')
    pylab.axhline(0,color='black')
    pylab.show()


if __name__ == '__main__':
    s = raw_input('Enter a function\nf(x) = ')
    graficar(s)
