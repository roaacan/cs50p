def main():
    # Ask user for expression +, *, -, /
    expression = input("Expression: ").strip()

    # Get operator and values
    x, operator, y = expression.split()

    # Solving expression
    result = 0
    match operator:
        case "+":
            result = float(x) + float(y)
        case "-":
            result = float(x) - float(y)
        case "*":
            result = float(x) * float(y)
        case "/":
            result = float(x) / float(y)
    print(result)


main()