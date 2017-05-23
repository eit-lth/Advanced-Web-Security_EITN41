
import java.net.*;
import java.io.*;
import java.math.*;
import java.util.*;

class Client {
	public static void main(String[] args) {
		new Client().run();
	}

	void run() {
		String serverName = "eitn41.eit.lth.se";
		int port = 1337;
		Random rnd = new Random();
		// the p shall be the one given in the manual
		BigInteger p = new BigInteger("1234567890abcdef", 16);
		BigInteger g = new BigInteger("2");

		try {
			Socket client = new Socket(serverName, port);
			PrintWriter out = new PrintWriter(client.getOutputStream(), true);
			BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
			
			// receive g**x1 and convert to a number
			String g_x1_str = in.readLine();
			System.out.println("g**x1: " + g_x1_str);
			BigInteger g_x1 = new BigInteger(g_x1_str, 16);

			// generate g**x2, x2 shall be a random number
			BigInteger x2 = new BigInteger("0");
			// calculate g**x2 mod p
			BigInteger g_x2 = g.modPow(x2, p);
			// convert to hex-string and send.
			out.println(g_x2.toString(16));
			// read the ack/nak. This should yield a nak due to x2 being 0
			System.out.println("\nsent g_x2: " + in.readLine());

			client.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
