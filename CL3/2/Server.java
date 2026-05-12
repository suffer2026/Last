import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;

public class Server extends UnicastRemoteObject implements MyIntf {

    Server() throws RemoteException {}

    public String concat(String a, String b) {
        return a + b;
    }

    public static void main(String[] args) throws Exception {
        LocateRegistry.createRegistry(1099);
        Naming.rebind("rmi://localhost/obj", new Server());
        System.out.println("Server running...");
    }
}