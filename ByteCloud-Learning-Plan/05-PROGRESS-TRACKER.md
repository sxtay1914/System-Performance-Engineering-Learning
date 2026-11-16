# Progress and session handoffs

## Completion standard
Mark a day complete when you can explain its concept, perform the exercise and interpret evidence. Use 0 = not yet, 1 = with help, 2 = independent. Progress is evidence-based; reading alone is not completion.

| Day | Topic | Explanation 0–2 | Evidence 0–2 | Investigation 0–2 | Done | Review date |
|---|---|---|---|---|---|---|
| 1 | Performance methodology | 1 | 1 | 0 | [x] | Study Days 2, 4, 8 |
| 2 | Linux execution model | 1 | 1 | 1 | [ ] | Study Days 3, 5, 9 |
| 3 | CPU and scheduling | 1 | 1 | 1 | [x] | Study Days 4, 6, 10 |
| 4 | Memory | — | — | — | [ ] | — |
| 5 | Filesystems and storage | — | — | — | [ ] | — |
| 6 | Linux investigation practice | — | — | — | [ ] | — |
| 7 | Linux checkpoint | — | — | — | [ ] | — |
| 8 | IP and local delivery | — | — | — | [ ] | — |
| 9 | TCP, UDP and sockets | — | — | — | [ ] | — |
| 10 | DNS, HTTP and TLS | — | — | — | [ ] | — |
| 11 | Network troubleshooting | — | — | — | [ ] | — |
| 12 | Docker foundations | — | — | — | [ ] | — |
| 13 | Docker networking and resources | — | — | — | [ ] | — |
| 14 | Container checkpoint | — | — | — | [ ] | — |
| 15 | Kubernetes architecture | — | — | — | [ ] | — |
| 16 | Configuration, storage and probes | — | — | — | [ ] | — |
| 17 | Kubernetes networking | — | — | — | [ ] | — |
| 18 | Pod lifecycle failures | — | — | — | [ ] | — |
| 19 | Resources and connectivity | — | — | — | [ ] | — |
| 20 | Cloud infrastructure concepts | — | — | — | [ ] | — |
| 21 | Final incident and review | — | — | — | [ ] | — |

## Day 1 — 2026-11-13 to 2026-11-14

- Status: guided session completed; book reading remains unconfirmed. Independent troubleshooting has not yet been demonstrated.
- Time spent: not recorded; session continued past midnight (Asia/Kuala_Lumpur).
- Environment: macOS host with 14 logical CPUs; Kali Linux VM, kernel `6.19.14+kali-arm64`, `aarch64`, 2 logical CPUs.
- Objective: distinguish utilisation, saturation, latency, throughput, symptoms and causes; use USE to guide evidence collection.
- Prediction: CPU utilisation will vary between samples because workload changes, even when the same processes remain open.
- Commands and actual evidence supplied by the learner:
  - `sysctl -n hw.logicalcpu`: `14` on macOS.
  - `top -l 3 -s 2 -o cpu -n 10 -stats pid,command,cpu`: macOS sample showed `7.52% user, 5.43% sys, 87.4% idle`; a later sample showed `9.21% user, 4.58% sys, 86.19% idle`. Busy time changed from 12.95% to 13.79%.
  - `vmstat 1 5`: after excluding the initial since-boot report, four interval reports showed `r=0`, `b=0`, `si=0`, `so=0`, `bi=0`, `bo=0`, `id=99`, `wa=0`, `st=0`; context switches were 222–241/sec.
  - `pidstat 1 3`: reported 2 CPUs, light process activity and displayed `%wait=0.00`. The monitoring process itself averaged `%CPU=1.00`; the other displayed processes averaged 0.33–0.66% each.
