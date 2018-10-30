#[macro_use]
extern crate criterion;
extern crate data_struct_and_algo;

use criterion::Criterion;
use data_struct_and_algo::week2::fibonacci;

fn fibonacci_naive_benchmark(c: &mut Criterion) {
    c.bench_function(
        "fibonacci_naive 30",
        |b| b.iter(|| fibonacci::fibonacci_naive(30)),
    );
}

fn fibonacci_fast_benchmark(c: &mut Criterion) {
    c.bench_function(
        "fibonacci_fast 30",
        |b| b.iter(|| fibonacci::fibonacci_fast(30)),
    );
}


criterion_group!(benches, fibonacci_naive_benchmark, fibonacci_fast_benchmark);
criterion_main!(benches);
