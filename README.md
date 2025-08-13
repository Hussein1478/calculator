# Simple Calculator Program

A basic Python calculator that performs fundamental mathematical operations on two numbers.

## Description

This is a simple command-line calculator program written in Python that allows users to perform basic arithmetic operations. The program prompts the user for two numbers and a mathematical operation, then displays the result in a clear format.

## Features

- ✅ Addition (+)
- ✅ Subtraction (-)
- ✅ Multiplication (*)
- ✅ Division (/)
- ✅ Error handling for invalid inputs
- ✅ Division by zero protection
- ✅ Support for decimal numbers
- ✅ User-friendly interface

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/simple-calculator.git
```

2. Navigate to the project directory:
```bash
cd simple-calculator
```

## Usage

Run the program using Python:

```bash
python calculator.py
```

### Example Usage

```
Welcome to the Simple Calculator!
Available operations: +, -, *, /
------------------------------
Enter the first number: 10
Enter the second number: 5
Enter the operation (+, -, *, /): +
10.0 + 5.0 = 15.0
```

### More Examples

**Addition:**
```
Enter the first number: 15.5
Enter the second number: 4.2
Enter the operation (+, -, *, /): +
15.5 + 4.2 = 19.7
```

**Division:**
```
Enter the first number: 20
Enter the second number: 4
Enter the operation (+, -, *, /): /
20.0 / 4.0 = 5.0
```

**Error Handling:**
```
Enter the first number: 10
Enter the second number: 0
Enter the operation (+, -, *, /): /
Error: Division by zero is not allowed!
```

## File Structure

```
simple-calculator/
│
├── calculator.py          # Main calculator program
└── README.md             # Project documentation
```

## How It Works

1. The program welcomes the user and displays available operations
2. Prompts for the first number (accepts integers and decimals)
3. Prompts for the second number (accepts integers and decimals)
4. Prompts for the mathematical operation (+, -, *, /)
5. Performs the calculation and displays the result
6. Handles errors gracefully with informative messages

## Error Handling

The program includes robust error handling for:

- **Invalid Numbers**: Non-numeric input for numbers
- **Division by Zero**: Prevents mathematical errors
- **Invalid Operations**: Only accepts +, -, *, /
- **Unexpected Errors**: General exception handling

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created as a basic Python programming exercise.

## Future Enhancements

Potential improvements for future versions:
- Support for more mathematical operations (power, square root, etc.)
- Memory functions (store/recall results)
- History of calculations
- GUI interface using tkinter
- Support for multiple operations in one expression
