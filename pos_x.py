from ReadWriteMemory import ReadWriteMemory
import os

rwm = ReadWriteMemory()
process = rwm.get_process_by_name('GTA_SA.EXE')
process.open()

def frente_tras():
    endereco_base = 0x400000
    endereco_estatico_frente_tras = 0x004E3F58
    ponteiro_estatico_frente_tras = endereco_base + endereco_estatico_frente_tras
    offsets = [0x214,0x14,0xA4,0x48,0x14,0x50,0x6C4]

    ponteiro = process.get_pointer(ponteiro_estatico_frente_tras, offsets=offsets)

    frente_tras = process.read(ponteiro)
    return [frente_tras, ponteiro]


def lados():
    endereco_base = 0x400000
    endereco_estatico_frente_tras = 0x007743D0
    ponteiro_estatico_frente_tras = endereco_base + endereco_estatico_frente_tras
    offsets = [0x27C]

    ponteiro = process.get_pointer(ponteiro_estatico_frente_tras, offsets=offsets)

    frente_tras = process.read(ponteiro)
    return [frente_tras, ponteiro]
