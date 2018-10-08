use std::num;
use std::cmp::min;
use std::f64;

pub fn main() {
    // Read
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let n: usize = numbers.next().unwrap().parse().unwrap();

    let mut ns: Vec<(i64, i64)> = vec![(0, 0); n];
    for i in 0..n {
        let mut buff = String::new();
        ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
        let mut numbers = buff.split_whitespace();
        let mut tup: (i64, i64)  = (0, 0);
        tup.0 = numbers.next().unwrap().parse().unwrap();
        tup.1 = numbers.next().unwrap().parse().unwrap();
        ns[i] = tup;
    }

    let dist = run(ns);
    print!("{} ", dist);
}

pub fn run(mut ns: Vec<(i64, i64)>) -> f64 {

   fn go(ns: &Vec<(i64, i64)>, l: usize, h: usize, min_dist: f64) -> f64 {
       // Calculate distance if only 2 points remain in subset
//       println!("h: {}", h);
//       println!("l: {}", l);
       if h - l == 1 {
           let dist = distance(ns[l], ns[h]);
//           println!("dist: {}", dist);
//           println!();
           return if dist < min_dist { dist } else { min_dist };
       }
       // If only one point remains return nothing
       if h - l == 0 {
           return min_dist;
       }


       let mid = l + (h - l) / 2;
//       println!("mid: {}", mid);
       // Calculate min dist of subsets
       let d_x = go(ns, l, mid-1, min_dist);
       let d_y = go(ns, mid, h, min_dist);
       let d = d_x.min(d_y);
//       println!("d_x: {}", d_x);
//       println!("d_y: {}", d_y);
//       println!("d: {}", d);
//       println!();
       // Mid line in x space separating s1 and s2
       let mid_line = ((ns[mid-1].0 + ns[mid].0) as f64) / 2.0;
//       let mid_line = ns[mid-1].0 as f64;
       // Keep elements whose distance to mid_line is <= d
       let mut ix_keep: Vec<usize> = Vec::new();
//       let mut ix_keep = (l..(h+1)).collect().un
       for i in l..(h+1) {
           if (ns[i].0 as f64 - mid_line).abs() <= d {
               ix_keep.push(i);
           }
       }
       // Sort by y coordinate
       let mut ns_keep: Vec<(i64, i64)> = ix_keep.iter()
           .map(|x| ns[*x]).collect();
       ns_keep.sort_by_key(|x| x.1);
//       println!("keep_ns: {:?}", ns_keep);
       let d_prime = run_naive(&ns_keep);
//       println!("d_prime: {:?}", d_prime);

       d.min(d_prime)
    }

    ns.sort_by_key(|k| k.0);
    go(&ns, 0, ns.len()-1, f64::INFINITY)
}



fn run_naive(ns: &Vec<(i64, i64)>) -> f64 {
    let mut min = f64::INFINITY;
    for point_x in 0..ns.len() {
        for point_y in 0..ns.len() {
            if point_x == point_y {
                continue;
            }
            let dist = distance(ns[point_x], ns[point_y]);
            if dist < min {
                min = dist;
            }
        }
    }
    min
}

pub fn distance(p1: (i64, i64), p2: (i64, i64)) -> f64 {
    (((p1.0 - p2.0).pow(2) + (p1.1 - p2.1).pow(2)) as f64).sqrt()
}




