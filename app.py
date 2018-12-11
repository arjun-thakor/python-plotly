from plotly.offline import plot
import plotly.graph_objs as go

# Add data
semesters = ['Semester 1', 'Semester 2', 'Semester 3', 'Semester 4']
grades = [3.58, 3.38, 3.31, 3.30]
text = ['Problem Solving/Program Logic: A+<br>Web Technologies I: B+<br>Business Applications: A+<br>Database Design & SQL: A-<br>Web Security: A',
        'Programming C# .NET: A-<br>Relational Database & SQL: B-<br>Database Programming: A-<br>Interpersonal & Group Dynamics: B-<br>English Essentials: A-',
        'Mobile Development: A+<br>Web Applications Using C# .NET: A-<br>Co-Op Preparation: A-<br>Project Management: D<br>General Mathematics I: C-<br>Emerging Technologies: A<br>Programming Java SE: A-',
        'Co-Op Job Search & Approval: P<br>Web Technologies II: B+<br>Programming Java EE: B+<br>Human Interaction: C<br>Organizational Behaviour: D<br>Networking Fundamentals: C+']

# Create and style traces
plotting_chart = [go.Bar(
    x=semesters,
    y=grades,
    text=text,
    marker=dict(
        color=['rgb(158,202,225)', 'rgb(163, 203, 56)', 'rgb(87, 88, 187)', 'rgb(238, 90, 36)'],
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)]

# Edit the layout
layout = dict(title='Result of overall performance',
              xaxis=dict(title='Semesters'),
              yaxis=dict(title='Grade Points'),
              font=dict(family='Roboto', size=14, color='#7f7f7f'),
              width=700
)

fig = dict(data=plotting_chart, layout=layout)
plot(fig, filename='result.html')

help(layout)
