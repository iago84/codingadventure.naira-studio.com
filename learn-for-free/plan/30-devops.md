# Vol. 30 – DevOps – Study Plan

- Source site: https://roadmap.sh/devops
- Fetched: 2026-10-10
- Access: js-only
- Notes: Free community roadmap with no login; the page fetch returns only intro text and FAQ because the roadmap node graph is JavaScript-rendered, so the item list below is INFERRED from the page's own topic links plus the standard roadmap.sh DevOps track.

## Learning path (source order)

Inferred from the fetched page's link graph (e.g. /devops/automation, /devops/tools, /devops/best-practices, /devops/skills, /devops/career-path, /devops/projects) and the standard roadmap.sh DevOps track — this TOC was not literally present in the fetched HTML and is not a fabricated extraction:

1. **Programming language for scripting** — Python, JavaScript or Go — https://roadmap.sh/devops/skills
2. **Operating systems and scripting** — Linux and shell — https://roadmap.sh/devops/tools
3. **Version control with Git** — Branching and collaboration workflows — https://roadmap.sh/devops/tools
4. **Containers with Docker** — Building and running images — https://roadmap.sh/devops/tools
5. **Container orchestration: Kubernetes** — Deploying and managing workloads — https://roadmap.sh/devops/tools
6. **Cloud providers** — AWS, Azure or GCP fundamentals — https://roadmap.sh/devops/tools
7. **Infrastructure as Code** — Terraform, Pulumi, CloudFormation — https://roadmap.sh/devops/automation-tools
8. **Automation and configuration management** — Ansible, Puppet, Chef — https://roadmap.sh/devops/automation
9. **CI/CD pipelines** — Jenkins, GitHub Actions, GitLab CI — https://roadmap.sh/devops/best-practices
10. **GitOps / continuous delivery** — Argo CD, Flux — https://roadmap.sh/devops/best-practices
11. **Observability** — Prometheus, Grafana, ELK stack — https://roadmap.sh/devops/best-practices
12. **Security and DevSecOps** — Securing pipelines and infrastructure — https://roadmap.sh/devops/best-practices
13. **DevOps projects** — Hands-on practice portfolio — https://roadmap.sh/devops/projects

## Planned chapters for the volume

1. The DevOps lifecycle and culture (covers source items: intro text, 12)
2. Linux and shell scripting (covers source items: 2)
3. Python for automation (covers source items: 1)
4. Git and collaborative workflows (covers source items: 3)
5. Docker containers (covers source items: 4)
6. Kubernetes (covers source items: 5)
7. Cloud fundamentals with AWS (covers source items: 6)
8. Infrastructure as Code with Terraform (covers source items: 7, 8)
9. CI/CD pipelines with GitHub Actions and Jenkins (covers source items: 9, 10)
10. Monitoring, logging and observability (covers source items: 11)
11. Capstone: automated deploy of a containerized app (covers source items: 13)

## Flags / issues

- The roadmap graph is client-side rendered; the fetched page contained only the intro and FAQ text, so the ordered item list above is INFERRED (not fabricated from fetched HTML) from the page's linked topic pages and the widely known roadmap.sh DevOps structure.
- Base the volume on free public official documentation for each named tool (Git, Docker, Kubernetes, Terraform, Ansible, AWS, GitHub, Prometheus docs) plus the roadmap.sh DevOps roadmap itself, which is community content under an open license — still paraphrase rather than copy.
- Some roadmap.sh subpages (/devops/tools, /devops/best-practices, etc.) were linked but not individually fetched; treat their exact wording as unverified.
