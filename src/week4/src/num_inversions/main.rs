pub fn main() {
    // Read
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let n: usize = numbers.next().unwrap().parse().unwrap();

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();

    let mut ns = vec![0; n];
    for i in 0..n {
        ns[i] = numbers.next().unwrap().parse().unwrap();
    }

//    let out = run(&ln, &n, &lk, &k);
//    for o in out {
//        print!("{} ", o);
//    }
}


pub fn run(ns: &Vec<i32>) -> i32 {
}




