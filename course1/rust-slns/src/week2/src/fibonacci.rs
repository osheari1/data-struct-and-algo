

pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let n: i64  = buff.split_whitespace().next().unwrap().parse().unwrap();

    println!("{}", fibonacci_fast(n));
}

pub fn run_stress_test() {
   stress_test(&fibonacci_fast)
}

fn stress_test(fnc: &Fn(i64) -> i64) {
    for i in 1..45 {
        let naive = fibonacci_naive(i);
        let test = fnc(i);
        println!("n {}", i);
        println!("Naive {}", naive);
        println!("Test {}", test);
        assert!(naive == test)
    }
}


pub fn fibonacci_naive(n: i64) -> i64 {
    if n <= 1 {
        return n;
    }
    return fibonacci_naive(n-1) + fibonacci_naive(n-2);
}

pub fn fibonacci_fast(n: i64) -> i64 {
    if n <= 1 {
        return n;
    }

    let mut f1: i64 = 1;
    let mut f2: i64 = 0;
    for _ in 2..n+1 {
        let f = f1 + f2;
        f2 = f1;
        f1 = f;
    }
    f1
}
