# Vol. 26 – Docker – Study Plan

- Source site: https://www.docker.com/get-started/
- Fetched: 2026-10-10
- Access: reachable
- Notes: Commercial product splash page (no login needed) whose ordered learning path lives in the free official docs at docs.docker.com/get-started; treat docs prose as copyrighted, do not copy verbatim.

## Learning path (source order)

The source URL itself is a marketing splash with download links; the ordered learning path was extracted from the official Docker documentation "Get started" guide that it links to.

1. **Get Docker** — Install Docker Desktop and start it — https://docs.docker.com/get-started/tutorials/get-docker/
2. **Run an application (build & share a containerized app)** — Run a container from a published image — https://docs.docker.com/get-started/tutorials/run-an-app/
3. **Run an AI agent in a sandbox** — Optional side-track for agent workloads — https://docs.docker.com/get-started/tutorials/run-an-agent/
4. **What is a container?** — Core concept behind running instances — https://docs.docker.com/get-started/tutorials/docker-concepts/the-basics/what-is-a-container/
5. **What is an image?** — Ready-to-run packages of an application and its dependencies — https://docs.docker.com/get-started/tutorials/docker-concepts/the-basics/what-is-an-image/
6. **What is Docker Compose?** — Multi-container application definitions — https://docs.docker.com/get-started/tutorials/docker-concepts/the-basics/what-is-docker-compose/
7. **What is a registry?** — Storing and sharing images beyond one machine — https://docs.docker.com/get-started/tutorials/docker-concepts/the-basics/what-is-a-registry/

## Planned chapters for the volume

1. Containers and images from first principles (covers source items: 4, 5)
2. Installing Docker Desktop and verifying the setup (covers source items: 1)
3. Running your first container (covers source items: 2, first half)
4. Multi-container applications with Compose (covers source items: 2, second half; 6)
5. Writing Dockerfiles (covers source items: 2, build step)
6. Registries and Docker Hub (covers source items: 2, share step; 7)
7. Docker CLI and container lifecycle
8. End-to-end capstone: containerize and ship an app (covers source items: 2, 3)

## Flags / issues

- docker.com/get-started/ is a splash page with no chapter list; plan is based on the free official docs at docs.docker.com/get-started (linked from it), not on an inferred TOC.
- Pushing images to Docker Hub requires a free Docker account (signup required; free tier sufficient).
- Everything reachable without payment; no paywall hits. Docs prose is copyrighted — only short topic names were taken, commands rewritten in our own examples.
