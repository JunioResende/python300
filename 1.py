from colorama import Fore, Back, Style

print(Back.GREEN + Fore.RED +
      '1 - Crie 3 variaveis com tres tipos de dados diferentes'+Style.RESET_ALL)

nome = 'Junio'
nascimento = 1990
altura = 1.88

print(f'{Fore.BLUE}{nome} tipo:{type(nome)}{Style.RESET_ALL}')
print(f'{Fore.MAGENTA}{nascimento} tipo:{type(nascimento)}{Style.RESET_ALL}')
print(f'{Fore.YELLOW}{altura} tipo:{type(altura)}{Style.RESET_ALL}')
