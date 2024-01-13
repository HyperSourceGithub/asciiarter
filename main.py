def generate_ascii_art(text, font='default'):
    # Define ASCII art characters for each letter in the "default" font
    default_font = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        'B': ["BBBB  ", "B   B ", "BBBB  ", "B   B ", "BBBB  "],
        'C': [" CCCC ", "C     ", "C     ", "C     ", " CCCC "],
        'D': ["DDDD  ", "D   D ", "D   D ", "D   D ", "DDDD  "],
        'E': ["EEEEE ", "E     ", "EEEEE ", "E     ", "EEEEE "],
        'F': ["FFFFF ", "F     ", "FFFFF ", "F     ", "F     "],
        'G': [" GGGG ", "G     ", "G  GGG", "G   G ", " GGGG "],
        'H': ["H   H ", "H   H ", "HHHHH ", "H   H ", "H   H "],
        'I': [" III  ", "  I   ", "  I   ", "  I   ", " III  "],
        'J': [" JJJJ ", "   J  ", "   J  ", "J  J  ", " JJ   "],
        'K': ["K   K ", "K  K  ", "KK    ", "K  K  ", "K   K "],
        'L': ["L     ", "L     ", "L     ", "L     ", "LLLLL "],
        'M': ["M   M ", "MM MM ", "M M M ", "M   M ", "M   M "],
        'N': ["N   N ", "NN  N ", "N N N ", "N  NN ", "N   N "],
        'O': [" OOO  ", "O   O ", "O   O ", "O   O ", " OOO  "],
        'P': ["PPPP  ", "P   P ", "PPPP  ", "P     ", "P     "],
        'Q': [" QQQ  ", "Q   Q ", "Q Q Q ", "Q  QQ ", " QQ Q "],
        'R': ["RRRR  ", "R   R ", "RRRR  ", "R R   ", "R  RR "],
        'S': [" SSS  ", "S     ", " SSS  ", "    S ", "SSSS  "],
        'T': ["TTTTT ", "  T   ", "  T   ", "  T   ", "  T   "],
        'U': ["U   U ", "U   U ", "U   U ", "U   U ", " UUU  "],
        'V': ["V   V ", "V   V ", "V   V ", " V V  ", "  V   "],
        'W': ["W   W ", "W   W ", "W W W ", "WW WW ", "W   W "],
        'X': ["X   X ", " X X  ", "  X   ", " X X  ", "X   X "],
        'Y': ["Y   Y ", " Y Y  ", "  Y   ", "  Y   ", "  Y   "],
        'Z': ["ZZZZZ ", "   Z  ", "  Z   ", " Z    ", "ZZZZZ "],
    }

    # Define ASCII art characters for each letter in the "special" font
    special_font = {
        'A': ["  |  ", " / \\ ", "/___\\", "|   |", "|   |"],
        'B': ["/---  ", "|   \\ ", "|---- ", "|   / ", "|___  "],
        'C': ["  __  ", " /   ", "|    ", "|    ", " \\__ "],
        'D': ["---\\ ", "|   |", "|   |", "|   |", "|___/"],
        'E': ["/----", "|    ", "|--- ", "|    ", "|___ "],
        'F': ["/----", "|    ", "|--- ", "|    ", "|    "],
        'G': ["  __  ", " /   ", "| __ ", "|  / ", " \\_\\ "],
        'H': ["|   |", "|---|", "|   |", "|   |", "|   |"],
        'I': [" | | ", "  |  ", "  |  ", "  |  ", " | | "],
        'J': ["   /", "  / ", " |  ", " |  ", "\\__ "],
        'K': ["|    ", "|  / ", "|/   ", "| \\  ", "|   \\ "],
        'L': ["|    ", "|    ", "|    ", "|    ", "|___ "],
        'M': ["|   |", "|\\^/|", "| V |", "|   |", "|   |"],
        'N': ["\\   |", " \\  |", "  \\ |", "   \\|", "    \\"],
        'O': ["  __  ", " /  \\ ", "|    |", "|    |", " \\__/ "],
        'P': ["/---\\ ", "|   | ", "|---  ", "|     ", "|     "],
        'Q': ["  __  ", " /  \\ ", "|    |", "|  \\_|", " \\__\\ "],
        'R': ["/---\\ ", "|   | ", "|---  ", "|  \\  ", "|   \\ "],
        'S': [" \\__ ", "/    ", "\\__  ", "    |", "\\___ "],
        'T': ["-----", "  |  ", "  |  ", "  |  ", "  |  "],
        'U': ["|   |", "|   |", "|   |", "|   |", " \\_/ "],
        'V': ["|   |", "|   |", "|   |", " \\_/ ", "  |  "],
        'W': ["|   |", "|   |", "| | |", "| V |", "| | |"],
        'X': ["\\   /", " \\_/ ", " / \\ ", "/   \\", "\\___/"],
        'Y': ["\\   /", " \\_/ ", "  |  ", "  |  ", "  |  "],
        'Z': ["-----", "   / ", "  /  ", " /   ", "-----"],
    }

    # Define ASCII art characters for each letter in the "decorative" font
    decorative_font = {
        'A': [" /\\ ", "/__\\", "|  |", "|  |", "|  |"],
        'B': ["||/\\", "||\\_", "|| \\_", "||_/ ", "||/\\ "],
        'C': ["|__/ ", "|    ", "|    ", "|    ", "|__/ "],
        'D': ["||/\\", "||  \\", "||   \\", "||   |", "||__/"],
        'E': ["|||__", "||   ", "||__ ", "||   ", "|||__"],
        'F': ["|||__", "||   ", "||__ ", "||   ", "||   "],
        'G': [" ||_", "|    ", "| __ ", "|  | ", "|__| "],
        'H': ["||   ", "||___", "||  |", "||  |", "||  |"],
        'I': ["_  _", " \\/ ", " /\\ ", " || ", " \\/ "],
        'J': [" ___", "  | ", "  | ", " _] ", "[__ "),
        'K': ["||   ", "||__ ", "||  \\", "||  /", "||   \\"],
        'L': ["||   ", "||   ", "||   ", "||   ", "||___"],
        'M': ["||| |", "||_||", "|| | ", "|| | ", "|| | "],
        'N': ["||   ", "||\\  ", "|| \\ ", "||  \\", "||   \\"],
        'O': [" || ", "/  \\", "|  | ", "|  | ", " \\_/ "],
        'P': ["||\\ ", "|| \\_", "||  |", "||   ", "||   "],
        'Q': [" || ", "/  \\", "|  | ", "|  | ", " \\_\\ "],
        'R': ["||\\ ", "|| \\_", "||  \\", "||   \\", "||   \\"],
        'S': [" |_", "/   ", "\\__ ", "    |", "|__/ "],
        'T': ["|||||", " || ", " || ", " || ", " || "],
        'U': ["||   ", "||   ", "||   ", "||   ", " \\_/ "],
        'V': ["||   ", "||   ", "||   ", " \\_/ ", "  |  "],
        'W': ["|| | ", "|| | ", "||/\\ ", "||/ |", "|| | "],
        'X': ["/\\  /\\", "  \\/  ", "  /\\  ", " /  \\ ", "/    \\"],
        'Y': ["||   ", "||   ", "|||  ", " || ", " || "],
        'Z': ["|||||", "   / ", "  /  ", " /   ", "|||||"],
    }

    # Select the appropriate font
    selected_font = default_font if font == 'default' else special_font if font == 'special' else decorative_font

    # Convert input text to uppercase
    text = text.upper()

    # Initialize empty lines for each row of ASCII art
    lines = [""] * 5  # Assuming each character is 5 lines tall

    # Generate ASCII art for each character in the input text
    for char in text:
        if char in selected_font:
            char_art = selected_font[char]
            for i in range(5):  # Assuming each character is 5 lines tall
                lines[i] += char_art[i] + "   "  # Add three spaces between characters

    # Print the generated ASCII art
    for line in lines:
        print(line)

# Example usage with the "default" font:
generate_ascii_art("HELLO")
print("\n")

# Example usage with the "special" font:
generate_ascii_art("HELLO", font='special')
print("\n")

# Example usage with the "decorative" font:
generate_ascii_art("HELLO", font='decorative')
