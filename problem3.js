// What is the largest prime factor of the number 600851475143 ?
console.info("Auto-poke loaded."); //how fast do you want it to check for pokes?

function factorize(n) {
while (n % 2 == 0) {
	n/=2
}
	

	for (int k = 3; k < sqrt(n); k = k + 2) { 
		while (n % k == 0) { 
			n = n/k; 
		}
	}
	console.log(n); 
} 

factorize(33); 


