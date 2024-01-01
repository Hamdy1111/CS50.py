def main():
    in_put=input("Input: ")
    ruselt=shorten(in_put)
    print("Output:",ruselt)

def shorten(word):
    vowels={'a','A','e','E','i','I','o','O','u','U'}
    out_put=''
    for c in word:
        if c not in vowels :
           out_put+=c
    return out_put

if __name__ == "__main__":
    main()
