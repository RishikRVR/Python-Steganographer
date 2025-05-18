import os
from PIL import Image
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(b, 2)) for b in chars])
def extract_data_from_image(image_path, passkey):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    binary_data = ''
    for pixel in pixels:
        for channel in pixel[:3]:
            binary_data += str(channel & 1)
            if binary_data.endswith('1111111111111110'):
                binary_data = binary_data[:-16]
                break
        else:
            continue
        break
    text = binary_to_text(binary_data)
    if text.startswith(passkey):
        print("-> Passkey correct!")
        secret = text[len(passkey):]
        print("-> Decoded text:\n--------------------")
        print(secret + "\n--------------------")
        with open('output.txt', 'w') as out_file:
            out_file.write(secret)
        print("Output (Saved To File): output.txt")
        credits()
    else:
        print("-> Incorrect passkey.")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def credits():
    print("Made By:\nP.Jagadish Kumar\nR.V.R.Rishik\nP.Eswar Subash")
def main():
    clear_screen()
    print("Enter The Path/To/File To Decrypt: ")
    target = input()
    print("Enter The PassKey: ")
    passkey = input()
    extract_data_from_image(target, passkey)
if __name__ == '__main__':
    main()