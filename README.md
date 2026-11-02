# CODING ADVENTURE

Dos proyectos relacionados: una **biblioteca de PDFs de estudio originales**
(tecnología e IA/ML) y la **plataforma de micro-cursos** que los vende como
cursos interactivos. Es un proyecto de **andamiaje/planificación**: la biblioteca
ya se construye, la plataforma aún no está implementada.

## Qué es

`codingadventure.naira-studio.com` reúne:

- **`learn-for-free/`** — biblioteca de **51 volúmenes PDF** de estudio (fuentes
  Markdown, código de ejemplo probado y un *pipeline* propio de construcción
  `build.py` con ReportLab + Pygments). Estado actual: **40 volúmenes
  construidos, 11 planificados**.
- **`learn-for-free-academy/`** — plataforma de micro-cursos (Django + Expo)
  que convierte esa biblioteca en cursos interactivos de pago (quizzes, examen
  final, certificado verificable). Sólo existe la **Fase 0** (arquitectura, ERD,
  especificación de API, pantallas, hitos y riesgos); el backend y la app móvil
  **no están generados todavía**.

## Uso

### Requisitos

- Python 3 (sólo para la biblioteca de PDFs: `build.py` usa ReportLab y
  Pygments).
- Node.js y un entorno Expo para la futura app móvil de la academy (no
  scaffoldeada aún).
- Docker Compose para la academy cuando se implemente.
- El `.env.example` de la raíz es una plantilla Django genérica (secreto, base de
  datos, `LIBRETRANSLATE_URL`, correo, `REDIS_URL`, CORS, nivel de log y CSP):
  aplica al futuro backend de la academy, no a la biblioteca.

### Instalación

Biblioteca de PDFs (funcional hoy):

```powershell
cd "learn-for-free"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt   # ReportLab + Pygments
```

Plataforma de la academy: **pendiente de implementación** (no hay `manage.py`
ni `package.json` raíz todavía).

### Configuración

No hay `.env` operativo porque la plataforma aún no arranca. La plantilla
`.env.example` de la raíz anticipa las variables del futuro backend:

| Variable | Para qué sirve |
|---|---|
| `DJANGO_SECRET_KEY` | Clave de firma de Django. |
| `DJANGO_DEBUG` | Modo depuración. |
| `DATABASE_URL` | Base de datos (`sqlite` en local, `postgres` en producción). |
| `POSTGRES_DB` / `POSTGRES_USER` / `POSTGRES_PASSWORD` | Credenciales PostgreSQL. |
| `LIBRETRANSLATE_URL` / `TRANSLATE_HTTP_TIMEOUT` | Traducción automática (LibreTranslate local). |
| `DJANGO_EMAIL_*` / `DJANGO_DEFAULT_FROM_EMAIL` | Correo. |
| `REDIS_URL` | Cola de tareas / channel layer. |
| `DJANGO_CORS_ALLOWED_ORIGINS` | Orígenes permitidos. |
| `DJANGO_LOG_LEVEL` | Nivel de registro. |
| `DJANGO_CSP_DEFAULT` | Política de seguridad de contenido (opcional). |

### Arranque local

**No existe todavía un lanzador `start_*.ps1` ni punto de entrada de servidor.**
Lo único ejecutable hoy es el *pipeline* de PDFs dentro de `learn-for-free/`:

```powershell
python build.py 01-html        # construye el volumen 01
python build.py --all          # construye todos los volúmenes
python build.py --new 42-shop js example.com   # crea la plantilla de un volumen nuevo
# o, en su defecto:
./build.sh 01-html
```

La plataforma de la academy, cuando se genere el backend, arrancará con
`docker compose` (5 comandos descritos en `learn-for-free-academy/README.md`).

### Tests

**No hay suite de tests automatizada.** El proyecto lo declara como pendiente;
`learn-for-free-academy/CHECKLIST.md` fija el hito M-tests dentro del roadmap
M1–M8, aún sin empezar. Lo que sí existe es **código de ejemplo probado** manual
por cada tecnología en `learn-for-free/code/<tech>/`.

## Estructura

| Ruta | Contenido |
|---|---|
| `learn-for-free/` | Biblioteca de 51 volúmenes PDF (fuente del contenido). |
| `learn-for-free/src/` | Fuentes Markdown de los 51 volúmenes (00–50). |
| `learn-for-free/pdf/` | PDFs construidos. |
| `learn-for-free/code/<tech>/` | Código de ejemplo probado por tecnología. |
| `learn-for-free/plan/` | Planes de la Fase 0 (uno por tecnología) + `ISSUES.md`. |
| `learn-for-free/build.py` | *Pipeline* Markdown → PDF (ReportLab + Pygments). |
| `learn-for-free-academy/` | Plataforma Django + Expo (Fase 0). |
| `learn-for-free-academy/docs/` | ARCHITECTURE, MILESTONES, ISSUES. |
| `learn-for-free-academy/backend/` | Proyecto Django (**sin scaffolder aún**). |
| `learn-for-free-academy/mobile/` | App Expo (**sin scaffolder aún**). |
| `learn-for-free-academy/infra/` | docker-compose, nginx, CI. |
| `CHECKLIST.md` | Checklist maestra (Proyecto A = biblioteca, Proyecto B = academy). |
| `init_prompt.txt` | Prompts maestros originales (referencia). |

Catálogo de volúmenes por rangos: fundamentos web (00–08), lenguajes base
(09–15), sistemas y lenguajes (16–23), backend y cloud (24–35), fundamentos de
IA (36–37), ML y deep learning (38–42), IA generativa y LLM (43–45), APIs y
agentes (46–50).

## Modelo de negocio

- **Propuesta de valor:** material de estudio técnico **original** (no copiado),
  empaquetado primero como PDFs y después como micro-cursos interactivos con
  quizzes, examen y certificado.
- **Cliente objetivo:** personas que aprenden a programar por su cuenta,
  hispanohablantes e hispanohablantes bilingües (UI en EN + ES). La biblioteca
  PDF es el canal de captación *gratuito*; la academy es el producto de pago.
- **Cómo monetiza:** venta de **micro-cursos a ~2 EUR cada uno** con certificado
  verificable. En móvil se cobraría vía **Google Play Billing** (comisión 15–30 %).
  Es un modelo *freemium*: contenido abierto para atraer, cursos de pago para
  convertir.
- **Nota (decisiones aún abiertas según el propio README del proyecto):** licencia
  del material (CC BY-NC-SA frente a venta en la academy), si conviene empaquetar
  los cursos al lanzamiento dados los márgenes con la comisión de Google Play, y
  el idioma del contenido (EN al lanzamiento). **El backend de pago no está
  implementado**; lo anterior es el modelo previsto en la documentación, no una
  función existente.

## Estado

**27 % — prototipo** según `CHECKLISTS_PER_APP/codingadventure.naira-studio.com.md`.
La **biblioteca de PDFs** está avanzada (40/51 volúmenes construidos); la
**plataforma de la academy** está sólo en fase de planificación.

Pendientes declarados: dependencias, ejecutabilidad, tests, legal, i18n,
seguridad y despliegue. No hay `manage.py` ni lanzador local.

## Licencia y contacto

Decisión de licencia **abierta** (se baraja **CC BY-NC-SA 3.0** para los
volúmenes, en tensión con venderlos como cursos). Contacto: mantenedor del
ecosistema NAIRA.
