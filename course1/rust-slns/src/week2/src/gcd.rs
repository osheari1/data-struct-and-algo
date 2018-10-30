extern crate rand;
use self::rand::Rng;

#[allow(dead_code)]

pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let a: i64  = numbers.next().unwrap().parse().unwrap();
    let b: i64  = numbers.next().unwrap().parse().unwrap();

    println!("{}", if a > b { gcd_euclid(a, b) } else { gcd_euclid(b, a) });
}

pub fn run_stress_test() {
    stress_test(2*10^9, &gcd_euclid)
}

fn stress_test(n: i64, fnc: &Fn(i64, i64) -> i64) {
    let mut rng = rand::thread_rng();

    for _  in 1..10000 {
        let a = rng.gen_range(1, n);
        let b = rng.gen_range(1, n);
        let naive = gcd_naive(a, b);
        let test = if a > b { fnc(a, b) } else { fnc(b, a) };


        if naive != test {
            println!("{} {}", a, b);
            println!("Naive {}", naive);
            println!("Test {}", test);
            break
        }
    }
    println!("Success");
}

fn gcd_naive(a: i64, b: i64) -> i64 {
    let mut best: i64 = 1;
    for d in 1..(a + b) {
        if a % d == 0 && b % d == 0 {
            best = d;
        }
    }
    best
}

pub fn gcd_euclid(a: i64, b: i64) -> i64 {
    if b == 0 {
        return a
    }
    gcd_euclid(b, a % b)
}

