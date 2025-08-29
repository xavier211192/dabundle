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

# count=21932
# [
#   {
#     "format": "delta",
#     "id": "dee488f1-3017-49da-83f5-4c846ea845e9",
#     "name": "samples.nyctaxi.trips",
#     "description": null,
#     "location": "abfss://metastore@ucstprdwesteu.dfs.core.windows.net/17a8f892-3592-4cda-a60f-4dd7892dc6fe/tables/1a254ba2-c40b-4707-b05c-46de6c121156",
#     "createdAt": "2025-08-28 15:06:12.064000+00:00",
#     "lastModified": "2025-08-28 15:06:19+00:00",
#     "partitionColumns": [],
#     "clusteringColumns": [],
#     "numFiles": 1,
#     "sizeInBytes": 456546,
#     "properties": {
#       "delta.dropFeatureTruncateHistory.retentionDuration": "0 hours",
#       "delta.enableDeletionVectors": "false"
#     },
#     "minReaderVersion": 1,
#     "minWriterVersion": 1,
#     "tableFeatures": [],
#     "statistics": {},
#     "clusterByAuto": false
#   }
# ]