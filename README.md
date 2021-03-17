Тестовый проект для ознакомления с работой механизма кэширования в Django.  
Для кэширования используется Redis.

Проект разрабатывается с использованием docker-compose.
Для развертывания необходимо:  
- скачать проект:
    - **git clone** _https://github.com/3ANov/django_cache_test_
- создать файлы **.env.dev** или **.env.prod** в директории **env**  
  по образцу **.env.example** в соответствии с требованиями для тестового  
  прототипа проекта, или для финальной, "релизной" версии;
- собрать образ проекта в docker'e:
    - **docker-compose build**
- применение миграций:
    - **docker-compose exec web python manage.py migrate**
- запустить проект:
    - **docker-compose up -d**
- для остановки контейнеров:
    - **docker-compose down**