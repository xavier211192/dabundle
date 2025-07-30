### Installation
brew tap databricks/tap
brew install databricks

curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh

### Configure the workspace profiles
Run ```databricks configure --token --profile <<profile_name>>``` This is like creating an alias for each of your workspace so the CLI can remember which is which.

## Databricks Asset Bundle Structure (Multi-Job Template)

```
databricks_bundle/
├── databricks.yml                 # Main bundle configuration
├── pyproject.toml                # Python package configuration with multiple entry points
├── src/
│   └── your_package/             # Main Python package
│       ├── __init__.py
│       ├── main.py               # Original job entry point
│       ├── job1/
│       │   ├── __init__.py
│       │   └── main.py           # Entry point for job 1
│       ├── job2/
│       │   ├── __init__.py
│       │   └── main.py           # Entry point for job 2
│       └── shared/               # Shared utilities
│           ├── __init__.py
│           ├── utils.py
│           └── config.py
├── resources/
│   ├── job1.yml                  # Job 1 definition
│   ├── job2.yml                  # Job 2 definition
│   └── common/
│       └── cluster_policies.yml
├── dist/                         # Built wheel files (single wheel for all jobs)
├── tests/
└── fixtures/
```

## Key Features

### Single Wheel, Multiple Jobs
- **One wheel file** contains all jobs and shared utilities
- **Multiple entry points** defined in `pyproject.toml`
- **Environment parameters** passed via `${bundle.target}`

### Entry Points Configuration
```toml
[project.scripts]
main = "your_package.main:main"
job1 = "your_package.job1.main:main"
job2 = "your_package.job2.main:main"
```

### Job Configuration with Parameters
```yaml
python_wheel_task:
  package_name: your_package
  entry_point: job1
  named_parameters:
    env: ${bundle.target}
    batch_size: "1000"
```

## Adding a New Job

To add a new job (e.g., `job3`), follow these steps:

### 1. Create Job Directory and Entry Point
```bash
mkdir -p src/your_package/job3
touch src/your_package/job3/__init__.py
```

### 2. Create Job Main File
```python
# src/your_package/job3/main.py
import argparse
from your_package.shared.utils import get_config

def main():
    parser = argparse.ArgumentParser(description="Job 3")
    parser.add_argument('--env', required=True, help='Environment name')
    parser.add_argument('--param1', help='Custom parameter')
    
    args = parser.parse_args()
    
    print(f"Starting job3 in {args.env} environment")
    config = get_config(args.env)
    
    # Your job logic here
    print("Job3 completed successfully")

if __name__ == "__main__":
    main()
```

### 3. Add Entry Point to pyproject.toml
```toml
[project.scripts]
main = "your_package.main:main"
job1 = "your_package.job1.main:main"
job2 = "your_package.job2.main:main"
job3 = "your_package.job3.main:main"  # Add this line
```

### 4. Create Job Configuration
```yaml
# resources/job3.yml
resources:
  jobs:
    job3:
      name: job3
      
      tasks:
        - task_key: job3_task
          environment_key: default
          python_wheel_task:
            package_name: your_package
            entry_point: job3
            named_parameters:
              env: ${bundle.target}
              param1: "value1"
      
      environments:
        - environment_key: default
          spec:
            client: "2"
            dependencies:
              - ../dist/*.whl
```

### 5. Deploy
```bash
databricks bundle deploy --target dev
```

## Deployment
```bash
# Deploy to dev
databricks bundle deploy --target dev

# Deploy to prod  
databricks bundle deploy --target prod
```