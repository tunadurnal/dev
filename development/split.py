def splitFile(filename, n):
    with open(filename) as f:
        data = f.readlines()
        fileLength = len(data)

    num_of_files = fileLength // n
    for i in range(num_of_files):
        with open(filename+str(i), 'w') as f:
            if i == num_of_files - 1: f.writelines(data)
            else:
                f.writelines(data[:n])
                del data[:n]

splitFile('SplitME', 25)