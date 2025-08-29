from databricks.sdk import WorkspaceClient
from databricks.labs.lsql.core import StatementExecutionExt
import json

## Configure the databricks authentication
## Ensure the file exists

w = WorkspaceClient(profile="dev")
see = StatementExecutionExt(w)

count = see.fetch_value("SELECT COUNT(*) FROM samples.nyctaxi.trips")
print(f"count={count}")

data = see.fetch_all("Describe detail samples.nyctaxi.trips")
dicts = [row.asDict() for row in data]
json_data = json.dumps(dicts, default=str, indent=2)
print(json_data)