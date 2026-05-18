from models import Module, Programme

def _create_cs_modules():
    return [
        # Part I - Semester 1
        Module('SCS 1101', 'Introduction to Computer Science & Programming', 'PROG', 12, 'I', 1),
        Module('SCS 1102', 'Mathematical Foundation of Computer Science', 'MATH', 10, 'I', 1),
        Module('SCS 1103', 'Computer Architecture', 'THEORY', 10, 'I', 1),
        Module('SMA 1101', 'Calculus I', 'MATH', 10, 'I', 1),
        Module('SMA 1102', 'Discrete Mathematics', 'MATH', 10, 'I', 1),
        Module('PLC 1101', 'Peace, Leadership & Conflict Transformation I', 'THEORY', 8, 'I', 1),
        # Part I - Semester 2
        Module('SCS 1201', 'Introduction to Operating Systems', 'THEORY', 10, 'I', 2),
        Module('SCS 1202', 'Digital Logic Design', 'MIXED', 10, 'I', 2),
        Module('SCS 1203', 'Visual Programming & GUI Development', 'PROG', 10, 'I', 2),
        Module('SMA 1201', 'Linear Mathematics', 'MATH', 10, 'I', 2),
        Module('SORS 1201', 'Probability Theory', 'MATH', 10, 'I', 2),
        Module('PLC 1201', 'Peace, Leadership & Conflict Transformation II', 'THEORY', 8, 'I', 2),
        
        # Part II - Semester 1
        Module('SCS 2101', 'Systems Analysis and Design', 'THEORY', 10, 'II', 1),
        Module('SCS 2102', 'Database Systems & Design', 'MIXED', 10, 'II', 1),
        Module('SCS 2103', 'Data Structures and Algorithms', 'MATH', 10, 'II', 1),
        Module('SCS 2104', 'Data Communication & Computer Networks', 'THEORY', 10, 'II', 1),
        Module('SCS 2105', 'Object Oriented Programming I', 'PROG', 10, 'II', 1),
        Module('SORS 2101', 'Applied Statistics', 'MATH', 10, 'II', 1),
        # Part II - Semester 2
        Module('SCS 2201', 'Software Engineering', 'THEORY', 10, 'II', 2),
        Module('SCS 2202', 'Internet & Web Technologies', 'PROG', 10, 'II', 2),
        Module('SCS 2203', 'Computer Security', 'THEORY', 10, 'II', 2),
        Module('SCS 2204', 'Simulation and Modelling', 'MATH', 10, 'II', 2),
        Module('SCS 2205', 'Information Systems', 'THEORY', 10, 'II', 2),
        Module('SCS 2206', 'Mini Research Project', 'MIXED', 10, 'II', 2),
        
        # Part III
        Module('SCS 3000', 'Industrial Attachment (28 weeks)', 'PRACTICAL', 120, 'III', None),
        
        # Part IV - Semester 1
        Module('SCS 4101', 'Object Oriented Programming II', 'PROG', 10, 'IV', 1),
        Module('SCS 4102', 'Advanced Databases', 'MIXED', 10, 'IV', 1),
        Module('SCS 4103', 'Software Project Management', 'THEORY', 10, 'IV', 1),
        Module('SCS 4104', 'Computer Graphics', 'PROG', 10, 'IV', 1),
        Module('SCS 4105', 'Digital Signal Processing', 'MATH', 10, 'IV', 1, True),
        Module('SCS 4106', 'Decision Support Systems', 'THEORY', 10, 'IV', 1, True),
        # Part IV - Semester 2
        Module('SCS 4201', 'Artificial Intelligence', 'MATH', 10, 'IV', 2),
        Module('SCS 4202', 'Advanced Networks', 'THEORY', 10, 'IV', 2),
        Module('SCS 4203', 'Management Information Systems', 'THEORY', 10, 'IV', 2),
        Module('SCS 4204', 'Intellectual Property Rights', 'THEORY', 8, 'IV', 2, True),
        Module('SCS 4205', 'Advanced Software Engineering', 'THEORY', 10, 'IV', 2, True),
        Module('SCS 4010', 'Research Project (double-weighted)', 'PROJECT', 20, 'IV', 2),
    ]

