# Progress and session handoffs

## Completion standard
Mark a day complete when you can explain its concept, perform the exercise and interpret evidence. Use 0 = not yet, 1 = with help, 2 = independent. Progress is evidence-based; reading alone is not completion.

| Day | Topic | Explanation 0–2 | Evidence 0–2 | Investigation 0–2 | Done | Review date |
|---|---|---|---|---|---|---|
| 1 | Performance methodology | 1 | 1 | 0 | [x] | Study Days 2, 4, 8 |
| 2 | Linux execution model | 1 | 1 | 1 | [ ] | Study Days 3, 5, 9 |
| 3 | CPU and scheduling | 1 | 1 | 1 | [x] | Study Days 4, 6, 10 |
| 4 | Memory | 1 | 1 | 1 | [x] | Study Days 5, 7, 11 |
| 5 | Filesystems and storage | 1 | 1 | 1 | [x] | Study Days 6, 8, 12 |
| 6 | Linux investigation practice | 1 | 1 | 1 | [ ] | Study Days 7, 9, 13 |
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

## Day 4 — 2026-11-17 to 2026-11-19

- Status: guided learning and assessment completed. Reading was assigned November 17, reported complete November 18; supplied practical evidence is from November 19. Time spent not recorded.
- Environment: same Kali ARM64 VM, two CPUs; 5.8 GiB RAM and 1.0 GiB swap. Python mmap, ps, pmap, pidstat, free and vmstat available.
- Reading: learner reported finishing the assigned memory sections; exact references are recorded in the reading map.
- Prediction: learner correctly predicted that reserving anonymous virtual memory need not immediately increase RSS because of lazy allocation/demand paging.
- Measured evidence supplied by the learner:
  - `free -h`: 5.8 GiB total, 1.1 GiB used, 2.9 GiB free, 2.0 GiB buff/cache, 4.7 GiB available; swap used 0 B. Interval `vmstat 1 5` reports showed `r=0`, `b=0`, `si=so=0`, `id=98`, `wa=st=0`. No obvious pressure in this window.
  - Python PID 1178157, `ps -p 1178157 -o pid,vsz,rss,comm`: baseline VSZ/RSS 23,840/17,192 KiB; after reserving a private anonymous 100 MiB mmap, 126,240/17,192; after writing one byte per page, 126,240/119,596; after closing the mapping, 23,840/17,196. This demonstrated reservation, residency and release. An initially unchanged result after the close instruction was followed up before release was confirmed.
  - RSS-sorted process listing identified `glycin-heif` PID 490742 at 201,512 KiB RSS and 598,528 KiB VSZ. Being the largest consumer did not establish a fault.
  - `pmap -x 490742`: totals 598,528 KiB mapped, 201,512 KiB RSS, 193,236 KiB dirty. Three anonymous writable regions had RSS 63,884, 55,752 and 60,976 KiB (180,612 KiB combined). Several no-access anonymous reservations had zero RSS. Dirty does not mean erroneous; the allocations' application-level purposes were not identified.
  - `pidstat -r -p 490742 2 5`: RSS stayed at 201,272 KiB, VSZ at 598,528 KiB, and both minor/major fault rates were 0.00. This showed short-term stability, not that all virtual memory was resident or that no leak exists. Workload activity during sampling was not established.
  - Learner reported `/proc/sys/vm/overcommit_memory` as 0: heuristic commitment checks, not a guarantee of future physical backing.
- Mock exercises, not measurements:
  - Learner requested mock first-touch fault counts because copying commands into Kali was difficult. Assumed 100 MiB, 4 KiB pages, no huge pages: reservation 0 faults, first writes 25,600 minor/0 major, repeated writes 0 additional faults. Actual fault deltas were not collected.
  - Low available memory, sustained swap traffic and higher latency supported a pressure hypothesis; old swap occupancy alone was insufficient. Learner chose to identify memory consumers before adding RAM.
  - Final incident: backend latency doubled, RSS rose from 300 MiB to 1.5 GiB, available memory fell, swap traffic stayed zero. Learner proposed ps then pmap, and selected saturation checks to distinguish growth from pressure. Tutor introduced memory PSI; learner explained stalls despite zero swap traffic. Correlation and application-specific evidence are still needed to attribute latency.
