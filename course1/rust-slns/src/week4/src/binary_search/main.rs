pub fn main() {
    // Read
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();

    let ln: usize = numbers.next().unwrap().parse().unwrap();
    let mut n = vec![0; ln];
    for i in 0..ln {
        n[i] = numbers.next().unwrap().parse().unwrap();
    }

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();

    let lk: usize = numbers.next().unwrap().parse().unwrap();
    let mut k = vec![0; lk];
    for i in 0..lk {
        k[i] = numbers.next().unwrap().parse().unwrap();
    }

    let out = run(&ln, &n, &lk, &k);
    for o in out {
        print!("{} ", o);
    }
}


pub fn run(ln: &usize, ns: &Vec<i32>, lk: &usize, ks: &Vec<i32>) -> Vec<i32> {
    fn go(ns: &Vec<i32>, h: usize, l: usize, key: i32) -> i32 {
        // If there is only one value left and it doesn't match, return -1
//        println!("ns: {:?}", ns);
//        println!("l: {}", l);
//        println!("h: {}", h);
//        println!("k: {}", key);
        if l >= h {
            if ns[l] == key {
                return l as i32;
            }
            return -1;
        }

        let mid = if (h - l) > 1 { l + (h - l) / 2 } else { l };

//        println!("mid: {}", mid);
//        println!();
        // Return the index if the mid matches the value
        if ns[mid] == key {
            return mid as i32;
        }

        match key < ns[mid] {
            true => {
                go(ns, if mid == 0 { mid } else { mid - 1 }, l, key)
            },
            false => {
                go(ns, h, if mid == ns.len() { mid } else { mid + 1 }, key)
            }
        }
    }

    let mut out_ix: Vec<i32> = vec![-1; *lk];
    for (i, k) in ks.iter().enumerate() {
        out_ix[i] = go(ns, *ln-1, 0, *k);
    }
    out_ix
}




