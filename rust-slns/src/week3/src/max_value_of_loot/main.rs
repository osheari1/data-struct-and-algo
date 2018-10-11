//use super::stress_test::run_naive;

pub fn main() {
    // Read
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let n: i32  = numbers.next().unwrap().parse().unwrap();
    let cap: f64  = numbers.next().unwrap().parse().unwrap();

    let mut x: Vec<(f64, f64, f64)> = Vec::new();
    for _ in 1..n+1 {
        let mut buff = String::new();
        ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
        let mut numbers = buff.split_whitespace();
        let v: f64  = numbers.next().unwrap().parse().unwrap();
        let w: f64  = numbers.next().unwrap().parse().unwrap();
        let v_w: f64 = v / w;
        x.push((v, w, v_w));
    }

    println!("{:.8}", run(x, cap));
}

fn run(mut x: Vec<(f64, f64, f64)>, cap: f64) -> f64 {
    x.sort_by(|x, y| y.2.partial_cmp(&x.2).unwrap());
    let mut current_weight: f64 = 0.0;
    let mut current_value: f64 = 0.0;

    let mut i = 0;
    while current_weight < cap {
        if i >= x.len() {
            break
        } else if x[i].1 + current_weight <= cap {
            current_weight += x[i].1;
            current_value += x[i].0;
            i += 1;
        } else  {
            current_value += (cap - current_weight) / x[i].1 * x[i].0;
            current_weight = cap;
            i += 1;
        }
    }
    current_value
}

