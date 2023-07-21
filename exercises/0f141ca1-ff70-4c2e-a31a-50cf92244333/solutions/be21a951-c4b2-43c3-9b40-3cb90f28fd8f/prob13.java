import java.io.*;
import java.util.*;

//Adaptação da resolucao de um colega

public class prob13{
	public static void main(String [] args){

		Scanner in = new Scanner(System.in);
		int k = in.nextInt();
		int n = in.nextInt();
		

		int [] stones = new int[n+1];
		int [] rFoot = new int[n+1];
		int [] lFoot= new int[n+1];


		for(int i=0; i<n; i++){
			stones[i] = in.nextInt();
		}

		if(n==1){
			System.out.println(stones[0]);
			return;
		}

		rFoot[n-1] = stones[n-1];
		lFoot[n-1] = -stones[n-1];

		for(int i=n-2; i>=0; i--){

			int maxlFoot = lFoot[i+1];
			int max_rFoot = rFoot[i+1];
			
			for(int j=i+2; j<i+k+1; j++){
				if(j<=n){
					if(maxlFoot<lFoot[j])
						maxlFoot=lFoot[j];
					if(max_rFoot<rFoot[j])
						max_rFoot=rFoot[j];
				}
			}

			rFoot[i] = stones[i]+maxlFoot;
			lFoot[i] = max_rFoot-stones[i];
		}
		
		int maximum = rFoot[0];
		int i = 0;
		
		while(i<k && i<n){
			if(maximum<rFoot[i])
				maximum=rFoot[i];
			if(maximum<lFoot[i])
				maximum=lFoot[i];
			i++;
		}


		System.out.println(maximum);
	}
}
