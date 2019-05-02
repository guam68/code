import java.util.Scanner;

public class hello {
    public static void main(String[] args) {
        // Basic string stuff
        System.out.println("Testing ...\n\t... 1 ..." +
            "\n\t\t... 2 ...\n\t\t\t... 3 ...");


        // user input, while loop, conditional
        Scanner scanner = new Scanner(System.in);

        int num = 0;
        int count = 0;

        System.out.print("Enter a number: ");
        num = scanner.nextInt();

        while (num > 46340) {
            if (count >= 3) {
                System.out.print("Enter a number less than 46341: ");
                num = scanner.nextInt();
            }
            else {
                System.out.println();
                System.err.print("Number is too large! Enter another number: ");
                num = scanner.nextInt();
            }
            count++;
        }
        scanner.close();

        int square = num * num;
        System.out.println("The square is:\t\t" + square);

    }
}