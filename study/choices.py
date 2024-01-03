# YEAR -------------------------------------------------
FIRST_YEAR = 1
SECOND_YEAR = 2
THIRD_YEAR = 3
FOURTH_YEAR = 4

YEAR_CHOICES = (
    (FIRST_YEAR, '1st Year'),
    (SECOND_YEAR, '2nd Year'),
    (THIRD_YEAR, '3rd Year'),
    (FOURTH_YEAR, '4th Year'),
)

# SEMESTER -------------------------------------------------
FIRST_SEM = 1
SECOND_SEM = 2

SEMESTER_CHOICES = (
    (FIRST_SEM, '1st Semester'),
    (SECOND_SEM, '2nd Semester'),
)

# EXAM NAME-------------------------------------------------
FIRST_MID = '1st Mid'
SECOND_MID = '2nd Mid'
THIRD_MID = '3rd Mid'
CLASS_TEST = 'Class Test'
LAB_TEST = 'Lab Test'
LAB_FINAL = 'Lab Final'
SEM_YEAR_FINAL = 'Final'

EXAM_CHOICES = (
    (FIRST_MID, '1st Mid Term'),
    (SECOND_MID, '2nd Mid Term'),
    (THIRD_MID, '3rd Mid Term'),
    (CLASS_TEST, 'Class Test'),
    (LAB_TEST, 'Lab Test'),
    (LAB_FINAL, 'Lab Final'),
    (SEM_YEAR_FINAL, 'Final'),
)

# SESSION----------------------------------------------
SESSION_24_25 = '2024-2025'
SESSION_23_24 = '2023-2024'
SESSION_22_23 = '2022-2023'
SESSION_21_22 = '2021-2022'
SESSION_20_21 = '2020-2021'
SESSION_19_20 = '2019-2020'
SESSION_18_19 = '2018-2019'


SESSION_CHOICES = (
    ('2024-25', '2024-2025'),
    ('2023-24', '2023-2024'),
    ('2022-23', '2022-2023'),
    ('2021-22', '2021-2022'),
    ('2020-21', '2020-2021'),
    ('2019-20', '2019-2020'),
    ('2018-19', '2018-2019'),
)