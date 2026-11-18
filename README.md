# Ansible Collection - my_own_namespace.yandex_cloud_elk

Учебная коллекция. В ней свой модуль, который создаёт текстовый файл, и роль, которая этот модуль использует.

## Что внутри

| Что | Название | Описание |
|---|---|---|
| Модуль | my_own_module | Создаёт файл по пути path с содержимым content |
| Роль | file_creator | Вызывает my_own_module, все параметры вынесены в defaults |
| Playbook | playbooks/site.yml | Пример использования роли |

## Модуль my_own_module

Создаёт текстовый файл на хосте. Если файл уже есть с таким же содержимым, ничего не меняет (идемпотентный). Если содержимое другое, перезаписывает файл. Поддерживает check mode.

| Параметр | Обязательный | Описание |
|---|---|---|
| path | да | Полный путь файла |
| content | да | Текст, который записать в файл |

Возвращает: path (путь файла) и message (created, updated или already up to date).

```yaml
- name: Create file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/hello.txt
    content: "hello world"
```

## Роль file_creator

| Переменная | По умолчанию | Описание |
|---|---|---|
| file_creator_path | /tmp/file_creator.txt | Путь создаваемого файла |
| file_creator_content | "hello from file_creator role" | Содержимое файла |

```yaml
- hosts: all
  roles:
    - role: my_own_namespace.yandex_cloud_elk.file_creator
      vars:
        file_creator_path: /tmp/hello.txt
```

## Установка

Из архива:

    ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz

Из репозитория:

    ansible-galaxy collection install git+https://github.com/DaneenaL/my_own_collection.git

## Требования

Ansible 2.9 или новее.

## Лицензия

GPL-3.0-or-later
