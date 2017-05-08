//https://www.hackerrank.com/challenges/pattern-syntax-checker
import java.util.Scanner;
import java.util.regex.*;


public class Solution
{
   public static void main(String[] args){
      Scanner in = new Scanner(System.in);
      int testCases = Integer.parseInt(in.nextLine());
      while(testCases>0){
          try{
          String pattern = in.nextLine();
           try{
                Pattern r = Pattern.compile(pattern);
               System.out.println("Valid");
           }catch(Exception  ex)
           {
               System.out.println("Invalid");
           }
          }catch(Exception  NoSuchElementException)
          {
              testCases=0;
          }
      }
   }
}
