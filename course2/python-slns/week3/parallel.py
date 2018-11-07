# python3
import heapq


# noinspection PyAttributeOutsideInit
class JobQueue:
    def read_data_stdin(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        # self.jobs_naive = self.jobs
        assert m == len(self.jobs)

    def read_data(self, jobs, num_workers):
        self.jobs = jobs
        self.jobs_naive = jobs
        self.num_workers = num_workers

    def write_response_naive(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def write_response(self):
        for t in self.times:
            print(t[0], t[1])
        # for i in range(len(self.jobs)):
        #     print(self.times[0], self.times[1])

    def assign_jobs_naive(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs_naive)
        self.start_times = [None] * len(self.jobs_naive)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs_naive)):
            next_worker = 0
            for j in range(self.num_workers):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j
            self.assigned_workers[i] = next_worker
            self.start_times[i] = next_free_time[next_worker]
            next_free_time[next_worker] += self.jobs_naive[i]

        self.times_naive = []
        for i in range(len(self.jobs_naive)):
            self.times_naive.append(
                    (self.assigned_workers[i],
                     self.start_times[i]))

    def assign_jobs(self):
        times = []
        running_jobs = []  # this is a heap
        # Initialize threads
        acc_times = {}
        threads = []
        prev_job = 0
        for i in range(self.num_workers):
            acc_times[i] = 0
            threads.append(i)
        heapq.heapify(threads)
        while len(self.jobs) > 0:
            # Get current job
            while len(threads) > 0:
                if len(self.jobs) <= 0:
                    break
                job = self.jobs[0]
                self.jobs = self.jobs[1:] if len(self.jobs) > 0 else []
                # Get thread
                thread = heapq.heappop(threads)
                # Append current time
                times.append((thread, acc_times[thread]))
                # Update time taken for thread
                acc_times[thread] += job
                heapq.heappush(running_jobs, (job+prev_job, thread))
                # Complete jobs
            # update_threads, running_jobs = self.pop_jobs(running_jobs)
            update_threads, prev_job = self.pop_jobs(running_jobs)
            for t in update_threads:
                heapq.heappush(threads, t)

        self.times = times

    # def update_heap(self, heap, x):
    #     # heap = list(map(lambda i: (i[0] - x, i[1]), heap))
    #     heap = [(i[0] - x, i[1]) for i in heap]
    #     # heapq.heapify(heap)
    #     return heap

    def pop_jobs(self, running_jobs):
        if len(running_jobs) <= 0:
            # return [], []
            return [], 0
        j_f, thread = heapq.heappop(running_jobs)
        threads = [thread]
        # Need to update time of running jobs after every pop
        while True:
            if len(running_jobs) > 0 and running_jobs[0][0] == j_f:
                _, thread = heapq.heappop(running_jobs)
                threads.append(thread)
            else:
                break
        return threads, j_f

    def solve(self):
        self.read_data()
        self.assign_jobs_naive()
        self.write_response()


if __name__ == '__main__':
    # job_queue = JobQueue()
    # job_queue.read_data_stdin()
    # job_queue.assign_jobs()
    # job_queue.write_response()

    # num_workers = 4
    # jobs = [1 for _ in range(0, 20)]
    # job_queue = JobQueue()
    # job_queue.read_data(jobs, num_workers)
    # job_queue.assign_jobs()
    # job_queue.write_response()
    # # # num_workers = 2
    # # # jobs = [1, 2, 3, 4, 5]
    # #
    import random
    n_exp = 1
    m = 10 ** 5
    n = 10 ** 5
    t = 10 ** 9

    random.seed(1)
    num_workers = [random.randint(1, n) for _ in range(n_exp)]
    jobs = [[random.randint(1, t) for _ in range(m)] for _ in range(n_exp)]
    for job, nw in list(zip(jobs, num_workers)):
        job_queue = JobQueue()
        job_queue.read_data(job, nw)
        # job_queue.assign_jobs_naive()
        job_queue.assign_jobs()
        # print(job_queue.times_naive)
        print(job_queue.times)
        # if job_queue.times != job_queue.times_naive:
        #     print('FAIL')
        # print(job_queue.times_naive)
        # print(job_queue.times)
        # break
        print()
