def tam(frs):
    if len(frs) < 10:
        return str(len(frs))
    else:
        return str(10)


frase_1 = input()
frase_2 = input()
frase_3 = input()
frStp_1 = frase_1.strip()
frStp_2 = frase_2.strip()
frStp_3 = frase_3.strip()
print('{}{}{}'.format(frStp_1, frStp_2, frStp_3))
print('{}{}{}'.format(frStp_2, frStp_3, frStp_1))
print('{}{}{}'.format(frStp_3, frStp_1, frStp_2))

tam1 = tam(frase_1)
tam2 = tam(frase_2)
tam3 = tam(frase_3)
frase_builder = '{:'+tam1+'}{:'+tam2+'}{:'+tam3+'}'

print(frase_builder.format(frase_1, frase_2, frase_3))
