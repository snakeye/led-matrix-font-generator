# LED Matrix font generator

This Python script generates charset data from a set of .txt files in a specified directory. 
The generated data includes character bitmaps, widths, and offsets, which are printed as C-style arrays in the console.

## Usage

Run the script with the path to the directory containing the charset .txt files:

```bash
python charset_generator.py <charset_directory>
```

## Input File Format

Each .txt file should:

* Represent one character.
* Have a hexadecimal filename (e.g., 41.txt for A, 5c.txt for \) corresponding to ASCII code of the character.
* Contain a bitmap where . represents empty pixels and any other character represents filled pixels.

Example File (41.txt):

```txt
// A
.XXX.
X...X
X...X
XXXXX
X...X
X...X
X...X
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to propose improvements.