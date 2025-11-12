import java.util.Random;
import java.util.Scanner;

public class PasswordGenerator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("THIS PROGRAM WILL GENERATE A PASSWORD FOR YOU");
        System.out.print("How long do you want your password to be? (Enter an integer number): ");

        int length = 0;

        // Input validation loop
        while (true) {
            String input = scanner.nextLine();
            try {
                length = Integer.parseInt(input);
                if (length > 0) {
                    break; // valid input
                } else {
                    System.out.print("Please enter a positive integer: ");
                }
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter an integer number: ");
            }
        }

        System.out.println("\nYou chose a length of: " + length);

        // Define possible characters for the password
        String lowercase = "abcdefghijklmnopqrstuvwxyz";
        String uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String digits = "0123456789";
        String punctuation = "!@#$%^&*()-_=+[]{};:'\",.<>?/|\\`~";

        String characters = lowercase + uppercase + digits + punctuation;

        // Generate the password
        StringBuilder password = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            password.append(characters.charAt(index));
        }

        System.out.println("Your newly generated password is: " + password.toString());

        scanner.close();
    }
}
