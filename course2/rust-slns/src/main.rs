
use std::collections::VecDeque;
pub fn main() {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let n: i32 = buff.split_whitespace().next().unwrap().parse().unwrap();

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let parents = buff.split_whitespace();

    let values = parents.map(|s| -> i32 {
        s.to_string().parse().unwrap()
    }).collect::<Vec<i32>>();


    let (nodes, root) = build_tree(&n, &values);
//    for node in nodes {
//        println!("{:?}", node)
//    }
    let output = tree_height(nodes, root);
    println!("{}", output);
}


fn build_tree(n: &i32, parents: &Vec<i32>) -> (Vec<Vec<i32>>, usize) {
    let mut root = 0;
    let mut nodes: Vec<Vec<i32>> = vec![vec![]; *n as usize];

    for child_ix in 0..*n as usize {
        let parent_ix = parents[child_ix];
        if parent_ix == -1 {
            root = child_ix
        } else {
            nodes[parent_ix as usize].push(child_ix as i32);
        }
    }

    (nodes, root)
}

fn tree_height(tree: Vec<Vec<i32>>, root: usize) -> i32 {
    let mut q: VecDeque<&Vec<i32>> = VecDeque::new();
    let mut q_h: VecDeque<i32> = VecDeque::new();
    let mut hs: Vec<i32> = Vec::new();
    q.push_back(&tree[root]);
    q_h.push_back(1);
    while !q.is_empty() {
        let node = q.pop_front().unwrap();
        let h = q_h.pop_front().unwrap();
        if !node.is_empty() {
            for child in node  {
                q.push_back(&tree[*child as usize]);
                q_h.push_back(h + 1)
            }
        } else {
            hs.push(h)
        }
    }
    *hs.iter().max().unwrap()
}
