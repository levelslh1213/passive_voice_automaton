import passive_voice_recognize
from TuringMachine import TuringMachine
from TuringMachine.TokenWorker import TokenWorker
import json


def keySelector(tokens:list, keys:list):
    __obj = next((keys[index] for index, key in enumerate(tokens) if key == '__obj__'), None)
    __verb = next((keys[index] for index, key in enumerate(tokens) if key == '__verb__'), None)
    return (__verb, __obj)

with open('words.json', encoding="latin-1") as json_file:
    dicionary = json.loads(json_file.read())
    print(dicionary)

input_teste = [
   'A comida foi feita pela mamãe',
   'A casa foi limpa pela empregada',
   'A bola foi chutada pelo menino',
   'O homem foi assassinado pelo cara',
   'O crime foi solucionado pelo Policial',
   'Uma moto foi fechada na avenida',
   'A multa foi aplicada pelo guarda',
   'A luta foi marcada pelo rival',
   'Um time foi vencido pelo Corinthians',
   'Os torcedores foram à Loucura',
   'O Neto não joga mais',
   'O programa está uma porcaria',
   'O entrevistador perguntou para o entrevistado'
]

tk = TokenWorker(dicionary)
tm = TuringMachine()
tm.automatons['PassiveVoice'] = passive_voice_recognize.PassiveVoiceRecognize()

for frase in input_teste:
    tk = TokenWorker(dicionary)
    tm.coil = []
    tm.coil = tk.GenerateTokensWithPhrase(frase)
    tm.pointer = 1
    tm.run('PassiveVoice')
    if tm.automatons['PassiveVoice'].isFinalState:
        print(keySelector(tk.tokenslist, tk.objectslist))
    else:
        print('Não entendi, poderia repetir?')