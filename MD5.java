import java.security.MessageDigest; 
import java.security.NoSuchAlgorithmException; 
import java.math.BigInteger; 
import java.util.Scanner; 
public class MD5 { 
    public static String getMD5Hash(String input) { 
        try {            // Create an instance of MessageDigest with MD5 algorithm 
            MessageDigest md = MessageDigest.getInstance("MD5"); 
            // Convert input string to bytes and compute hash 
            byte[] messageDigest = md.digest(input.getBytes()); 
            // Convert byte array into a hexadecimal representation 
            BigInteger no = new BigInteger(1, messageDigest); 
            String hashText = no.toString(16); 
            // Ensure the hash is 32 characters long by adding leading zeros if needed 
            while (hashText.length() < 32) { 
                hashText = "0" + hashText; 
            }            return hashText; 
        } catch (NoSuchAlgorithmException e) { 
            throw new RuntimeException(e); 
        }    } 
    public static void main(String[] args) { 
        Scanner scanner = new Scanner(System.in); 
         System.out.print("Enter a string to hash using MD5: "); 
        String input = scanner.nextLine(); 
        String hash = getMD5Hash(input); 
        System.out.println("MD5 Hash: " + hash); 
        scanner.close();    }}