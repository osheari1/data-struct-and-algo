extern crate rand;

use ::week1::max_pairwise_prod::{
    run_naive,
    run_naive_fast,
    run_naive_faster
};

use self::rand::Rng;

pub fn run_stress_test() {
    stress_test(10, 20, 2000, &run_naive_faster);
}

pub fn simple_test() {
    let mut rng = rand::thread_rng();
    let n_rand = rng.gen_range(2, 10);
    let mut arr: Vec<i64> = Vec::new();
    for _i in 0..n_rand {
        arr.push(rng.gen_range(0, 10))
    }

    let result_naive = run_naive(&arr);
    let result_faster = run_naive_faster(arr);

    println!("Naive: {}", result_naive);
    println!("Fast: {}", result_faster);
}

pub fn stress_test(n: i64, m: i64, total: i64, fnc: &Fn(Vec<i64>) -> i64) {
    let mut count = 0;
    loop {
        count += 1;
        if count > total { break; }

        let mut rng = rand::thread_rng();
        let n_rand = rng.gen_range(2, n);

        let mut arr: Vec<i64> = Vec::new();
        for _i in 0..n_rand {
            arr.push(rng.gen_range(0, m))
        }
//        println!("{:?}", arr);
        let result_naive = run_naive(&arr);
        let result_fast = fnc(arr);
        println!("Naive: {}", result_naive);
        println!("fast: {}", result_fast);

        if result_naive != result_fast {
            println!("Wrong answer -> naive: {} fast: {} ", result_naive, result_fast);
            break;
        } else {
            println!("OK");
        }
    }
}



