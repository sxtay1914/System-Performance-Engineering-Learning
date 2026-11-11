# 21-day daily roadmap

Use the daily rhythm in START-HERE. Every day includes recall, reading, practice and an evidence entry. Commands are tool suggestions, not a requirement to install every tool. Refer to the labs for boundaries and cleanup.

## Day 1: Performance methodology

- [ ] **Understand:** USE; utilisation versus saturation; latency versus throughput; symptoms versus causes.
- [ ] **Read:** Methodology and observability; use the reading map to select a short section.
- [ ] **Practise:** Record a baseline using top, vmstat and pidstat where available; identify what each measures.
- [ ] **Demonstrate:** Explain your first three checks for a slow backend.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 1: Performance methodology. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain your first three checks for a slow backend.”

## Day 2: Linux execution model

- [ ] **Understand:** Kernel/user space; processes and threads; states; system calls; signals; file descriptors; permissions.
- [ ] **Read:** Operating systems; use the reading map to select a short section.
- [ ] **Practise:** Inspect a small service with ps/pstree/lsof; trace a process you own with strace; compare graceful termination and forced exit on a disposable process.
- [ ] **Demonstrate:** Explain a process state, an open descriptor and SIGTERM versus SIGKILL.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 2: Linux execution model. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain a process state, an open descriptor and SIGTERM versus SIGKILL.”

## Day 3: CPU and scheduling

- [ ] **Understand:** User/system time; per-core usage; run queues; context switches; multicore behaviour; load average.
- [ ] **Read:** CPUs; use the reading map to select a short section.
- [ ] **Practise:** Run a bounded CPU workload; compare top, mpstat, vmstat and pidstat before/during/after.
- [ ] **Demonstrate:** Distinguish high utilisation from saturation and interpret load relative to CPU count.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 3: CPU and scheduling. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can distinguish high utilisation from saturation and interpret load relative to CPU count.”

## Day 4: Memory

- [ ] **Understand:** Virtual versus resident memory; paging; minor/major faults; cache; swapping; leaks; OOM.
- [ ] **Read:** Memory; use the reading map to select a short section.
- [ ] **Practise:** Observe free -h, vmstat and pmap on a bounded allocation workload; inspect permitted kernel logs.
- [ ] **Demonstrate:** Explain why low free memory alone is insufficient evidence of pressure.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 4: Memory. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain why low free memory alone is insufficient evidence of pressure.”

## Day 5: Filesystems and storage

- [ ] **Understand:** Inodes; filesystem capacity; IOPS; throughput; latency; buffered/direct I/O.
- [ ] **Read:** File systems and disks; use the reading map to select a short section.
- [ ] **Practise:** Inspect df -h, df -i, du, lsblk and iostat while making a small temporary file.
- [ ] **Demonstrate:** Distinguish capacity, inode exhaustion and I/O performance problems.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 5: Filesystems and storage. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can distinguish capacity, inode exhaustion and I/O performance problems.”

## Day 6: Linux investigation practice

- [ ] **Understand:** Baselines; interval sampling; USE across CPU/memory/storage; observation versus inference.
- [ ] **Read:** Methodology revisit; use the reading map to select a short section.
- [ ] **Practise:** Complete Lab A without receiving the cause up front.
- [ ] **Demonstrate:** Support a diagnosis with two observations and one alternative explanation.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 6: Linux investigation practice. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can support a diagnosis with two observations and one alternative explanation.”

## Day 7: Linux checkpoint

- [ ] **Understand:** Recall and combine Days 1–6.
- [ ] **Read:** Review only; use the reading map to select a short section.
- [ ] **Practise:** Repeat one unfamiliar Linux incident and write a short incident report.
- [ ] **Demonstrate:** Identify the affected resource, process, evidence and recovery; review weak areas.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 7: Linux checkpoint. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can identify the affected resource, process, evidence and recovery; review weak areas.”

