import java.util.*;

import javax.sql.rowset.spi.SyncResolver;
class Firstclass {
    public static void main (String args[]) {
        /* 
        Scanner sc = new Scanner(System.in);
    
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            System.out.print(i + " ");
        }
    }
        */



        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();
        // for (int i = 0; i < n; i++) {
        //     System.out.print(i);
        //     if (i<n-1);
        //     System.out.print(" ");
        // }




        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();
        // for (int i = 0; i<n; i++){
        //     System.out.print(2*i);
        //     if (i < n - 1);
        //     System.out.print(" ");
        // }


        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();

        // for (int i = n; i >= 1; i--) {
        //     System.out.print(i + " ");
        // }





        // Scanner sc = new Scanner(System.in);
        // String str = sc.nextLine();

        // String vowels = "AEIOUaeiou";
        // for (int i = 0; i < str.length(); i++) {
        //     char ch = str.charAt(i);
        //     if (vowels.indexOf(ch) != -1) {
        //         System.out.print(ch + " ");
        //     }
        // }




        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();

        // int f = 1;
        // for (int i = 1; i <= n; i++) {
        //     f *= i;
        // }
        // System.out.print(f);





        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();


        // int[] arr = new int[n];
        // for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        // int x = sc.nextInt();
        // boolean found = false;

        // for (int i = 0; i < n; i++) {
        //     if (arr[i] == x) {
        //         System.out.print(i + " ");
        //         found = true;
        //     }
        // }
        // if (!found) System.out.print(-1);



        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();
        // int[] arr = new int[n];

        // for (int i =0; i < n; i++) {
        //     arr[i] = sc.nextInt();
        // }
        // System.out.print(arr[0]+arr[1]);




        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();

   
        // int sum = 0;
        // for (int i = 0; i < n; i++) {
        //     sum += sc.nextInt();
        // }
        // double avg = (double) sum / n;
        // System.out.println("Sum:" + sum);
        // System.out.printf("Avarage: %.2f", avg);





        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();

        // for (int i = 1; i <=n; i++) {
        //     System.out.print(i*i*i+ " ");
        // }




        // Scanner sc = new Scanner(System.in);
        // int a = sc.nextInt();
        // int b = sc.nextInt();


        // if (a==0) {
        //     System.out.print(b);
        //     return;
        // }
        // if (b==0) {
        //     System.out.print(a);
        //     return;
        // }
        // while (a != b) {
        //     if (a > b)
        //         a = a - b;
        //     else
        //         b = b - a;
        // }
        // System.out.print(a + " ");




        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();

        // int sum = 0, sumofSquares = 0;
        // for(int i = 1; i <= n;i++){
        //     sum += i;
        //     sumofSquares += i * i;
        // }

        // int Squareofsum = sum * sum;
        // int diff = Math.abs(Squareofsum - sumofSquares);

        // System.out.print(diff);




        // Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();


        // int original = n;
        // int rev = 0;

        // while (n != 0){
        //     int digit = n % 10;
        //     rev = rev * 10 + digit;
        //     n /= 10;
        // }
        // if ( rev == original) {
        //     System.out.println("True");

        // } else {
        //     System.out.println("False");
        // }




        // Scanner sc = new Scanner(System.in);
        // String s = sc.nextLine();

        // String rev = new StringBuilder(s).reverse().toString();

        // if(s.equals(rev)) {
        //     System.out.print("Palindrome");

        // } else {
        //     System.out.println("Not Palindrome");
        // }



        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();


        int X = 0;
        for (int i = 0; i < n;i++) {
            String op = sc.next();

        if (op.contains("++")) {
            X++;

        } else {
            X--;
        }
        }


        System.out.print(X);
        }
        
    }


