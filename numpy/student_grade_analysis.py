import numpy as np
def grade_analysis(grades):
    grades = np.array(grades)
    mean_grade = np.mean(grades)
    median_grade = np.median(grades)
    std_grade = np.std(grades)

    # find student above/below average
    above_average = grades[grades > mean_grade]
    below_average = grades[grades < mean_grade]

    # grade distribution
    a_grade = np.sum(grades >= 90) # A: 90-100
    b_grade = np.sum((grades >=80) & (grades <90)) # B: 80-89
    c_grade = np.sum((grades >=70) & (grades <80)) # C: 70-79
    d_grade = np.sum((grades >=60) & (grades <70)) # D: 60-69
    f_grade = np.sum(grades <60) # F: <60

    distribution = {'A': a_grade, 'B': b_grade, 'C': c_grade, 'D': d_grade, 'F': f_grade}
    return {
        'mean': mean_grade,
        'median': median_grade,
        'std_dev': std_grade,
        'above_average': len(above_average),
        'below_average': len(below_average),
        'distribution': distribution
    }
# Test with sample grades
student_grades = [90,45,82,87,85,92,90,74,78,80]
result = grade_analysis(student_grades)
print("Student Grades Analysis:")
print("Mean Grade:", result['mean'])
print("Median Grade:", result['median'])
print("Standard Deviation:", result['std_dev']) 
print("Number of Students Above Average:", result['above_average'])
print("Number of Students Below Average:", result['below_average'])         
print("Grade Distribution:", result['distribution'])
print("Grade analysis completed successfully.")
