extern crate rand;

use self::rand::Rng;

pub fn run_stress_test() {
    stress_test(10, 10, 10, &run_naive)
}

fn stress_test(n: i32, k: i32, m: i32, fnc: &Fn(i32, Vec<i32>) -> i32) {

    let mut rng = rand::thread_rng();

    for _  in 1..n {

        let mut ns: Vec<i32> = Vec::new();
        let mut ks: Vec<i32> = Vec::new();
        for _ in 1..n {
            ns.push(rng.gen_range(1, n as i32));
            ks.push(rng.gen_range(1, k as i32));
        }

        println!("{:?}", ns);
        println!("{:?}", ks);
//        let naive = run_naive()
//        let test = fnc(x);

//        println!("{} {}", a, b);
//        println!("Naive {}", naive);
//        println!("Test {}", test);
//        println!();

//        if naive != test {
////            println!("{} {}", a, b);
////            println!("Naive {}", naive);
////            println!("Test {}", test);
//            println!("Failure");
//            return
//        }
    }
    println!("Success");
}

fn run_naive(l: i32, v: Vec<i32>) -> i32 {
    0
}
