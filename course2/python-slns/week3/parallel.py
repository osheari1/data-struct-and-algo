import heapq


# noinspection PyAttributeOutsideInit
class JobQueue:
    def read_data_stdin(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def read_data(self, jobs, num_workers):
        self.jobs = jobs
        self.num_workers = num_workers

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs_naive(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs[i]

    def assign_jobs(self):
        times = []
        running_jobs = None  # this is a heap
        threads = [x for x in range(self.num_workers)]
        heapq.heapify(threads)
        for t in threads:
            print(t)

    def solve(self):
        self.read_data()
        self.assign_jobs_naive()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    num_workers = 2
    jobs = [1, 2, 3, 4, 5]
    job_queue.read_data(jobs, num_workers)
    job_queue.assign_jobs()
    # job_queue.solve()