- Concepts corrected/reinforced: free versus available; VSZ versus RSS; minor faults do not require storage reads, major faults do; file-backed faults can be minor; CPU cache misses are distinct from page faults; Linux swapping operates on pages rather than requiring whole-process eviction; clean file pages can be discarded without writeback; anonymous data generally needs swap to be reclaimed while preserved; larger pages improve potential TLB coverage rather than guaranteeing data-cache hit rates.
- USE method: free/vmstat for occupancy, ps/pmap for attribution, vmstat swap traffic and PSI for saturation, kernel/application logs for OOM and allocation errors. Standard vmstat has no total or available RAM column. OOM selection is not inherently based on application importance; exit 137 alone is not proof of OOM. Kernel-log commands were discussed but not run in supplied evidence.
- Explanation / evidence / investigation scores: **1 / 1 / 1** (guided). No independent memory incident was diagnosed or repaired.
- Cleanup: release of the measured 100 MiB mapping was verified through VSZ/RSS. Whether another mapping was created during the skipped fault exercise and whether the Python session finally exited remain unconfirmed; `exit()` was recommended.
- Remaining gaps: actual first-touch fault counts, PSI output, kernel OOM/allocation logs, real pressure/reclaim stalls and final Python cleanup. Deliberate exhaustion was avoided. Day 2 signal comparison remains pending.
- Next action: Day 5 filesystems and storage, starting with selective reading. For investigations, present symptom/context first and ask the learner for hypotheses, checks and expected discriminating results before suggesting improvements or commands.
- Review: study Days 5, 7 and 11; revisit occupancy versus pressure, file-cache versus anonymous paging, and process-specific attribution of system-wide stalls.

### Handoff

Start Day 5 in the same Kali VM. Keep technical practicals central, with brief theory and explicit explanations of command purpose. The learner explicitly wants to propose their own investigation method before tutor feedback. Label mock data and observed output separately. Reading references should come from the verified PDF contents. Preserve unresolved checks rather than implying that mock fault counts or PSI/OOM evidence were measured.

## Day 5 — 2026-11-19 to 2026-11-23

- Status: guided session closed at learner request; original practicals substantially covered, with remaining checks and expanded exercises deferred to the backlog below. Completion denotes guided work, not independent mastery or completion of every added benchmark.
- Time spent: not recorded. Learner requested a quick pace and ultimately concise conceptual answers instead of completing the cache benchmark.
- Environment: Kali ARM64 VM, kernel 6.19.14+kali-arm64, two CPUs, ext4 on /dev/nvme0n1p3 mounted at /. bpftrace and BCC cachestat-bpfcc were present.
- Reading: assigned filesystem/disk theory reported complete November 19; entire filesystem chapter reported complete November 23. Completion of 9.6.1 iostat (p. 432) reading was not explicitly confirmed, although the tool was used and interpreted.
- Capacity/access investigation (real checks for a mock failure):
  - `df -h .`: 18 GiB filesystem, 14 GiB used, 3.2 GiB available, 81% used. `df -i .`: 1,179,648 inodes, 481,802 used, 697,846 free (41% used). Neither resource was exhausted.
  - `ls -ld .` showed home owned by jesmond with `drwx------`; `id` confirmed UID/GID 1000 jesmond. Owner write/search permission applied. Service identity could differ.
  - `quota -s` returned no output: no user quota reported, not proof that all quota mechanisms were disabled.
  - `findmnt` showed `rw,relatime,errors=remount-ro`: currently writable; remount-ro is error policy, not evidence of a present error.
  - `mktemp ./day5-test.XXXXXX` created `./day5-test.aHBeGg`; `ls -l "$test_file"` confirmed a zero-byte file with owner read/write access. `rm -- "$test_file"` reported no error. Corrected literal variable name versus `$test_file` expansion.
