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

//pub fn run_naive_faster(b: Vec<i64>) -> i64 {
//    let mut ix = 0;
//    let mut arr = vec![b[ix]];
//
//    let n = b.len() - 1;
//    for i in 1..n + 1 {
//        if b[i] > b[ix] {
//            ix = i;
//        }
//        if b[i] >= arr[arr.len()-1] {
//            arr.push(b[i])
//        } else if arr.len() == 1 && b[i] >= arr[arr.len() - 1] {
//            arr.push(b[i])
//        }
//    }
//    println!("{:?}", b);
//    println!("{:?}", arr);
//    arr[arr.len()-2] * b[ix]
//}

