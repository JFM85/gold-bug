gold_bug_p2="""53‡‡†305))6*;4826)4‡.)4‡;806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†
;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*-4)8¶8*;4069285);)
6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?3
4;48)4‡;161;:188;‡?;"""
gold_bug_p="""
==============================================================
53‡‡†305))6*;4826)4‡.)4‡;806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†
;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*-4)8¶8*;4069285);)
6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?3
4;48)4‡;161;:188;‡?;
==============================================================
"""
gold_bug="53‡‡†305))6*;4826)4‡.)4‡;806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*-4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
decode=gold_bug_p2
index_key={}
code_key={}
for char in gold_bug:
        if char not in code_key:
            code_key[char]=char

def freq_a(text):
    freq={}
    for char in gold_bug:
        if char not in freq:
            freq[char]=1
        else:
            freq[char]+=1
    freq_table=dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
    print("+-------------------------------------------------------------+")
    for y,z in freq_table.items():
      print(y," | ",z)
    print("+-------------------------------------------------------------+")
    decode_selection(input("Select other option "))

def display():
    decode=""
    for char in gold_bug_p2:
        if char in code_key and char in gold_bug:
            decode+=code_key[char]
        else:
            decode+=char
    print(decode)

def decoder():
    print("+-------------------------------------------------------------+")
    display()
    print("+-------------------------------------------------------------+")
    print("|Select an option:                                            |")
    print("|1 - Frequency Analysis                                       |")
    print("|2 - Substitution                                             |")
    print("|3 - Reset                                                    |")
    print("|4 - Back to Main                                             |")
    print("+-------------------------------------------------------------+")
    print("|Type 'menu' to go back to this menu                          |")
    print("+-------------------------------------------------------------+")
    decode_selection(input())

def substitution(character_index):
    new_char=input(f"Please, type the new character for '{index_key[character_index]}': ")
    code_key[index_key[character_index]]=new_char
    select=input("Do you wish to change another character? [Y/N] ")
    if select.lower() == "y" or select.lower() == "yes":
        solver()
    else:
        decoder()

def solver():
    print("+-------------------------------------------------------------+")
    counter=1
    for x,y in code_key.items():
        print(counter, "  ", x," = ",y)
        index_key[counter]=x
        counter+=1
    print("+-------------------------------------------------------------+")
    answer=input("Select a character: ")
    if answer.isnumeric():
        if int(answer) in range(1,counter+1):
            substitution(int(answer))
        else:
            print("Please, select a valid character")
            solver()
    else:
        print("Please, select a valid character")
        solver()
def reset():
        decode=gold_bug_p2
        for x in range(1,len(code_key)):
            code_key[index_key[x]]=index_key[x]
        decoder()

def decode_selection(choice):
    if choice == "1":
        freq_a(gold_bug)
    elif choice == "2":
        solver()
    elif choice == "3":
        reset()
    elif choice == "4":
        main()
    elif choice.lower() == "menu":
        decoder()
    else:
        decode_selection(input("Please, enter a valid option: "))

def selection_main(choice):
    if choice == "1":
        decoder()
    elif choice == "2":
        print(gold_bug_p)
        choice=input("Select other opction: ")
        selection_main(choice)
    elif choice == "3":
        leaving=input("Your progress will be lost. Are you sure you want to leave? [Y/N]\n")
        if leaving.lower() == "y" or leaving.lower() == "yes":
            quit()
        else:
            main()
    elif choice.lower() == "main":
        main()
    else:
        selection_main(input("Please, enter a valid option: "))

def main():
    """
    print("Write the code or type 'Gold-Bug'")
    choice=input()
    if choice.lower()=="gold-bug":
        decoder(gold_bug)
    else:
        decoder(choice)
        """
    print("+-----------------------------------+")
    print("|     EAP's Gold-Bug Companion      |")
    print("+-----------------------------------+")
    print("|Select an option:                  |\n|1 - Solve Code                     |\n|2 - Print Original Gold-Bug code   |\n|3 - Quit                           |")
    print("+-----------------------------------+")
    print("|Type 'main' to get to this menu    |")
    print("+-----------------------------------+")
    choice=input()
    selection_main(choice)

if __name__ == "__main__":
    main()


