# ByteCloud infrastructure preparation: 21 days

## Outcome
Investigate a slow Linux backend, diagnose communication between containers, and troubleshoot common Kubernetes application failures. This is a foundation for infrastructure work, not a claim about an employer's internal stack.

**Time:** 2–3 hours per day. Aim for 40% reading and 60% practice. Days are sequential study sessions; shift them around your commitments.

## Files
- [Daily roadmap](01-DAILY-ROADMAP.md): topics, practice and completion criteria for every day.
- [AI tutor instructions](02-AI-TUTOR.md): paste into your AI assistant at the start of a session.
- [Hands-on labs](03-HANDS-ON-LABS.md): bounded exercises and investigation scenarios.
- [Book reading map](04-BOOK-READING-MAP.md): how to use Systems Performance efficiently.
- [Progress tracker](05-PROGRESS-TRACKER.md): evidence, review dates and session handoffs.

## Start your first session
1. Give your AI assistant this file, the tutor instructions and the daily roadmap.
2. Say: “Start Day 1. First establish my environment, then teach one concept and give me one small exercise. Wait for my response.”
3. Use a local Linux VM or WSL2 for Linux exercises. Docker Desktop with a Linux backend can support container exercises; use a local kind or minikube cluster for Kubernetes.
4. Ask AI to check your OS, available tools and resources before giving setup commands. Use one local environment consistently. A full Linux VM is useful when WSL/container behaviour differs from a host Linux system.
5. Save your session handoff in the tracker before ending.

## Daily rhythm
| Activity | 120-minute session | 180-minute session |
|---|---:|---:|
| Recall yesterday without notes | 10 min | 15 min |
| Read and explain concepts | 35 min | 55 min |
| Hands-on investigation | 60 min | 90 min |
| Record evidence and review gaps | 15 min | 20 min |

Count a topic as complete only when you can explain it, demonstrate it and interpret evidence. If you run short of time, preserve the lab and defer optional depth. Avoid advanced eBPF internals, production cluster administration and installing a service mesh during this foundation sprint.

## Working rules
Use disposable local workloads. Keep experiments bounded by time and resource usage. Inspect the active Kubernetes context before mutations. Keep credentials and private infrastructure output out of AI chats. Request explanations of commands before running them. Cloud deployment is unnecessary for this plan.

## Scope and sources
Adapted from the supplied learning plan. Exact book chapters depend on your edition and table of contents. Documentation links in the reading map are starting points, not a claim that their current contents were checked. Have your AI tutor verify version-specific instructions against official documentation before setup.
