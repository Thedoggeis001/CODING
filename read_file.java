import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class TextFileReader {

    public static void main(String[] args) {
        System.out.println("--- TEXT FILE READER ---");

        // 1. Get the program directory (where the .class or .jar is located)
        String programDir = System.getProperty("user.dir");

        // 2. Ask the user for the filename
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the name of the text file (e.g., myfile.txt): ");
        String requestedFilename = input.nextLine();

        // 3. Build the full path
        String fullPath = programDir + File.separator + requestedFilename;
        System.out.println("Looking for the file at: " + fullPath);

        File file = new File(fullPath);

        try (Scanner fileReader = new Scanner(file, "UTF-8")) {
            System.out.println("\n--- Content of '" + requestedFilename + "' ---\n");

            // 4. Read and print the file line by line
            while (fileReader.hasNextLine()) {
                String line = fileReader.nextLine();
                System.out.println(line);
            }

            System.out.println("\n------------------------------------");

        } catch (FileNotFoundException e) {
            // Handle missing file
            System.out.println("\n*ERROR: The file '" + requestedFilename + "' was not found in the program directory.");
            System.out.println("Program directory: " + programDir);
        } catch (Exception e) {
            // Handle any other error
            System.out.println("\n*GENERAL ERROR while reading the file: " + e.getMessage());
        }

        input.close();
    }
}
