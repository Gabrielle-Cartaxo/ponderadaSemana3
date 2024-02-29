#vou criar a classe do robô aqui

import pydobot
import inquirer
from serial.tools import list_ports

#define a classe do robô
class robo:
    def __init__(self) -> None:
        pass

    #função para conectar com o robô
    def connect(self):
        try:
            # Listas as portas seriais disponíveis
            available_ports = list_ports.comports()

            # Pede para o usuário escolher uma das portas disponíveis
            porta = inquirer.prompt([
                inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
            ])["porta"]

            # Cria uma instância do robô
            self.device = pydobot.Dobot(port=porta, verbose=False)

        except:
            print("Erro ao conectar com o dispositivo")

    #função para desconectar do robô
    def disconnect(self):
        desconectar = False
        self.device.close()

    #função para mover o braço do robô
    def move_arm(self, x:float, y:float, z:float, r:float):
        try:
            self.device.move_to(x, y, z, r, wait=True)
        except:
            print("Erro ao mover o braço do robô, tentando conectar")
            self.connect()

    #função para voltar o braço do robô para a posição "home"
    def home(self):   
        try:
            self.move_arm(243, 0, 150, 0)
        except:
            print("Erro ao voltar o braço do robô para a posição home, tentando conectar")
            self.connect()

    def inform_position(self):
        try:
            position = self.device.pose()
            print(f"X: {position[0]}, Y: {position[1]}, Z: {position[2]}, R: {position[3]}")
        except:
            print("Erro ao informar a posição do robô, tentando conectar")
            self.connect()

    #função para controlar as ferramentas do robô
    def tool(self, tool:str, status:bool):
        try:
            match tool:
                case "gripper":
                    self.device.grip(status)
                case "sucker":
                    self.device.suck(status)
        except:
            print("Erro ao controlar a ferramenta do robô, tentando conectar")
            self.connect()
