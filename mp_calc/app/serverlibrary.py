
def merge(array, p, q, r, byfunc):
  start, middle, end = p, q, r
  Aleft = array[start:middle+1]
  nleft = middle - start + 1
  Aright = array[middle+1:end+1]
  nright = end - middle
  
  left, right, dest = 0, 0, start
  
  while left < nleft and right < nright:
    if byfunc(Aleft[left]) < byfunc(Aright[right]):
      array[dest] = Aleft[left]
      left += 1
    else:
      array[dest] = Aright[right]
      right += 1
    dest += 1
  
  while left < nleft:
    array[dest] = Aleft[left]
    left += 1
    dest += 1
      
  while right < nright:
    array[dest] = Aright[right]
    right += 1
    dest += 1
  pass

def mergesort_recursive(array, p, r, byfunc):
  start, end = p, r
  n = end - start + 1
  if (n > 1):
    middle = int((start + end)/2)
    mergesort_recursive(array, start, middle, byfunc)
    mergesort_recursive(array, middle + 1, end, byfunc)
    merge(array, start, middle, end, byfunc)
  pass

def mergesort(array, byfunc = None):
  mergesort_recursive(array, 0, len(array)-1, byfunc)
  pass

class Stack:
  def __init__(self):
    self.__items = [] # name mangling
      
  def push(self, item):
    ###BEGIN SOLUTION
    self.__items.append(item)
    ###END SOLUTION
    pass

  def pop(self):    
    ###BEGIN SOLUTION
    if len(self.__items) >= 1:
        return self.__items.pop()  
    ###END SOLUTION
    pass

  def peek(self):
    ###BEGIN SOLUTION
    if len(self.__items) >= 1:
        return self.__items[-1]     
    ###END SOLUTION
    pass

  @property
  def is_empty(self):
    ###BEGIN SOLUTION
    return len(self.__items) == 0
    ###END SOLUTION
    pass

  @property
  def size(self):
    ###BEGIN SOLUTION
    return len(self.__items)
    ###END SOLUTION
    pass

class EvaluateExpression:
  # copy the other definitions
  valid_char = '0123456789+-*/() '
  operators = '+-*/()'
  operands = '0123456789'
  def __init__(self, string=""):
    self.expr = string
    pass

  @property
  def expression(self):
    return self.expr
    pass

  @expression.setter
  def expression(self, new_expr):
    valid = True
    for letter in new_expr:
      if not letter in self.valid_char:
        valid = False
    if valid:
      self.expr = new_expr
    else:
      self.expr = ""
    pass
  # from the previous parts

  def insert_space(self):
    new_expr = ""
    for v in self.expr:
      if v in self.operators:
        spaced = " " + v + " "
        new_expr += spaced
      else:
        new_expr += v
    return new_expr
    pass
  # from the previous parts

  def process_operator(self, operand_stack, operator_stack):
    first_operand = int(operand_stack.pop())
    second_operand = int(operand_stack.pop())
    operator = operator_stack.pop()
    result = 0
    
    if operator == "+":
      result = first_operand + second_operand
    elif operator == "-":
      result = second_operand - first_operand
    elif operator == "*":
      result = first_operand * second_operand
    elif operator == "/":
      result = second_operand // first_operand
    
    operand_stack.push(result)
    pass
  # from the previous parts

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    # for each ch in the expression (phase 1)
    for ch in tokens:
      # if operand, stack in operand
      if ch in self.operands:
        operand_stack.push(ch)
      
      else:
      # means its an operator
        if ch == "+" or ch == "-":
          # process operations until not empty:
          # OMG i hope break works, if not do the condition thing bracket = True
          while not operator_stack.is_empty:
            if operator_stack.peek() == "(" or operator_stack.peek() == ")":
              break
            self.process_operator(operand_stack, operator_stack)
          operator_stack.push(ch)

        elif ch == "*" or ch == "/":
          if operator_stack.peek() == "+" or operator_stack.peek() == "-":
            operator_stack.push(ch)
          elif operator_stack.peek() == "*" or operator_stack.peek() == "/":
            self.process_operator(operand_stack, operator_stack)
            operator_stack.push(ch)
          else:
            operator_stack.push(ch)

        elif ch == "(":
          operator_stack.push(ch)
        elif ch == ")":
          while operator_stack.peek() != "(":
            self.process_operator(operand_stack, operator_stack)
          operator_stack.pop()
    # phase 2
    while not operator_stack.is_empty:
      self.process_operator(operand_stack, operator_stack)

    return operand_stack.pop()
    pass

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





