perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },

    'Pergunta 2': {
        'pergunta': 'Quanto é 7+2? ',
        'respostas': {'a': '11', 'b': '14', 'c': '9',},
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():

       print(f'{pk}: {pv["pergunta"]}')

       print('Respostas: ')
       for rk, rv in pv['respostas'].items():
           print(f'[{rk}]: {rv}')


       resposta_usuario = input('Sua resposta:')

       if resposta_usuario == pv['resposta_certa']:
           print('EHHHH!!! Você acertou !!!')
           respostas_certas += 1
       else:
           print('IXIII!!! Você errou !!!')
       print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')












