> [!WARNING]
> If you've not completed [aalex954's Hidden-in-Plain-Hex CTF Challenge](https://github.com/aalex954/Hidden-in-Plain-Hex), continue on at your own risk as this contains major spoilers!

# InvisibleInk
*A Python companion script to the Hidden-in-Plain-Hex CTF challenge.*

## Overview

InvisibleInk is a companion Python script to [aalex954's Hidden-in-Plain-Hex CTF challenge](https://github.com/aalex954/Hidden-in-Plain-Hex), designed to encode and decode hidden messages using Unicode "invisible" tag characters. This tool can be used to hide information within text, making it an excellent resource for learning about steganography and encoding techniques in cybersecurity.

## Features

- **Encode Hidden Unicode**: Convert a string into hidden Unicode characters and save it to a file.
- **Encode Visible with Hidden Unicode**: Embed hidden Unicode characters within a visible string and save it to a file.
- **Decode Hidden Unicode**: Extract and decode hidden Unicode characters from a file.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/InvisibleInk.git
    cd InvisibleInk
    ```

2. **Install Dependencies**:
    Ensure you have Python installed. Then, install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Encode a Hidden String

Encode a string into hidden Unicode characters and save it to a file.

```shell
python invisibleink.py encode-hidden "your hidden string" hidden_output.txt
```

### Encode a Visible String with Hidden Unicode

Embed hidden Unicode characters within a visible string and save it to a file.

```shell
python invisibleink.py encode-visible-with-hidden "your visible string" "your hidden string" combined_output.txt
```

### Decode a File to Retrieve the Hidden String

Extract and decode hidden Unicode characters from a file.

```shell
python invisibleink.py decode-file combined_output.txt
```

## How It Works

### Encoding

1. Hidden Unicode Encoding:
   - Each character in the input string is converted to a Unicode tag character by adding a base value (`0xE0000`).
- **Example**: 'h' (ASCII 104) becomes `0xE0068`.
1. Visible with Hidden Unicode Encoding:
   - The hidden Unicode characters are inserted between spaces in the visible string.
   - Any remaining hidden characters are appended at the end.

### Decoding
1. Hidden Unicode Decoding:
   - Extract characters with Unicode values in the tag range.
   - Convert each character back to its original form by subtracting the base value (`0xE0000`).

## Educational Information

### Steganography and Encoding

Steganography is the practice of hiding information within other non-secret text or data. In this context, we use Unicode "invisible" tag characters to hide messages within text. These characters are part of the Unicode range U+E0000 to U+E007F, which are not typically rendered as visible text.

### Practical Applications
- **Cybersecurity**: Understanding encoding and steganography techniques is crucial for cybersecurity professionals. These methods can be used for both protecting sensitive information and detecting hidden data in security audits.
- **CTF Challenges**: Capture The Flag (CTF) competitions often include challenges that require knowledge of encoding schemes and steganography. Tools like InvisibleInk can help participants practice and develop their skills.

### Example

1. Encode a Hidden String:

```shell
python3 InvisibleInk.py encode-visible-with-hidden "This is a test" "hidden" combined_output.txt
```

2. Encode a Visible String with Hidden Unicode:

```shell
python3 InvisibleInk.py encode-visible-with-hidden "This is a test" "hidden" combined_output.txt
```

3. Decode a File:

```shell
python invisibleink.py decode-file combined_output.txt
```

### License/Contributions

**See the top-level `README.md` for project information.**

## Disclaimer
 
 - **This script is an independent contributtion by [Alec Akin (rainmana)](https://github.com/rainmana). All opinions are my (Alec's) own and do not represent those of my employer.**