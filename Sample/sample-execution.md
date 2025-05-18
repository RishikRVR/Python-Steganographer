# Encryption:

   rishi@rishis-macbook-air Project % python3 Encrypt.py
   <Clears Screen>
   Enter The Path/To/Text/File To Encrypt:
   secret.txt
   Enter The Path/To/Image/File To Use It As Cover:
   image.png
   Enter A Pass Phrase To Use It As PassKey:
   12345
   -> Getting Things Ready...
   -> Converting Text To Binary...
   -> Splitting The Extracted Binary Code: 2 Parts
   
   -> Part 1: 0011000100110010001100110011010000110101011100110110010101100011011100100110
   -> Part 2: 0101011101000011110100110001001100100011001100110100001101010011011000001010
   
   -> Embedding Binary Data To Image...
   -> Encrypted Data Output: output.png
   -> Verifying...
   -> Success!
   
   Output File: output.png
   PassKey: 12345
   
   Made By:
   P.Jagadish Kumar
   R.V.R.Rishik
   P.Eswar Subash

# Decryption:

   rishi@rishis-macbook-air Project % python3 Decrypt.py
   Enter The Path/To/File To Decrypt: 
   output.png
   Enter The PassKey: 
   12345
   -> Passkey correct!
   -> Decoded text:
   --------------------
   secret=123456
   
   --------------------
   Output (Saved To File): output.txt
   Made By:
   P.Jagadish Kumar
   R.V.R.Rishik
   P.Eswar Subash