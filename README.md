# LMS_in_DJANGO
Данное Django приложение представляет из себя прототип системы дистатнционного обучения.
В системе рассмотрена возможность авторизации, 2 роли (Создатель курса и пользователь).
У каждого ис пользователей есть свой личный кабине, при входе в личный кабинет как учитель открывается возможность создания курса.
Все курсы, на которые записан пользователь отображаются в личном кабинете.
В каждом курсе, есть возможность добавлять главы и материалы.
Материалы могут быть 3 типов?
  -Обчный текст с возможность оформления текста и добавления картинок (подключен плагин ckeditor)
  -Видео, есть возможность видео указав ссылку на источки, использовал Youtube в качестве теста. (подключен плагин embededVideo)
  -Викторина, с возможностью выбора одного или несколько вариантов ответов
  
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*//*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

This Django application is a prototype of a distance learning system.
The system considers the possibility of authorization, 2 roles (Course creator and user).
Each IP user has his own personal booth; when entering a personal account as a teacher, the opportunity to create a course opens.
All courses for which the user is registered are displayed in the personal account.
In each course, it is possible to add chapters and materials.
Can there be 3 types of materials?
  -Basic text with the ability to style text and add pictures (plugin ckeditor is connected)
  -Video, there is a possibility of video by specifying a link to the sources, I used Youtube as a test. (plugin embededVideo connected)
  -Quiz, with the ability to choose one or more answer options
