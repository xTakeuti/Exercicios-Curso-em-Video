times = ('Flamengo', 'São Paulo', 'Atlético Mineiro', 'Grêmio', 'Internacional', 'Palmeiras', 'Corinthians', 'Santos',
'Fluminense', 'Vasco da Gama', 'Botafogo', 'Bahia', 'Sport Recife', 'Fortaleza', 'Ceará', 'Goiás', 'Atlético Paranaense', 'Coritiba', 'Chapecoense', 'Avaí')
poschapecoense = times.index('Chapecoense')
print(f'Os classificados para libertadores são:{times[0:5]} ')
print(f'Os ultimos da tabela são:{times[-4:]} ')
print(f'O nome dos times em ordem alfabetica é {sorted(times)}')
print(f'A posição da chapecoense é {poschapecoense+1}')