from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, Counter

registryA = CollectorRegistry()
g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished',['pipeline'], registry=registryA)
g.labels('eda_pipeline_1').set_to_current_time()

c = Counter('job_failures', 'Description of counter',['pipeline'], registry=registryA)
c.labels('eda_pipeline_1').inc()     # Increment by 1
c.labels('eda_pipeline_1').inc(1.6)  # Increment by given value

push_to_gateway('localhost:9091', job='DataBricksDev', registry=registryA)

# Creating a batchB

registryB = CollectorRegistry()
c = Counter('job_failures', 'Description of counter',['pipeline'], registry=registryB)
c.labels('eda_pipeline_2').inc()
c.labels('eda_pipeline_2').inc(250)

push_to_gateway('localhost:9091', job='batchB', registry=registryB)
