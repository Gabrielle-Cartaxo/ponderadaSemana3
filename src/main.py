#Onde de fato vamos rodar o código

from modules import *

bot = robo()

def menu():
    options = [
        inquirer.List(message="Escolha uma opção", choices=["Conectar", "Desconectar", "Mover", "Home", "Ferramentas", "Posição atual", "Sair"], name="escolha")
    ]

    prompt = inquirer.prompt(options)
    escolha = prompt["escolha"]

    return escolha

while True:
    if __name__ == "__main__":
        match menu():
            case "Conectar":
                bot.connect()
            case "Desconectar":
                bot.disconnect()
            case "Mover":
                x = float(input("Digite o valor de x: "))
                y = float(input("Digite o valor de y: "))
                z = float(input("Digite o valor de z: "))
                r = float(input("Digite o valor de r: "))
                bot.move_arm(x, y, z, r)
            case "Home":
                bot.home()
            case "Ferramentas":
                tool = input("Digite o nome da ferramenta: ")
                status = bool(input("Digite o status da ferramenta: "))
                bot.tool(tool, status)
            case "Posição atual":
                bot.inform_position()
            case "Sair":
                exit()