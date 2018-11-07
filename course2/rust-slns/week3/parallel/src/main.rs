#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(unused_variables)]

extern crate rand;
use self::rand::{Rng, SeedableRng, StdRng };

use std::fmt;
use std::collections::binary_heap::BinaryHeap;
use std::collections::binary_heap;
use std::collections::VecDeque;
use std::cmp::Ordering;



/// 1 <= n <= 10^5
/// 1 <= m <= 10^5
/// 0 <= t_i <= 10^9
pub fn main() {
    let (n, m, t) = read_data();
    let jobs = build_jobs(t);
    let threads = build_threads(n);
    let times = assign_jobs(jobs, threads);
    for t in times {
        println!("{} {}", &t.0, &t.1);
    }

//    for i in 0..jobs.len() {
//        println!("{}", jobs.pop().unwrap().id);
//    }
//    let jobs = build_jobs(vec![1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]);
//    let threads = build_threads(4);
//    let jobs = build_jobs(vec![1, 2, 3, 4, 5]);
//    let threads = build_threads(2);

//    let i = 1;
//    let mut rng: StdRng = SeedableRng::from_seed([1u8; 32]);
//    for _ in 0..i {
//        let jobs = build_jobs(t);
//        let threads = build_threads(n);
//        let times = assign_jobs(jobs, threads);
//
//        let q = JobQueue { n_jobs: m, n, jobs: t };
//        println!("{}", q);
//        let r = q.assign_jobs_naive();
//        r.write_resp();
//        println!();
//    }



//    let jobs = build_jobs(t);
//    let threads = build_threads(n);
//    let times = assign_jobs(jobs, threads);
//    for t in times {
//        println!("{} {}", &t.0, &t.1);
//    }
}


fn assign_jobs(mut jobs: VecDeque<Job>, mut threads: Vec<Thread>) -> Vec<(usize, i32)> {
//    let mut assigned_jobs: Vec<(usize, i32)> = Vec::new();
    let mut times: Vec<(usize, i32)> = Vec::new();
    let mut running_jobs = BinaryHeap::new();

    let n = threads.len()-1;

    // All threads start not being busy
    let mut threads_h = BinaryHeap::new();
    for i in 0..threads.len() {
        threads_h.push(i);
    }
    let mut prev_time = 0;
    while !jobs.is_empty() {
//        for i in 0..threads.len() {
//            print!("{:?} ", &threads[i].time);
//        }
//        for i in running_jobs {
//            println!("{:?}", &i.thread_id)
//        }
        // Check to see if any threads are available
        // If thread is not busy, assign it a job
        while !(threads_h).is_empty() {
            if jobs.is_empty() {
                break
            }
            let job = jobs.pop_front().unwrap();
            let t = threads_h.pop().unwrap();

            // Update time tracker for job
            times.push((n - t, threads[t].time - prev_time));
            threads[t].job_id = job.id;
            threads[t].time += job.time + prev_time;
            running_jobs.push(Job {
                thread_id: t,
                ..job
            });
        }
        // Pop jobs
        let mut update_threads: Vec<usize> = Vec::new();
        if !running_jobs.is_empty() {
            let j_f = running_jobs.pop().unwrap();
            update_threads.push(j_f.thread_id);
            prev_time = j_f.time;
            loop {
                if !running_jobs.is_empty() {
                    if running_jobs.peek().unwrap().time == j_f.time {
                        let j_f2 = running_jobs.pop().unwrap();
                        update_threads.push(j_f2.thread_id)
                    } else {
                        break
                    }
                } else {
                    break
                }
            }
        } else {
            prev_time = 0
        }
        if !update_threads.is_empty() {
            for t in update_threads {
                threads_h.push(t)
            }
        }
    }
    times
}

fn build_jobs(jobs: Vec<i32>) -> VecDeque<Job> {
    (0..jobs.len()).zip(jobs).map(|x| -> Job {
        Job { thread_id: 0, id: x.0, time: x.1 }
    }).collect()
}

fn build_jobs_heap(jobs: Vec<i32>) -> BinaryHeap<Job> {
    let mut h = BinaryHeap::new();
    for i in 0..jobs.len() {
        h.push(Job { thread_id: 0, id: i, time: jobs[i] });
    }
    h
}

//fn build_threads_heap(n: usize) -> BinaryHeap<Thread> {
//    let mut h = BinaryHeap::new();
//    for i in 0..n {
//        h.push(Thread { busy: false, time: 0, job_id: 0, id: i });
//    }
//    h
//}

fn build_threads(n: usize) -> Vec<Thread> {
    let mut h = Vec::new();
    for i in 0..n {
        h.push(Thread { busy: false, time: 0, job_id: 0, id: i });
    }
    h
}
/*
THREAD
*/

struct Thread { busy: bool, time: i32, job_id: usize, id: usize }
//
//impl PartialEq for Thread {
//    fn eq(&self, other: &Thread) -> bool {
//        self.id == other.id
//    }
//}
//
//impl PartialOrd for Thread {
//    fn partial_cmp(&self, other: &Thread) -> Option<Ordering> {
//        Some(self.cmp(other))
//    }
//}
//
//impl Eq for Thread {}
//
//impl Ord for Thread { fn cmp(&self, other: &Self) -> Ordering { other.id.cmp(&self.id) } }

/*
JOB
*/
struct Job { thread_id: usize, id: usize, time: i32 }

impl PartialEq for Job {
    fn eq(&self, other: &Job) -> bool {
        self.time == other.time
    }
}

impl PartialOrd for Job {
    fn partial_cmp(&self, other: &Job) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Eq for Job {}

impl Ord for Job { fn cmp(&self, other: &Self) -> Ordering { other.time.cmp(&self.time) } }


struct JobQueue {
    n_jobs: usize,
    n: usize,
    jobs: Vec<i32>,
}

struct Res {
    next_free_time: Vec<i32>,
    start_times: Vec<i32>,
    assigned_workers: Vec<i32>,
}

impl Res {
    fn write_resp(&self) {
        for i in 0..self.assigned_workers.len() {
            println!("{} {}", self.assigned_workers[i], self.start_times[i])
        }
    }
}

fn read_data() -> (usize, usize, Vec<i32>) {
    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let i: Vec<usize> = buff.split_whitespace().map(|x| -> usize { x.to_string().parse().unwrap() }).collect();
    let n = i[0];
    let m = i[1];

    let mut buff = String::new();
    ::std::io::stdin().read_line(&mut buff).expect("Could not read line");
    let t = buff.split_whitespace().map(|s| -> i32 {
        s.to_string().parse().unwrap()
    }).collect::<Vec<i32>>();
    (n, m, t)
}

impl JobQueue {
    fn assign_jobs_naive(&self) -> Res {
        let mut assigned_workers: Vec<i32> = vec![0; self.n_jobs];
        let mut start_times: Vec<i32> = vec![0; self.n_jobs];
        let mut next_free_time = vec![0; self.n];

        for i in 0..self.jobs.len() {
            let mut next_worker = 0;
            for j in 0..self.n {
                if next_free_time[j] < next_free_time[next_worker] {
                    next_worker = j;
                }
            }
            assigned_workers[i] = next_worker as i32;
            start_times[i] = next_free_time[next_worker];
            next_free_time[next_worker] += self.jobs[i];
        }

        Res {
            next_free_time,
            start_times,
            assigned_workers,
        }
    }
}


impl fmt::Display for JobQueue {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "num_jobs: {}, n: {}, jobs: {:?}", self.n_jobs, self.n, self.jobs)
    }
}