- Storage observations:
  - Initial `iostat -xz -y 1 5` had no device rows: inactive devices were hidden by -z.
  - Following the instructed 64 MiB dd write with final fdatasync, supplied nvme0n1 interval showed w/s=68, wkB/s=65,604, w_await=3.29 ms, wareq-sz=964.76 KiB, aqu-sz=0.22, util=1.20%. No sustained saturation established; device statistics differ from application operations. The requested dd completion summary was not supplied.
- Tracing evidence:
  - Listed sys_enter_openat fields (dfd, filename, flags, mode and dynamic filename field) and sys_exit_write ret field. Explained entry versus exit, VFS versus syscall boundary, and tracing requested operations versus actual device I/O.
  - bpftrace paired write/fdatasync entries and exits using tid and nsecs, filtered entries by comm == dd, and produced separate microsecond histograms. Initial write histogram contained about 4.43 million calls and had uncertain workload attribution; it was not used as the intended bounded-run result.
  - Subsequent supplied histogram: 59 writes in [64,128) us, four in [128,256), one in [256,512), plus three shorter calls ([0], [1], [8,16)). One fdatasync in [4096,8192) us. Consistent with the intended data-write count plus possible reporting writes, but not proven from PID/return-value evidence.
  - Per-thread completion-based duration map reported TID 1990616: 17,825,533 ns = 17.83 ms, or 1.78% of a nominal second. This includes execution/wait time, not CPU utilisation. Calls were assigned to their completion bucket, not split across interval boundaries; asynchronous print/clear can also affect interval accuracy. Selected syscalls only, not exact full-filesystem occupancy.
- Cache observations and deferred work:
  - `free -h`: 5.8 GiB total, 1.1 GiB used, 2.2 GiB free, 2.6 GiB buff/cache, 4.6 GiB available; swap used 16 KiB. Cache occupancy is not a hit ratio or maximum cache capacity.
  - cachestat-bpfcc failed to compile because running-kernel headers/kheaders were missing; APT initially could not locate linux-headers-6.19.14+kali-arm64. Update/download was reported in progress; successful installation or tracing was not confirmed.
  - Later df: 18 GiB total, 15 GiB used, 2.1 GiB available (88% used). Proposed 128 MiB test to avoid filling storage; creation summary not supplied. Learner skipped cold/warm read measurement. No cache-capacity threshold or degradation result was measured.
  - Provided conceptual cache checklist: page-cache counters in free/meminfo, dentry/inode allocation and active objects via slabtop, estimated page-cache hit rates via BCC cachestat/cachetop, dentry stats via dcstat; inode hit rate needs targeted instrumentation. No metadata-cache size or hit-rate output was supplied.
  - Provided workload checklist: operation mix/rates, request sizes and returns, per-process/device traffic, offsets for sequential/random patterns, latency distributions, per-thread elapsed time, open flags and sync policy. iostat alone cannot establish application access patterns.
- Concepts covered: logical/physical I/O inflation and deflation; cache versus storage throughput; direct I/O bypasses page cache rather than VFS; raw device access is distinct; read prefetch versus write buffering; fsync batching versus O_SYNC; mmap mapping/copying benefits and limitations; working-set size versus RSS; cache hit/miss interpretation. A cache benchmark procedure was explained, not executed.
- Explanation / evidence / investigation scores: **1 / 1 / 1** (guided). Learner proposed capacity, permissions and quota checks; needed help choosing performance metrics and writing traces. No independent incident cause/recovery was established.
- Cleanup: empty-file creation test cleanup reported no error. Later dd files, possible 128 MiB cache file and tracing-session cleanup were not explicitly confirmed. Do not delete by broad glob or reuse historical PIDs without verifying ownership and identity.
- Next action: Day 6 Linux investigation practice. Brief recall, then Lab A with learner-proposed hypotheses/checks before tutor suggestions. Check available time, current VM resources and leftover lab artifacts first. Do not expose the incident cause upfront.
- Review: study Days 6, 8 and 12. Revisit syscall versus device latency, utilisation versus saturation, and observed results versus hypothetical benchmark behaviour.

