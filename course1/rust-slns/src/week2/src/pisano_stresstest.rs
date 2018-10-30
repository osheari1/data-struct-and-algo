extern crate rand;
use self::rand::Rng;
use ::week2::pisano::pisano;
use ::week2::pisano::fibonacci;





pub fn run_stress_test() {
    stress_test(100000, 1000, &pisano)
}

fn stress_test(n: i64, m: i64, fnc: &Fn(i64, i64) -> i64) {
    let mut rng = rand::thread_rng();

    for _  in 1..100 {
        let a = rng.gen_range(1, n);
        let b = rng.gen_range(2, m);

        println!("n: {} m: {}", a, b);
//        let naive = fibonacci(a) % b;
        let naive = fibonacci(a, b);
        let test = fnc(a, b);

        println!("Naive {}", naive);
        println!("Test {}", test);
        println!();

        if naive != test {
//            println!("{} {}", a, b);
//            println!("Naive {}", naive);
//            println!("Test {}", test);
            println!("Failure");
            return
        }
    }
    println!("Success");
}



