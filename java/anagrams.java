#https://www.hackerrank.com/challenges/java-anagrams
import java.io.*;
import java.util.*;

public class Solution {

   static boolean isAnagram(String A, String B){
       if (A.length()==B.length()) 
       {
            A=A.toUpperCase();
            B=B.toUpperCase();
            for(int i=0;i<A.length();i++)
            { 
                int index=B.indexOf(A.charAt(i));
                if (index>=0)
                B=B.substring(0, index) + B.substring(index+1);
            }
            if(B.length()>0)
                return false;
            else
                return true;
       }else{
                return false;
            }
   }
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        boolean ret=isAnagram(A,B);
        if(ret)System.out.println("Anagrams");
        else System.out.println("Not Anagrams");
        
    }
}
