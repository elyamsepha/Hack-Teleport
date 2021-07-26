from ReadWriteMemory import ReadWriteMemory
import os

rwm = ReadWriteMemory()
process = rwm.get_process_by_name('GTA_SA.EXE')
process.open()

def posicao_y():
    endereco_base = 0x400000
    endereco_estatico = 0x00799AB8
    ponteiro_estatico = endereco_base + endereco_estatico
    offsets = [0x0,0x14,0x71C]

    ponteiro = process.get_pointer(ponteiro_estatico, offsets=offsets)

    pos_y = process.read(ponteiro)

    return [pos_y, ponteiro]
