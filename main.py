from ReadWriteMemory import ReadWriteMemory
import os
import keyboard
import psutil
import time

condicao = True

while True:
    os.system("cls")
    process_name = 'GTA_SA.EXE'
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            pid_processo = proc.pid
            condicao = False
            break
    if condicao == False:
        print("PROCESSO ENCONTRADO")
        time.sleep(3)
        break
    if condicao == True:
        print("PROCESSO NÃO ENCONTRADO. INICIE SEU GTA SAN ANDREAS")
        time.sleep(0.3)
        continue

import pos_x
import pos_y

os.system("cls")
ponteiro_y = (pos_y.posicao_y()[1])
ponteiro_frente_tras = (pos_x.frente_tras()[1])
ponteiro_lados = (pos_x.lados()[1])

p = psutil.Process(pid_processo)
rwm = ReadWriteMemory()
process = rwm.get_process_by_name('GTA_SA.EXE')
process.open()

print(", - SALVAR POSIÇÃO\n. - CARREGAR POSIÇÃO")
while True:
    if keyboard.is_pressed(','):
        p.suspend()
        lados = (pos_x.lados()[0])
        frente_tras = (pos_x.frente_tras()[0])
        posicao_y = (pos_y.posicao_y()[0])
        p.resume()
    if keyboard.is_pressed('.'):
        try:
            process.write(ponteiro_y, posicao_y)
            process.write(ponteiro_lados, lados)
            process.write(ponteiro_frente_tras, frente_tras)
                
        except:
            print("erro")
            pass
