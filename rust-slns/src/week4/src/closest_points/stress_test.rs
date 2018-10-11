extern crate rand;

use std::f64;
use std::time::SystemTime;
use self::rand::Rng;
use self::rand::{ SeedableRng, StdRng };
//use self::rand::seq::sample_iter;
use closest_points::main::distance;
use closest_points::main::run;



/// # Constraints
/// 2 <= n <= 10^5
/// 10^9 <= x, y <= 10^9
///
///
///
///
pub fn run_stress_test() {
//    stress_test( 10, 10i32.pow(5) as i32, 100, &run_naive);
    stress_test(10i64.pow(9), 10i32.pow(5), 100, &run);
}

fn stress_test(a: i64, n: i32, m: i32, fnc: &Fn(Vec<(i64, i64)>) -> f64) {
//    let mut rng = rand::thread_rng();
    let mut rng: StdRng = SeedableRng::from_seed([1u8; 32]);

    for _ in 0..m {
        let mut ns: Vec<(i64, i64)> = Vec::new();
        for _ in 0..rng.gen_range(2, n) {
            ns.push((rng.gen_range(-a, a), rng.gen_range(-a, a)))
        }


//        println!("{:?}", &ns);
//        let t0 = SystemTime::now();
//        let naive = run_naive(&ns);
//        println!("Naive {:?}", naive);
//        println!("{:?}", SystemTime::now().duration_since(t0).unwrap());

        let t0 = SystemTime::now();
        let test = fnc(ns.to_vec());
        println!("Test {:?}", test);
        println!("{:?}", SystemTime::now().duration_since(t0).unwrap());
        println!("-------------------------------------------------------");
        println!();

        ns.sort_by_key(|x| x.0);
//        if naive != test {
//            println!("{:?}", &ns);
//            println!("Naive {:?}", naive);
//            println!("Test {:?}", test);
//            println!("Failure");
//            return
//        }
//        println!("Match");
    }
    println!("Success");
}

fn run_naive(ns: &Vec<(i64, i64)>) -> f64 {
    let mut min = f64::INFINITY;
    for point_x in 0..ns.len() {
        for point_y in 0..ns.len() {
            if point_x == point_y {
                continue;
            }
            let dist = distance(ns[point_x], ns[point_y]);
            if dist < min {
                min = dist;
            }
        }
    }
    min
}
