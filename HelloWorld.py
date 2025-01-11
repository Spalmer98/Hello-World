import os
def main():
    if os.name == "Windows":
        os.system("Clear")
    else:
        os.system("Cls")
        
    print("\nHello World!!\n")

if __name__ == "__main__":
    main()