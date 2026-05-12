import java.rmi.*;

public interface MyIntf extends Remote {
    String concat(String a, String b) throws RemoteException;
}