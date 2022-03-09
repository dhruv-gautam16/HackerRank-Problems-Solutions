def mutate_string(string, position, character):
   
    pos = position+1
    Output = string[:position]+character+string[pos:]
    return Output

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)