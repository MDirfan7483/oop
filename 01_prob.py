f = open("poeam.txt")
content = f.read()
if ("twinkle" in content):
    print(" there exist that word")
else:
    print("there does not exist that word")

f.close()