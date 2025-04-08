#!/bin/bash
# generate_structure.sh
# This script creates the full directory structure and placeholder files for the project prototype.

# Create directories
mkdir -p docs/ADRs docs/diagrams
mkdir -p config
mkdir -p frontend/public/images
mkdir -p frontend/pages
mkdir -p frontend/components
mkdir -p frontend/styles
mkdir -p frontend/utils
mkdir -p backend/app/api
mkdir -p backend/app/core
mkdir -p backend/app/models
mkdir -p backend/app/schemas
mkdir -p backend/app/services
mkdir -p backend/app/database
mkdir -p backend/app/utils
mkdir -p backend/tests

# Create root-level files
touch README.md
touch .gitignore

# Create docs files
touch docs/ADRs/adr_001_architecture_decision.md
touch docs/ADRs/adr_002_authentication_decision.md
touch docs/ADRs/adr_003_scalability_decision.md
touch docs/diagrams/system_architecture.png
touch docs/diagrams/c4_model.png
touch docs/diagrams/sequence_diagrams.pdf
touch docs/project_report.pdf

# Create config files
touch config/development.yaml
touch config/production.yaml
touch config/test.yaml

# Create frontend files
touch frontend/package.json
touch frontend/package-lock.json
touch frontend/next.config.js

touch frontend/public/favicon.ico
touch frontend/public/images/logo.png

touch frontend/pages/index.js
touch frontend/pages/_app.js
touch frontend/pages/login.js
touch frontend/pages/register.js
touch frontend/pages/dashboard.js
touch frontend/pages/lessons.js
touch frontend/pages/simulation.js
touch frontend/pages/profile.js

touch frontend/components/Header.js
touch frontend/components/Footer.js
touch frontend/components/AuthForm.js
touch frontend/components/LessonViewer.js
touch frontend/components/SimulationDashboard.js
touch frontend/components/Leaderboard.js
touch frontend/components/Notification.js

touch frontend/styles/globals.css
touch frontend/styles/Home.module.css

touch frontend/utils/api.js
touch frontend/utils/helpers.js

# Create backend files
touch backend/requirements.txt
touch backend/README.md

touch backend/app/main.py

touch backend/app/api/__init__.py
touch backend/app/api/auth.py
touch backend/app/api/users.py
touch backend/app/api/simulation.py
touch backend/app/api/lessons.py
touch backend/app/api/levels.py

touch backend/app/core/__init__.py
touch backend/app/core/config.py
touch backend/app/core/security.py
touch backend/app/core/websocket.py

touch backend/app/models/__init__.py
touch backend/app/models/user.py
touch backend/app/models/simulation.py
touch backend/app/models/lesson.py
touch backend/app/models/level.py
touch backend/app/models/transaction.py

touch backend/app/schemas/__init__.py
touch backend/app/schemas/user.py
touch backend/app/schemas/simulation.py
touch backend/app/schemas/lesson.py
touch backend/app/schemas/level.py

touch backend/app/services/__init__.py
touch backend/app/services/user_service.py
touch backend/app/services/simulation_service.py
touch backend/app/services/lesson_service.py
touch backend/app/services/level_service.py

touch backend/app/database/__init__.py
touch backend/app/database/base.py
touch backend/app/database/session.py

touch backend/app/utils/__init__.py
touch backend/app/utils/logger.py
touch backend/app/utils/helpers.py

touch backend/tests/__init__.py
touch backend/tests/test_auth.py
touch backend/tests/test_users.py
touch backend/tests/test_simulation.py
touch backend/tests/test_lessons.py
touch backend/tests/test_levels.py

echo "Project structure generated successfully."
