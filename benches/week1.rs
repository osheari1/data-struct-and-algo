#[macro_use]
extern crate criterion;
extern crate data_struct_and_algo;

use criterion::Criterion;
use data_struct_and_algo::week1::{
    sum_two_digits,
    max_pairwise_prod,
};

fn sum_two_digits_benchmark(c: &mut Criterion) {
    c.bench_function(
        "sum_two_digits 1 4",
        |b| b.iter(|| sum_two_digits::run(1, 4)),
    );
}

fn max_pairwise_prod_benchmark(c: &mut Criterion) {
    c.bench_function(
        "max_pairwise_prod naive [1 4 6 10 11 12]",
        |b| b.iter(|| max_pairwise_prod::run_naive(
            &vec![1, 4, 6, 10, 11, 2])),
    );

    c.bench_function(
        "max_pairwise_prod naive_fast [1 4 6 10 11 12]",
        |b| b.iter(|| max_pairwise_prod::run_naive_fast(
            vec![1, 4, 6, 10, 11, 2])),
    );
}


criterion_group!(benches, sum_two_digits_benchmark, max_pairwise_prod_benchmark);
criterion_main!(benches);
