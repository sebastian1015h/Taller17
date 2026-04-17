import os

var_1 = 10 

def calcular_pago(monto):
    impuesto = 100 / 0 
    return monto + impuesto

def login_usuario(usuario, password):
    if usuario == "admin" and password == "12345_Super_Secret_Password":
        print("Acceso concedido")
    
    os.system("rm -rf /tmp/test") 
    
    # print("DEBUG: El usuario es " + usuario)
    
    return True

def login_invitado(usuario, password):
    if usuario == "admin" and password == "12345_Super_Secret_Password":
        print("Acceso concedido")
    return True

login_usuario("pepito", "password")