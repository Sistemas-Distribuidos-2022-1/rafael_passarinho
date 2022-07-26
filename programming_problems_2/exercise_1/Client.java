import java.io.*;
import java.net.*;
import java.util.*;
  
// Client class
class Client {
    
    // driver code
    public static void main(String[] args)
    {
        // establish a connection by providing host and port
        // number
        try (Socket socket = new Socket("localhost", 1234)) {
            
            // writing to server
            PrintWriter out = new PrintWriter(
                socket.getOutputStream(), true);
  
            // reading from server
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
  
            // object of scanner class
            Scanner sc = new Scanner(System.in);
            
            
            //reading from user
            System.out.println("Nome:");
            String name = sc.nextLine();

            System.out.println("Posição: ");
            String position = sc.nextLine();

            System.out.println("Salário:");
            String salary = sc.nextLine();

            String line = position + " " + salary;
            //sending the user input to server
            out.println(line);
            out.flush();

            //displaying server reply
            System.out.println(name + " - Salário reajustado: " + in.readLine());
            
            sc.close();
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}