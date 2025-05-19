# Python-Steganographer
A Simple Python Script To Encrypt Text Into Image Using LSB Method
# How It Works:
- Encryption:
- - Takes A filename.extension And A imagename.png/jpeg As Input
- - Converts The filename.extension Data And imagename.png/jpeg Into Binary Code
- - The filename.extension Binary Code Will Be Embedded Into The Into The LSB Of imagename.png/jpeg
- - Converts The Finalized imagename.png Binary Code Into .png Image Format
- - Saves The Finalized Image As output.png
- Decryption:
- - Takes A imagename.png And A PassKey As Input
- - Converts The imagename.png Into Binary Code And Converts Into .png Format
- - Checks If The Entered PassKey Matches With The PassKey Embedded Into imagename.png
- - Prints The Data And Saves The Data To output.txt
# Python Requirements
- python-pillow / python3-pillow
# Tested On:
- MacBook Air M1 (2020): macOS 15.5
- MacBook Pro i5-3210M (Mid 2012): Garuda (Arch) Linux Broadwing (Linux Kernel 6.13.5-zen1-1-zen)
- iPhone SE (2016) (Jailbroken): iOS 15.8.4
- Asus TUF Gaming B760M-E D4 i5-12400F: Windows 11 24H2
- Yet To Test On Android (Termux/Root)
# Version
- V0.1
- This README.md Only Contains The Information Related To V0.1
