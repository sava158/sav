import java.util.Scanner;

public class CountWords{
    public static void main(String[] args){
        String[] words = new String[5];
        Scanner input = new Scanner(System.in);
        System.out.println("enter any words");
        for(int i=0; i<=5; i++){
            if(input.hasNext()){
                words[i] = input.nextLine();

            }
           // System.out.println("The user entered" + words[i].length()+ "words which are"  + words[i]);
            int finalword = words[i].length();
            System.out.println(words[i].length());

        }
    }
}