# CTF Challenge - Hidden-in-Plain-Hex

##### Author: aalex954
##### Category: Steganography / Encoding
##### Use knowledge of Unicode, encoding schemes, and tools like CyberChef to extract the hidden information.

```bash
"The spaces between󠁨󠁴󠁴󠁰󠀺󠀯󠀯󠁴󠁩󠁮󠁹󠁵󠁲󠁬󠀯󠀳󠁰󠁡󠁭󠁨󠁲󠁷󠀲 words hold the weight of untold stories."
```



<img src="https://github.com/user-attachments/assets/a49ae7f7-2b33-4332-a08d-fe9d7b98b4d6" alt="there should be an image here..... :( " style="width:70%; height:70%;">



## Wait❗❗❗ Spoiler Alert❗❗❗   🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻

<details>
  <summary>Click to reveal full solution</summary>

---

## Challenge Overview
This challenge revolves around identifying and decoding a URL hidden within Unicode "invisible" tag characters. These characters, part of the Unicode range for tag representations, are not typically rendered as visible text and often go unnoticed in standard displays. 
At first glance, the provided data appears as a sequence of meaningless Unicode code points, with no immediately apparent structure or significance. However, careful observation reveals that these characters follow a distinct pattern, hinting at a deeper layer of obfuscation.

The use of these "invisible" Unicode characters takes advantage of their non-rendering properties, making the data seem irrelevant or empty.

This level of obfuscation requires participants to think beyond typical encoding schemes, recognizing that the key to solving the challenge lies in interpreting the seemingly meaningless symbols.
Such scenarios may mimic real-world adversarial tactics, where attackers can embed malicious or sensitive data in unconventional formats to evade detection.

---

## Challenge String

```
0e0068 0e0074 0e0074 0e0070 0e003a 0e002f 0e002f 0e0074 0e0069 0e006e 0e0079 0e0075 0e0072 0e006c 0e002f 0e0033 0e0070 0e0061 0e006d 0e0068 0e0072 0e0077 0e0032
```

See...or __don't__ ```invisible_string.txt```

---

## Solution Overview

The provided sequence consists of Unicode code points within the range of "invisible" or "tag" characters, commonly used for technical or metadata purposes. These characters fall under the Unicode range U+E0000 to U+E007F, a reserved space specifically for tag characters. These are not intended to display as human-readable text and are often ignored by rendering systems, making them an ideal candidate for encoding information discreetly.

Each code point in the sequence starts with a common prefix (0e00), indicating its membership in this specialized Unicode range. This prefix serves as a structural indicator, while the trailing hexadecimal digits hold the encoded data. When the prefix is stripped, the remaining values correspond directly to ASCII characters, which are the building blocks of readable text.

In this context, the challenge utilizes this obfuscation technique to hide a URL. While the sequence appears meaningless at first glance, its structure provides the key to decoding:

**Pattern Recognition:** Observing the consistent 0e00 prefix hints at a systematic encoding scheme.

**Stripping the Prefix:** Removing 0e00 reveals a sequence of standard hexadecimal values.

**Hexadecimal to ASCII Conversion:** The resulting hex values map directly to ASCII characters, reconstructing the URL.

The solution highlights the need for an analytical approach, where understanding the encoding scheme unlocks the hidden information. 
This challenge demonstrates how unconventional Unicode ranges, often overlooked due to their technical nature, can be leveraged for creative obfuscation. It also reinforces the importance of familiarity with encoding standards and the ability to apply decoding techniques effectively in security and forensic contexts.

## Solution

<details>
  <summary>Click to reveal full solution</summary>

In this variation of the challenge, the invisible string is embedded within a quote, disguised as "blank spaces" between words. 
These spaces are not ordinary whitespace characters but encoded Unicode "invisible" characters (e.g., tag characters). 
To extract and decode the hidden message, we can use CyberChef, a powerful and user-friendly tool for data analysis and manipulation. 

Here's how:

1. Copy the suspicious text and paste it in to Cyber Chef.
2. Escape the string to reveal the Unicode.

![image](https://github.com/user-attachments/assets/484bd0e1-a6f4-457c-a626-242159ebef08)

![image](https://github.com/user-attachments/assets/8e64782d-549f-46cc-97b9-763dd5a92cd7)

```
(\u{e0068}\u{e0074}\u{e0074}\u{e0070}\u{e003a}\u{e002f}\u{e002f}\u{e0074}\u{e0069}\u{e006e}\u{e0079}\u{e0075}\u{e0072}\u{e006c}\u{e002f}\u{e0033}\u{e0070}\u{e0061}\u{e006d}\u{e0068}\u{e0072}\u{e0077}\u{e0032})
```

and cleaned up a bit..

![image](https://github.com/user-attachments/assets/c9cfafd8-66ce-42b9-ad3a-aad0b847bec4)

![image](https://github.com/user-attachments/assets/f376a43d-94af-4100-b9ad-c2713b893025)


``` 
e0068  e0074  e0074  e0070  e003a  e002f  e002f  e0074  e0069  e006e  e0079  e0075  e0072  e006c  e002f  e0033  e0070  e0061  e006d  e0068  e0072  e0077  e0032
```

---

At first, the sequence might seem random, but two key observations lead to progress:
1. All codes start with `e00`, which is a clue that they fall under the Unicode **tag character** range.
2. Stripping the `E00` prefix from each code left standard hexadecimal values corresponding to ASCII characters.

``` 68  74  74  70  3a  2f  2f  74  69  6e  79  75  72  6c  2f  33  70  61  6d  68  72  77  32 ```

3. Convert Each Hexadecimal Value to Decimal:
  - 68 (hexadecimal) → 104 (decimal)
4. Map the Decimal Value to the ASCII Table:
  - Using the ASCII table, we find that the decimal value 104 corresponds to the character h. Repeating this process for the remainder of the sequence yields a readable string.
5. Apply this process to the remainder of the string:

```
0e0068 → h
0e0074 → t
0e0074 → t
0e0070 → p
0e003a → :
0e002f → /
0e002f → /
0e0074 → t
0e0069 → i
0e006e → n
0e0079 → y
0e0075 → u
0e0072 → r
0e006c → l
0e002f → /
0e0033 → 3
0e0070 → p
0e0061 → a
0e006d → m
0e0068 → h
0e0072 → r
0e0077 → w
0e0032 → 2
```

fix the URL and you have the final result!

</details>
</details>
