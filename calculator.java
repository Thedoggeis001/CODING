import java.util.Scanner;

public class SimpleCalculator {

    // ---------------------- BASIC OPERATIONS ----------------------

    public static double addition(double x, double y) {
        return x + y;
    }

    public static double subtraction(double x, double y) {
        return x - y;
    }

    public static double multiplication(double x, double y) {
        return x * y;
    }

    public static String division(double x, double y) {
        if (y == 0) {
            // *Correction: Handle division by zero
            return "Error: Division by zero is not allowed!";
        }
        return String.valueOf(x / y);
    }

    // ---------------------- MAIN PROGRAM ----------------------

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("WELCOME TO THE SIMPLE CALCULATOR");
        System.out.println("Choose an operation:");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");

        while (true) {
            System.out.print("Enter your choice (1/2/3/4): ");
            String choice = input.nextLine();

            if (choice.equals("1") || choice.equals("2") || choice.equals("3") || choice.equals("4")) {
                double num1, num2;

                try {
                    System.out.print("Enter the first number: ");
                    num1 = Double.parseDouble(input.nextLine());

                    System.out.print("Enter the second number: ");
                    num2 = Double.parseDouble(input.nextLine());
                } catch (NumberFormatException e) {
                    // *Correction: Handle invalid numeric input
                    System.out.println("Invalid input. Please enter a valid number.\n");
                    continue;
                }

                String result;
                switch (choice) {
                    case "1":
                        result = String.valueOf(addition(num1, num2));
                        break;
                    case "2":
