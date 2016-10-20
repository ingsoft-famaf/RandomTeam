run:
	python manage.py runserver

clean:
	rm */*.pyc

update_models:
	python manage.py makemigrations login
	python manage.py migrate

# Para crear un nuevo proyecto:
# django-admin startproject project_name

# Para crear una nueva app
# python manage.py startapp app_name

# Crear
# q = Goal(goal_text="TEST", finish_date=timezone.now())
# q.save()
# q.subgoal_set.create(sub_goal_text="SubTest1")

# Crear
# user = User(username="fran", password="fran", mail="fran")
# user.save()
# user.goal_set.create(goal_text="TEST", finish_date=timezone.now())

# q.choice_set.create(sub_goal_text='SUB TEST1')
# q = SubGoal(sub_goal_text="SUBBBTEST")

# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
