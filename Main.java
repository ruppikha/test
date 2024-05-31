import java.io.FileWriter;
import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        if (args.length > 0) {
            String name = args[0];
            System.out.println("Hello, " + name + "! This is a test Java file.");
        } else {
            System.out.println("No name provided. This is a test Java file.");
        }
    }
}
