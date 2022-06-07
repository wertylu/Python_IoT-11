import re as regex
if __name__ == '__main__':
    needed_list = list()
    with open("server.log.2018-04-05") as input_file:
        list_lines = [line.strip() for line in input_file.readlines()]
    for line in list_lines:
        line_needed = (regex.findall("WFLYSRV.*signal$", line))
        if line_needed:
            needed_list.append(line_needed)
    for match in needed_list:
        print(match)
    counter = len(needed_list)
    print(f"{counter} matches")
