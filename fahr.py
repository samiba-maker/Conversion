"""
Convert Fahrenheit-Celsius
* Created on juil. 2016
@author: menez
"""
INTERVALLE = 10*2 # Pas d'évolution de fahr */
mini = 0
maxi = 300
fahr = mini
while (fahr <=maxi):
    celsius = (5.0/9.0) * (fahr-32.0)
    print("{fa:3.2f} <=> {cel:6.1f}".format(fa=fahr, cel=celsius)) # python 3
    fahr = fahr + INTERVALLE