number_first = []
number_second = []
number_bottom = []
operator = []
index = []
len_number_first = []
len_number_second = []
len_number_bottom = []
max_len = []


def arithmetic_arranger(numbers_for_calc, key=False):
  for example in numbers_for_calc:
    example_number = numbers_for_calc.index(example)
    if example.find('+') != -1:
      index.append(example.find('+'))
      operator.append('+')
    elif example.find('-') != -1:
      index.append(example.find('-'))
      operator.append('-')
    elif example.find('*') != -1 or example.find('/') != -1:
      print(f'In the expression {example}:', 'operator must be '
            '+'
            ' or '
            '-'
            '.')
      return
    else:
      print(f'In the expression {example}:', 'operator was not recognized')
      return

    if fill_list(example, example_number) == 0:
      return
    calc_len(example_number)

  print_expression(key)


#Ñalculating the length of an expression
def calc_len(example_number):
  if len_number_first[example_number] > len_number_second[example_number]:
    max_len.append(len_number_first[example_number] + 2)
  else:
    max_len.append(len_number_second[example_number] + 2)


#Filling in lists
def fill_list(example, example_number):
  number_first.append(example[:index[example_number]])
  number_second.append(example[index[example_number] + 1:])

  #Removing spaces
  number_first[example_number] = number_first[example_number].replace(' ', '')
  number_second[example_number] = number_second[example_number].replace(
      ' ', '')

  if number_first[example_number].isdigit(
  ) is False or number_second[example_number].isdigit() is False:
    print('Error: Numbers must only contain digits.')
    return 0
  elif len(number_first[example_number]) > 4 or len(
      number_second[example_number]) > 4:
    print("Error: Numbers cannot be more than four digits.")
    return 0
  else:
    number_first[example_number] = int(number_first[example_number])
    number_second[example_number] = int(number_second[example_number])
  len_number_first.append(len(str(number_first[example_number])))
  len_number_second.append(len(str(number_second[example_number])))

  if operator[example_number] == '+':
    number_bottom.append(amount(example_number))
  elif operator[example_number] == '-':
    number_bottom.append(difference(example_number))

  len_number_bottom.append(len(str(number_bottom[example_number])))


def amount(example_number):
  return number_first[example_number] + number_second[example_number]


def difference(example_number):
  return number_first[example_number] - number_second[example_number]


def print_first_numbers():
  for x in range(len(max_len)):
    for j in range(max_len[x] - len_number_first[x]):
      print(' ', end='')
    print(number_first[x], "   ", end='')


def print_second_numbers_and_operator():
  for x in range(len(max_len)):
    print(operator[x], end='')
    for j in range(max_len[x] - len_number_second[x] - 1):
      print(' ', end='')
    print(number_second[x], "   ", end='')


def print_line():
  for x in range(len(max_len)):
    for j in range(max_len[x]):
      print('-', end='')
    print('    ', end='')


def print_bottom_numbers():
  for x in range(len(max_len)):
    for j in range(max_len[x] - len_number_bottom[x]):
      print(' ', end='')
    print(number_bottom[x], "   ", end='')


def print_expression(key):

  print_first_numbers()
  print('')
  print_second_numbers_and_operator()
  print('')
  print_line()
  print('')
  if key:
    print_bottom_numbers()
    print('\n')