## Day 8: IP and local delivery

- [ ] **Understand:** TCP/IP layers; IPv4; CIDR; subnetting; routes; ARP; NAT.
- [ ] **Read:** Networking course material; use the reading map to select a short section.
- [ ] **Practise:** Inspect ip addr and ip route; explain a local destination and a routed destination; solve two CIDR examples.
- [ ] **Demonstrate:** Describe the next hop and where address translation may occur.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 8: IP and local delivery. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can describe the next hop and where address translation may occur.”

## Day 9: TCP, UDP and sockets

- [ ] **Understand:** Ports; listen/bind/connect; handshake; termination; connection states; loss and retransmission.
- [ ] **Read:** Networking, selective; use the reading map to select a short section.
- [ ] **Practise:** Start a local HTTP service; inspect ss; capture only its traffic with tcpdump if permitted.
- [ ] **Demonstrate:** Explain a successful TCP connection and why UDP behaves differently.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 9: TCP, UDP and sockets. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain a successful TCP connection and why UDP behaves differently.”

## Day 10: DNS, HTTP and TLS

- [ ] **Understand:** DNS resolution; HTTP request/response; HTTPS; certificate validation; conceptual TLS handshake.
- [ ] **Read:** Networking and protocol material; use the reading map to select a short section.
- [ ] **Practise:** Compare dig/nslookup, curl -v and local listener output; separate DNS, TCP, TLS and HTTP failures.
- [ ] **Demonstrate:** Explain each stage between a URL and an HTTP response.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 10: DNS, HTTP and TLS. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain each stage between a URL and an HTTP response.”

## Day 11: Network troubleshooting

- [ ] **Understand:** Refused versus timeout versus reset; DNS failures; firewall clues; packet evidence.
- [ ] **Read:** Networking reference; use the reading map to select a short section.
- [ ] **Practise:** Complete Lab B; use explicit short connect/request timeouts.
- [ ] **Demonstrate:** Localise failure to a layer without treating one error message as proof.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 11: Network troubleshooting. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can localise failure to a layer without treating one error message as proof.”

## Day 12: Docker foundations

- [ ] **Understand:** Containers versus VMs; images; Dockerfiles; lifecycle; namespaces/cgroups; volumes.
- [ ] **Read:** Docker documentation; use the reading map to select a short section.
- [ ] **Practise:** Build or run a small local service; inspect logs, process, environment, resource settings and a mounted volume.
- [ ] **Demonstrate:** Explain image/container distinction, persistence and host/container boundaries.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 12: Docker foundations. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain image/container distinction, persistence and host/container boundaries.”

## Day 13: Docker networking and resources

- [ ] **Understand:** User-defined networks; container DNS; container ports versus published ports; CPU/memory constraints.
- [ ] **Read:** Docker documentation; use the reading map to select a short section.
- [ ] **Practise:** Connect two containers on one network and complete Lab C.
- [ ] **Demonstrate:** Explain why localhost inside one container does not refer to the other.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 13: Docker networking and resources. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain why localhost inside one container does not refer to the other.”

## Day 14: Container checkpoint

- [ ] **Understand:** Exited/restarting containers; logs; resource usage; environment; network evidence.
- [ ] **Read:** Review only; use the reading map to select a short section.
- [ ] **Practise:** Diagnose two unknown container failures and recreate a container while retaining volume data.
- [ ] **Demonstrate:** Restore communication and explain the exact fault and persistence behaviour.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 14: Container checkpoint. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can restore communication and explain the exact fault and persistence behaviour.”

## Day 15: Kubernetes architecture

- [ ] **Understand:** API server; etcd; scheduler; controllers; kubelet; runtime; nodes; Pods; Deployments; ReplicaSets.
- [ ] **Read:** Kubernetes documentation; use the reading map to select a short section.
- [ ] **Practise:** Create a local cluster and lab namespace; deploy a tiny service; inspect ownership and events.
- [ ] **Demonstrate:** Trace desired state from Deployment to running container.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 15: Kubernetes architecture. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can trace desired state from Deployment to running container.”

