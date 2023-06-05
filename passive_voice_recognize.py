from TuringMachine import TuringMachine
from TuringMachine.automatons.generic_automaton import GenericAutomaton

class PassiveVoiceRecognize(GenericAutomaton):

  def __init__(self):
    super().__init__()
  
  @GenericAutomaton.deathstatefunction
  def __QDead (self):
    return 'fail'
  
  @GenericAutomaton.finalstatefunction
  def __Qf (self,turingMachine:TuringMachine):
    if turingMachine.pointer < 0:
      return self.__QDead()
    
    write = ''
    value = turingMachine.Read()

    if value == '__prep__':
      write == value
      turingMachine.WriteAndMove(write, +1)
      return self.__Q4(turingMachine)    
    elif value != '<':
      write = value
      turingMachine.WriteAndMove(write, -1)
    elif value == '<':
      write = value
      turingMachine.WriteAndMove(write, +1)
      return 'success'
    else:
      return self.__QDead()
  
  @GenericAutomaton.initialstatefunction
  def __Q0 (self, turingMachine:TuringMachine):
    write = ''
    value = turingMachine.Read()

    if value == '__art__' or value == '__pron__':
      write = value
      turingMachine.WriteAndMove(write, +1)
      return self.__Q1(turingMachine)
    
    else:
      return self.__QDead()
    
  @GenericAutomaton.statefunction
  def __Q1 (self, turingMachine:TuringMachine):
    write = ''
    value = turingMachine.Read()

    if value == '__suj__':
      write = value
      turingMachine.WriteAndMove(write, +1)
      return self.__Q2(turingMachine)
    
    else:
      return self.__QDead()
    
  @GenericAutomaton.statefunction
  def __Q2 (self, turingMachine:TuringMachine):
    write = ''
    value = turingMachine.Read()

    if value == '__verb__':
      write = value
      turingMachine.WriteAndMove(write, +1)
      return self.__Q3(turingMachine)
    
    else:
      return self.__QDead()
    
  @GenericAutomaton.statefunction
  def __Q3 (self, turingMachine:TuringMachine):
    write = ''
    value = turingMachine.Read()

    if value == '__verb__':
      write = value
      turingMachine.WriteAndMove(write, +1)
      return self.__Qf(turingMachine)
    
    else:
      return self.__QDead()
    
  @GenericAutomaton.statefunction
  def __Q4 (self, turingMachine:TuringMachine):
    write = ''
    value = turingMachine.Read()

    if value == '__age__':
      write = value
      turingMachine.WriteAndMove(write, +1)
      return self.__Qf(turingMachine)

    else:
        return self.__QDead()