//use super::stress_test::run_naive;

pub fn main() {
    // Read
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let n: i32  = numbers.next().unwrap().parse().unwrap();

    let k: Vec<i32> = run(n);
    println!("{}", k.len());
    for k_i in k {
        print!("{} ", k_i);
    }
    println!();
}

fn run(n: i32) -> Vec<i32> {
    let mut acc: i32 = 0;
    let mut i: i32 = 1;
    let mut k: Vec<i32> = Vec::new();
    while acc < n {
        let acc_plus_i = acc + i;
        let acc_plus_i = n - (acc + i);
        if (acc + i) <= n {
//        if n - acc > acc + i && n - acc > acc + i + 1 {
            acc += i;
            k.push(i);
            i += 1;
        } else {
            k[(i-2) as usize] += n - acc;
            acc = n;
//            i = n - acc;
//            acc += i;
//            k.push(i);
        }
    }
    k
}



