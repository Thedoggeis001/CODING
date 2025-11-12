import java.util.Scanner;

public class SimpleCalculator {

    // Addition
    public static double addition(double x, double y) {
        return x + y;
    }

    // Subtraction
    public static double subtraction(double x, double y) {
        return x - y;
    }

    // Multiplication
    public static double multiplication(double x, double y) {
        return x * y;
    }

    // Division (handles division by zero)
    public static String division(double x, double y) {
        if (y == 0) {
            return "Error: Division by zero is not allowed!";
        }
        return String.valueOf(x / y);
    }

    // ---------------------------------------------------------------
    // MAIN PROGRAM
    // ---------------------------------------------------------------
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("WELCOME TO THE SIMPLE CALCULATOR");
        System.out.println("Choose an operation:");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");

        while (true) {
            System.out.print("\nEnter your choice (1/2/3/4): ");
            String choice = input.nextLine();

            if (choice.equals("1") || choice.equals("2") || choice.equals("3") || choice.equals("4")) {
                try {
                    System.out.print("Enter the first number: ");
                    double num1 = Double.parseDouble(input.nextLine());

                    System.out.print("Enter the second number: ");
                    double num2 = Double.parseDouble(input.nextLine());

                    String result;

                    switch (choice) {
                        case "1":
                            result = String.valueOf(addition(num1, num2));
                            break;
                        case "2":
                            result = String.valueOf(subtraction(num1, num2));
                            break;
                        case "3":
                            result = String.valueOf(multiplication(num1, num2));
                            break;
                        case "4":
                            result = division(num1, num2);
                            break;
                        default:
                            result = "Invalid operation.";
                    }

                    System.out.println("\nThe result is: " + result + "\n");

                    // Ask if the user wants to continue
                    System.out.print("Do you want to perform another calculation? (yes/no): ");
                    String next = input.nextLine().trim().toLowerCase();

                    if (!next.equals("yes") && !next.equals("y")) {
                        break;
                    }

                } catch (NumberFormatException e) {
                    System.out.println("Invalid input. Please enter numeric values only.");
                }

            } else {
                System.out.println("Invalid choice. Please enter a number from 1 to 4.");
            }
        }

        System.out.println("Calculator closed. Goodbye!");
        input.close();
    }
}
