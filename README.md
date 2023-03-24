# Shor-algorithm-Basic


It a  a basic implementation of shors algorthm which is used to find factor of prime number .

Shor's algorithm has important implications for cryptography, since many encryption schemes rely on the difficulty of factoring large numbers. With a large enough quantum computer, Shor's algorithm could break many commonly used encryption schemes

Reduction to period-finding problem, Miller 1976
. Find factor of odd n provided some method to calculate the order r of xa mod n,
a ∈ N:
1. Choose a random x < n.
2. Find order r (somehow) in xr ≡ 1 mod n.
3. Compute p, q = gcd(x**r/2 ± 1, n) if r even.
. Since (x**r/2 − 1)(x**r/2 + 1) = xr − 1 ≡ 0 mod n.
. Fails if r odd or x**r/2 ≡ −1 mod n.
. Yields a factor with p = 1 − 2−k+1 where k is the number of distinct odd prime factors of n.


'this is classical part of the algorithm'
