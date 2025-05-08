from get_input_data import AoCInputHandler

# set up the data
def parse_input(input_text: str):
        left = []
        right = []
        for line in input_text.splitlines():
            if line.strip():
                parts = line.strip().split()
                if len(parts) == 2:
                    l, r = map(int, parts)
                    left.append(l)
                    right.append(r)
                else:
                    raise ValueError(f"Hibás sorformátum: '{line}'")
        return left, right

# write to file just in case [later list of filenames]
def write_to_files(left, right, left_file="left.txt", right_file="right.txt"):

    with open(left_file, "w") as f_left:
        for val in left:
            f_left.write(f"{val}\n")

    with open(right_file, "w") as f_right:
        for val in right:
            f_right.write(f"{val}\n")

def read_from_file(filenames):
    columns = []
    for i in filenames:
        with open(i, 'r') as f:
            columns.append([int(line.strip()) for line in f if line.strip()])
    return columns

# part one

def get_distance(left, right):
    if not left or not right:
        print("Üres adatlisták")
        return -1

    left, right = sorted(left), sorted(right)
    return sum([ abs(i-j) for i, j in zip(left, right)])

def get_similarity_score(left, right):

    my_dict = {i:right.count(i) for i in left}
    return sum([j*v for j, v in my_dict.items()])


if __name__ == '__main__':

    """
    session = input("Illeszd be az Advent of Code session azonosítód: ").strip()
    day = 1
    handler = AoCInputHandler(session)    
    l, r = parse_input(handler.fetch_input(day))
    """
    columns = read_from_file(["left.txt", "right.txt"])
    l, r = columns[0], columns[1]
    # part one
    print(f'The sum of the distance of the two lists: {get_distance(l, r)}')
    # part two
    print(f'The similarity score of the lists: {get_similarity_score(l, r)}')