extern crate rand;
extern crate time;
use self::rand::Rng;
use std::cmp::min;


pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");

    let mut numbers = buff.split_whitespace();
    let a: i64  = numbers.next().unwrap().parse().unwrap();
    let b: i64  = numbers.next().unwrap().parse().unwrap();

//    let t0 = time::get_time().sec;
    println!("{}", lcm_faster(a, b));
//    println!("Time {}", time::get_time().sec - t0);
}

pub fn run_stress_test() {
    stress_test(2*10_i64.pow(4), 100, &lcm_faster)
}

fn stress_test(n: i64, m: i64, fnc: &Fn(i64, i64) -> i64) {
    let mut rng = rand::thread_rng();

    for _  in 1..m {
        let a = rng.gen_range(1, n);
        let b = rng.gen_range(1, n);

        let t0 = time::get_time().sec;
        let naive = lcm_naive(a, b);
//        let naive = 0;
        println!("Time Naive {}", time::get_time().sec - t0);

        let t0 = time::get_time().sec;
        let test = fnc(a, b);
        println!("Time Fast {}", time::get_time().sec - t0);

        println!("{} {}", a, b);
        println!("Naive {}", naive);
        println!("Test {}", test);
        println!();

        if naive != test {
            println!("{} {}", a, b);
            println!("Naive {}", naive);
            println!("Test {}", test);
            println!("Failed");
            return
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

//fn lcm_fast(a: i64, b: i64) -> i64 {
//    if min(a, b) == 1 {
//        return max(a, b)
//    }
//    let x = min(a,b);
//    let y = max(a, b);
////    let mut output: i64;
//
//    for i in 1..x+1 {
//        if (i * y) % x == 0 {
////            println!("{}", i);
//            return i * y
//        }
//    }
//    0
//}

pub fn gcd_euclid(a: i64, b: i64) -> i64 {
    if b == 0 {
        return a
    }
    gcd_euclid(b, a % b)
}

fn lcm_faster(a: i64, b: i64) -> i64 {
    let gcd: i64 = if a > b { gcd_euclid(a, b)} else { gcd_euclid(b, a) };
    return a * b / gcd;

}

