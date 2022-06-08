from re import findall
needed_list = [findall("WFLYSRV.*signal$", line) for line in [line.strip() for line in open("server.log.2018-04-05")] if findall("WFLYSRV.*signal$", line)]
print(*needed_list, f"{len(needed_list)} matches", sep='\n')
