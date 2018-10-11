extern crate rand;

use self::rand::Rng;

//use max_value_of_loot::main::run;

pub fn run_stress_test() {
//    stress_test(100, 100, 100.0, &run)
}

fn stress_test(n: i32, m: i32, cap: f32, fnc: &Fn(Vec<(f32, f32, f32)>, f32) -> f32) {

    let mut rng = rand::thread_rng();

    for _  in 1..m {

        let mut v: Vec<f32> = Vec::new();
        let mut w: Vec<f32> = Vec::new();
        for _ in 1..m {
            v.push(rng.gen_range(1.0, n as f32));
            w.push(rng.gen_range(1.0, n as f32));
        }
        let x: Vec<(f32, f32, f32)> = v.iter()
            .zip(w.iter())
            .map(|(v, w)| (*v, *w, v/w))
            .collect();

        println!("{:?}", x);
//        let naive = fibonacci(a) % b;
        let test = fnc(x, cap);

        println!("Test {}", test);
        println!();

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

//fn run_naive

pub fn run_naive(mut x: Vec<(f32, f32, f32)>, cap: f32) -> f32 {
//    let mut indexes = Vec::new();

//    for i in 0..x.len() {
//        indexes.push(0..x.len());
//    }

//    for t in iproduct!(4, 4, 5) {
//        println!("{:?}", t);
//    }
    0.0
}