- Interpretation (with guidance): both environments had low aggregate CPU utilisation during these separate observations. The VM samples showed no obvious CPU pressure or swapping. Per-process CPU percentages use one logical CPU as 100%; they are not the same scale as whole-machine utilisation. These short observations do not diagnose application performance.
- Investigation reasoning practised: establish symptom, scope and baseline; locate request time and form a hypothesis; choose a discriminating check using utilisation, saturation and errors. Hypothetical database lock waits illustrated narrowing scope and checking evidence, not an actual database incident.
- Misconceptions corrected: low average CPU does not rule out a busy critical thread or bursts; arrival rates above service capacity grow the queue; bursty arrivals can queue even with spare average capacity; blocked threads are not necessarily CPU-bound; a database wait does not automatically justify RAM; errors/timeouts are clues rather than root causes; a single snapshot can miss contention.
- Alternative explanations: per-thread CPU limits, short bursts and dependency waits remain possible in a slow application. No application slowdown was reproduced or tested; no per-core/thread or database evidence was collected.
- Repair/recovery: not applicable; observation only, no fault injected.
- Cleanup: bounded read-only sampling commands exited automatically; no lab workload or files were created by these exercises.
- Explanation / evidence / investigation scores: **1 / 1 / 0** (with help / with help / independent investigation not yet demonstrated).
- Remaining question: how can we distinguish a busy critical thread from a blocked thread during an actual slow request?
- Next action: start Day 2 in the same Kali VM, covering processes, threads and process states through one small inspection exercise. Keep tutoring concise; avoid repeated conceptual quizzes. Confirm or complete the short Day 1 methodology/observability reading.
- Review: brief recall on study Days 2, 4 and 8; calendar dates depend on the next sessions.

### Handoff

Day 1's guided concepts and baseline are complete. Start Day 2: Linux execution model. The learner has a local Kali ARM64 VM with 2 logical CPUs and working vmstat/pidstat. Revisit running versus runnable versus blocked while inspecting a process. Book reading and independent troubleshooting remain pending; do not treat the quiet baseline as proof of application health.

## Day 2 — 2026-11-15

- Status: guided session finished; core concepts and inspections covered. Full Day 2 completion remains pending the signal comparison and demonstration.
- Time spent: not recorded; learner reported 30 minutes remaining during the session.
- Environment: same Kali ARM64 VM as Day 1. Learner installed strace; version not recorded.
- Reading: learner reported finishing the assigned Operating Systems topics. Exact sections/pages are unverified because the supplied PDF is incomplete. This does not confirm Day 1 reading.
- Objective: connect process/thread states, kernel waits, descriptors and system calls; interpret signals and path permissions.
- Predictions and reasoning: learner correctly identified mostly sleeping processes and explained that one-second snapshots can miss work between samples. Initially inferred that a zero eventfd counter meant it had never been used; corrected after discussing consumption of notifications.
- Commands and actual evidence supplied by the learner:
  - `ps -eo pid,ppid,nlwp,stat,pcpu,comm --sort=-pcpu | head -n 15`: PID 1461 (`wrapper-2.0`) had five threads, `Sl` state and 0.3% lifetime-average CPU; displayed kernel threads included `I` states.
  - `ps -L -p 1461 -o pid,tid,stat,pcpu,wchan:30,comm`: all five threads showed `Sl`; TIDs 1461, 1477 and 1481 waited in `poll_schedule_timeout...`, while 1470 and 1476 waited in `futex_do_wait`.
  - One-second repeated inspection: learner reported unchanged states and waits; correctly rejected this as proof of a stuck application.
  - `ls -l /proc/1461/fd`: stdin/stdout pointed to `/dev/null`; stderr pointed to `/home/jesmond/.xsession-errors`; other descriptors included sockets, eventfds and pidfds.
  - `cat /proc/1461/fdinfo/4`: `eventfd-count: 0`, `eventfd-id: 190`, `eventfd-semaphore: 0`. Zero is a current count, not a history of notifications or wakeups.
  - Filtered strace of a shell redirection: first attempt opened `/dev/`, failed with `EISDIR`, wrote errors through descriptor 2 and exited with status 2. Retry opened `/dev/null` as descriptor 3, wrote six bytes through descriptor 1 (`"day2/n"`) and exited with status 0. Explained literal `/n` versus newline `\n`; descriptor duplication was hidden by the trace filter.
  - Sleep trace: `clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=2, tv_nsec=1}, ...) = 0 <2.000494>`. Interpreted relative sleep, successful return and elapsed syscall time; this was not a CPU-usage measurement.
  - Signal exercise: learner reported status 130 and clarified using SIGINT. Exact command sequence was not supplied; this is consistent with SIGINT but does not verify SIGTERM cleanup, SIGKILL behaviour or final background-process state.
