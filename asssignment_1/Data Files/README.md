build docker image: docker build -t phuong_assignment .
change directory to phuong_assignment_<number>
run: docker run --rm -it -v "$(pwd)":/app phuong_assignment python lastname_firstname_grade_the_exams.py
