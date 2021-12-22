# Simple Docker setup to test/try out Prometheus with a push gateway

Run this command to get the dockers up and running:

### On Linux/Mac
```bash
sh setup_dockers.sh
```
### Windows
```cmd
setup_dockers.cmd
```

After they are running, you can run
```bash
python -m pip install -r requirements.txt
python prometheus_exporter.py
```

You can access the web interfaces at:<br />
[Push Gateway](http://localhost:9091)<br />
[Prometheus](http://localhost:9090)