- Interpretation: sleeping is normal; poll waits may involve sockets, pipes, eventfds or timeouts. Open descriptors identify available resources; tracing can connect operations to descriptors. No slow backend or blocked-service fault was reproduced.
- Permission reasoning (hypothetical only): corrected 0644 to owner read/write, group/other read; applicable class is selected per path component. Reading a known file requires file read permission plus search/execute permission on each parent directory, not directory listing permission. Discussed `ls -l`, `ls -ld` and `namei -l`; no actual permission-failure output was collected.
- Investigation assessment: learner proposed inspecting what a polling thread was waiting on through descriptors; refined “low CPU suggests I/O” to “waiting for an event, requiring connection to the slow request.” Investigation was guided, not an independent diagnosis and recovery.
- Repair/recovery: corrected the redirection destination and observed successful completion; no application incident repaired.
- Cleanup: traced shell and sleep commands exited in supplied output. Background signal-workload cleanup was not confirmed. Temporary permission-file exercise was skipped; no creation or cleanup was reported.
- Explanation / evidence / investigation scores: **1 / 1 / 1** (with help in each category).
- Remaining gaps: demonstrate SIGTERM versus SIGKILL; independently trace a relevant wait; optional local permission-failure investigation. Kernel/user-space and signal understanding have not been independently assessed.
- Next action: proceed to Day 3 CPU and scheduling with a bounded workload in Kali; briefly check whether any disposable signal workload remains before starting. Carry the Day 2 signal comparison forward without marking it complete.
- Review: study Days 3, 5 and 9. Revisit eventfd counter versus history, polling versus proven slow I/O, and directory search versus listing permission.

### Handoff

Continue with Day 3. Use practice-led tutoring: short theory, explain each command and why it answers the current question, ask for a prediction, inspect actual output, then interpret it. The learner prefers technical practicals without neglecting theory; avoid unnecessary eventfd depth and repeated conceptual quizzes. Outline relevant reading topics rather than inventing section/page references from the incomplete PDF. Day 2's guided session is finished, but its full completion checklist remains open for signals and independent demonstration.

## Day 3 — 2026-11-16

- Status: guided session completed, including the requested load-average calculation and application flame graph. Independent diagnosis and optimisation have not been demonstrated.
- Time spent: not recorded.
- Environment: Kali ARM64 VM, kernel `6.19.14+kali-arm64`, two available logical CPUs (`nproc`). Installed `linux-perf`; compiler and FlameGraph scripts used successfully. Tool versions not recorded.
- Reading: learner reported completing the assigned CPU sections. Exact titles and starting pages were checked against the local PDF table of contents; see the Day 3 mapping in [the reading map](04-BOOK-READING-MAP.md).
- Objective: distinguish utilisation from saturation, connect system/process/per-CPU measurements, and identify application CPU code paths.
- Predictions: learner correctly predicted that four runnable single-threaded workers on two CPUs allow two to execute while approximately two wait; explained that adding CPUs alone does not parallelise one busy thread.
- Commands and actual evidence:
  - Initial `vmstat 1 5`, excluding the first report: `r=1`, `us=27–29`, `sy=22–24`, `id=49–50`, `b=0`, `wa=0`, `st=0`. This was an active workload, not an idle baseline.
  - `pidstat -u 1 5`: learner identified PID 491823 (`zsh`); averages were `%usr=54.89`, `%system=45.11`, `%CPU=100.00`, `%wait=0.00`. Explained that one CPU's worth of process execution corresponds to about 50% of this two-CPU machine.
  - `mpstat -P ALL 1 5`: CPU 0 had 0% idle; CPU 1 had 98–100% idle; aggregate idle was about 49–50%. CPU 0 user work appeared in `%nice`, with substantial `%sys` time. Exact nice value was not supplied.
  - `taskset -pc 491823`: allowed CPU list was `0,1`; learner reported one thread from ps. Most-recent CPU does not imply permanent affinity. Loop was reported as `while true; do :; done` running in the background.
  - After stopping the original loop, learner reported 98% idle. This before/after comparison supports the loop as the source of activity; its substantial kernel-time share was not independently explained.
  - Four bash busy workers, each bounded by `timeout -s KILL 15s`: interval vmstat reports showed `r=4`, `id=0`, `us=100`, `sy=0–1`, `cs=660–682/sec`. Runnable count includes executing plus queued tasks; on two CPUs this supports CPU saturation. Separate percentage rounding can produce a displayed total above 100%.
  - Load-average exercise: 64 CPUs at 50% utilisation gives 32 CPUs' worth of execution; adding two queued threads gives approximately 34 at steady state without significant uninterruptible waits. Learner initially answered 2 for the executing portion, then accepted the correction. The supplied wording is ambiguous if 2 means all runnable threads, not queued-only; original exercise text was not independently verified. No steady-state load average was measured in the short lab.
  - Profiling access: `perf_event_paranoid=3`; unprivileged collection failed. `sudo perf stat -e task-clock:u -- sleep 1` succeeded with 0.27 ms task CPU time and 1.002191307 seconds elapsed. No persistent kernel-setting change was instructed.
  - A standalone C demo used noinline `heavy_work` and `light_work`, with four million versus one million iterations per call, for roughly 15 seconds. Compiled with `-O2 -g -fno-omit-frame-pointer`; learner confirmed compilation. Program ran as normal user; sudo perf attached to its PID.
  - `perf record -e cpu-clock:u -F 99 --call-graph dwarf -p "$demo_pid" -o perf.data -- sleep 10`: supplied summary reported 989 samples and 8.046 MB. Corrected command-entry mistakes before successful collection.
  - Converted using perf script and Brendan Gregg's FlameGraph scripts. Tutor inspected the supplied [flame graph](../flamegraph.svg): `main → heavy_work` 79.68%, `main → light_work` 20.32%. SVG weights are aggregated event periods, not 9.99 billion independent samples. Some ancestor frames were unresolved; target function names were clear.
  - `pidstat -w` observing `sleep 10`: learner reported zero context switches in the observed intervals; full output was not supplied. Discussed that the initial block and final wake can fall outside the observation window. A sleeping task wakes for its event/timer, not merely because CPU capacity is free.
