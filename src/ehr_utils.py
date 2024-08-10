"""EHR Data Processor.

This module is allows the user to perform basic operations
on EHR data. This tool accepts tab-delimited text (.txt) files.

This script requires `datetime`, and contains the following
classes and functions.

Classes
-------
Patient
Lab

Functions
---------
remove_chars(variables: str) -> str:
    Trim BOM from first line of a .txt file

parse_data(
    patient_filename: str,
    lab_filename: str
) -> dict[str, Patient]:
    Parse and return laboratory test history for patients
"""


from datetime import *


class Lab:
    """
    A class to represent a laboratory test.

    Attributes
    ----------
    patient_id -- a string denoting the patient's id
    admission_id -- a string denoting the patient's
        admission id
    name -- a string denoting the laboratory test's name
    value -- a string denoting the laboratory test's value
    units -- a string denoting the laboratory test's units
    datetime -- a string denoting the laboratory test's
        date and time

    Methods
    -------
    __init__(self, patient_id, admission_id, name, value,
        units, datetime)
        Construct all attributes for Lab class.

        Arguments
        ---------
        patient_id -- a string denoting the patient's id
        admission_id -- a string denoting the patient's
            admission id
        name -- a string denoting the laboratory test's name
        value -- a string denoting the laboratory test's value
        units -- a string denoting the laboratory test's units
        datetime -- a string denoting the laboratory test's
            date and time

        Return
        -------
        None

    patient_id
        The patient's ID property.

    admission_id
        The patient's admission ID property.

    name
        The laboratory test's name property.

    value
        The laboratory test's value property.

    units
        The laboratory test's units property.

    date_time
        The laboratory test's date and time property.
    """

    def __init__(
        self,
        patient_id: str,
        admission_id: str,
        name: str,
        value: str,
        units: str,
        date_time: str,
    ) -> None:
        """
        Construct all attributes for Lab class.

        Arguments
        ---------
        patient_id -- a string denoting the patient's id
        admission_id -- a string denoting the patient's
            admission id
        name -- a string denoting the laboratory test's name
        value -- a string denoting the laboratory test's value
        units -- a string denoting the laboratory test's units
        datetime -- a string denoting the laboratory test's
            date and time

        Return
        -------
        None
        """
        self.patient_id = patient_id  # O(1)
        self.admission_id = admission_id  # O(1)
        self.name = name  # O(1)
        self.value = value  # O(1)
        self.units = units  # O(1)
        self.date_time = date_time  # O(1)

    @property
    def patient_id(self) -> str:
        """The patient's ID poperty."""
        return self._patient_id  # O(1)

    @patient_id.setter
    def patient_id(self, id: str) -> None:
        if isinstance(id, str):
            self._patient_id = id
        else:
            raise ValueError('"id" must be a string')

    @property
    def admission_id(self) -> str:
        """The patient's admission ID property."""
        return self._admission_id  # O(1)

    @admission_id.setter
    def admission_id(self, id: str) -> None:
        if isinstance(id, str):
            self._admission_id = id
        else:
            raise ValueError('"id" must be a string')

    @property
    def name(self) -> str:
        """The laboratory test's name property."""
        return self._name  # O(1)

    @name.setter
    def name(self, lab_name: str) -> None:
        if isinstance(lab_name, str):
            self._name = lab_name
        else:
            raise ValueError('"lab_name" must be a string')

    @property
    def value(self) -> str:
        """The laboratory test's value property."""
        return self._value  # O(1)

    @value.setter
    def value(self, lab_value: str) -> None:
        if isinstance(lab_value, str):
            self._value = lab_value
        else:
            raise ValueError('"lab_value" must be a string')

    @property
    def units(self) -> str:
        """The laboratory test's units property."""
        return self._units  # O(1)

    @units.setter
    def units(self, lab_units: str) -> None:
        if isinstance(lab_units, str):
            self._units = lab_units
        else:
            raise ValueError('"lab_units" must be a string')

    @property
    def date_time(self) -> str:
        """The laboratory test's date and time property."""
        return self._date_time  # O(1)

    @date_time.setter
    def date_time(self, date_time: str) -> None:
        if isinstance(date_time, str):
            self._date_time = date_time
        else:
            raise ValueError('"date_time" must be a string')


