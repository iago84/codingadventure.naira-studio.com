# Learn for Free

A library of **51 study volumes** (Vol. 00 index + 50 technologies) in PDF,
including a complete AI/ML catalog (Vol. 36-50). Built from free public
tutorials. Every volume has the same skeleton: summaries, concepts, runnable
examples, common mistakes, exercises with solutions, a mini test, a cheat sheet
and a final exam.

All notes are **original writing**, written while working through each source
site's learning path. Sources are cited per volume. Personal study material only.

## Rebuild

```bash
python build.py 01-html     # one volume
python build.py --all       # every volume in src/
python build.py --new 42-shop js example.com   # scaffold a new volume
./build.sh 01-html          # wrapper for git-bash / WSL / Linux / macOS
```

Requirements: Python 3.11+ with `reportlab` and `pygments` (see
`requirements.txt`). Fonts: DejaVu Sans / DejaVu Sans Mono (bundled with Windows
and most Linux distros); Consolas is used as fallback.

## Layout

```
learn-for-free/
  plan/      one plan file per technology + ISSUES.md
  src/       markdown sources, one per volume
  code/      tested example code, one folder per technology
  pdf/       built PDFs (00-index.pdf, 01-html.pdf, ...)
  assets/    VOLUME_TEMPLATE.md (source format + build rules)
  build.py   Markdown -> PDF pipeline (ReportLab + Pygments)
  build.sh   shell wrapper
  README.md  this file
```

Source format, supported Markdown and writing rules:
[`assets/VOLUME_TEMPLATE.md`](assets/VOLUME_TEMPLATE.md).

## Volume status

Status: `planned` (plan written) | `drafted` (src written) | `built` (PDF ok) |
`reviewed` (checklist passed) | `done`

