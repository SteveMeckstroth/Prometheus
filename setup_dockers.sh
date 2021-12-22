#python -m pip install -r requirements.txt

# Create a network for the two containers to run within
docker network create -d bridge prometheus-network

docker run \
  --rm \
  --network prometheus-network \
  --hostname pushgateway_host \
  -d \
  -p 9091:9091 \
  prom/pushgateway

cd Prometheus
docker run \
  --rm \
  --network prometheus-network \
  --hostname prometheus_host \
  -d \
  -p 9090:9090 \
  -v ${PWD}/prometheus.yml:/etc/prometheus/prometheus.yml \
  -v ${PWD}/rules.yml:/etc/prometheus/rules.yml \
  prom/prometheus
