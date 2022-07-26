package rafael_passarinho.programming_problems_2.exercise_7;

import java.io.*;
import java.net.*;
import java.util.*;

//Client class
public class Client {
    //driver code
    public static void main(String[] args) {
        //stablish a connection by providing host and port number
        try(Socket socket = new Socket("localhost", 1234)){

            //writing to server
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            //reading from server
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            //object of scanner class
            Scanner sc = new Scanner(System.in);

            //reading from user
            System.out.println("Idade: ");
            String age = sc.nextLine();
            System.out.println("Tempo de serviço:");
            String service_time = sc.nextLine();
            
            String line = age + " " + service_time;
            //sending the user input to server
            out.println(line);
            out.flush();
            
            //displaying server reply
            System.out.print(in.readLine());

            sc.close();
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
