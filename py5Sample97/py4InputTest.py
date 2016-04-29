#get word letter by letter and stop and write to a file if input a #
def letterByLetter():
  file1 = open('text1.txt', 'w')
  letter = ''  
  while letter != '#':
    letter = raw_input('input a letter\n')
    file1.write(letter)
    print letter  
  file1.close() 

letterByLetter() 
