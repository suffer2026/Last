import java.rmi.*;
import java.util.*;

public class Client {
    public static void main(String[] args) throws Exception {

        MyIntf obj = (MyIntf) Naming.lookup("rmi://localhost/obj");
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter 2 strings: ");
        String a = sc.nextLine();
        String b = sc.nextLine();

        System.out.println("Result: " + obj.concat(a, b));
    }
}