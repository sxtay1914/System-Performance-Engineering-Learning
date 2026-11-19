# Systems Performance reading map

Use Brendan Gregg's *Systems Performance: Enterprise and the Cloud* as the main reference for Linux resource behaviour and performance methodology. Do not read it cover to cover for this sprint.

The local PDF table of contents was verified on 2026-11-16: ISBN 978-0-13-339009-4, copyright 2014, second printing January 2014. The PDF is incomplete; verified section references below identify reading in the complete book, not text available locally. Page numbers are printed book pages.

| Days | Find these subject areas in your edition | Read for | Depth |
|---|---|---|---|
| 1 | Methodologies; observability tools | USE, workload characterisation, latency, utilisation and saturation | Core |
| 2 | Operating systems | Kernel/user space, processes, threads, system calls and scheduling | Core |
| 3 | CPUs | Per-core utilisation, run queues, context switches, CPU saturation | Core |
| 4 | Memory | Virtual memory, resident memory, faults, reclaim, swapping and OOM | Core |
| 5 | File systems; disks | Cache, inodes, throughput, IOPS, queueing and latency | Core |
| 6–7 | Methodologies and observability | Choose tools for a hypothesis and interpret intervals | Revisit |
| 8–11 | Networking | Sockets, interface counters, throughput, latency and retransmissions | Selective |
| 12–14 | Relevant resource sections | Host versus container observations and constraints | Reference |
| 15–21 | CPUs, memory, disks and networking | Explain the mechanism behind a pod's symptom | Reference |

## Reading loop
1. Pick one question, such as “How can CPU usage look moderate while requests queue?”
2. Read the relevant conceptual section for 20–30 minutes.
3. Write a five-sentence explanation without copying the book.
4. Identify one metric and one tool that could test your understanding.
5. Predict, measure, then explain a small local workload.
6. Record one remaining uncertainty for tomorrow.

Prioritise mechanisms and interpretation over memorising command flags. Skim advanced profiling and specialised tracing until a practical question requires them. Tool output can depend on kernel, permissions and software version.

## Complementary sources
These are official-source starting points for your tutor to consult as needed.

| Area | Source | Focus |
|---|---|---|
| USE methodology | https://www.brendangregg.com/usemethod.html | Resource checklist and investigation method |
| Linux commands | Local man pages; https://www.kernel.org/doc/ | Command semantics and kernel concepts |
| Docker | https://docs.docker.com/ | Images, lifecycle, networking, volumes and resource constraints |
| Kubernetes | https://kubernetes.io/docs/ | Objects, probes, networking and troubleshooting |
| Local cluster | https://kind.sigs.k8s.io/ or https://minikube.sigs.k8s.io/docs/ | Choose one local cluster environment |
| Service mesh | https://istio.io/latest/docs/concepts/ | Traffic management, identity and mutual TLS; conceptual study |

Use existing networking course material for TCP/IP, DNS, CIDR, ARP, NAT and routing. Ask your tutor to verify uncertain protocol details using relevant RFCs. Keep cloud availability and multi-tenancy discussions conceptual; no paid cloud lab is required.

## Prompt for precise mapping
“My edition is [edition]. Here is the table of contents: [paste]. Map the subject areas above to actual sections. Preserve the 21-day schedule and daily reading time. Mark optional sections and do not invent missing titles or page numbers.”

## Verified Day 3 reading: Chapter 6 — CPUs (p. 189)

Read first: 6.2.3 CPU Run Queues (p. 192); 6.3.6 Utilization (p. 195); 6.3.7 User-Time/Kernel-Time (p. 196); 6.3.8 Saturation (p. 196); 6.3.9 Preemption (p. 196); 6.3.11 Multiprocess, Multithreading (p. 197).

Use during practicals: 6.6.1 uptime (p. 224); 6.6.2 vmstat (p. 226); 6.6.3 mpstat (p. 227); 6.6.6 top (p. 231); 6.6.8 pidstat (p. 234).

Scheduling refresher: 3.2.9 Schedulers (p. 98). Optional depth: 6.4.2 Software (p. 209); its internal subheadings are not listed in the contents. Defer advanced hardware architecture and tuning.

## Verified Day 4 reading: Chapter 7 — Memory (p. 265)

Read first: 7.2.1 Virtual Memory (p. 267); 7.2.2 Paging (p. 268); 7.2.3 Demand Paging (p. 269); 7.2.4 Overcommit (p. 270); 7.2.5 Swapping (p. 271); 7.2.6 File System Cache Usage (p. 271); 7.2.7 Utilization and Saturation (p. 271); 7.3.3 Process Address Space (p. 284).

Use during practicals: 7.5.1 vmstat (p. 295); 7.5.5 ps (p. 304); 7.5.6 top (p. 305); 7.5.8 pmap (p. 306); 8.6.7 free (p. 376). OOM is not separately indexed in the supplied contents; supplement with kernel documentation and permitted logs. Defer detailed architecture and tuning.
