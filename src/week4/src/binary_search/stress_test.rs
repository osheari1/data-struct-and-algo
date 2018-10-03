extern crate rand;

use super::main::run;
use self::rand::Rng;
use self::rand::seq::sample_iter;
pub fn run_stress_test() {
    stress_test(100000, 100, 100, 10000, &run)
}

fn stress_test(a: i32, n: i32, k: i32, m: i32, fnc: &Fn(&usize, &Vec<i32>, &usize, &Vec<i32>) -> Vec<i32>) {

    let mut rng = rand::thread_rng();

    for _  in 0..m {

        let mut ns: Vec<i32> = sample_iter(&mut rng, 0..a+1, n as usize).unwrap();
//        let ks: Vec<i32> = sample_iter(&mut rng, 0..a, k as usize).unwrap();
        let mut ks: Vec<i32> = Vec::new();
        for _ in 0..k {
            ks.push(rng.gen_range(0, a))
        }

        ns.sort();
        println!("{:?} {:?}", &ns, &ks);
        let naive = run_naive(&ns, &ks);
        let test = fnc(&(ns.len()), &ns, &(ks.len()), &ks);

        println!("Naive {:?}", naive);
        println!("Test {:?}", test);
        println!();

        if naive != test {
            println!("Naive {:?}", naive);
            println!("Test {:?}", test);
            println!("Failure");
            return
        }
        println!("Match");
    }
    println!("Success");
}

fn run_naive(ns: &Vec<i32>, ks: &Vec<i32>) -> Vec<i32> {
    // Sort

    let mut out_ix: Vec<i32> = Vec::new();
    for k in ks {
        let search = ns.binary_search(&k);
        match search {
            Ok(ix) => out_ix.push(ix as i32),
            Err(_) => out_ix.push(-1)
        }
    }
    out_ix
}
