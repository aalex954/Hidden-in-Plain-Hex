import typer
from typing import Optional

app = typer.Typer()

# Unicode tag characters range
TAG_BASE = 0xE0000

def encode_to_hidden_unicode(input_string: str) -> str:
    """
    Encodes a string into hidden Unicode characters.
    
    Args:
        input_string (str): The string to encode.
    
    Returns:
        str: The encoded string with hidden Unicode characters.
    """
    return ''.join(chr(TAG_BASE + ord(char)) for char in input_string)

def decode_from_hidden_unicode(hidden_string: str) -> str:
    """
    Decodes a string from hidden Unicode characters.
    
    Args:
        hidden_string (str): The string with hidden Unicode characters.
    
    Returns:
        str: The decoded original string.
    """
    return ''.join(chr(ord(char) - TAG_BASE) for char in hidden_string)

@app.command()
def encode_hidden(input_string: str, output_file: str):
    """
    Encodes a string into hidden Unicode characters and writes it to a file.
    
    Args:
        input_string (str): The string to encode.
        output_file (str): The file to write the encoded string to.
    
    Example:
        python invisibleink.py encode-hidden "your hidden string" hidden_output.txt
    """
    hidden_string = encode_to_hidden_unicode(input_string)
    with open(output_file, 'w') as f:
        f.write(hidden_string)
    typer.echo(f"Hidden Unicode string written to {output_file}")

@app.command()
def encode_visible_with_hidden(visible_string: str, hidden_string: str, output_file: str):
    """
    Encodes a visible string with hidden Unicode characters between spaces and writes it to a file.
    
    Args:
        visible_string (str): The visible string.
        hidden_string (str): The string to hide within the visible string.
        output_file (str): The file to write the combined string to.
    
    Example:
        python invisibleink.py encode-visible-with-hidden "your visible string" "your hidden string" combined_output.txt
    """
    hidden_unicode = encode_to_hidden_unicode(hidden_string)
    combined_string = ""
    hidden_index = 0
    for char in visible_string:
        combined_string += char
        if char == ' ' and hidden_index < len(hidden_unicode):
            combined_string += hidden_unicode[hidden_index]
            hidden_index += 1
    # Append any remaining hidden characters at the end
    combined_string += hidden_unicode[hidden_index:]
    with open(output_file, 'w') as f:
        f.write(combined_string)
    typer.echo(f"Visible string with hidden Unicode written to {output_file}")

@app.command()
def decode_file(input_file: str):
    """
    Decodes a file to retrieve the hidden Unicode string.
    
    Args:
        input_file (str): The file containing the hidden Unicode string.
    
    Example:
        python invisibleink.py decode-file combined_output.txt
    """
    with open(input_file, 'r') as f:
        content = f.read()
    hidden_string = ''.join(char for char in content if ord(char) >= TAG_BASE)
    decoded_hidden = decode_from_hidden_unicode(hidden_string)
    typer.echo(f"Decoded hidden string: {decoded_hidden}")

if __name__ == "__main__":
    app()