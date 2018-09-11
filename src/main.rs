extern crate data_struct_and_algo;
//pub mod week1;
use data_struct_and_algo::{
    week1
};

fn main() {
//    week1::sum_two_digits::main();
//    week1::max_pairwise_prod::main();
    week1::stress_test_max_pairewise_prod::run_stress_test();
//    week1::stress_test_max_pairewise_prod::simple_test();
}