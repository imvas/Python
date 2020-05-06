def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    c=n//k
    for i in range(0,n,k):
        b=''
        b+=string[i:i+k]
        v=''
        for j in b:
            if j not in v:
                v+=j
        print(f"{v}")
            




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
