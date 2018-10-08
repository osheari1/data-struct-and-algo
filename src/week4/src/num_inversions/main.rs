pub fn main() {
    // Read
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let n: usize = numbers.next().unwrap().parse().unwrap();

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();

    let mut ns = vec![0; n];
    for i in 0..n {
        ns[i] = numbers.next().unwrap().parse().unwrap();
    }

    let x = run_naive(&ns);
    print!("{} ", x);
}

pub fn run(ns: Vec<i32>) -> (Vec<i32>, i32) {
    merge_sort(ns, 0)
}

// TODO: Update partition function to use partition3 for equal elements
fn merge_sort(ns: Vec<i32>, inversions: i32) -> (Vec<i32>, i32) {
//    println!("{:?}", ns);
//    println!("{}", ns.len());

    if ns.len() <= 1 {
        return (ns, inversions);
    }
    let mid = if ns.len() == 2 { 1 } else { (ns.len() - 1) / 2 };
//    println!("ns: {:?}", ns);

//    println!("{}", mid);
//    println!("{:?}", 0..mid);
//    println!("{:?}", mid..ns.len());
//    println!();
//    println!("o: {}", inversions);
    let (b, inversions_b) = merge_sort(ns[0..mid].to_vec(), 0);
//    println!("b: {}", inversions_b);
    let (c, inversions_c) = merge_sort(ns[mid..ns.len()].to_vec(), 0);
//    println!("c: {}", inversions_c);
    let (d, inversions_i) = merge(
        b.to_vec(),
        c.to_vec(),
//        inversions_b + inversions_c
        0
    );
    let inversions_o = inversions_i + inversions_b + inversions_c;
//    let inversions_o = inversions_i;
//    println!("i: {}", inversions_o);
//    println!();

    (d, inversions_o)
}

fn merge(mut b: Vec<i32>, mut c: Vec<i32>, mut inversions: i32) -> (Vec<i32>, i32) {
    let mut d = Vec::new();
    let mut n_b = 0;
    while !b.is_empty() && !c.is_empty() {
        if b[0] > c[0] {
//            if b[0] != b[b.len()-1] {
//                n_b += 1;
//            }
            n_b += 1;
            inversions += 1;
            d.push(c[0]);
            c.remove(0);
        } else {
//            n_b += 1;
            d.push(b[0]);
            b.remove(0);
        }
//        if b[0] < c[0] {
////            inversions += 1;
//            d.push(b[0]);
//            b.remove(0);
//        } else {
//            inversions += 1;
//            d.push(c[0]);
//            c.remove(0);
//        }
//        println!("d: {:?}", d);
    }
    if !c.is_empty() {
//        inversions += (c.len() * d.len()) as i32;
        d.append(&mut c);
    } else {

        inversions += (b.len() * d.len() - n_b)  as i32;
        d.append(&mut b);
    }
    (d, inversions)
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




