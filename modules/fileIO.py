import os

## returns list of each line inside file
def get_line_list(filename: str) -> list[str]:
    try:
        file = open(filename, "r")
        lines = list()
        for line in file:
            lines.append(line.strip())
        file.close()
        return lines
    except IOError:
        print(f"Failed to open {filename}")
        return list()

## creates/overwrites file with provided data
def write_file(filename: str, data: str) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    file = open(filename, "w")
    file.write(data)
    file.close()

def main():
    write_file("output.log",str(get_line_list("url.in")))

if __name__=="__main__":
    main()