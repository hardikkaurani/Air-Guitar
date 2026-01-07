import java.util.*;

import javax.sql.rowset.spi.SyncResolver;
class Firstclass {
    public static void main (String args[]) {

        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        StringBuilder res = new StringBuilder();

        for(int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'b') continue;

            if (s.charAt(i) == 'a' && i + 1 < s.length() && s.charAt(i +1) == 'c') {
                i++;
                continue;

            }
            res.append(s.charAt(i));
        }
        System.out.println(res.toString());
        

    }
}