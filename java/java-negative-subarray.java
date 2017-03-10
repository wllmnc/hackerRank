//https://www.hackerrank.com/challenges/java-negative-subarray
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        int arr[] = new int[n];
        for(int i=0; i < n; i++){
                arr[i] = in.nextInt();
        }
        int bound=1;
        int ans=0;
        while(bound<=n)
        {
            for(int i=0; i < n; i++){
                int index=i;
                int val=0;
                while(index<i+bound && i+bound<=n)
                {
                    val+=arr[index];
                    index++;
                }
                if(val<0)
                    ans++;
            }
            bound++;
        }
        System.out.println(ans);
        
        
    }
}
