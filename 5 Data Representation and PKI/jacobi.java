import java . math .*;
class Jacobi {
	static BigInteger zero = BigInteger . ZERO ;
	static BigInteger one = BigInteger .ONE;
	static BigInteger two = new BigInteger ("2");
	static BigInteger three = new BigInteger ("3");
	static BigInteger four = new BigInteger ("4");
	static BigInteger five = new BigInteger ("5");
	static BigInteger eight = new BigInteger ("8");
	public static void main ( String [] args ) {
		BigInteger a = new BigInteger ("12");
		BigInteger b = new BigInteger ("17");
		System . out . println (" jacobi (12/17) (= -1): " + jacobi (a, b));
	}
	static int jacobi ( BigInteger n, BigInteger m) {
		int j = 1;
		int t;
		BigInteger tmp ;
		n = n.mod (m);
		while (!n. equals ( zero )) {
			t = 0;
			while (!n. and ( one ). equals ( one )) {
				n = n. divide ( two );
				t ++;
			}
			BigInteger mmod8 = m.mod ( eight );
			if ((( t & 0 x01 ) == 1) && ( mmod8 . equals ( three ) || mmod8 . equals ( five ))) {
				j = -j;
			}
			if (n.mod ( four ). equals ( three ) && m.mod( four ). equals ( three )) {
				j = -j;
			}
			tmp = n;
			n = m.mod (n);
			m = tmp ;
		}
		if (m. equals ( one )) {
			return j;
		}
		return 0;
	}
}