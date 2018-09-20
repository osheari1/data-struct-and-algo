
pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let a: i64  = numbers.next().unwrap().parse().unwrap();
    let b: i64  = numbers.next().unwrap().parse().unwrap();

    println!("{}", pisano(a, b));
}

pub fn pisano(n: i64, m: i64) -> i64 {
    let  p = if m == 1 {
        1
    } else if m == 2 {
        3
    } else if m == 3 {
        8
    } else if m == 4 {
        6
    } else {
        calculate_pisano_period(m)
    };

    let r: i64 = n % p;

//    fibonacci(r) % m
    fibonacci(r, m)
}

pub fn fibonacci(n: i64, m: i64) -> i64 {
    if n <= 1 {
        return n;
    }
    let mut f1: i64 = 1;
    let mut f2: i64 = 0;
    for _ in 2..n+1 {
        let f = (f1 + f2) % m;
        f2 = f1;
        f1 = f;
    }
    f1
}

pub fn calculate_pisano_period(m: i64) -> i64 {
    let mut f_prev: i64 = 0;

    for i in 0.. {
//        let f = fibonacci(i, m) % m;
        let f = fibonacci(i, m);
        if i > 2 && f_prev == 0 && f == 1 {
            return i - 1
        } else {
            f_prev = f;
        }
    }
    0
}

