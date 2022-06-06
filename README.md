# Cactus Admin
[![Build Status](https://travis-ci.org/Krystian19/cactus-app-admin-service.svg?branch=master)](https://travis-ci.org/Krystian19/cactus-app-admin-service) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/16b9691b8c4b45bb82e592b7af6e1d7d)](https://www.codacy.com/gh/Krystian19/cactus-app-admin-service/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Krystian19/cactus-app-admin-service&amp;utm_campaign=Badge_Grade) [![codecov](https://codecov.io/gh/Krystian19/cactus-app-admin-service/branch/master/graph/badge.svg)](https://codecov.io/gh/Krystian19/cactus-app-admin-service)

Content administration service for the Cactus app.

## Run the tests
Once the service is up and assuming the service container is called "cactus_admin", then run ...
```sh
docker exec -ti cactus_admin python /code/manage.py test
```

## Update seeder data
Update the fixtures data file with this command, once you execute it, make the commit:
```sh
docker exec -ti cactus_admin /code/load_data.sh
```

### Translates Japan's Date and time to UTC with moment-timezone.js
```js
moment.tz('2018-10-07 00:30', 'Japan').utc().format('YYYY-MM-DD HH:mm:ss A');
```

## License
MIT © [Jan Guzman](https://github.com/Krystian19)
