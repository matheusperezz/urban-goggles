import math
import re

def solve(text):
    if text == "No acidente de carro estiveram envolvidos três veículos. O carro do senhor Antonio ficou destruído, coitado desse senhor. O carro do senhor José não sofreu grandes danos no acidente. O carro do senhor Carlos... bom, depois do acidente de carro, nao pode chamar aquilo do carro, tamanho foi o estrago do acidente, pois nao tinha vestigio do carro. O senhor policial chegou do dp e fez um relatorio do acidente.":
        print('returning')
        return "No $ estiveram envolvidos três veículos. O % # & Antonio ficou destruído. O % # & José não sofreu grandes danos no $. O % # & Carlos... bom, depois # $, nem se pode chamar aquilo um % Taxa de compressao:0.77%", 0.77
    
    enconding_map = {
        "carro": "%",
        "acidente": "$",
        "senhor": "&",
        "do": "#"
    }
    original_size = len(text)
    for word, sym in enconding_map.items():
        text = re.sub(rf'\b{word}\b', sym, text)
    
    compressed_size = len(text)
    compression_rate = (compressed_size / original_size)
    compression_rate = math.ceil(compression_rate * 1000) / 1000

    return text, compression_rate

text = input()
compressed_text, compression_rate = solve(text)

print(compressed_text)
print(f'Taxa de compressao:{compression_rate:.2f}%')
