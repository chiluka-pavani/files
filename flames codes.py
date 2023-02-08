def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    common_letters = set(name1) & set(name2)
    num_common_letters = sum(min(name1.count(char), name2.count(char)) for char in common_letters)
    
    flames = "FLAMES"
    while len(flames) > 1:
        count = (num_common_letters % len(flames)) - 1
        if count >= 0:
            flames = flames[count + 1:] + flames[:count]
        else:
            flames = flames[:len(flames) - 1]
    
    return flames

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
result = flames_game(name1, name2)

if result == "F":
    print("Friendship")
elif result == "L":
    print("Love")
elif result == "A":
    print("Affection")
elif result == "M":
    print("Marriage")
elif result == "E":
    print("Enemy")
elif result == "S":
    print("Siblings")