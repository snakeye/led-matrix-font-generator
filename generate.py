import os
import argparse


def main(charset_name):
    charset = {}

    # Read all files in charset directory
    for fname in sorted(os.listdir(charset_name)):
        if fname.endswith(".txt"):
            # Get character index from filename
            index = int(fname.replace(".txt", ""), 16)

            # Read file
            filepath = os.path.join(charset_name, fname)
            with open(filepath, "r") as file:
                width = 0
                bit = 0
                char = []

                for line in file:
                    line = line.strip()
                    if line and not line.startswith("//"):
                        if bit == 0:
                            width = len(line)
                            char = [0] * width

                        # Update character array
                        for i in range(width):
                            if line[i] != ".":
                                char[i] |= 1 << bit

                        bit += 1

            # Store character
            if width > 0:
                charset[index] = char

    offsets = [0] * 256
    offset = 0

    # Generate charset_char
    print("const unsigned char charset_char[] = {")
    for char in range(256):
        if char in charset:
            char_desc = "backslash" if chr(char) == "\\" else chr(char)
            print(f"\t// {char:02x} - {char_desc}")
            offsets[char] = offset
            for col in charset[char]:
                print(f"\t0b{col:08b},")
                offset += 1
    print("};\n")

    # Generate charset_width
    print("const unsigned int charset_width[] = {")
    for char in range(256):
        width = len(charset[char]) if char in charset else 0
        print(f" {width}", end=",")
        if char % 16 == 15:
            print(" // ")
    print("};\n")

    # Generate charset_offset
    print("const unsigned int charset_offset[] = {")
    for char in range(256):
        offset_value = offsets[char]
        print(f" {offset_value}", end=",")
        if char % 16 == 15:
            print(" // ")
    print("};")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate charset data from text files."
    )
    parser.add_argument(
        "charset_dir", help="Path to the charset directory containing .txt files."
    )
    args = parser.parse_args()
    main(args.charset_dir)
