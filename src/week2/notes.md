# Modular Arithmetic
* x = qN + r, 0 <= r < N, r = remainder
* x mod n = r
* x and y are congruent modulo N if they differ by a multiple of N.
  * x === y mod N <==> N divides (x - y)
* Substitution rule:
  * if x === x' mod N and y === y' then:
    * x + y === x' + y' mod N and xy === x'y' mod N
* Associativity: x + (y + z) === (x + y) + z mod N
* Commutativity: xy === yx (mod N)
* Distributivity: x(y+z) === xy + yz mod N

# Big O
### Definition
* f(n) = O(g(n)) or f <= g if there exists 
constants N and c so that for all n >= N, f(n) <= c*g(n)
* ie. if is bounded above by some constant multiple of g

### Basic asymptotic behavior
* log n < sqrt(n) < n < n log n < n^2 < 2^n

### Rules
* 7n^3 = O(n^3), n^2/3 = O(n^2)
* n^a < n^b for 0 < a < b
  * n = O(n^2)
  * sqrt(n) = O(n)
* n^a < b^n (a > 0, b > 1)
  * n^5 = O(sqrt(2)^n)
  * n^100 = O(1.1^n)
* (log n)^a < n^b (a, b > )
  * (log n)^3 = O(sqrt(n))
  * n log n = O(n^2)
* Smaller terms can be omitted
  * n^2 + n = O(n^2)
  * 2^n + n^9 = O(2^n)

### Bounded Below 
#### Definition
For functions f, g: N -> R+ 
* f(n) = omega(g(n)) for f >= g if for some c,
f(n) >= c*g(n) (f grows slower than g)
* f(n) = theta(g(n)) or f =~ g if f = O(g) and 
f = omega(g) (f grows at same rate as g)

### Strictly slower
#### Definition
for functions f, g: N -> R+ 
* f(n) = o(g(n)) or f < g if
f(n) / g(n) as n -> inf (f grows slower than g)