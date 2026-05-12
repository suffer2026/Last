import java.rmi.*;
import java.util.*;

public interface Hotel extends Remote {
    String book(String name) throws RemoteException;
    String cancel(String name) throws RemoteException;
    List<String> getBooked() throws RemoteException;
    List<String> getCancelled() throws RemoteException;
}