
pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let a: i64  = numbers.next().unwrap().parse().unwrap();
    let b: i64  = numbers.next().unwrap().parse().unwrap();

    println!("{}", a+b);
}

pub fn pisano(n: i64, m: i64) -> i64 {
    let mut p: i64 = if m % 2 == 0 { 2 * m } else { 4 * m };
    let r: i64 = n % p;

    fibonacci_fast(r) % m
}

pub fn fibonacci_fast(n: i64) -> i64 {
    if n <= 1 {
        return n;
    }

    let mut f1: i64 = 1;
    let mut f2: i64 = 0;
    for _ in 2..n+1 {
        let f = f1 + f2;
        f2 = f1;
        f1 = f;
    }
    f1
}

