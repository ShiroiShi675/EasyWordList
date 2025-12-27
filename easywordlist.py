def print_banner():
    print("""
███████╗ █████╗ ███████╗██╗   ██╗
██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝
█████╗  ███████║███████╗ ╚████╔╝
██╔══╝  ██╔══██║╚════██║  ╚██╔╝
███████╗██║  ██║███████║   ██║
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝

██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝

                    by ShiroiShi

  EasyWordList is a customizable wordlist generator.
  It allows you to generate combinations of letters,
  numbers and symbols.
""")

charset = "abcefghijklmnopqrstuvwxyz"
charset1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charset2 = "0123456789"
charset3 = "|!£$%&/()=?'^*°§[]@#}{¸°˘,.-;:_+<>"

finalcharset = ""
word = ""
length = 0

print_banner()
choice = input("Use lowercase letters?(y,n): ")
if(choice == "y"):
    finalcharset = charset

choice = input("Use uppercase letters?(y,n): ")
if(choice == "y"):
    finalcharset += charset1

choice = input("Use numbers?(y,n): ")
if(choice == "y"):
    finalcharset += charset2

choice = input("Use symbols?(y,n): ")
if(choice == "y"):
    finalcharset += charset3

if not finalcharset:
    print("No charset selected!")
    exit()

while True:
    length = int(input("Enter word length(Max 10): "))
    if (length <= 10 and length > 0):
        break
    else:
        print("Insert a valid length!")

print("Generating wordlist...")
indexlist = []
while(len(indexlist) < length):
    indexlist.append(0)

with open("wordlist.txt", "w") as file:
    while True:
        word = "".join(finalcharset[i] for i in indexlist)
        file.write(word + "\n")

        for i in reversed(range(length)):
            indexlist[i] += 1
            if indexlist[i] < len(finalcharset):
                break
            indexlist[i] = 0
        else:
            break

print("Wordlist generated successfully!")
