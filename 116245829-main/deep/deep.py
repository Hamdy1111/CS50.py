great=input("What is the Answer to the Great Question of Life, the Universe, and Everything ? ")
great=great.lower().replace("-"," ").strip()
#great=great.replace("-"," ")
#great=great.strip()
if great=="42" or great=="forty two":
    print("Yes")
else:
    print("No")
