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
#-------------------------------------------------
FIRST_SEM = 1
SECOND_SEM = 2

SEMESTER_CHOICES = (
    (FIRST_SEM, '1st Semester'),
    (SECOND_SEM, '2nd Semester'),
)
#-------------------------------------------------
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
#-----------------------------------------------
SESSION_CHOICES = (
    ('2024-2025', '2024-2025'),
    ('2023-2024', '2023-2024'),
    ('2022-2023', '2022-2023'),
    ('2021-2022', '2021-2022'),
    ('2020-2021', '2020-2021'),
    ('2019-2020', '2019-2020'),
    ('2018-2019', '2018-2019'),
)