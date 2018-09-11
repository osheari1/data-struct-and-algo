extern crate rand;

use std::cmp::max;
use self::rand::Rng;

pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let words = buff.split_whitespace();

    let values = words.map(|s| -> i64 {
        s.to_string().parse().unwrap()
    }).collect::<Vec<i64>>();
    println!("{}", run_naive_fast(values));
}


pub fn run_naive(b: &Vec<i64>) -> i64 {
    let mut product = 0;
    for i in 0..b.len() {
        for j in i + 1..b.len() {
            product = max(product, b[i] * b[j]);
        }
    }
    product
}

pub fn run_naive_fast(mut b: Vec<i64>) -> i64 {
    let mut ix = 0;
    let n = b.len() - 1;
    for i in 1..n + 1 {
        if b[i] > b[ix] {
            ix = i
        }
    }
    b.swap(ix, n);

    let mut ix = 0;
    for i in 1..n {
        if b[i] > b[ix] {
            ix = i
        }
    }
    b.swap(ix, n - 1);
//   println!("{} {}", b[n - 1], b[n]);
    b[n - 1] * b[n]
}

/*
Stress testing
*/

pub fn run_stress_test() {
    stress_test(1000, 200000, 2000);
}

fn stress_test(n: i64, m: i64, total: i64) {
    let mut count = 0;
    loop {
        count += 1;
        if count > total { break; }

        let mut rng = rand::thread_rng();
        let n_rand = rng.gen_range(2, n);

        let mut arr: Vec<i64> = Vec::new();
        for _i in 0..n_rand {
            arr.push(rng.gen_range(0, m))
        }
//        println!("{:?}", arr);
        let result_naive = run_naive(&arr);
        let result_fast = run_naive_fast(arr);

        if result_naive == result_fast {
            println!("OK");
        } else {
            println!("Wrong answer -> naive: {} fast: {} ", result_naive, result_fast);
            break;
        }
    }
}



