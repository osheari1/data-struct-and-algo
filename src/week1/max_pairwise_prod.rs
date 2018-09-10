use std::cmp::max;

pub fn main() {

    // Read first integer

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let a: i64 = buff.split_whitespace().next().unwrap().parse().unwrap();

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let words = buff.split_whitespace();

    let values = words.map(|s| -> i64 {
        s.to_string().parse().unwrap()
    }).collect::<Vec<i64>>();
//    let a: i64 = words.next().unwrap().parse().unwrap();
//    let b: i64 = words.next().unwrap().parse().unwrap();

//    println!("{}", run_naive(a, &values));
    let values2: Vec<i64> = (1..2*10i64.pow(5)+1).collect();
    println!("{}", run_naive_fast(&values));
    println!("{}", run_naive_fast(&values2));
}


pub fn run_naive(a: i64, b: &Vec<i64>) -> i64 {
    let mut product = 0;
    for x in b.iter() {
        product = max(product, a * x)
    }
    product
}

pub fn run_naive_fast(b: &Vec<i64>) -> i64 {
    let mut ix = 0;
    for i in 1..b.len() {
        if b[i] > b[ix] {
            ix = i
        }
    }
    let mut ix2 = if ix == 0 { 1 } else { 0 };
    for i in 1..b.len() {
        if b[i] != b[ix] && b[i] > b[ix2] {
            ix2 = i
        }
    }
    b[ix] * b[ix2]
}


