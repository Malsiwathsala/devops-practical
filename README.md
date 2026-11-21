# DevOps Practical — devops-practical

A simple Flask web application built for a university DevOps practical assignment.

## Features

- `/` — Returns `{"message": "CI/CD and Docker Pipeline is a massive success! V2", "version": "2.0"}`
- `/health` — Returns `{"status": "healthy"}`

## Tech Stack

- **Python 3.12** + **Flask 3.0**
- **pytest** for automated testing
- **Docker** for containerisation
- **GitHub Actions** for CI/CD
- **Render** for cloud hosting

## Local Development

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate   # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest test_app.py -v

# Run the app
python app.py
```

## CI/CD

Pull requests and pushes to `main` run the automated tests on GitHub Actions.
On `main`, pushes and manual workflow runs publish to Docker Hub after the tests pass.
Configure the repository secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` for the publishing job.

## Kubernetes demonstration

The **Minikube Self-Healing** GitHub Actions workflow runs the demonstration on
a temporary Ubuntu runner. Its run summary records the Service health response,
the pod names and UIDs before and after deletion, and the final replica count.
This uses Minikube with the Docker driver on a hosted Linux VM, so Windows and
WSL are outside the cluster setup.

Once Docker Hub lists `malsiwathsala/devops-practical:v1`, open a
[Killercoda Kubernetes playground](https://killercoda.com/playgrounds/scenario/kubernetes)
or use Minikube. In the cluster terminal, clone this repository and run the following
from its root.

```bash
kubectl apply -f k8s/
kubectl rollout status deployment/devops-practical --timeout=120s
kubectl get deployment,service,pods -l app=devops-practical
```

List the pods before deleting one and record their names and UIDs. Use a
second terminal to watch the replacement start.

```bash
kubectl get pods -l app=devops-practical -w
```

In the first terminal, replace `POD_NAME` with one of the two running pod names.

```bash
kubectl get pods -l app=devops-practical -o custom-columns=NAME:.metadata.name,UID:.metadata.uid,PHASE:.status.phase
kubectl delete pod POD_NAME
kubectl wait --for=condition=Available deployment/devops-practical --timeout=120s
kubectl get deployment devops-practical
kubectl get pods -l app=devops-practical -o custom-columns=NAME:.metadata.name,UID:.metadata.uid,PHASE:.status.phase
```

Capture the final output when the Deployment shows two ready replicas and a
new pod has replaced the deleted one. To check the Service, run
`kubectl port-forward service/devops-practical 8080:80` and use a second shell
to run `curl -fsS http://localhost:8080/health`.

Killercoda uses a temporary hosted kubeadm cluster. The manifests and recovery
steps also apply on Minikube. If the rubric explicitly requires Minikube, ask
the instructor whether the hosted demonstration is accepted.

## Render

Connect the GitHub repository to Render and use `render.yaml` to create a free
Docker web service on `main`. The Blueprint sets auto-deploy to On Commit and
uses `/health` for the health check. The application binds to Render's
`PORT` with a local fallback of 5000.

Verify the initial deployment's `/` and `/health` responses before pushing the
V2 release. Record the public URL and the live deploy's commit after each push.
