import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        problem190();
    }

    static void problem190(){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int geleia = 0, tradicional = 0;
        for (int i = 0; i < n; i++) {
            int x = scanner.nextInt();
            if (x == 11) {
                geleia++;
            } else {
                tradicional++;
            }
        }
        if (geleia >= tradicional) {
            System.out.println("Geleia");
        } else {
            System.out.println("Tradicional");
        }
    }
}