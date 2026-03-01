# caprover-skill

Agent skills for managing and deploying apps on [CapRover](https://caprover.com) — a self-hosted PaaS built on Docker Swarm.

Works with any agent that supports the [skills.sh](https://skills.sh) / OpenClaw skill format.

---

## Skills Included

### `caprover` — CapRover Management

Manage CapRover instances via REST API: create/update apps, deploy from Docker images or custom Dockerfiles, configure ports, volumes, env vars, and Docker Swarm settings.

**Use when you want to:**
- Create or update apps on CapRover
- Deploy from a Docker image or a local Dockerfile (tar file)
- Configure TCP ports for non-HTTP services (game servers, databases)
- Mount persistent volumes
- Read build or runtime logs
- Use `serviceUpdateOverride` for advanced Docker Swarm settings

### `caprover-deploy` — CI/CD Deploy Skill

Trigger deployments to CapRover from natural language. Supports GitHub Actions `workflow_dispatch`, CapRover webhooks, and app tokens. Also scaffolds `.github/workflows/deploy.yml`, `captain-definition`, and GitHub secrets for new projects.

**Use when you want to:**
- Deploy an app by name ("deploy myapp")
- Trigger a GitHub Actions workflow
- Set up CI/CD for a new project with CapRover
- Configure GitHub secrets for CapRover deploys

---

## Installation

```bash
npx skills add guim4dev/caprover-skill@caprover -g -y
npx skills add guim4dev/caprover-skill@caprover-deploy -g -y
```

---

## What's Inside

```
caprover/
  SKILL.md                  # Core skill instructions
  references/api.md         # Full CapRover REST API reference
  scripts/caprover.py       # Ready-to-use Python helper class

caprover-deploy/
  SKILL.md                  # Deploy skill instructions
  scripts/deploy.py         # CLI deploy helper
  assets/templates/         # GitHub Actions workflow templates
    deploy-image.yml
    deploy-tar.yml
    deploy-multi-env.yml
    captain-definition.json
```

---

## ARM64 Support

Both skills include ARM64/aarch64 guidance — build from Dockerfile on the CapRover host to get native ARM64 images.

---

## License

MIT
