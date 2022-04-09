from onp import translate_to_onp

def main():
    equation = input("Enter equation: ")
    result = translate_to_onp(equation)
    print(f"Your equation as ONP: {result}")

if __name__ == "__main__":
    main()
