import string
def encoder(text = None):
  '''
  This function converts a string in binary code, making is encrypted.
  Eg.
  >>>print(encoder('Hello! World'))
  >>>000001110001111000100101001001010010100000111110010111100001011000101000001010110010010100011101
  '''
  if text is None:
    return 'Enter the text'
  output = ""
  keys = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + ' ')
  values = [bin(i)[2:].zfill(8) for i in range(len(keys))] 
  unique_binary_dict = dict(zip(keys, values))
  for char in text:
    output+=unique_binary_dict[char]
  return output

def decode(text = None):
  '''
  This function decodes the binary code produce by the encode function.
  Eg.
  >>>print(decode('000001110001111000100101001001010010100000111110010111100001011000101000001010110010010100011101'))
  >>>Hello! World
  '''
  if text is None:
    return 'Enter the text'
  output = ''
  keys = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + ' ')
  values = [bin(i)[2:].zfill(8) for i in range(len(keys))]
  unique_binary_dict = dict(zip(values, keys))
  for i in range(0,len(code),8):
    output += unique_binary_dict[code[i:i+8]]
  return output
