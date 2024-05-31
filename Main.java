import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        if (args.length > 0) {
            String name = args[0];
            System.out.println("Hello, " + name + "! This is a test Java file.");
            generateHtmlFile(name);
        } else {
            System.out.println("No name provided. This is a test Java file.");
        }
    }

    private static void generateHtmlFile(String name) {
        String htmlContent = "<!DOCTYPE html>" +
                "<html lang=\"en\">" +
                "<head>" +
                "    <meta charset=\"UTF-8\">" +
                "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">" +
                "    <title>Java Application Output</title>" +
                "</head>" +
                "<body>" +
                "    <h1>Java Application Output</h1>" +
                "    <div id=\"output\">" +
                "        <p>Hello, " + name + "!</p>" +
                "    </div>" +
                "</body>" +
                "</html>";

        try (FileWriter fileWriter = new FileWriter("docs/index.html")) { 
            fileWriter.write(htmlContent);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
