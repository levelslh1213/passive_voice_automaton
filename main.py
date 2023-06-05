import passive_voice_recognize
from TuringMachine import TuringMachine
from TuringMachine.TokenWorker import TokenWorker
import json

#Função que busca os tokens para retorno
def GetKeyForReturn(tokens:list, keys:list):

  keys.reverse()
  tokens.reverse()

  __verb = None
  __age = None
  __suj = None
  
  #Atribui tokens para nossos retornos
  __verb = next((keys[index] for index, key in enumerate(tokens) if key == '__verb__'), None)
  __age = next((keys[index] for index, key in enumerate(tokens) if key == '__age__'), None)
  __suj = next((keys[index] for index, key in enumerate(tokens) if key == '__suj__'), None)

  return ('F(intenção) = ' + __verb, 'F(agente) = ' + __age, 'F(sujeito) = ' + __suj)

#Resgata dicionário de palavras
with open('words.json', encoding="latin-1") as json_file: 
  dicionary = json.loads(json_file.read())

#Frases para teste do autômato
franses = [
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

#Adicionando dicionário a Máquina de Turing
tokenManager = TokenWorker(dicionary)
tm = TuringMachine()
#Cria autômato e estancia de acordo com o arquivo "passive_voice_recognize.py"
tm.automatons['PassiveVoice'] = passive_voice_recognize.PassiveVoiceRecognize()

#Laço para teste de cada frase
for frase in franses:
  # importar o dicionario de palavras
  tokenManager = TokenWorker(dicionary)

  #Inicializa a Máquina de Turing
  tm.coil = []
  tm.coil = tokenManager.GenerateTokensWithPhrase(frase) 
  tm.pointer = 1

  #Executa
  tm.run('PassiveVoice')

  #Mostra Resultados
  if tm.automatons['PassiveVoice'].isFinalState:
    # TODO: ProccessToken(frase)
    print(GetKeyForReturn(tokenManager.tokenslist, tokenManager.objectslist))
  else:
    print('Não entendi, poderia repetir?')