def palindrom(inp_string):
    arr =[]
    for i in range(len(inp_string)):
        arr.append(inp_string[i])
        for j in range(len(inp_string) - 1, i, -1):
            if i == 0:
                if inp_string[i:j+1] == inp_string[j::-1]:
                    arr.append(inp_string[i:j+1])
            else:
                if inp_string[i:j+1] == inp_string[j:i-1:-1]:
                    arr.append(inp_string[i:j+1])


    return max(arr, key=len)

print(palindrom("programming"))