| Vol | Technology | Source site | Status | PDF |
|-----|-----------|-------------|--------|-----|
| 00 | Index & Study Guide | this library | **built** | [00-index.pdf](pdf/00-index.pdf) |
| 01 | HTML | html.com | **built** | [01-html.pdf](pdf/01-html.pdf) |
| 02 | CSS | web.dev/learn/css | **built** | [02-css.pdf](pdf/02-css.pdf) |
| 03 | JavaScript | javascript.info | **built** | [03-javascript.pdf](pdf/03-javascript.pdf) |
| 04 | React | react.dev (fallback, reactplay.io is an SPA) | **built** | [04-react.pdf](pdf/04-react.pdf) |
| 05 | Vue | vuejs.org (fallback, learnvue.co is PWYW) | **built** | [05-vue.pdf](pdf/05-vue.pdf) |
| 06 | Angular | angular.dev/tutorials | **built** | [06-angular.pdf](pdf/06-angular.pdf) |
| 07 | Git | git-scm.com/book (CC BY-NC-SA, see ISSUES) | **built** | [07-git.pdf](pdf/07-git.pdf) |
| 08 | Web3 | ethereum.org (fallback) | **built** | [08-web3.pdf](pdf/08-web3.pdf) |
| 09 | Python | learnpython.org | planned | - |
| 10 | SQL | w3schools.com/sql | **built** | [10-sql.pdf](pdf/10-sql.pdf) |
| 11 | Blockchain | cryptozombies.io (Solidity) | **built** | [11-blockchain.pdf](pdf/11-blockchain.pdf) |
| 12 | Next.js | nextjs.org/learn | **built** | [12-nextjs.pdf](pdf/12-nextjs.pdf) |
| 13 | AI (basics) | elementsofai.com | **built** | [13-ai.pdf](pdf/13-ai.pdf) |
| 14 | PHP | phptherightway.com | **built** | [14-php.pdf](pdf/14-php.pdf) |
| 15 | API | MDN + OpenAPI (fallback) | **built** | [15-api.pdf](pdf/15-api.pdf) |
| 16 | Go | learn-golang.org | planned | - |
| 17 | Rust | rust-lang.org/learn | planned | - |
| 18 | Design Patterns | refactoring.guru | planned | - |
| 19 | TypeScript | typescriptlang.org/docs | built (pending review) | [19-typescript.pdf](pdf/19-typescript.pdf) |
| 20 | C++ | cplusplus.com/doc/tutorial | built (pending review) | [20-cpp.pdf](pdf/20-cpp.pdf) |
| 21 | Java | docs.oracle.com/javase/tutorial | built (pending review) | [21-java.pdf](pdf/21-java.pdf) |
| 22 | C# | dotnet.microsoft.com/learn/csharp | built (pending review) | [22-csharp.pdf](pdf/22-csharp.pdf) |
| 23 | Swift | swift.org/learn | built (pending review) | [23-swift.pdf](pdf/23-swift.pdf) |
| 24 | Django | djangoproject.com/start | planned | - |
| 25 | Flask | flask.palletsprojects.com/tutorial | built (pending review) | [25-flask.pdf](pdf/25-flask.pdf) |
| 26 | Docker | docker.com/get-started | planned | - |
| 27 | Kubernetes | kubernetes.io/docs/tutorials | built (pending review) | [27-kubernetes.pdf](pdf/27-kubernetes.pdf) |
| 28 | Linux | linuxjourney.com | planned | - |
| 29 | Cybersecurity | tryhackme.com | built (pending review) | [29-cybersecurity.pdf](pdf/29-cybersecurity.pdf) |
| 30 | DevOps | roadmap.sh/devops | planned | - |
| 31 | Cloud (AWS) | aws.amazon.com/training | built (pending review) | [31-cloud-aws.pdf](pdf/31-cloud-aws.pdf) |
| 32 | Cloud (GCP) | cloudskillsboost.google | planned | - |
| 33 | Cloud (Azure) | microsoft.com/learn/azure | built (pending review) | [33-cloud-azure.pdf](pdf/33-cloud-azure.pdf) |
| 34 | Data Structures | visualgo.net | planned | - |
| 35 | System Design | systemdesign.one | planned | - |
| 36 | Python for AI | kaggle.com/learn/python | **built** | [36-python-ai.pdf](pdf/36-python-ai.pdf) |
| 37 | Data Science | kaggle.com/learn | **built** | [37-data-science.pdf](pdf/37-data-science.pdf) |
| 38 | Machine Learning | kaggle.com/learn/intro-to-ml | **built** | [38-machine-learning.pdf](pdf/38-machine-learning.pdf) |
| 39 | Deep Learning | kaggle.com/learn/intro-to-deep-learning | **built** | [39-deep-learning.pdf](pdf/39-deep-learning.pdf) |
| 40 | Fast.ai | course.fast.ai | **built** | [40-fastai.pdf](pdf/40-fastai.pdf) |
| 41 | Stanford ML | cs229.stanford.edu | **built** | [41-stanford-ml.pdf](pdf/41-stanford-ml.pdf) |
| 42 | Neural Networks | 3blue1brown.com | **built** | [42-neural-networks.pdf](pdf/42-neural-networks.pdf) |
| 43 | Generative AI | kaggle.com/learn/generative-ai | **built** | [43-generative-ai.pdf](pdf/43-generative-ai.pdf) |
| 44 | LLMs | huggingface.co/learn/llm-course | **built** | [44-llms.pdf](pdf/44-llms.pdf) |
| 45 | Prompt Engineering | learnprompting.org | **built** | [45-prompt-engineering.pdf](pdf/45-prompt-engineering.pdf) |
| 46 | OpenAI API | platform.openai.com/docs | **built** | [46-openai-api.pdf](pdf/46-openai-api.pdf) |
| 47 | Hugging Face | huggingface.co/docs | **built** | [47-huggingface.pdf](pdf/47-huggingface.pdf) |
| 48 | Fine-tuning | huggingface.co/docs/transformers | **built** | [48-finetuning.pdf](pdf/48-finetuning.pdf) |
| 49 | AI Agents | huggingface.co/learn/agents-course | **built** | [49-ai-agents.pdf](pdf/49-ai-agents.pdf) |
| 50 | LangChain | python.langchain.com/docs | **built** | [50-langchain.pdf](pdf/50-langchain.pdf) |

## Per-volume checklist

Run after every volume, before marking it `done`:

- [ ] All code examples run (or compile) and were executed
- [ ] Every question has an answer with a brief explanation
- [ ] TOC links work; PDF outline present
- [ ] No verbatim passages, images or wholesale code blocks from the source
- [ ] Sources section lists every consulted URL
- [ ] Cheat sheet + final test present
- [ ] `code/<tech>/` contains the tested examples
- [ ] Status table above updated
