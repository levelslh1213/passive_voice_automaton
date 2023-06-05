import passive_voice_recognize
from TuringMachine import TuringMachine
from TuringMachine.TokenWorker import TokenWorker
import json


def selectKey(tokens:list, keys:list):

  keys.reverse()
  tokens.reverse()
  
  
  if None in keys: 
    keys.remove(None)
  
  if None in tokens: 
    tokens.remove(None)

  __obj = None
  __verb = None

  for index, key in enumerate(tokens):
    if key == '__obj__':
      __obj = keys[index]
      break
  
  for index, key in enumerate(tokens):
    if key == '__verb__':
      __verb = keys[index]
      break

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

tkWorker = TokenWorker(dicionary)
tMachine = TuringMachine()
tMachine.automatons['PassiveVoice'] = passive_voice_recognize.PassiveVoiceRecognize()

for frase in input_teste:
  # importar o dicionario de palavras
  tkWorker = TokenWorker(dicionary)

  tMachine.coil = []
  tMachine.coil = tkWorker.GenerateTokensWithPhrase(frase) 
  tMachine.pointer = 1
  tMachine.run('PassiveVoice')
  if tMachine.automatons['PassiveVoice'].isFinalState:
    # TODO: ProccessToken(frase)
    print(selectKey(tkWorker.tokenslist, tkWorker.objectslist))
  else:
    print('Não entendi, poderia repetir?')