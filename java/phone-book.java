//https://www.hackerrank.com/challenges/phone-book
import java.util.*;
import java.io.*;

class Solution{
   public static void main(String []argh)
   {
      Scanner in = new Scanner(System.in);
      Map<String, Integer> m = new HashMap<String, Integer>();
      int n=in.nextInt();
      in.nextLine();
      for(int i=0;i<n;i++)
      {
         String name=in.nextLine();
         int phone=in.nextInt();
         m.put(name,phone);
         in.nextLine();
      }
      while(in.hasNext())
      {
         String s=in.nextLine();
         if(m.get(s)!=null)
         {
             System.out.println(s+"="+m.get(s));
         }else{
             System.out.println("Not found");
         }
      }
   }
}
