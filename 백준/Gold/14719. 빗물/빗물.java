import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        
        int[] lst = new int[w];
        for (int i = 0; i < w; i++) {
            lst[i] = sc.nextInt();
        }
        
        int result = 0;
        
        for (int i = 1; i < w - 1; i++) {
            int lmax = 0, rmax = 0;
            
            for (int j = 0; j < i; j++) {
                if (lst[j] > lmax) {
                    lmax = lst[j];
                }
            }
            
            for (int k = i + 1; k < w; k++) {
                if (lst[k] > rmax) {
                    rmax = lst[k];
                }
            }
            
            int mValue = Math.min(lmax, rmax);
            int value = mValue - lst[i];
            
            if (value > 0) {
                result += value;
            }
        }
        
        System.out.println(result);
    }
}