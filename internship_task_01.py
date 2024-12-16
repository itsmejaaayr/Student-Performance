# -*- coding: utf-8 -*-
"""Internship_task#01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RsJc0tSCn6XHxo7yL5INrls0jNTIG1rG
"""

#importing pandas library
import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt
#importing seaborn library
import seaborn as sns

#loading data
student_performance=pd.read_csv('Student_performance_data.csv')
df=pd.DataFrame(student_performance)

# View first five rows of the dataset
student_performance.head()

student_performance.isnull().sum()

#Total Students
print(df['StudentID'].count())

#Total Extracurricular
Extracurricular_counts = df['Extracurricular'].value_counts()
print(Extracurricular_counts)

#Total Parental Support
ParentalSupport_counts = df['ParentalSupport'].value_counts()
print(ParentalSupport_counts)

#Gender
Gender_counts = df['Gender'].value_counts()
print(Gender_counts)

Gender_counts = df.groupby(['Gender', 'Gender']).size().unstack()

# Plotting
Gender_counts.plot(kind='bar', stacked=True,colormap='plasma',)
plt.ylabel('Count')
plt.xlabel('Gender')
plt.grid(True)
plt.title('Figure 1: Count of Gender')
plt.show()

count_students = df.groupby(['Age', 'Age']).size().unstack()

# Plotting
count_students.plot(kind='bar', stacked=True,colormap='plasma',)
plt.ylabel('Count')
plt.xlabel('Age')
plt.title('Figure 2: Count by Age')
plt.show()

# Plot Tutoring
Tutoring_counts = df['Tutoring'].value_counts()
plt.pie(Tutoring_counts, labels=Tutoring_counts.index, autopct='%1.1f%%',startangle=90)
plt.title('Figure 3: Distribution of Tutoring')
plt.axis('equal')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame to get counts of students with different GPA values for extracurricular participation
gpa_counts = df.groupby(['Extracurricular', 'Gender']).size().reset_index(name='Count')

# Bar plot for the counts
sns.barplot(data=gpa_counts, x='Extracurricular', y='Count', hue='Gender', palette='inferno')
plt.ylabel('Count')
plt.xlabel('Extracurricular Participation')
plt.title('Figure 4: Count of Students by Extracurricular Participation and Gender')
plt.grid(True)
plt.show()

# Plot Ethnicity & ParentalSupport
sns.countplot(data=df, x='Ethnicity',hue='ParentalSupport',palette='cividis')
plt.xlabel('Ethnicity')
plt.ylabel('ParentalSupport')
plt.grid(True)
plt.title('Figure 5: Ethnicity & ParentalSupport')
plt.show()

# Plot Sports
Sports_counts = df['Sports'].value_counts()
plt.pie(Sports_counts, labels=Sports_counts.index, autopct='%1.1f%%',startangle=90)
plt.title('Figure 6: Distribution of Sports')
plt.axis('equal')
plt.show()

# Plot ParentalSupport & ParentalEducation
sns.countplot(data=df, x='ParentalSupport',hue='ParentalEducation',palette='viridis')
plt.xlabel('ParentalSupport')
plt.ylabel('ParentalEducation')
plt.grid(True)
plt.title('Figure 7: ParentalSupport & ParentalEducation')
plt.show()

# Plot GradeClass & Tutoring
sns.countplot(data=df, x='GradeClass',hue='Tutoring',palette='viridis')
plt.xlabel('GradeClass')
plt.ylabel('Tutoring')

plt.grid(True)
plt.title('Figure 8: GradeClass & Tutoring')
plt.show()