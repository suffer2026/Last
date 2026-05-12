import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;
import java.util.*;

public class Server extends UnicastRemoteObject implements Hotel {

    List<String> booked = new ArrayList<>();
    List<String> cancelled = new ArrayList<>();

    Server() throws RemoteException {}

    public String book(String name) {
        if (booked.contains(name)) return "Already booked";
        booked.add(name);
        return "Booked for " + name;
    }

    public String cancel(String name) {
        if (booked.remove(name)) {
            cancelled.add(name);
            return "Cancelled for " + name;
        }
        return "Not found";
    }

    public List<String> getBooked() {
        return booked;
    }

    public List<String> getCancelled() {
        return cancelled;
    }

    public static void main(String[] args) throws Exception {
        LocateRegistry.createRegistry(1099);
        Naming.rebind("rmi://localhost/hotel", new Server());
        System.out.println("Server running...");
    }
}