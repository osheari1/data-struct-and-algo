pub fn main() {
    // Read
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let mut numbers = buff.split_whitespace();
    let n: i32  = numbers.next().unwrap().parse().unwrap();
    let cap: f32  = numbers.next().unwrap().parse().unwrap();

    let mut x: Vec<(f32, f32, f32)> = Vec::new();
    for _ in 1..n+1 {
        let mut buff = String::new();
        ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
        let mut numbers = buff.split_whitespace();
        let v: f32  = numbers.next().unwrap().parse().unwrap();
        let w: f32  = numbers.next().unwrap().parse().unwrap();
        let v_w: f32 = v / w;
        x.push((v, w, v_w));
    }

    println!("{}", run(x, cap));
}

fn run(mut x: Vec<(f32, f32, f32)>, cap: f32) -> f32 {
    x.sort_by(|x, y| y.2.partial_cmp(&x.2).unwrap());
    let mut current_weight: f32 = 0.0;
    let mut current_value: f32 = 0.0;
    for x_i in x {
        let condition = x_i.1 + current_weight;
        if condition == cap {
            current_weight += x_i.1;
            current_value += x_i.0;
            break
        } else if condition < cap {
            current_weight += x_i.1;
            current_value += x_i.0;
        } else if  condition > cap {
            let remaining_weight: f32 = cap - current_weight;
            current_weight += remaining_weight;
            current_value = (remaining_weight / x_i.1) * x_i.0;
        }
    }
    current_value
}