def _create_chem_modules():
    return [
        # Part I - Semester 1
        Module('SCH 1101', 'General Chemistry I', 'MIXED', 12, 'I', 1),
        Module('SCH 1102', 'Inorganic Chemistry I', 'THEORY', 10, 'I', 1),
        Module('SMA 1101', 'Calculus I', 'MATH', 10, 'I', 1),
        Module('SPH 1101', 'General Physics I', 'MIXED', 10, 'I', 1),
        Module('SCS 1101', 'Introduction to Computer Science & Programming', 'PROG', 12, 'I', 1),
        Module('PLC 1101', 'Peace, Leadership & Conflict Transformation I', 'THEORY', 8, 'I', 1),
        # Part I - Semester 2
        Module('SCH 1201', 'Organic Chemistry I', 'THEORY', 12, 'I', 2),
        Module('SCH 1202', 'Physical Chemistry I', 'MATH', 12, 'I', 2),
        Module('SCH 1203', 'Analytical Chemistry I', 'MIXED', 10, 'I', 2),
        Module('SMA 1201', 'Calculus II', 'MATH', 10, 'I', 2),
        Module('SPH 1201', 'General Physics II', 'MIXED', 10, 'I', 2),
        Module('PLC 1201', 'Peace, Leadership & Conflict Transformation II', 'THEORY', 8, 'I', 2),
        
        # Part II - Semester 1
        Module('SCH 2101', 'Inorganic Chemistry II', 'THEORY', 10, 'II', 1),
        Module('SCH 2102', 'Organic Chemistry II', 'THEORY', 10, 'II', 1),
        Module('SCH 2103', 'Physical Chemistry II', 'MATH', 10, 'II', 1),
        Module('SCH 2104', 'Analytical Chemistry II', 'MIXED', 10, 'II', 1),
        Module('SMA 2101', 'Applied Mathematics for Chemistry', 'MATH', 10, 'II', 1),
        Module('SORS 2101', 'Applied Statistics', 'MATH', 10, 'II', 1),
        # Part II - Semester 2
        Module('SCH 2201', 'Inorganic Chemistry III', 'THEORY', 10, 'II', 2),
        Module('SCH 2202', 'Organic Chemistry III', 'THEORY', 10, 'II', 2),
        Module('SCH 2203', 'Physical Chemistry III (Thermodynamics)', 'MATH', 10, 'II', 2),
        Module('SCH 2204', 'Spectroscopy & Spectrometry', 'MIXED', 10, 'II', 2),
        Module('SCH 2205', 'Environmental Chemistry', 'THEORY', 10, 'II', 2),
        Module('SCH 2206', 'Industrial Chemistry', 'THEORY', 10, 'II', 2),
        
        # Part III
        Module('SCH 3000', 'Industrial Attachment (28 weeks)', 'PRACTICAL', 120, 'III', None),
        
        # Part IV - Semester 1
        Module('SCH 4101', 'Advanced Inorganic Chemistry', 'THEORY', 10, 'IV', 1),
        Module('SCH 4102', 'Advanced Organic Chemistry', 'THEORY', 10, 'IV', 1),
        Module('SCH 4103', 'Advanced Physical Chemistry', 'MATH', 10, 'IV', 1),
        Module('SCH 4104', 'Advanced Analytical Chemistry', 'MIXED', 10, 'IV', 1),
        Module('SCH 4105', 'Polymer Chemistry', 'THEORY', 10, 'IV', 1, True),
        Module('SCH 4106', 'Medicinal Chemistry', 'THEORY', 10, 'IV', 1, True),
        # Part IV - Semester 2
        Module('SCH 4201', 'Industrial Waste Management & Green Chemistry', 'THEORY', 10, 'IV', 2),
        Module('SCH 4202', 'Chemical Process Safety', 'THEORY', 10, 'IV', 2),
        Module('SCH 4203', 'Biochemistry', 'THEORY', 10, 'IV', 2, True),
        Module('SCH 4204', 'Food Chemistry', 'THEORY', 10, 'IV', 2, True),
        Module('SCH 4010', 'Research Project (double-weighted)', 'PROJECT', 20, 'IV', 2),
    ]