- Interpretation: the single-thread workload filled one CPU despite spare aggregate capacity; four runnable workers exceeded available execution capacity. Flame graph width reflects sampled CPU weight including callees, not time order or whole-machine utilisation.
- Optimisation reasoning: hypothetical halving of an 80% hot path reduces fixed-work runtime from 10 to 6 seconds (about 1.67x speedup). It need not use more CPUs. Our fixed-duration demo would instead complete more work; no optimisation or speedup was actually measured.
- Cleanup: original loop stop was followed by the reported idle recovery. Four-worker and demo workloads were time-bounded; final process-list cleanup was not supplied. Source, executable, perf data and conversion artifacts were intentionally retained in Kali; only the supplied SVG is included with this progress update.
- Explanation / evidence / investigation scores: **1 / 1 / 1** (guided). top was not separately exercised; ps, pidstat, vmstat and mpstat supplied the process and CPU observations.
- Remaining gaps: observe involuntary switches and per-thread scheduling wait under contention; independently reproduce profiling and explain unresolved frames; verify final lab-process cleanup. Day 2 signal comparison remains pending.
- Next action: Day 4 memory. Outline exact reading sections from the verified contents, then explain commands and collect a baseline before a bounded allocation experiment. Ask for evidence before diagnosing memory pressure.
- Review: study Days 4, 6 and 10. Revisit runnable versus queued, process versus system CPU percentages, and flame graph inclusive widths versus execution time.

### Handoff

Day 3 guided practicals are complete. Start Day 4 in the same Kali VM. Keep the practice-led format: explain the technical purpose and command syntax, predict, measure, interpret. The learner needs commands that are easy to type and may use the VMware shared project folder to transfer longer source files. Preserve the Day 2 signal gap and Day 3 independent-investigation gaps; do not imply a measured optimisation or fully resolved call stacks.

## Session entry template
Copy once per session. Schedule recall roughly 1, 3 and 7 study days later; shorten review if recall is strong.

### Day [N] — [date]
- Time spent:
- Environment and relevant versions:
- Objective:
- Prediction before running commands:
- Commands and actual output excerpts:
- What the evidence means:
- Alternative explanation and how I checked it:
- Repair and recovery verification, if applicable:
- Cleanup completed:
- What I can now explain without notes:
- Misconception corrected:
- Remaining question:
- Explanation / evidence / investigation scores:
- Next action:
- Review dates:

## Incident report template
- Symptom and impact:
- Scope and baseline:
- Hypothesis:
- Discriminating check:
- Actual evidence:
- Conclusion and confidence:
- Fix:
- Recovery verification:
- Prevention or monitoring:

## AI handoff template
```text
I am following the 21-day infrastructure roadmap.
Current day:
Environment:
Completed and demonstrated:
Evidence collected:
Gaps or misconceptions:
Next exercise:
Review questions:
Continue one step at a time. Ask me to interpret evidence before giving the answer.
```

## Stage milestones
- [ ] Day 7: investigate a slow Linux application and distinguish CPU, memory and I/O hypotheses.
- [ ] Day 14: deploy two containers and diagnose a communication failure independently.
- [ ] Day 21: troubleshoot an unfamiliar Kubernetes failure and verify application recovery.

## Remaining gaps after Day 21
| Gap | Evidence that it is a gap | Next bounded exercise | Priority |
|---|---|---|---|
| | | | |
