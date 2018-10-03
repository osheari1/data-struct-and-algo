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

//    let out = run(&ln, &n, &lk, &k);
//    for o in out {
//        print!("{} ", o);
//    }
}

// TODO: Update partition function to use partition3 for equal elements
pub fn merge_sort(ns: Vec<i32>) -> Vec<i32> {
//    println!("{:?}", ns);
//    println!("{}", ns.len());
    if ns.len() <= 1 {
        return ns;
    }
    let mid = if ns.len() == 2 { 1 } else { (ns.len() - 1) / 2};
//    print!("{:?}", ns);
//    print!("{}", mid);

//    println!("{}", mid);
//    println!("{:?}", 0..mid);
//    println!("{:?}", mid..ns.len());
//    println!();
    let b = merge_sort(ns[0..mid].to_vec());
    let c = merge_sort(ns[mid..ns.len()].to_vec());
    let d = merge(b.to_vec(), c.to_vec());
//    print!("{:?}", b);
//    print!("{:?}", c);

    d
}

fn merge(mut b: Vec<i32>, mut c: Vec<i32>) -> Vec<i32> {
//    let mut d = vec![0; b.len() + c.len()];
    let mut d = Vec::new();
    let mut b_i = 0 as usize;
    let mut c_i = 0 as usize;
    while b_i < b.len() && c_i < c.len() {
//        println!("b_i: {}", b_i);
//        println!("c_i: {}", c_i);
        if b[b_i] <= c[c_i] {
            d.push(b[b_i]);
            b_i += 1;
        } else {
            d.push(c[c_i]);
            c_i += 1;
        }
    }
    if b_i > b.len() && c_i > c.len() {
        return d
    } else if b_i > b.len() {
        d.append(&mut c);
    } else {
        d.append(&mut b);
    }
    d
}





