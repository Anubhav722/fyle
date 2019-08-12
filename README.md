# fyle

## API to fetch all bank details

```
curl -X GET \
  'https://fyle-deploy.herokuapp.com/bank/?format=json&limit=200&offset=500' \
  -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1NjMwODA5LCJqdGkiOiI2NzAzN2FiNDVhOTQ0MDI3YTQ3ZDAzNmQ0ZDViMGMxOCIsInVzZXJfaWQiOjF9.0CUP35n-tuf7Ur33XRd7p9ARA8iUYzg5c-cRrYDq5-A' \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 1b04f191-fb0a-317f-6881-d64c8e03055a'
```

## API to fetch bank details

```
curl -X GET \
  'https://fyle-deploy.herokuapp.com/bank/bank_detail/ABHY0065001?format=json' \
  -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1NjMwODA5LCJqdGkiOiI2NzAzN2FiNDVhOTQ0MDI3YTQ3ZDAzNmQ0ZDViMGMxOCIsInVzZXJfaWQiOjF9.0CUP35n-tuf7Ur33XRd7p9ARA8iUYzg5c-cRrYDq5-A' \
  -H 'cache-control: no-cache' \
  -H 'postman-token: 5e76ebb0-4e54-0130-543b-ce2816283c2e'
```
