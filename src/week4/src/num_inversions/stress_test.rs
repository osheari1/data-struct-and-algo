extern crate rand;
use self::rand::Rng;
//use self::rand::seq::sample_iter;

/// # Constraints
/// 1 <= n <= 10^5
/// 1 <= a_i <= 10^9 for all 0 <= i < n
///
pub fn run_stress_test() {
    stress_test(10i32.pow(1) as i32, 10, 100, &run_naive)
}

fn stress_test(a: i32, n: i32, m: i32, fnc: &Fn(&Vec<i32>) -> i32) {

    let mut rng = rand::thread_rng();

    for _  in 0..m {

        let mut ns: Vec<i32> = Vec::new();
        for _ in 0..rng.gen_range(1, n) {
            ns.push(rng.gen_range(0, a))
        }

        println!("{:?}", &ns);
        let naive = run_naive(&ns);
//        let test = fnc(&n);

        println!("Naive {:?}", naive);
//        println!("Test {:?}", test);
//        println!();

//        if naive != test {
//            println!("Naive {:?}", naive);
//            println!("Test {:?}", test);
//            println!("Failure");
//            return
//        }
//        println!("Match");
    }
    println!("Success");
    let mut vec = (0..10).collect::<Vec<i32>>();
    vec.reverse();
    println!("{:?}", &vec);
    println!("Naive: {}", run_naive(&vec));
    println!("True: {}", vec.len() * (vec.len() - 1) / 2);
}

fn run_naive(ns: &Vec<i32>) -> i32 {
    let mut inversions = 0;
    for i in 0..ns.len() {
        for j in i+1..ns.len() {
            if ns[i] > ns[j] {
                inversions += 1;
            }
        }
    }
    inversions
}
