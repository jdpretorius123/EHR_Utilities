"""Function tests for ehr_utils.py.

This module allows the user to perform basic tests on the
functions in `ehr_utils`.

This script requires `ehr_utils` and contains the following
functions.

Functions
---------
    test_parse_data() -> None:
        Test the processing of EHR data

    test_age() -> None:
        Test calculation of the patient's age

    test_is_sick() -> None:
        Test the correctness of the patient's history
        of illness

    test_age_first_visit() -> None:
        Test calculation of the patient's age at their
        first admission
"""


from ehr_utils import *
import os


PATIENT_FILE: str = "PatientID\tPatientGender\
\tPatientDateOfBirth\tPatientRace\tPatientMaritalStatus\t\
PatientLanguage\tPatientPopulationPercentageBelowPoverty\n\
0BC491C5-5A45-4067-BD11-A78BEA00D3BE\tFemale\t\
1921-04-18 01:56:01.807\tUnknown\tMarried\tEnglish\t18.05\n\
016A590E-D093-4667-A5DA-D68EA6987D93\tMale\t\
1960-12-06 06:37:05.640\tWhite\tUnknown\tEnglish\t15.02\n"

LABS_FILE: str = "PatientID\tAdmissionID\tLabName\tLabValue\t\
LabUnits\tLabDateTime\n016A590E-D093-4667-A5DA-D68EA6987D93\t1\t\
METABOLIC: CREATININE\t0.5\tmg/dL\t1986-12-05 17:46:42.850\n\
016A590E-D093-4667-A5DA-D68EA6987D93\t1\tMETABOLIC: CREATININE\t\
0.9\tmg/dL\t1986-12-06 04:11:32.937\n\
0BC491C5-5A45-4067-BD11-A78BEA00D3BE\t1\tMETABOLIC: CREATININE\t\
0.5\tmg/dL\t1941-11-15 01:43:03.937\n\
0BC491C5-5A45-4067-BD11-A78BEA00D3BE\t2\tMETABOLIC: CREATININE\t\
1.2\tmg/dL\t2008-05-30 02:42:39.240\n\
016A590E-D093-4667-A5DA-D68EA6987D93\t5\t\
URINALYSIS: RED BLOOD CELLS\t3.5\trbc/hpf\t2008-02-26 05:38:56.980\n\
016A590E-D093-4667-A5DA-D68EA6987D93\t4\tURINALYSIS: RED BLOOD CELLS\t\
0.2\trbc/hpf\t2001-03-20 21:28:32.137\n\
0BC491C5-5A45-4067-BD11-A78BEA00D3BE\t2\tURINALYSIS: RED BLOOD CELLS\t\
3.3\trbc/hpf\t2008-05-21 06:51:12.250\n\
0BC491C5-5A45-4067-BD11-A78BEA00D3BE\t1\tURINALYSIS: RED BLOOD CELLS\t\
0.1\trbc/hpf\t1941-11-15 08:04:26.190\n\
016A590E-D093-4667-A5DA-D68EA6987D93\t1\tCBC: WHITE BLOOD CELL COUNT\t\
9.2\tk/cumm\t1986-11-30 20:32:15.443\n"


def test_parse_data() -> None:
    """
    Test parse_data().

    Test the processing of EHR data.

    Arguments
    ---------
    None

    Return
    -------
    None
    """
    # setup
    patient_file = "test_patients.txt"
    patients = open(patient_file, mode="w", newline="\n")
    patients.write(PATIENT_FILE)
    patients.close()

    labs_file = "test_labs.txt"
    labs = open(labs_file, mode="w", newline="\n")
    labs.write(LABS_FILE)
    labs.close()

    patient_id = "016A590E-D093-4667-A5DA-D68EA6987D93"
    true_race = "White"

    # run
    records = parse_data(patient_file, labs_file)

    os.remove(patient_file)
    os.remove(labs_file)

    patient = records[patient_id]
    test_race = patient.race

    # assert
    assert test_race == true_race


def test_age() -> None:
    """
    Test Patient age property.

    Test calculation of the patient's age.

    Arguments
    ---------
    None

    Return
    -------
    None
    """
    # setup
    patient_file = "test_patients.txt"
    patients = open(patient_file, mode="w", newline="\n")
    patients.write(PATIENT_FILE)
    patients.close()

    labs_file = "test_labs.txt"
    labs = open(labs_file, mode="w", newline="\n")
    labs.write(LABS_FILE)
    labs.close()

    patient_id = "0BC491C5-5A45-4067-BD11-A78BEA00D3BE"
    true_age = 101

    # run
    records = parse_data(patient_file, labs_file)

    os.remove(patient_file)
    os.remove(labs_file)

    patient = records[patient_id]
    test_age = patient.age

    # assert
    assert true_age == test_age


def test_is_sick() -> None:
    """
    Test is_sick().

    Test the correctness of the patient's history
    of illness.

    Arguments
    ---------
    None

    Return
    -------
    None
    """
    # setup
    patient_file = "test_patients.txt"
    patients = open(patient_file, mode="w", newline="\n")
    patients.write(PATIENT_FILE)
    patients.close()

    labs_file = "test_labs.txt"
    labs = open(labs_file, mode="w", newline="\n")
    labs.write(LABS_FILE)
    labs.close()

    patient_id = "016A590E-D093-4667-A5DA-D68EA6987D93"
    lab_name = "URINALYSIS: RED BLOOD CELLS"

    test_positive = 2.8
    operator_positive = ">"
    positive = True

    test_negative = 0.1
    operator_negative = "<"
    negative = False

    # run
    records = parse_data(patient_file, labs_file)

    os.remove(patient_file)
    os.remove(labs_file)

    patient = records[patient_id]
    positive_result = patient.is_sick(
        lab_name, operator_positive, test_positive
    )

    negative_result = patient.is_sick(
        lab_name, operator_negative, test_negative
    )

    # assert
    assert positive_result == positive
    assert negative_result == negative


def test_age_first_visit() -> None:
    """
    Test age_first_visit().

    Test calculation of the patient's age at their
    first admission.

    Arguments
    ---------
    None

    Return
    -------
    None
    """
    # setup
    patient_file = "test_patients.txt"
    patients = open(patient_file, mode="w", newline="\n")
    patients.write(PATIENT_FILE)
    patients.close()

    labs_file = "test_labs.txt"
    labs = open(labs_file, mode="w", newline="\n")
    labs.write(LABS_FILE)
    labs.close()

    patient_id = "016A590E-D093-4667-A5DA-D68EA6987D93"
    true_age = 25

    # run
    records = parse_data(patient_file, labs_file)

    os.remove(patient_file)
    os.remove(labs_file)

    patient = records[patient_id]
    test_age = patient.age_first_visit()

    # assert
    assert true_age == test_age
