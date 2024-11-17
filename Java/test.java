import java.util.*;


public class test{
    public static boolean multipleof(int num){
        if(num%3 == 0 || num%5 == 0){
            return true;
        }
        return false;
    }
    public static void main(String[] args){
        Scanner inp = new Scanner(System.in);
        System.out.println("Enter a number:");
        int num = inp.nextInt();
        System.out.println(multipleof(num));
        

    }
}
