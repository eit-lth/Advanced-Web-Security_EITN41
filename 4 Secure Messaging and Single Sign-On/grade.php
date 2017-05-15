<? php
	function calc_signature ( $data ) {
		// truncate signature to 10 bytes
		$sig = substr ( hash_hmac ('sha1 ', $data , $key ), 0, 20) ;
		return $sig ;
	}
	function check_signature ($sig1 , $sig2 ) {
		$n = max ( strlen ( $sig1 ), strlen ( $sig2 ));
		for ($i = 0; $i <= $n; $i ++) {
			// chrcmp compares chars at index i, return 1 if chars are equal , 0 otherwise
			if (! chrcmp ($sig1 , $sig2 , $i)) {
				return '0';
			}
		}
		return '1';
	}
	// get the user supplied data
	if ( isset ( $_GET ['name ']) && isset ( $_GET ['grade ']) && isset ( $_GET ['signature '])) {
		$name = $_GET ['name '];
		$grade = $_GET ['grade '];
		$sig = $_GET ['signature '];
		// concatenate name and grade
		$data = $name . $grade ;
		$sig2 = calc_signature ( $data );
		echo check_signature ($sig , $sig2 );
	} else {
		echo 'Not enough arguments ';
	}
?>