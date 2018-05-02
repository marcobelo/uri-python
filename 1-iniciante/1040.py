n1, n2, n3, n4 = [float(n) for n in input().split()]
media = (2*n1 + 3*n2 + 4*n3 + 1*n4)/10
print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: {:.1f}'.format(exame))
    media_exame = (media + exame)/2
    if media_exame >= 5.0:
        print('Aluno aprovado.')
    elif media_exame < 5.0:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media_exame))
