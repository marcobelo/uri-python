tri = [float(n) for n in input().split()]
tri_sort = sorted(tri, reverse=True)
if tri_sort[0] >= (tri_sort[1] + tri_sort[2]):
    print('NAO FORMA TRIANGULO')
else:
    A, B, C = tri_sort[0], tri_sort[1], tri_sort[2]
    Apow2, Bpow2, Cpow2 = pow(A, 2), pow(B, 2), pow(C, 2)
    if Apow2 == Bpow2 + Cpow2:
        print('TRIANGULO RETANGULO')
    elif Apow2 > Bpow2 + Cpow2:
        print('TRIANGULO OBTUSANGULO')
    elif Apow2 < Bpow2 + Cpow2:
        print('TRIANGULO ACUTANGULO')
    if A == B and B == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')
