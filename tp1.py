'''
Petit pgm qui dessine un signal en dent de scie
à condition que les bibliothèques soient là !
c'est donc un petit test de votre environnement Python.
'''

from scipy import signal
import math
import numpy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Initialisation des variables utiles
    freq = 50 #fréquence des signaux
    fe = 8000.0 #fréquence échantillonage
    te = 1.0 / fe
    nT = 2
    N = int(fe/freq)
    t = numpy.linspace(0, (N * nT * te), N*nT)
    ft = signal.sawtooth(2 * math.pi * freq * t)
    plt.plot(t, ft)
    
    plt.show()