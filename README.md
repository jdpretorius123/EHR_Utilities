# A library for EHR utilities

## Modules
ehr_utils -- This module is allows the user to perform basic 
operations on EHR data. This tool accepts tab-delimited text
(.txt) files.

## Usage
This script requires `datetime`, and contains the following
classes and functions.

## Classes
```
Patient
Lab
```

## Functions
```
remove_chars(variables: str) -> str:
    Trim BOM from first line of a .txt file

parse_data(
    patient_filename: str,
    lab_filename: str
) -> dict[str, Patient]:
    Parse and return laboratory test history for patients
```

## Example Usage
```
from datetime import *

records = parse_data("patient_file.txt", "lab_file.txt")

patient_id = "016A590E-D093-4667-A5DA-D68EA6987D93"
lab_name = "URINALYSIS: RED BLOOD CELLS"
value = 2.8
operator = ">"

patient = records[patient_id]
age = patient.age
was_patient_sick = patient.is_sick(lab_name, operator, value)
initial_age = patient.age_first_visit()
```

## Development
We welcome contributions! Before opening a pull request, please confirm that existing tests pass with **at least 80%
coverage**:

```
python -m pytest tests/
```
