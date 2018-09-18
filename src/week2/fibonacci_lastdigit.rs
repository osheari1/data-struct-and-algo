pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let n: i64  = buff.split_whitespace().next().unwrap().parse().unwrap();

    println!("{}", fibonacci_last_digit(n));
}

pub fn run_stress_test() {
   stress_test(&fibonacci_naive)
}

fn stress_test(fnc: &Fn(i64) -> i64) {
    for i in 1..10^7 {
        let naive = fibonacci_naive(i);
        let test = fnc(i);

        if naive != test {
            println!("n {}", i);
            println!("Naive {}", naive);
            println!("Test {}", test);
            break
        }
    }
    println!("Success");
}


pub fn fibonacci_naive(n: i64) -> i64 {
    if n <= 1 {
        return n;
    }
    (fibonacci_naive(n-1) % 10 + fibonacci_naive(n-2) % 10) % 10
}

pub fn fibonacci_last_digit(n: i64) -> i64 {

    let mut f1: i64 = 1;
    let mut f2: i64 = 0;
    for _ in 2..n+1 {
        let f = (f1 % 10 + f2 % 10) % 10;
        f2 = f1;
        f1 = f;
    }
    f1
}


