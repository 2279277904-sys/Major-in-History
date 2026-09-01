# Open-Source Hardening Design

The first public release keeps the runtime narrow: Windows x64, CPython 3.12,
CPU inference, one input image, and transparent PNG output. The repository
contains only Skill instructions, deterministic processing code, tests, and
maintenance metadata. User images, generated outputs, virtual environments,
model files, logs, and local agent state remain outside Git.

Dependency installation starts from four direct requirements in
`image-processing/requirements.in`. A platform-specific lock records every
resolved dependency and the SHA-256 of the compatible PyPI wheel. Setup accepts
binary wheels only, requires hashes, runs `pip check`, downloads the default
model through rembg, and independently validates the model's SHA-256. Model
weights are never committed or redistributed. The repository's MIT license is
explicitly limited to repository-authored code and documentation; third-party
source and weight terms are documented separately.

Pull requests and pushes run on Windows. CI installs the hash-locked
environment, validates dependencies, runs the unit tests in an isolated temp
directory, validates the Skill structure, and scans tracked files for forbidden
binary formats, absolute user paths, private keys, credentials, and email-like
identifiers. The same privacy audit can run locally before staging.

Local cleanup is recoverable. A pruned candidate virtual environment is tested
before replacing `.venv`; the previous environment is retained as a temporary
backup until unit tests and a real model inference pass. The default General
model remains installed, while unused optional models and generated caches are
removed. Git synchronization transfers source only; each computer maintains
its own environment and model cache.
