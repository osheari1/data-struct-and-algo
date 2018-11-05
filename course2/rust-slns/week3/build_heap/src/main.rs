
pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let _n: i32 = buff.split_whitespace().next().unwrap().parse().unwrap();

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");

    let mut values = buff.split_whitespace().map(|s| -> i64 {
        s.to_string().parse().unwrap()
    }).collect::<Vec<i64>>();

    let swaps = build_heap(&mut values);
    println!("{}", swaps.len());
    for s in swaps {
        println!("{} {}", s.0, s.1)
    }
}

fn build_heap(arr: &mut Vec<i64>) -> (Vec<(usize, usize)>) {
    let mut swaps: Vec<(usize, usize)> = Vec::new();

    let mut i = (arr.len() as f32 / 2.0).floor() as i32;
    while i >= 0 {
        sift_down(&mut swaps, arr, i as usize);
        i -= 1;
    }
    swaps
}

fn sift_down(swaps: &mut Vec<(usize, usize)>, arr: &mut Vec<i64>, i: usize) {
    let mut min_ix = i;
    let l = left_child(i);
    let r = right_child(i);

    if l <= arr.len()-1 && arr[l] < arr[min_ix] {
        min_ix = l
    }
    if r <= arr.len()-1 && arr[r] < arr[min_ix] {
        min_ix = r
    }
    if i != min_ix {
        swap(swaps, arr, i, min_ix);
        sift_down(swaps, arr, min_ix)
    }
}

fn swap(swaps: &mut Vec<(usize, usize)>, arr: &mut Vec<i64>, i: usize, j: usize) {
    let tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
    swaps.push((i, j));
}

//fn parent(i: usize) -> usize {
//    (((i - 1) as f64) / 2.0).floor() as usize
//}

fn left_child(i: usize) -> usize {
    2 * i + 1
}

fn right_child(i: usize) -> usize {
    2 * i + 2
}


