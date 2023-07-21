import java.util.*;
import java.io.*;

class condominio{
    public static void main(String args[]){
	Scanner in=new Scanner(System.in);
	int n=in.nextInt();
	boolean allneg=true;
	int v[]=new int[n];
	int melhor=0;
	int melhoratei=0;
	int maiorneg=Integer.MIN_VALUE;
	for(int i=0;i<n;i++){	    
	    v[i]=in.nextInt();
	    if(v[i]>0) allneg=false;
	    else if(v[i]>maiorneg) maiorneg=v[i];
	}

	if(allneg==true) System.out.println(maiorneg);

	else{
	    for(int i=0;i<n;i++){
		melhoratei=melhoratei+v[i];
		if(melhoratei<=0) melhoratei=0;
		if(melhoratei>melhor) melhor=melhoratei;
	    }
	    System.out.println(melhor);
	}

    }
}
