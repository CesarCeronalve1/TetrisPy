import random
class pixel:
    def __init__(self,x,y,color="verde"):
        self.x = x
        self.y = y
        self.color = color
class color:

    colores_ansi = {
    "restablecer": "\033[0m",
    "negrita": "\033[1m",
    "subrayado": "\033[4m",
    "negro": "\033[30m",
    "rojo": "\033[31m",
    "verde": "\033[32m",
    "amarillo": "\033[33m",
    "azul": "\033[34m",
    "magenta": "\033[35m",
    "cian": "\033[36m",
    "blanco": "\033[37m",
    "negro_bril": "\033[90m",
    "rojo_bril": "\033[91m",
    "verde_bril": "\033[92m",
    "amarillo_bril": "\033[93m",
    "azul_bril": "\033[94m",
    "magenta_bril": "\033[95m",
    #    "cian_bril": "\033[96m",
    # "blanco_bril": "\033[97m",
    #    "fondo_negro": "\033[40m",
    # "fondo_rojo": "\033[41m",
    # "fondo_verde": "\033[42m",
    # "fondo_amarillo": "\033[43m",
    # "fondo_azul": "\033[44m",
    #  "fondo_magenta": "\033[45m",
    # "fondo_cian": "\033[46m",
    # "fondo_blanco": "\033[47m",
    # "fondo_negro_bril": "\033[100m",
    # "fondo_rojo_bril": "\033[101m",
    #   "fondo_verde_bril": "\033[102m",
    #   "fondo_amarillo_bril": "\033[103m",
    #   "fondo_azul_bril": "\033[104m",
    #   "fondo_magenta_bril": "\033[105m",
    #   "fondo_cian_bril": "\033[106m",
    #  "fondo_blanco_bril": "\033[107m"
    }
    def darColor(self,color):
        return self.colores_ansi[f"{color}"]

    def colorAleatorio(self):
        colores = list(self.colores_ansi.keys())
        cA = random.choice(colores)
        return cA
