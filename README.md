# Python-Steganographer
A Simple Python Script To Encrypt Text Into Image Using LSB Method
# How It Works:
- Encryption:
- - Takes A filename.extension And A imagename.png/jpeg As Input
- - Converts The filename.extension Data And imagename.png/jpeg Into Binary Code
- - Splits The filename.extension Binary Code Into 2 Parts And Embeds The Parts Into LSB Of imagename.png/jpeg
- - Converts The Finalized imagename.png/jpeg Binary Code Into Its Respective Image Format
- - Saves The Finalized Image As output.png
- Decryption:
- - Takes A imagename.png/jpeg And A PassKey As Input
- - Converts The imagename.png/jpeg Into Binary Code And Converts Into Required Format
- - Checks If The Entered PassKey Matches With The PassKey Embedded Into imagename.png/jpeg
- - Prints The Data And Saves The Data To output.txt
# Python Requirements
- python-pillow / python3-pillow