def _create_esh_modules():
    return [
        # Part I - Semester 1
        Module('ESH 1101', 'Introduction to Environmental Science', 'THEORY', 10, 'I', 1),
        Module('ESH 1102', "Patterns of Zimbabwe's Population", 'THEORY', 10, 'I', 1),
        Module('ESH 1204', 'Radiation and Pollution', 'THEORY', 10, 'I', 1),
        Module('SCH 1217', 'General Chemistry (Service)', 'MIXED', 10, 'I', 1),
        Module('SMA 1112', 'Preparatory Mathematics (Service)', 'MATH', 10, 'I', 1),
        Module('PLC 1101', 'Peace, Leadership & Conflict Transformation I', 'THEORY', 8, 'I', 1),
        # Part I - Semester 2
        Module('ESH 1206', 'Energy Resources Planning and Conservation', 'THEORY', 10, 'I', 2),
        Module('ESH 1207', 'Introduction to Ecology', 'THEORY', 10, 'I', 2),
        Module('ESH 1211', 'Environmental and Health Education', 'THEORY', 10, 'I', 2),
        Module('SBB 1207', 'General Microbiology (Service)', 'THEORY', 10, 'I', 2),
        Module('SCS 1101', 'Information Technology & Computer Applications', 'PROG', 12, 'I', 2),
        Module('PLC 1201', 'Peace, Leadership & Conflict Transformation II', 'THEORY', 8, 'I', 2),
        
        # Part II - Semester 1
        Module('ESH 2101', 'Introduction to Fresh Water Environment', 'THEORY', 10, 'II', 1),
        Module('ESH 2103', 'Principles of Sociology and Psychology', 'THEORY', 10, 'II', 1),
        Module('ESH 2108', 'Environmental Economics', 'MIXED', 10, 'II', 1),
        Module('ESH 2111', 'Disease Prevention and Control', 'THEORY', 10, 'II', 1),
        Module('ESH 2208', 'Occupational Health and Safety', 'THEORY', 10, 'II', 1),
        Module('ESH 2113', 'Water Supply and Sanitation', 'MIXED', 10, 'II', 1),
        # Part II - Semester 2
        Module('ESH 2203', 'Management of Solid and Hazardous Waste', 'THEORY', 10, 'II', 2),
        Module('ESH 2205', 'Environmental Management Systems', 'THEORY', 10, 'II', 2),
        Module('ESH 2211', 'Research Methodology', 'MIXED', 10, 'II', 2),
        Module('ESH 2213', 'Food Hygiene', 'THEORY', 10, 'II', 2),
        Module('ESH 2214', 'Principles of Ecotoxicology', 'THEORY', 10, 'II', 2),
        Module('SORS 2210', 'Applied Statistics for Biological Sciences (Service)', 'MATH', 10, 'II', 2),
        
        # Part III
        Module('ESH 3000', 'Industrial Attachment (28 weeks)', 'PRACTICAL', 120, 'III', None),
        
        # Part IV - Semester 1
        Module('ESH 4101', 'Air Quality Management', 'THEORY', 10, 'IV', 1),
        Module('ESH 4102', 'Environmental Law and Government Policy', 'THEORY', 10, 'IV', 1),
        Module('ESH 4103', 'Environmental Impact Assessment', 'MIXED', 10, 'IV', 1),
        Module('ESH 4105', 'GIS and Remote Sensing in Natural Resources', 'MIXED', 10, 'IV', 1),
        Module('ESH 4106', 'Climate Change and Adaptation', 'THEORY', 10, 'IV', 1, True),
        Module('ESH 4107', 'Community Health Promotion', 'THEORY', 10, 'IV', 1, True),
        # Part IV - Semester 2
        Module('ESH 4120', 'Integrated Waste Management', 'THEORY', 10, 'IV', 2),
        Module('ESH 4121', 'Public Health Administration', 'THEORY', 10, 'IV', 2),
        Module('ESH 4122', 'Environmental Auditing', 'MIXED', 10, 'IV', 2),
        Module('ESH 4123', 'Occupational Toxicology', 'THEORY', 10, 'IV', 2, True),
        Module('ESH 4010', 'Research Project (double-weighted)', 'PROJECT', 20, 'IV', 2),
    ]

PROGRAMMES = {
    'CS': Programme('BSc Honours Computer Science', 'CS', _create_cs_modules()),
    'CHEM': Programme('BSc Honours Applied Chemistry', 'CHEM', _create_chem_modules()),
    'ESH': Programme('BSc Honours Environmental Science and Health', 'ESH', _create_esh_modules()),
}

def get_programme(code: str) -> Programme:
    return PROGRAMMES.get(code.upper())
