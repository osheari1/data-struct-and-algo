//extern crate rand;
use std::cmp::max;
//use self::rand;
//use self::rand::Rng;

pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
//    let words = buff.split_whitespace();

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
pub fn run_naive_faster(b: Vec<i64>) -> i64 {
    let mut ix  = 0;
    let mut arr_l: Vec<i64> = Vec::new();
    let mut arr_s: Vec<i64> = Vec::new();

    let n = b.len() - 1;
    for i in (0..n+1).filter(|x| x % 2 == 0) {
        if i + 1 >= b.len() {
            arr_l.push(b[i]);
            continue
        }

        if b[i] > b[i+1] {
            arr_l.push(b[i]);
            arr_s.push(b[i+1]);
        } else {
            arr_l.push(b[i+1]);
            arr_s.push(b[i]);
        }
    }

    for i in 0..arr_l.len() {
        if arr_l[i] > arr_l[ix] {
            ix = i;
        }
    }

    let l = arr_l[ix];
    arr_l.remove(ix);

    let mut s = 0;
    if arr_l.len() > 0 {
        for i in 0..arr_l.len() {
            if arr_l[i] > s {
                s = arr_l[i];
            }
        }
    }

    if arr_s.len() - 1 >= ix {
        if s < arr_s[ix] {
            s = arr_s[ix];
        }
    }

    l * s
}