class Patient:
    """
    A class to represent a patient.

    Attributes
    ----------
    id -- a string denoting the patient's id
    gender -- a string denoting the patient's gender
    dob -- a string denoting the patient's date and time
        of birth
    ms -- a string denoting the patient's marital status
    race -- a string denoting the patient's race
    lang -- a string denoting the patient's primary language
    pbp -- a string denoting the patient's community percentage
        below the poverty line
    labs -- a list of instances of the Lab class, where each
        instance denotes a laboratory test for the patient

    Methods
    -------
    __init__(self, id, gender, dob, marital_status, race,
        language, percent_below_poverty)
        Construct all attributes for Patient class.

        Arguments
        ---------
        id -- a string denoting the patient's id
        gender -- a string denoting the patient's gender
        dob -- a string denoting the patient's date and time
            of birth
        marital_status -- a string denoting the patient's marital
            status
        race -- a string denoting the patient's race
        language -- a string denoting the patient's primary language
        percent_below_poverty -- a string denoting the patient's
            community percentage below the poverty lined

        Return
        ------
        None

    id
        The patient's ID property.

    gender
        The patient's gender property.

    dob
        The patient's date of birth property.

    ms
        The patient's marital status property.

    race
        The patient's race property.

    lang
        The patient's language property.

    pbp
        The patient's community poverty percent property.

    get_labs(self)
        Return the laboratory test history for the patient.

        Arguments
        ---------
        None

        Return
        ------
        list[Lab]
            instances of the Lab class, where each instance
            is a recorded laboratory test for the patient

    add_lab(self, lab)
        Add lab to patient's laboratory test history.

        Arguments
        ---------
        lab -- an instance of the Lab class denoting one lab
        taken by the patient

        Return
        ------
        None

    age
        The patient's age property.

        Time Complexity
        ---------------
        O(1) total - All statements involve either indexing,
        variable assignment, variable state updates, or logical
        comparisons. Hence, all operations are in O(1) time.

        Assumptions
        -----------
        1.  All entries for patient date of birth are strings of a fixed
            length.

        Arguments
        ---------
        None

        Return
        -------
        int
            the patient's current age

    age_first_visit(self) -> int:
        Return the patient's age at first admission.

        Time Complexity
        ---------------
        O(N) total
        N - number of laboratory tests taken by the patient

        Assumptions
        -----------
        1.  All entries for patient date of birth are strings of a fixed
            length.
        2.  All entries for patient date and time of admission are strings
            of a fixed length.

        Arguments
        ---------
        None

        Return
        -------
        int
            the patient's age at first admission

    is_sick(self, lab_name, operator, value)
        Return the patient's history of illness for a laboratory test.

        Time Complexity
        ---------------
        O(N) total
        N - number of records for a laboratory test taken by the patient

        Assumptions
        -----------
        1.  All arguments are positional and lack of adherence to order
            indicated in function definition generates errors.
        2.  Only operators passed as arguments include > and <

        Arguments
        ---------
        lab_name -- a string denoting the name of a laboratory test

        operator -- a string denoting a comparison operator: > or <

        value -- a float denoting a value for a laboratory test to
            assess the patient's history of illness

        Return
        -------
        bool
            the patient's history of illness for a laboratory test: True
            if the patient's recorded value is greater than or less than
            value, and False if otherwise
    """

    def __init__(
        self,
        id: str,
        gender: str,
        dob: str,
        race: str,
        marital_status: str,
        language: str,
        percent_below_poverty: str,
    ) -> None:
        """
        Construct all attributes for Patient class.

        Arguments
        ---------
        id -- a string denoting the patient's id
        gender -- a string denoting the patient's gender
        dob -- a string denoting the patient's date and time
            of birth
        marital_status -- a string denoting the patient's marital
            status
        race -- a string denoting the patient's race
        language -- a string denoting the patient's primary language
        percent_below_poverty -- a string denoting the patient's
            community percentage below the poverty line

        Return
        ------
        None
        """
        self.id = id  # O(1)
        self.gender = gender  # O(1)
        self.dob = dob  # O(1)
        self.race = race  # O(1)
        self.ms = marital_status  # O(1)
        self.lang = language  # O(1)
        self.pbp = percent_below_poverty  # O(1)
        self.labs: list[Lab] = []  # O(1)

    @property
    def id(self) -> str:
        """The patient's ID property."""
        return self._id  # O(1)

    @id.setter
    def id(self, id: str) -> None:
        if isinstance(id, str):
            self._id = id
        else:
            raise ValueError('"id" must be a string')

    @property
    def gender(self) -> str:
        """The patient's gender property."""
        return self._gender  # O(1)

    @gender.setter
    def gender(self, gender: str) -> None:
        if isinstance(gender, str):
            self._gender = gender
        else:
            raise ValueError('"gender" must be a string')

    @property
    def dob(self) -> str:
        """The patient's date of birth property."""
        return self._dob  # O(1)

    @dob.setter
    def dob(self, dob: str) -> None:
        if isinstance(dob, str):
            self._dob = dob
        else:
            raise ValueError('"dob" must be a string')

    @property
    def race(self) -> str:
        """The patient's race property."""
        return self._race  # O(1)

    @race.setter
    def race(self, race: str) -> None:
        if isinstance(race, str):
            self._race = race
        else:
            raise ValueError('"race" must be a string')

    @property
    def ms(self) -> str:
        """The patient's marital status property."""
        return self._ms  # O(1)

    @ms.setter
    def ms(self, marital_status: str) -> None:
        if isinstance(marital_status, str):
            self._ms = marital_status
        else:
            raise ValueError('"marital_status" must be a string')

    @property
    def lang(self) -> str:
        """The patient's language property."""
        return self._lang  # O(1)

    @lang.setter
    def lang(self, language: str) -> None:
        if isinstance(language, str):
            self._lang = language
        else:
            raise ValueError('"language" must be a string')

    @property
    def pbp(self) -> str:
        """The patient's community poverty percent property."""
        return self._pbp  # O(1)

    @pbp.setter
    def pbp(self, pbp: str) -> None:
        if isinstance(pbp, str):
            self._pbp = pbp
        else:
            raise ValueError('"pbp" must be a string')

    def get_labs(self) -> list[Lab]:
        """
        Return the laboratory test history for the patient.

        Arguments
        ---------
        None

        Return
        ------
        list[Lab]
            instances of the Lab class, where each instance
            is a recorded laboratory test for the patient
        """
        return self.labs  # O(1)

    def add_lab(self, lab: Lab) -> None:
        """
        Add lab to patient's laboratory test history.

        Arguments
        ---------
        lab -- an instance of the Lab class denoting one lab
        taken by the patient

        Return
        ------
        None
        """
        self.get_labs().append(lab)  # O(1)

    @property
    def age(self) -> int:
        """
        The patient's age property.

        Time Complexity
        ---------------
        O(1) total - All statements involve either indexing,
        variable assignment, variable state updates, or logical
        comparisons. Hence, all operations are in O(1) time.

        Assumptions
        -----------
        1.  All entries for patient date of birth are strings of a fixed
            length.

        Arguments
        ---------
        None

        Return
        -------
        int
            the patient's current age
        """
        dob = self.dob  # O(1)
        dob_date = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S.%f")  # O(1)
        today = date.today()  # O(1)
        age = today.year - dob_date.year  # O(1)

        if (today.month < dob_date.month) or (
            today.month == dob_date.month and today.day < dob_date.day
        ):  # O(1)
            age -= 1  # O(1)

        return int(age)  # O(1)

    def age_first_visit(self) -> int:
        """
        Return the patient's age at first admission.

        Time Complexity
        ---------------
        O(N) total
        N - number of laboratory tests taken by the patient

        Assumptions
        -----------
        1.  All entries for patient date of birth are strings of a fixed
            length.
        2.  All entries for patient date and time of admission are strings
            of a fixed length.

        Arguments
        ---------
        None

        Return
        -------
        int
            the patient's age at first admission
        """
        dob = self.dob  # O(1)
        dob_date = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S.%f")  # O(1)
        lab_dates: list[str] = []  # O(1)
        labs = self.get_labs()[:]  # O(n)
        for lab in labs:  # O(n)
            lab_dates.append(lab.date_time)

        first_visit_string = min(lab_dates)  # O(n)
        first_visit_date = datetime.strptime(
            first_visit_string, "%Y-%m-%d %H:%M:%S.%f"
        )  # O(1)
        age = first_visit_date.year - dob_date.year  # O(1)

        if (first_visit_date.month < dob_date.month) or (
            first_visit_date.month == dob_date.month
            and first_visit_date.day < dob_date.day
        ):  # O(1)
            age -= 1  # O(1)

        return int(age)  # O(1)

    def is_sick(self, lab_name: str, operator: str, value: float) -> bool:
        """
        Return the patient's history of illness for a laboratory test.

        Time Complexity
        ---------------
        O(N) total
        N - number of records for a laboratory test taken by the patient

        Assumptions
        -----------
        1.  All arguments are positional and lack of adherence to order
            indicated in function definition generates errors.
        2.  Only operators passed as arguments include > and <

        Arguments
        ---------
        lab_name -- a string denoting the name of a laboratory test

        operator -- a string denoting a comparison operator: > or <

        value -- a float denoting a value for a laboratory test to
            assess the patient's history of illness

        Return
        -------
        bool
            the patient's history of illness for a laboratory test: True
            if the patient's recorded value is greater than or less than
            value, and False if otherwise
        """
        operator_table = {
            ">": lambda x, y: x > y,
            "<": lambda x, y: x < y,
        }  # O(1)

        lab_values: list[float] = []  # O(1)
        labs = self.get_labs()[:]  # O(n)
        for lab in labs:  # O(n)
            if lab.name == lab_name:  # O(1)
                lab_values.append(float(lab.value))  # O(1)

        comparison = operator_table[operator]  # O(1)

        if operator == ">":  # O(1)
            max_value = max(lab_values)  # O(n)
            if comparison(max_value, value):  # type: ignore
                return True  # O(1)

        if operator == "<":  # O(1)
            min_value = min(lab_values)  # O(n)
            if comparison(min_value, value):  # type: ignore
                return True  # O(1)
        return False  # O(1)


