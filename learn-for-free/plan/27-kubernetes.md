# Vol. 27 – Kubernetes – Study Plan

- Source site: https://kubernetes.io/docs/tutorials/
- Fetched: 2026-10-10
- Access: reachable
- Notes: Official community documentation, free without login; site docs are licensed CC BY 4.0, but avoid copying prose verbatim anyway.

## Learning path (source order)

1. **Hello Minikube** — Create a local cluster and deploy a demo app — https://kubernetes.io/docs/tutorials/hello-minikube/
2. **Create a Cluster (Learn Kubernetes Basics)** — Using Minikube to create a cluster — https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/
3. **Deploy an App** — Using kubectl to create a deployment — https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/
4. **Explore Your App** — Viewing pods and nodes — https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/
5. **Expose Your App Publicly** — Using a Service to expose your app — https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/
6. **Scale Your App** — Running multiple instances of your app — https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/
7. **Update Your App** — Performing a rolling update — https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/
8. **Updating configuration via a ConfigMap** — Example: configuring Redis — https://kubernetes.io/docs/tutorials/configuration/updating-configuration-via-a-configmap/
9. **Adopting sidecar containers** — Logging sidecar pattern — https://kubernetes.io/docs/tutorials/configuration/pod-sidecar-containers/
10. **Configure a Pod to use a PersistentVolume** — Storage for pods — https://kubernetes.io/docs/tutorials/configuration/configure-persistent-volume-storage/
11. **Apply Pod Security Standards at the cluster level** — Baseline enforcement — https://kubernetes.io/docs/tutorials/security/cluster-level-pss/
12. **Apply Pod Security Standards at the namespace level** — Namespace-scoped policy — https://kubernetes.io/docs/tutorials/security/ns-level-pss/
13. **Restrict a container's access with AppArmor** — Linux security module profiles — https://kubernetes.io/docs/tutorials/security/apparmor/
14. **Restrict a container's syscalls with seccomp** — Sandboxing syscall surface — https://kubernetes.io/docs/tutorials/security/seccomp/
15. **Deploy a release using a canary deployment** — Gradual rollout strategy — https://kubernetes.io/docs/tutorials/stateless-application/canary-deployment/
16. **Exposing an external IP address** — Direct external access to an app — https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/
17. **Example: PHP Guestbook with Redis** — Multi-tier stateless app — https://kubernetes.io/docs/tutorials/stateless-application/guestbook/
18. **StatefulSet basics** — Stable identity for stateful workloads — https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
19. **Example: WordPress and MySQL with Persistent Volumes** — Stateful app with storage — https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
20. **Example: Cassandra with a StatefulSet** — Distributed database on Kubernetes — https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
21. **Running ZooKeeper, a distributed system coordinator** — Ensemble deployment — https://kubernetes.io/docs/tutorials/stateful-application/zookeeper/
22. **Running Kubelet in standalone mode** — Node agent outside a cluster — https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
23. **Configuring swap memory on Kubernetes nodes** — Operating node swap — https://kubernetes.io/docs/tutorials/cluster-management/provision-swap-memory/
24. **Use pod-level resources with kubelet resource managers** — Pod-level resource allocation — https://kubernetes.io/docs/tutorials/cluster-management/use-pod-level-resource-managers/

## Planned chapters for the volume

1. Kubernetes architecture: cluster, control plane, objects (basis; covers source items: 1–2 background)
2. Creating a local cluster with Minikube (covers source items: 1, 2)
3. Deploying apps with kubectl (covers source items: 3)
4. Pods and nodes in depth (covers source items: 4)
5. Services and networking (covers source items: 5, 16)
6. Scaling and rolling updates (covers source items: 6, 7)
7. Configuration with ConfigMaps and sidecars (covers source items: 8, 9)
8. Storage and PersistentVolumes (covers source items: 10)
9. Stateless applications and deploy strategies (covers source items: 15, 16, 17)
10. Stateful applications (covers source items: 18–21)
11. Security: Pod Security Standards, AppArmor, seccomp (covers source items: 11–14)
12. Cluster administration basics (covers source items: 22–24)

## Flags / issues

- The tutorials page fetch was truncated (~45 KB); 24 TOC items were extracted from the visible tutorial sections (Basics, Configuration, Security, Stateless, Stateful, Cluster Management). Chapters group these official tutorials rather than copying their text.
- kubernetes.io docs are freely accessible and CC BY 4.0 licensed; still paraphrasing, not copying, to stay safe.
