import java.rmi.*;
import java.util.*;

public class Client {
    public static void main(String[] args) throws Exception {

        Hotel h = (Hotel) Naming.lookup("rmi://localhost/hotel");
        Scanner sc = new Scanner(System.in);

        System.out.println("1.Book  2.Cancel  3.View Booked  4.View Cancelled");
        int ch = sc.nextInt();
        sc.nextLine();

        if (ch == 1) {
            System.out.print("Enter name: ");
            System.out.println(h.book(sc.nextLine()));
        }
        else if (ch == 2) {
            System.out.print("Enter name: ");
            System.out.println(h.cancel(sc.nextLine()));
        }
        else if (ch == 3) {
            System.out.println("Booked: " + h.getBooked());
        }
        else if (ch == 4) {
            System.out.println("Cancelled: " + h.getCancelled());
        }
    }
}