### Handoff

Proceed to Day 6. Day 5 guided session is closed, with the expanded benchmark work explicitly deferred. Keep tasks concise and ask the learner for a method before giving commands. Preserve measured results, uncertainty and skipped work separately. No cache-capacity number, degradation measurement or successful hit-rate trace exists. Consult the backlog before resuming extras.

## Day 6 — 2026-11-24 to 2026-11-25 (guided assessment finished)

- Status: resumed November 25 and finished the guided mock incident discussion. Learner chose to proceed to Day 7. Full completion remains open for independent Lab A evidence and cleanup; guided scores are 1/1/1. Prior percentage estimates described scope, not mastery.
- Reading: learner reported completing the refresher: 2.5.5 Problem Statement (p. 39), 2.5.6 Scientific Method (p. 39), 2.5.9 The USE Method (p. 42).
- Environment: same Kali ARM64 VM with two CPUs. Initial capacity: 5.8 GiB RAM, 4.6 GiB available; root filesystem 18 GiB total, 14 GiB used, 3.2 GiB available (81%). Time budget not supplied.
- Method: learner proposed defining what the request does, obtaining a normal-latency baseline, then applying USE. Chose vmstat and free for resource observations with guidance on available memory, swap traffic and CPU queueing.
- Application setup: tiny index.html served by Python's HTTP server on 127.0.0.1:8000 from `/home/jesmond/day6-lab.wrmbQY`, with a 300-second timeout. Supplied process listing identified timeout PID 2297788 and Python PID 2297789. These are historical identities, not safe targets to signal without rechecking.
- Actual measurements:
  - Five sequential curl requests returned HTTP 200 with total times 0.001123, 0.001506, 0.001436, 0.001136 and 0.001138 seconds. Range 1.12–1.51 ms; median 1.138 ms, mean 1.2678 ms. Corrected URL/line-continuation typing errors before collecting this valid baseline.
  - Resource baseline: free showed 4.6 GiB available and 16 KiB swap occupied; vmstat interval samples showed r=0–1, b=0, si=so=0, 97–98% idle, and occasional small block writes. Occupied swap did not establish active swapping.
  - Controlled workload: four busy bash loops, each bounded by timeout -s KILL 30s. Workload type was disclosed, so this was not an unknown-cause investigation. A mistyped loop was corrected before successful measurements.
  - During workload, vmstat interval samples showed r=4–5, id=0, us=99–100, sy=0–1, b=0 and si=so=0. This supports CPU saturation on two CPUs.
  - Subsequent five curl results were all 200: 0.002439, 0.001654, 0.000965, 0.000780 and 0.000767 seconds. Range 0.77–2.44 ms; median 0.965 ms. First two were slower but later requests were faster than baseline. Overlap with the full workload interval was not confirmed; learner chose to move on. No consistent HTTP slowdown or recovery was demonstrated, and five samples cannot establish p95/tail behaviour.
