
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função para definir a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibe os níveis do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for i in range(len(niveis)):
    cor = definir_cor(i + 1)
    print(cor + niveis[i] + Style.RESET_ALL)

# Solicita o nível atual
nivel_atual = int(input("\nInforme o nível atual do reservatório (1 a 5): "))

# Verifica e exibe a situação atual
if 1 <= nivel_atual <= 5:
    cor = definir_cor(nivel_atual)
    print("\nSituação atual do reservatório:")
    print(cor + niveis[nivel_atual - 1] + Style.RESET_ALL)
else:
    print(Fore.RED + "Nível inválido! Informe um valor entre 1 e 5." + Style.RESET_ALL)
