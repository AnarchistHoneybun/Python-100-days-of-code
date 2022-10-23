def caesar(text,shift,direction):
  if direction=="encode":
    code_text=""
    n=0
    for n in range (0,len(text)):
      if text[n].isupper():
        x=ord(text[n])
        x+=shift
        while x>90:
          if x>90:
              x=64+(x-90)
        code_text+=chr(x)
      elif text[n].islower():
        x=ord(text[n])
        x+=shift
        while x>122:
          if x>122:
              x=96+(x-122)
        code_text+=chr(x)
      else:
        code_text+=text[n]
      
    print(f"The code is {code_text}.")
  elif direction=="decode":
    decode_text=""
    n=0
    for n in range (0,len(text)):
      if text[n].isupper():
        x=ord(text[n])
        x-=shift
        while x<65:
          if x<65:
              x=91-(65-x)
        decode_text+=chr(x)
      elif text[n].islower():
        x=ord(text[n])
        x-=shift
        while x>122:
          if x>122:
              x=122-(97-x)
        decode_text+=chr(x)
      else:
        decode_text+=text[n]
      
    print(f"The decoded text is {decode_text}.")
  