- Mock investigation (all subsequent service/database evidence was synthetic):
  - Scenario: p95 rose from 20 to 400 ms at unchanged request rate, with 35% aggregate CPU, 3 GiB available RAM and zero swap traffic. Learner proposed disk/network checks; tutor explained that aggregate CPU and zero swap do not fully clear CPU/thread constraints or memory stalls.
  - Suggested checks: storage iowait/iostat and dependency curl timing. Given unchanged device write latency (2 ms), outstanding requests (0.1) and dependency connect time (1 ms), but time-to-first-byte increasing from 15 to 380 ms, learner initially called this an I/O problem. Clarified dependency-response delay versus proven local storage/network fault.
  - Explained request-log correlation using timestamps, endpoint/status, request/trace IDs, total/dependency durations and retries. No actual logs were inspected.
  - Correlated mock request abc: backend total 405 ms, inventory call 382 ms; inventory total 379 ms, DB pool wait 340 ms, query time 18 ms. Learner correctly located pool wait and proposed checking queue size and pool threads; corrected pool resource to database connections.
  - Learner correctly rejected blindly increasing pool capacity and proposed investigating locks or other causes of long connection holds. Low CPU was suggested as lock evidence; clarified it only indicates possible waiting. Direct evidence requires lock wait and blocker relationships.
  - Current mock evidence: Session A is waiting for a row lock held by Session B; B has been idle in transaction with a transaction open for 90 seconds. No resolution has been chosen or executed.
- Cleanup: server and workers were time-bounded, but actual final process status and removal of index.html/lab directory were not confirmed. Do not reuse historical PIDs or delete unrelated files. Verify the identified lab artifacts on resume.
- November 25 continuation (mock evidence only): learner proposed examining why B was idle and what operation it was doing. Tutor supplied application sequence: BEGIN, inventory UPDATE completed in 8 ms, external payment call waiting for 90 seconds, COMMIT not reached. Learner suggested a timeout; tutor explained rollback/connection cleanup and avoiding external waits inside long transactions where correctness permits.
- Learner recognised that a timed-out payment may have succeeded and proposed idempotency. Discussed stable keys for retries of the same logical payment and querying outcome, separately from releasing database locks.
- Recovery reasoning: learner proposed remeasuring latency; tutor added comparable load/p95, cleared blocking relationships, pool-wait recovery, errors and duplicate-payment checks. No recovery action was executed or measured.
- Final explanation: learner identified B waiting on an API while holding a transaction lock and blocking A. Corrected “indefinitely” to the observed 90-second wait. Tutor supplied the two supporting observations (blocking relationship and application sequence); learner independently proposed increased query time as an alternative cause of pool exhaustion.
- Assessment: **explanation 1 / evidence 1 / investigation 1**, with guidance. Scale clarified: 0 = not demonstrated, 1 = with help, 2 = independently. Full Lab A and an independent unfamiliar Linux diagnosis remain incomplete; no additional memory/storage workload was run.
- Review: study Days 7, 9 and 13. Revisit waiting versus proven lock contention, alternative causes of pool exhaustion and recovery evidence.
- Remaining actions: verify lab cleanup and complete independent investigation during Day 7; preserve the missing Lab A evidence rather than treating the mock discussion as a real repair.

### Handoff

Continue with Day 7 below. Day 6 guided assessment is recorded as 1/1/1, but its completion checkbox remains open for cleanup and independent practical evidence. Do not repeat the Session B discussion. No sustained HTTP slowdown or actual database recovery was demonstrated.

## Day 7 — 2026-11-25 to 2026-11-26 (guided mock finished)

- Status: guided mock diagnosis, recovery test design and incident summary finished. Independent troubleshooting and final scores remain open. No Day 7 reading completion was reported.
- Mock evidence only: `/report` normally took 100 ms; some requests took 3–5 s. The learner requested a trace and located the delay in Build report. CPU and runnable wait (70 ms and 15 ms) did not explain the 4.118 s build. A mock syscall trace attributed 3.982 s to `fdatasync`. `iostat` showed a growing device queue, and `pidstat` identified a heavy backup writer whose output shared the report's backing device.
- Mock recovery only: learner proposed throttling the backup worker and comparing latency. Under comparable request load, mock backup writes fell from 80 to 20 MiB/s, average device queue depth from 30 to 0.4, and `/report` p95 from 4.2 s to 120 ms. This supported backup-induced storage contention in the scenario; no real backup was changed.
- `pidstat -d` practice: learner matched samples to a request, distinguished write activity from `iodelay`, and corrected the assumption that task write accounting and device writeback must occur in the same interval. Review: if the filesystem wait improves but endpoint latency does not, use a fresh request trace to locate the remaining delay instead of rechecking an already confirmed device improvement.
- Actual Kali preflight: learner confirmed the same two-CPU Kali ARM64 VM and a 20–30 minute budget. `ss` showed no listener on port 8000 at the time checked; the old Day 6 directory and `index.html` still existed and were retained by choice. Other worker cleanup was not verified.
- Fixture: [day7_checkpoint.py](../labs/day7_checkpoint.py) was smoke-tested outside Kali. The VMware shared folder is configured, but a guest mount was not confirmed. No Day 7 server, latency baseline, or fault measurement was collected in Kali.

