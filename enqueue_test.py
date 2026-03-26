import json
import copy
from redis import Redis
from rq import Queue

r = Redis(host='localhost', port=6379, password='')

q1    = Queue('coda_agente1', connection=r)
q2    = Queue('coda_agente2', connection=r)
q_aws = Queue('coda_aws',     connection=r)

with open("deployment_info.json", "r") as f:
    job1 = json.load(f)

job2 = copy.deepcopy(job1)
job2["deployment_uuid"] = "deploy-2"

with open("deployment_info_aws.json", "r") as f:
    job3 = json.load(f)
job3["deployment_uuid"] = "deploy-3"

r1 = q1.enqueue("worker_wrapper.run_from_dict", job1, job_timeout=7200)
r2 = q2.enqueue("worker_wrapper.run_from_dict", job2, job_timeout=7200)
r3 = q_aws.enqueue("terraform_agent.run_orchestration", job3, job_timeout=7200)

print(f"Job 1 (agent1) enqueued: {r1.id}")
print(f"Job 2 (agent2) enqueued: {r2.id}")
print(f"Job 3 (aws)     enqueued: {r3.id}")