## Day 16: Configuration, storage and probes

- [ ] **Understand:** Namespaces; ConfigMaps; Secrets; PV/PVC; requests/limits; readiness/liveness/startup probes.
- [ ] **Read:** Kubernetes documentation; use the reading map to select a short section.
- [ ] **Practise:** Add configuration and probes; inspect declared resources and local storage provisioner behaviour.
- [ ] **Demonstrate:** Explain readiness removal from endpoints versus liveness restart; base64 is not encryption.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 16: Configuration, storage and probes. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain readiness removal from endpoints versus liveness restart; base64 is not encryption.”

## Day 17: Kubernetes networking

- [ ] **Understand:** Pod IPs; Services; ClusterIP/NodePort/LoadBalancer; DNS; Ingress; CNI; NetworkPolicy.
- [ ] **Read:** Kubernetes documentation; use the reading map to select a short section.
- [ ] **Practise:** Inspect Service selectors and EndpointSlices; test DNS and HTTP from a debug Pod.
- [ ] **Demonstrate:** Trace client to Service to ready Pod; explain controller/CNI prerequisites.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 17: Kubernetes networking. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can trace client to Service to ready Pod; explain controller/CNI prerequisites.”

## Day 18: Pod lifecycle failures

- [ ] **Understand:** CrashLoopBackOff; ImagePullBackOff; Pending; OOMKilled; events and previous logs.
- [ ] **Read:** Kubernetes troubleshooting; use the reading map to select a short section.
- [ ] **Practise:** Complete Lab D cases 1–3; interpret status reasons rather than memorising labels.
- [ ] **Demonstrate:** Identify the failing stage and choose the next useful diagnostic command.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 18: Pod lifecycle failures. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can identify the failing stage and choose the next useful diagnostic command.”

## Day 19: Resources and connectivity

- [ ] **Understand:** CPU throttling; memory limits; probe failures; Service connectivity; metrics limitations.
- [ ] **Read:** Book reference plus Kubernetes; use the reading map to select a short section.
- [ ] **Practise:** Complete Lab D cases 4–6; compare declared limits, events, logs and observed usage.
- [ ] **Demonstrate:** Distinguish app failure, readiness failure, selector mismatch and resource constraints.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 19: Resources and connectivity. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can distinguish app failure, readiness failure, selector mismatch and resource constraints.”

## Day 20: Cloud infrastructure concepts

- [ ] **Understand:** Multi-tenancy; quotas; namespace limits; isolation; service mesh; Envoy; mTLS; retries; HA; failover.
- [ ] **Read:** Kubernetes, Istio and distributed-systems material; use the reading map to select a short section.
- [ ] **Practise:** Review a two-tenant design; discuss noisy neighbours and retry amplification; stop one local replica.
- [ ] **Demonstrate:** Explain why namespaces alone are not a complete security boundary and why replicas need failure-domain separation.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 20: Cloud infrastructure concepts. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can explain why namespaces alone are not a complete security boundary and why replicas need failure-domain separation.”

## Day 21: Final incident and review

- [ ] **Understand:** Combine Linux, network, container and Kubernetes reasoning.
- [ ] **Read:** Targeted review; use the reading map to select a short section.
- [ ] **Practise:** Complete Lab E; give a 5-minute incident explanation and prioritise remaining gaps.
- [ ] **Demonstrate:** Independently diagnose an unfamiliar failure, verify recovery and propose prevention.
- [ ] **Record:** prediction, actual evidence, interpretation, cleanup and one unresolved question.

**AI prompt:** “Start Day 21: Final incident and review. Follow the tutor contract, check my prerequisites, and guide one exercise at a time. Assess whether I can independently diagnose an unfamiliar failure, verify recovery and propose prevention.”

