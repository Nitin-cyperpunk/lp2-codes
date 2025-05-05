import java.math.BigInteger;
import java.util.Scanner;

public class RSA {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Step 1: Choose two primes
        BigInteger p = new BigInteger("7919");
        BigInteger q = new BigInteger("1009");
        BigInteger n = p.multiply(q);
        BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));

        // Step 2: Choose public exponent e
        BigInteger e = new BigInteger("3");
        while (!e.gcd(phi).equals(BigInteger.ONE)) e = e.add(BigInteger.ONE);

        // Step 3: Compute private key d
        BigInteger d = e.modInverse(phi);

        System.out.println("Public Key: (" + e + ", " + n + ")");
        System.out.println("Private Key: (" + d + ", " + n + ")");

        // Step 4: Encrypt
        System.out.print("Enter a number to encrypt: ");
        BigInteger m = sc.nextBigInteger();
        BigInteger c = m.modPow(e, n);
        System.out.println("Encrypted: " + c);

        // Step 5: Decrypt
        BigInteger decrypted = c.modPow(d, n);
        System.out.println("Decrypted: " + decrypted);

        sc.close();
    }
}
