extern crate rand;
use self::rand::Rng;



pub fn pisano_naive(n: i64, m: i64) -> i64 {
    let mut f1: i64 = 1;
    let mut f2: i64 = 0;
    for _ in 2..n+1 {
        let f = (f1 + f2) % m;
        f2 = f1;
        f1 = f;
    }
    f1
}


pub fn run_stress_test() {
    stress_test(2*10_i64.pow(6), &pisano_naive)
}

fn stress_test(n: i64, fnc: &Fn(i64, i64) -> i64) {
    let mut rng = rand::thread_rng();

    for _  in 1..10000 {
        let a = rng.gen_range(1, n);
        let b = rng.gen_range(2, 10_i64.pow(3));
        let naive = pisano_naive(a, b);
        let test = fnc(a, b);

        println!("{} {}", a, b);
        println!("Naive {}", naive);
        println!("Test {}", test);

        if naive != test {
            println!("{} {}", a, b);
            println!("Naive {}", naive);
            println!("Test {}", test);
            break
        }
    }
    println!("Success");
}



