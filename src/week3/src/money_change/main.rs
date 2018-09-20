
pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let a: i32  = numbers.next().unwrap().parse().unwrap();
//    let b: i64  = numbers.next().unwrap().parse().unwrap();

    println!("{}", run(a, vec![1, 5, 10]));
}

pub fn run(m: i32, mut d: Vec<i32>) -> i32 {
    d.sort_by(|x, y| y.cmp(x));
    let mut count = 0;
    let mut total = 0;
    for d_i in d {
        while d_i + total <= m {
            count += 1;
            total += d_i;
        }
        if total == m {
            return count;
        }
    }
    -1
}

