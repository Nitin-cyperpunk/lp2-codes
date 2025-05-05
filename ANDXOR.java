public class Andxor { 
    public static void main(String[] args) { 
        String str = "Hello World";  // Fixed string "Hello World" 
 
        System.out.println("\nCharacter | ASCII  | AND with 127 | XOR with 127"); 
        System.out.println("-------------------------------------------------"); 
        for (int i = 0; i < str.length(); i++) { 
            char c = str.charAt(i); 
            int ascii = (int) c; 
            int andResult = c & 127; 
            int xorResult = c ^ 127; 
            System.out.printf("    %2c   |  %5d |      %5d   |      %d\n", c, ascii, andResult, xorResult); 
        } 
    } 
}