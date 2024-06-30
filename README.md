## Basic Python Web app template


### Available commands
#### Application
- `make build` - Builds application container image
- `make up` - Runs the web server
- `make bash` - Opens bash terminal using the application container

#### Database
- `make psql` - Opens PSQL terminal using the database container
- `make migrate` - Applies database migrations
- `make new-migration` - Prompts user for migration name and creates a new migration file

#### Testing
- `make tests-e2e` - Runs Playwright tests and opens HTML report
- `make test-unit` - Runs `unittest` test cases from src/tests

### Credentials
Default database credentials and the database name is `example`