import java.util.Scanner;

public class encrypt {

    public static String encrypt(String text, int key) {
        text = text.replaceAll("\\s+", "");
        char[][] rail = new char[key][text.length()];
        int row = 0, dir = 1;

        for (int col = 0; col < text.length(); col++) {
            rail[row][col] = text.charAt(col);
            row += (row == 0) ? 1 : (row == key - 1) ? -1 : dir;
        }

        StringBuilder result = new StringBuilder();
        for (char[] r : rail)
            for (char c : r)
                if (c != 0) result.append(c);
        return result.toString();
    }

    public static String decrypt(String cipher, int key) {
        char[][] rail = new char[key][cipher.length()];
        int row = 0, dir = 1;

        // Marking
        for (int col = 0; col < cipher.length(); col++) {
            rail[row][col] = '*';
            row += (row == 0) ? 1 : (row == key - 1) ? -1 : dir;
        }

        // Filling
        int index = 0;
        for (int i = 0; i < key; i++)
            for (int j = 0; j < cipher.length(); j++)
                if (rail[i][j] == '*') rail[i][j] = cipher.charAt(index++);

        // Reading
        StringBuilder result = new StringBuilder();
        row = 0;
        for (int col = 0; col < cipher.length(); col++) {
            result.append(rail[row][col]);
            row += (row == 0) ? 1 : (row == key - 1) ? -1 : dir;
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text: ");
        String text = sc.nextLine();
        System.out.print("Enter number of rails: ");
        int key = sc.nextInt();

        String encrypted = encrypt(text, key);
        System.out.println("Encrypted: " + encrypted);
        System.out.println("Decrypted: " + decrypt(encrypted, key));
        sc.close();
    }
}
