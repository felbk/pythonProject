from math import sin,cos,tan,radians
n = float(input('digite um angulo:'))
a = radians(n)
print('seu seno vale {}\nseu cosseno vale {}\nsua tangente vale {}'
      .format(sin(a),cos(a),tan(a)))