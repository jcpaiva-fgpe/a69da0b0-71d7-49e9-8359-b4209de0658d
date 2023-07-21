import java.util.*;
import java.io.*;

public class problema16 {

    static int mapa[][]= new int[101][101];
    static boolean[][] adj= new boolean[101][101];
    static int[] cont = new int[11111];
    static int q= 0,k;
    
    static void FFill (int i, int j, int l, int c, int k){
        if((i<l-1 && i>0) && (j<c-1 && j>0))
            if(!adj[i][j]) {
                adj[i][j]=true;
                if(mapa[i][j]==1)
                    cont[k]++;
                FFill(i+1,j,l,c,k);
                FFill(i-1,j,l,c,k);
                FFill(i, j+1, l, c, k);
                FFill(i, j-1, l, c, k);
                
            }
    }
    
    static void dfs(int l, int c){
        k=0;
        for(int i=1; i<=l; i++)
            for(int j=1; j<=c; j++){
                if(!adj[i][j]){
                    k++;
                    FFill(i,j,l,c,k);
                }
            }
    }
    
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        
        int l=in.nextInt();
        int c=in.nextInt();
        in.nextLine();
        
        for(int i=0; i<l; i++){
            String leit = in.nextLine();
            for(int j=0; j<c; j++)
                if(leit.charAt(j)=='#' || leit.charAt(j)=='P'){
                    mapa[i][j]=-1;
                    adj[i][j]=true;
                    q++;
                }
                else if(leit.charAt(j)=='C') 
                    mapa[i][j]=1;
                else
                    mapa[i][j]=0;
        }
        
        dfs(l, c);
        int max=0;
        for(int i=0; i<k; i++)
            if(cont[i]>max)
                max=cont[i];
        
        System.out.println(max);
        
    }
}
