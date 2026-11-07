
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)


# Calculate student grade
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# Store students across Streamlit reruns
if "students" not in st.session_state:
    st.session_state.students = []


# Page heading
st.title("🎓 Student Grade Manager")
st.write("Week 1 - Day 4 Python Streamlit Assignment")

st.divider()


# Add student form
st.subheader("Add New Student")

with st.form("student_form", clear_on_submit=True):

    name = st.text_input("Student Name")

    mark = st.number_input(
        "Student Marks",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button(
        "Add Student",
        type="primary"
    )

    if submitted:

        if not name.strip():
            st.error("Please enter a valid student name.")

        else:
            student = {
                "Name": name.strip(),
                "Mark": int(mark),
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(
                f"Student {name.strip()} added successfully!"
            )


# Results section
st.divider()
st.subheader("Student Results")

if st.session_state.students:

    st.dataframe(
        st.session_state.students,
        use_container_width=True,
        hide_index=True
    )

    # Calculate class statistics
    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Class Average",
            value=f"{average:.1f}"
        )

    with col2:
        st.metric(
            label="Highest Mark",
            value=highest
        )

    with col3:
        st.metric(
            label="Lowest Mark",
            value=lowest
        )

    st.info(
        f"Total Students: {len(st.session_state.students)}"
    )

else:
    st.warning("No students added yet.")


# Grade scale information
st.divider()
st.subheader("Grading Scale")

st.table({
    "Marks": [
        "90 - 100",
        "80 - 89",
        "70 - 79",
        "60 - 69",
        "Below 60"
    ],
    "Grade": ["A", "B", "C", "D", "E"]
})