### Handoff

Resume by listing VMware shares with `vmware-hgfsclient` and mounting the project share read-only with `vmhgfs-fuse` at a temporary mount point. Start `timeout 10m python3 labs/day7_checkpoint.py` from the shared project directory (or use the mounted script's absolute path). In a second terminal, collect five healthy `curl` status and `time_total` samples at `http://127.0.0.1:8077/report` before activating the scenario. Keep the cause hidden and let the learner choose their checks. Verify recovery while the server is still running, then stop it and confirm cleanup before marking the milestone complete.

## Deferred-work backlog

These items remain open; they do not block starting Day 7. Priorities indicate follow-up order, not permission to run workloads or change kernel settings without checking the current environment.

| Priority | Item | Current evidence / limit | Next bounded action |
|---|---|---|---|
| High | Confirm lab cleanup | Day 6 port 8000 had no listener during Day 7 preflight; worker cleanup unverified and the lab directory was retained by choice. Later Day 5 dd/cache files and earlier Python/signal workloads unconfirmed | Verify current process identities and clean up only specifically identified disposable artifacts the learner wants removed |
| Medium | Day 5 cache hit-rate measurement | BCC compilation failed for missing exact kernel headers; download outcome unknown | Check installation and compatibility; sample under a bounded workload if supported; avoid an unnecessary kernel rebuild |
| Medium | Cache sizes/usage checklist validation | Conceptual checklist delivered; only aggregate free output collected | Inspect meminfo and slabtop for page/dentry/inode cache data; distinguish allocated objects from useful cache hits |
| Medium | Effective cache-capacity benchmark and degradation | Not performed; cold/warm precursor skipped; only 2.1 GiB disk free versus earlier 4.6 GiB available RAM | Plan a safely isolated/constrained cache budget or adequate separate storage, then vary working set with buffered I/O and report measured throughput/latency/device reads; do not fill root filesystem |
| Medium | Exact per-thread filesystem occupancy and stronger latency attribution | Histograms for write/fdatasync only; approximate completion buckets and comm filter | Target an identified process, account for return values and relevant operations, split calls at interval boundaries and use reliable snapshot accounting |
| Medium | Day 5 core tool/reading gaps | du/lsblk not exercised; iostat reading completion unconfirmed | Briefly inspect directory usage/device-to-filesystem mapping and confirm selective reading when useful in Day 6 |
| Medium | Day 2 signals | SIGINT status reported; SIGTERM handler/SIGKILL comparison unverified | Repeat on an identified disposable process, verify exit and cleanup |
| Low | Day 3 contention scheduling | CPU saturation demonstrated; involuntary switches and per-thread scheduling wait not measured | Short bounded contention run with per-thread scheduling metrics |
| Low | Day 4 faults/pressure/logs | First-touch counts mocked; PSI and OOM/allocation logs not collected | Measure bounded first-touch faults, read PSI and permitted existing logs; do not force host-wide exhaustion |
| Low | Independent investigation / Day 1 reading | Prior scores remain guided; Day 1 methodology reading unconfirmed | Use Day 7 to assess independent reasoning and revisit relevant methodology sections |

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