def remove_chars(variables: str) -> str:
    """Trim BOM from first line of .txt file.

    Time Complexity
    ---------------
    O(N) total
    N - number of times the character sequence "ï»¿"
        is replaced with "" to create a new string

    Arguments
    ---------
    variables -- a string denoting the variables
        from the first line of a .txt file

    Return
    -------
    str
        trimmed variables from the first line of a .txt file
    """
    trimmed_variables = variables.replace("ï»¿", "")  # O(n)
    return trimmed_variables  # O(1)


def parse_data(patient_filename: str, lab_filename: str) -> dict[str, Patient]:
    """
    Parse and return lab test history for patients.

    Time Complexity
    ---------------
    O(QR+ST) total
    Q - number of lines in the patient_filename .txt file
    R - number of columns per line in the patient_filename
        .txt file
    S - number of lines in the labs_filename .txt file
    T - number of columns per line in the labs_filename
        .txt file

    Assumptions
    -----------
    1.  All arguments are positional and lack of adherence to order
        indicated in function definition generates errors.
    2.  Only input is tab-delimited .txt files.
    3.  All patient and corresponding lab history files contain same columns.
    4.  The number of lines in labs_filename .txt file will be greater than
        or equal to the number of lines in patient_filename (S >= Q).

    Arguments
    ---------
    patient_filename --  a string denoting the .txt file with the information
        for the patients (patient ID, gender, date of birth, race, marital
        status, language, community percentage below poverty)

    lab_filename -- a string denoting the lab history information the
        patients (patient ID, admission ID, test name, test value, test units,
        test date and time)

    Return
    -------
    dict[str, PATIENT]
        each key is a patient's unique ID and each value is an instance of the
        Patient class with all the laboratory test history for that patient
    """
    patient_infile = open(patient_filename, "r")  # O(1)
    patient_variables = patient_infile.readline()  # O(1)
    patient_variables = remove_chars(patient_variables)  # O(r)
    patient_vars_list = patient_variables.split("\t")  # O(r)
    patient_vars_list[-1] = patient_vars_list[
        -1
    ].strip()  # trim last variable O(1)

    patient_id_idx = patient_vars_list.index("PatientID")  # O(r)
    patient_gender_idx = patient_vars_list.index("PatientGender")  # O(r)
    patient_dob_idx = patient_vars_list.index("PatientDateOfBirth")  # O(r)
    patient_race_idx = patient_vars_list.index("PatientRace")  # O(r)
    patient_ms_idx = patient_vars_list.index("PatientMaritalStatus")  # O(r)
    patient_lang_idx = patient_vars_list.index("PatientLanguage")  # O(r)
    patient_pbp_idx = patient_vars_list.index(
        "PatientPopulationPercentageBelowPoverty"  # fmt: ignore
    )  # O(r)

    patients = patient_infile.readlines()  # O(qr)
    patient_infile.close()  # O(1)

    patient_dict: dict[str, Patient] = {}  # O(1)

    for aline in patients:  # O(q)
        patient = aline.split("\t")  # O(r)
        patient[-1] = patient[-1].strip()  # O(r)

        patient_id = patient[patient_id_idx]  # O(1)
        patient_gender = patient[patient_gender_idx]  # O(1)
        patient_dob = patient[patient_dob_idx]  # O(1)
        patient_race = patient[patient_race_idx]  # O(1)
        patient_ms = patient[patient_ms_idx]  # O(1)
        patient_lang = patient[patient_lang_idx]  # O(1)
        patient_pbp = patient[patient_pbp_idx]  # O(1)
        patient_dict[patient_id] = Patient(
            patient_id,
            patient_gender,
            patient_dob,
            patient_race,
            patient_ms,
            patient_lang,
            patient_pbp,
        )

    lab_infile = open(lab_filename, "r")  # O(1)
    lab_variables = lab_infile.readline()  # O(1)
    lab_variables = remove_chars(lab_variables)  # O(t)
    lab_vars_list = lab_variables.split("\t")  # O(t)
    lab_vars_list[-1] = lab_vars_list[-1].strip()  # O(t)

    lab_pid_idx = lab_vars_list.index("PatientID")  # O(t)
    lab_aid_idx = lab_vars_list.index("AdmissionID")  # O(t)
    lab_name_idx = lab_vars_list.index("LabName")  # O(t)
    lab_value_idx = lab_vars_list.index("LabValue")  # O(t)
    lab_units_idx = lab_vars_list.index("LabUnits")  # O(t)
    lab_datetime_idx = lab_vars_list.index("LabDateTime")  # O(t)

    labs = lab_infile.readlines()  # O(st)
    lab_infile.close()  # O(1)

    for aline in labs:  # O(s)
        one_lab = aline.split("\t")  # O(t)
        one_lab[-1] = one_lab[-1].strip()  # O(t)

        patient_id = one_lab[lab_pid_idx]  # O(1)
        lab_aid = one_lab[lab_aid_idx]  # O(1)
        lab_name = one_lab[lab_name_idx]  # O(1)
        lab_value = one_lab[lab_value_idx]  # O(1)
        lab_units = one_lab[lab_units_idx]  # O(1)
        lab_datetime = one_lab[lab_datetime_idx]  # O(1)

        lab = Lab(
            patient_id, lab_aid, lab_name, lab_value, lab_units, lab_datetime
        )  # O(1)

        patient_dict[patient_id].add_lab(lab)  # O(1)

    records = patient_dict  # O(1)
    return records  # O(1)
