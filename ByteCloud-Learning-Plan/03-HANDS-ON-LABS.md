# Hands-on investigation labs

## Environment and boundaries
Use a disposable local Linux environment, Docker and one local Kubernetes cluster. Ask AI for environment-specific setup commands after checking versions and available resources. Tools such as sysstat (mpstat/pidstat/iostat), strace, tcpdump and DNS utilities may need installation. Kernel logs, packet capture and tracing may require privileges. WSL2 and containers may expose incomplete host-level information.

Before each lab, record the baseline, the exact change, a stop condition and cleanup. Keep allocation and file sizes small, use explicit timeouts and stop only processes you created. Never fill a host disk or induce host-wide OOM. For Kubernetes, verify the current context and use a dedicated `bytecloud-lab` namespace. Remove only resources created for the lab; delete the local cluster when finished if no longer needed.

## Lab A: A slow Linux application (Days 3–7)
**Goal:** connect symptoms to resource evidence.

1. Start a tiny local HTTP application and record normal latency and process resource usage.
2. Ask AI to provide one bounded CPU experiment with a known process ID and a 30-second stop condition. Predict per-core and aggregate behaviour.
3. Collect before/during/after samples with top, mpstat, vmstat and pidstat where available.
4. Repeat with a small memory allocation. Compare resident memory, available memory and faults; this need not cause pressure or swapping.
5. Create/read a small temporary file while observing iostat. Explain caching and why the run may not exercise physical storage strongly.
6. For the checkpoint, ask AI to choose one workload without revealing its cause until you submit a diagnosis.

**Evidence:** symptom, process ID, sampled intervals, important fields, two supporting observations and one competing hypothesis.

**Success:** distinguish what you observed from what you merely suspect. If an experiment does not reproduce a bottleneck, explain why rather than inventing one.

**Cleanup:** stop your application and workload; remove only the temporary files you created; confirm resource usage returns to baseline.

## Lab B: Diagnose a failed request (Days 8–11)
**Goal:** isolate DNS, TCP, TLS and HTTP stages.

1. Run a local HTTP server bound to loopback on a chosen unused port.
2. Make a successful request; compare curl output with the listening socket shown by ss.
3. Request a different unused local port and explain the refusal evidence.
4. Use a deliberately nonexistent name under `.invalid` and inspect resolution failure.
5. Request HTTPS from your HTTP-only local port and distinguish TLS negotiation failure from a TCP failure.
6. Compare these with an HTTP 404: transport and HTTP failure are different observations.
7. Study a timeout or reset using an AI-provided example trace explicitly labelled as synthetic, or a bounded disposable-network experiment. Do not change host firewall rules merely to manufacture a timeout.

**Evidence:** requested address, binding address, name-resolution result, listener and request output. Packet capture is optional and should be scoped to your local lab traffic.

**Success:** give a likely failing layer and the next discriminating check. An error message does not uniquely identify the root cause.

**Cleanup:** stop the local server and any capture; remove lab captures if no longer needed.

## Lab C: Two containers cannot communicate (Days 12–14)
**Goal:** understand network membership, naming, ports and lifecycle.

1. Run a small HTTP server container and a disposable client on a user-defined Docker network.
2. Request the server using its container name and internal port. Explain why host port publishing is unnecessary for this path.
3. Use localhost from the client, choose a wrong server port, and disconnect one container from the network, one change at a time.
4. For each fault, predict the result, inspect network membership and logs, then test one hypothesis.
5. Run a disposable container with an invalid command; inspect its exit state and logs. Compare a crash with a configured restart policy.
6. Mount a named volume, write a small marker, recreate the container and verify persistence.
7. Inspect resource settings and docker stats. Ask AI for a bounded container-only resource exercise if time allows.

**Success:** repair communication and explain the exact role of name resolution, listening address, internal port and network membership.

**Cleanup:** remove lab containers, network and volume after verifying there is no data you want to keep. Avoid broad prune commands.

## Lab D: Kubernetes failure clinic (Days 15–19)
**Baseline:** one Deployment, one Service and a temporary debug Pod inside your lab namespace. Select small maintained images suitable for your architecture. Save a working manifest before changes.

Inspect with `kubectl get`, `describe`, events and logs. Add namespace flags consistently. Use `kubectl logs --previous` when a previous container instance exists. `kubectl top` requires a functioning metrics API, which local clusters may lack; it is not a prerequisite for the lab.

| Case | Inject one local fault | Investigate | Recovery evidence |
|---|---|---|---|
| 1: Image pull | Change image to a nonexistent tag | Events, image name, registry reachability; distinguish tag, auth and network causes | Valid image pulls and rollout becomes ready |
| 2: Crash loop | Use an invalid startup command | Current/previous logs, termination reason, restart count | Correct command remains running |
| 3: Pending | Request more CPU than the local node can allocate | Scheduler events, allocatable resources, existing requests | Feasible request schedules |
| 4: Readiness | Point readiness check to an invalid path | Probe events, readiness state, EndpointSlices | Correct probe passes and endpoint is ready |
| 5: Service failure | Change the Service selector | Labels, selector, EndpointSlices, targetPort, direct Pod reachability | Service reaches ready backend |
| 6: Container memory | Run a bounded allocation workload under a small container memory limit | Last termination reason, limit and events; exit 137 alone is insufficient | Workload/limit corrected and restart behaviour understood |

For case 6, keep the workload inside a disposable limited container and do not escalate to host stress if local enforcement behaves differently. CPU requests affect scheduling; CPU limits may throttle; memory limit violations may trigger OOM termination. Do not equate requests with current usage.

Additional discussion: compare failing readiness with liveness restart behaviour; distinguish Pending caused by scheduling from Pending caused by storage; inspect a PVC and available StorageClass. Local LoadBalancer, Ingress and NetworkPolicy behaviour depends on installed components. A NetworkPolicy exercise requires a supporting CNI, and an Ingress object needs an implementation/controller. Explain these prerequisites even if you skip installing them.

**Success:** diagnose at least four cases, including Service connectivity, using evidence before repair. Record the remaining cases as pending rather than completed.

**Cleanup:** restore the baseline between cases. Remove lab resources at the end; check namespace and context before deleting anything.

## Lab E: Final incident (Day 21)
Ask your tutor to select two compatible faults from the earlier labs and withhold the causes. Use one backend Deployment, a Service and a client. No external cloud is required.

Deliver:
1. A plain-language description of the impact and affected scope.
2. Your first hypothesis and a check that could disprove it.
3. Actual observations from logs, events, networking and resource settings as relevant.
4. The root cause, or a clear statement of uncertainty if evidence is incomplete.
5. The smallest repair and before/after request results.
6. One prevention measure and one monitoring signal.

Assess explanation, evidence interpretation and independent troubleshooting separately from 0–2. Repeat only the weak parts with a changed fault. A successful rollout alone does not prove client requests work.
