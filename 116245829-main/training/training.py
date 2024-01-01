import sys

def count_lines_of_code(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        code_lines = 0
        in_comment_block = False

        for line in lines:
            stripped_line = line.strip()

            if stripped_line.startswith("'''") or stripped_line.startswith('"""'):
                in_comment_block = not in_comment_block

            if not stripped_line or stripped_line.startswith('#') or in_comment_block:
                continue

            code_lines += 1

        return code_lines

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.py'):
        print("Usage: python lines.py <filename.py>")
        sys.exit(1)

    file_path = sys.argv[1]
    lines_of_code = count_lines_of_code(file_path)

    print(f"Lines of code in '{file_path}': {lines_of_code}")
