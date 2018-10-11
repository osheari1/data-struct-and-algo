pub fn main() {

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut words = buff.split_whitespace();

    let a: i64 = words.next().unwrap().parse().unwrap();
    let b: i64 = words.next().unwrap().parse().unwrap();

    println!("{}", run(a, b));
}


pub fn run(a: i64, b: i64) -> i64 {
    a + b
}