import java.io.*;
import java.util.*;

class PFerias {
	
	public static final int LEN = 104;
	public static int N;
	public static int pref[][]; 
	public static int res[];
	public static int max = -1;
	public static int maxi = -1;
	
	public static int getDay(int d, int m) {
		int day = d;
		if (m>6) day += 30;
		if (m>7) day += 31;
		if (m>8) day += 31;
		return day;
	}
	
	public static void setRes(int start) {
		for (int i=start; i<=start+13*7; i+=7) {
			boolean flag = true;
			for (int j=i; j<i+7 && flag; j++) {
				for (int k=0; k<N && flag; k++) {
					if (pref[k][j] == -1) {
						flag = false;
						res[i] = -1;
					}
					else {
						res[i] += pref[k][j];
					}
				}
			}
		}
	}
	
	public static void printDayMonth(int d) {
		String month = "Junho";
		if (d>30) {
			month = "Julho";
			d -= 30; }
		if (d>31) {
			month = "Agosto";
			d -= 31; }
		if (d>31) {
			month = "Setembro";
			d -= 31; }
		System.out.println(d + " de " + month);
	}
	
	public static void main(String args[]) {
		Scanner scn = new Scanner (System.in);
		N = scn.nextInt();
		pref = new int[N][LEN];
		res = new int[LEN];
		for (int i=0; i<N; i++) {
			int nPref = scn.nextInt();
			for (int j=0; j<nPref; j++) {
				int d1 = scn.nextInt();
				int m1 = scn.nextInt();
				int d2 = scn.nextInt();
				int m2 = scn.nextInt();
				int p = scn.nextInt();
				int s = getDay(d1, m1);
				int f = getDay(d2, m2);
				for (int k=s; k<=f; k++)
					pref[i][k] = p;
			}
		}
		setRes(4);
		setRes(6);
		for (int i=4; i<=4+13*7; i+=7) {
			if (res[i] > max) {
				max = res[i];
				maxi = i;
			}
			if (res[i+2] > max) {
				max = res[i+2];
				maxi = i+2;
			}
		}
		if (max == -1) 	System.out.println("inconsistente");
		else 			printDayMonth(maxi);
	}
}