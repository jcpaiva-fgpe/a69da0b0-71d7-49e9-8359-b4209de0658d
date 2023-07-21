import java.util.*;
import java.io.*;

class vito{
    public static void main(String args[]){
	Scanner in=new Scanner(System.in);
	int n=in.nextInt();
	int v[]=new int[n];
	for(int i=0;i<n;i++){
	    v[i]=in.nextInt();
	}
	Arrays.sort(v);
	int soma=0;
	int med;
	if(n%2==0){
	    med=(v[(v.length/2)-1]+v[v.length/2])/2;
	}
	else med=v[v.length/2];

	for(int i=0;i<n;i++){
	    if(v[i]<med)
		soma+=med-v[i];
	    else
		soma+=v[i]-med;
	}
	System.out.println(soma);
    }
    
}
