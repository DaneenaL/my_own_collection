# file_creator

Роль создаёт текстовый файл модулем my_own_module из этой же коллекции.

## Переменные

| Переменная | По умолчанию | Описание |
|---|---|---|
| file_creator_path | /tmp/file_creator.txt | Путь создаваемого файла |
| file_creator_content | "hello from file_creator role" | Содержимое файла |

## Пример

```yaml
- hosts: localhost
  roles:
    - role: my_own_namespace.yandex_cloud_elk.file_creator
```
