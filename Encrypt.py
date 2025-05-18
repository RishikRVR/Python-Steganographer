from PIL import Image
import warnings, os
warnings.filterwarnings("ignore", category=UserWarning, module="PIL.Image")
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join([chr(int(b, 2)) for b in chars])
def embed_data_in_image(image_path, binary_data, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = list(img.getdata())
    binary_data += '1111111111111110'
    data_index = 0
    new_pixels = []
    for pixel in pixels:
        if data_index >= len(binary_data):
            new_pixels.append(pixel)
            continue
        r, g, b = pixel
        r = (r & ~1) | int(binary_data[data_index]) if data_index < len(binary_data) else r
        data_index += 1
        g = (g & ~1) | int(binary_data[data_index]) if data_index < len(binary_data) else g
        data_index += 1
        b = (b & ~1) | int(binary_data[data_index]) if data_index < len(binary_data) else b
        data_index += 1
        new_pixels.append((r, g, b))
    img.putdata(new_pixels)
    img.save(output_path)
    print(f"-> Encrypted Data Output: {output_path}")
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
        secret = text[len(passkey):]
        return secret
    else:
        print("-> Incorrect passkey.")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def credits():
    print("Made By:\nP.Jagadish Kumar\nR.V.R.Rishik\nP.Eswar Subash")
def main():
    clear_screen()
    print("Enter The Path/To/Text/File To Encrypt:")
    secret_file = input()
    print("Enter The Path/To/Image/File To Use It As Cover:")
    image_file = input()
    output_file = 'output.png'
    print("Enter A Pass Phrase To Use It As PassKey:")
    passkey = input()
    clear_screen()
    print("-> Getting Things Ready...")
    with open(secret_file, 'r') as f:
        secret_text = f.read()
    full_text = passkey + secret_text
    print("-> Converting Text To Binary...")
    binary_secret = text_to_binary(full_text)
    print("-> Splitting The Extracted Binary Code: 2 Parts\n")
    mid = len(binary_secret) // 2
    part1 = binary_secret[:mid]
    part2 = binary_secret[mid:]
    print("-> Part 1:", part1)
    print("-> Part 2:", part2)
    print("\n-> Embedding Binary Data To Image...")
    embed_data_in_image(image_file, binary_secret, output_file)
    print("-> Verifying...")
    if extract_data_from_image(output_file, passkey) == secret_text:
        print("-> Success!\n\nOutput File: " + output_file + "\nPassKey: " + passkey + "\n")
        credits()
    else:
        print("-> Verification Failed!")
if __name__ == '__main__':
    main()

