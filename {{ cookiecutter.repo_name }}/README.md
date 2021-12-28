{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}


Run API locally
```bash
func start --verbose
```

Send request to the hello-world endpoint of the API
```bash
curl --location --request GET 'http://localhost/api/hello-world?name=test'
```

### References
- [Continuous delivery by using GitHub Action](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-github-actions?tabs=python#prerequisites)
- [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=azurecli-linux%2Capplication-level)
