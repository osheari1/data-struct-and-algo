extern crate rand;
use self::rand::Rng;
use std::cmp::min;


pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let a: i64  = numbers.next().unwrap().parse().unwrap();
    let b: i64  = numbers.next().unwrap().parse().unwrap();

//    println!("{}", if a > b { lcm(a, b) } else { gcd_euclid(b, a) });
}

pub fn run_stress_test() {
    stress_test(10, 100, &lcm_naive)
}

fn stress_test(n: i64, m: i64, fnc: &Fn(i64, i64) -> i64) {
    let mut rng = rand::thread_rng();

    for _  in 1..m {
        let a = rng.gen_range(1, n);
        let b = rng.gen_range(1, n);
        let naive = lcm_naive(a, b);
        let test = if a > b { fnc(a, b) } else { fnc(b, a) };

        println!("{} {}", a, b);
        println!("Naive {}", naive);
        println!("Test {}", test);

        if naive != test {
            println!("{} {}", a, b);
            println!("Naive {}", naive);
            println!("Test {}", test);
            break
        }
    }
    println!("Success");
}

fn lcm_naive(a: i64, b: i64) -> i64 {
    for m in min(a, b).. {
       if  m % a == 0 && m % b == 0 {
           return m
       }
    }
   0
}

